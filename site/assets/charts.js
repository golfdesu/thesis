/* ============================================================
   Table Trend Charts - dependency-free SVG chart generator
   Scans markdown tables, renders an interactive bar chart panel
   beneath each numeric table. Theme-aware via CSS variables.
   ============================================================ */
(function () {
  "use strict";

  var W = 760, H = 250, PAD_T = 30, PAD_B = 34, PAD_X = 10;
  var MAX_COLS = 12, MAX_SERIES = 16;

  function stripTags(s) {
    return String(s == null ? "" : s).replace(/<[^>]*>/g, "");
  }
  function decodeEnt(s) {
    if (s.indexOf("&") === -1) return s;
    var d = document.createElement("textarea");
    d.innerHTML = s;
    return d.value;
  }
  function clean(s) {
    return decodeEnt(stripTags(s)).replace(/\s+/g, " ").trim();
  }
  function escXml(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;")
      .replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }

  function parseNum(t) {
    t = (t || "").trim().replace(/^~\s*/, "");
    if (!t || /^[-\u2014\u2013]+$/.test(t) || /^n\/?a\.?$/i.test(t)) return null;
    var neg = /^\(.*\)$/.test(t);
    var x = t.replace(/[()\s]/g, "").replace(/[$\u20AC\u00A3,%]/g, "");
    var m = x.match(/^([+-]?\d+(?:\.\d+)?)\s*(T|B|M|K)?$/i);
    if (!m) return null;
    var v = parseFloat(m[1]);
    var mult = { T: 1e12, B: 1e9, M: 1e6, K: 1e3 }[(m[2] || "").toUpperCase()] || 1;
    v *= mult;
    return neg ? -v : v;
  }

  function isNoiseHeader(h) {
    return /yoy|%|growth|chg|change|delta|cagr|margin\s*%/i.test(h);
  }

  function analyze(table) {
    var headEls = Array.prototype.slice.call(table.querySelectorAll("thead th"));
    var trs = Array.prototype.slice.call(table.querySelectorAll("tbody tr"));
    if (!headEls.length || !trs.length) return null;
    var head = headEls.map(function (th) { return clean(th.textContent); });

    var xs = [];
    for (var c = 1; c < head.length && xs.length < MAX_COLS; c++) {
      if (isNoiseHeader(head[c])) continue;
      var cnt = 0, tot = 0;
      trs.forEach(function (tr) {
        var td = tr.children[c];
        if (!td) return;
        tot++;
        if (parseNum(td.textContent) !== null) cnt++;
      });
      if (tot > 0 && cnt / tot >= 0.5) xs.push(c);
    }
    if (xs.length < 2) return null;

    var rows = [];
    trs.forEach(function (tr) {
      var label = tr.children[0] ? clean(tr.children[0].textContent) : "";
      if (!label || label.length > 64) return;
      var vals = xs.map(function (c) {
        var td = tr.children[c];
        return td
          ? { raw: clean(td.textContent), v: parseNum(td.textContent) }
          : { raw: "", v: null };
      });
      if (vals.filter(function (p) { return p.v !== null; }).length >= 2) {
        rows.push({ label: label, vals: vals });
      }
    });
    if (!rows.length) return null;
    return { head: head, xs: xs, rows: rows.slice(0, MAX_SERIES) };
  }

  function draw(state) {
    var d = state.data;
    var row = d.rows[state.si];
    var svg = state.svgWrap;
    var n = d.xs.length;
    var plotW = W - PAD_X * 2;
    var plotH = H - PAD_T - PAD_B;
    var slot = plotW / n;

    var vmax = -Infinity, vmin = Infinity;
    row.vals.forEach(function (p) {
      if (p.v === null) return;
      if (p.v > vmax) vmax = p.v;
      if (p.v < vmin) vmin = p.v;
    });
    if (vmax === -Infinity) return;
    vmin = Math.min(0, vmin);
    var range = (vmax - vmin) || 1;

    function y(v) { return PAD_T + ((vmax - v) / range) * plotH; }

    var bw = Math.max(6, Math.min(46, slot * 0.52));
    var showVals = slot >= 34;
    var parts = [];

    for (var g = 1; g <= 3; g++) {
      var gy = y(vmin + range * g / 4);
      parts.push('<line class="grid-line" x1="' + PAD_X + '" y1="' + gy.toFixed(1) +
        '" x2="' + (W - PAD_X) + '" y2="' + gy.toFixed(1) + '"/>');
    }
    parts.push('<line class="axis-line" x1="' + PAD_X + '" y1="' + y(0).toFixed(1) +
      '" x2="' + (W - PAD_X) + '" y2="' + y(0).toFixed(1) + '"/>');

    row.vals.forEach(function (p, i) {
      var cx = PAD_X + slot * i + slot / 2;
      var xl = cx > W - 30 ? W - 30 : cx;
      var lbl = escXml(trunc(d.head[d.xs[i]] || "", 16));
      parts.push('<text class="x-label" x="' + xl.toFixed(1) + '" y="' + (H - 12) +
        '" text-anchor="middle">' + lbl + "</text>");
      if (p.v === null) return;
      var bx = cx - bw / 2;
      var by = p.v >= 0 ? y(p.v) : y(0);
      var bh = Math.max(1.5, Math.abs(y(p.v) - y(0)));
      var tip = escXml(row.label + " \u00b7 " + (d.head[d.xs[i]] || "") + ": " +
        (p.raw || p.v));
      parts.push('<rect class="bar" x="' + bx.toFixed(1) + '" y="' + by.toFixed(1) +
        '" width="' + bw.toFixed(1) + '" height="' + bh.toFixed(1) +
        '" rx="3"><title>' + tip + "</title></rect>");
      if (showVals && p.raw) {
        var vy = p.v >= 0 ? by - 6 : by + bh + 13;
        parts.push('<text class="val-label" x="' + cx.toFixed(1) + '" y="' + vy.toFixed(1) +
          '" text-anchor="middle">' + escXml(trunc(p.raw, 9)) + "</text>");
      }
    });

    svg.innerHTML =
      '<svg viewBox="0 0 ' + W + " " + H + '" role="img" aria-label="Trend chart: ' +
      escXml(row.label) + '">' + parts.join("") + "</svg>";
  }

  function trunc(s, n) {
    s = String(s || "");
    return s.length > n ? s.slice(0, n - 1) + "\u2026" : s;
  }

  function render(container, data) {
    var state = { si: 0, data: data };

    var headEl = document.createElement("div");
    headEl.className = "tbl-chart-head";
    var title = document.createElement("span");
    title.className = "tbl-chart-title";
    title.textContent = "Trend";
    headEl.appendChild(title);

    var svgWrap = document.createElement("div");
    svgWrap.className = "tbl-chart-svg";
    state.svgWrap = svgWrap;

    data.rows.forEach(function (r, i) {
      var b = document.createElement("button");
      b.type = "button";
      b.className = "chip-btn" + (i === 0 ? " active" : "");
      b.textContent = trunc(r.label, 28);
      b.title = r.label;
      b.addEventListener("click", function () {
        state.si = i;
        headEl.querySelectorAll(".chip-btn").forEach(function (x) {
          x.classList.remove("active");
        });
        b.classList.add("active");
        draw(state);
      });
      headEl.appendChild(b);
    });

    container.appendChild(headEl);
    container.appendChild(svgWrap);
    draw(state);
  }

  function initAll() {
    document.querySelectorAll(
      ".markdown-body .table-wrap table, .markdown-body .table-wrapper table"
    ).forEach(function (table) {
      if (table.dataset.charted) return;
      var data = analyze(table);
      if (!data) {
        table.dataset.charted = "skip";
        return;
      }
      table.dataset.charted = "1";
      var wrap = document.createElement("div");
      wrap.className = "tbl-chart";
      var holder = table.closest(".table-wrap") || table.closest(".table-wrapper");
      if (holder && holder.parentNode) {
        holder.insertAdjacentElement("afterend", wrap);
      } else {
        table.insertAdjacentElement("afterend", wrap);
      }
      render(wrap, data);
    });
  }

  var tId = null;
  function debounced() {
    clearTimeout(tId);
    tId = setTimeout(initAll, 120);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initAll);
  } else {
    initAll();
  }
  new MutationObserver(debounced).observe(document.documentElement,
    { childList: true, subtree: true });

  window.TableCharts = { init: initAll };
})();
