// EV Research Hub — Interactive Script
// Preserves all original behavior (theme, tree, search, counters, PJAX)
// and adds modern polish: scroll reveal, header state, back-to-top.
document.addEventListener("DOMContentLoaded", () => {
  const htmlEl = document.documentElement;
  htmlEl.classList.add("js");

  // 1. Theme Management
  const themeToggleBtn = document.getElementById("theme-toggle");
  const savedTheme = localStorage.getItem("kb-theme");
  const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

  let currentTheme = savedTheme || (systemPrefersDark ? "dark" : "light");
  setTheme(currentTheme);

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener("click", () => {
      currentTheme = currentTheme === "dark" ? "light" : "dark";
      setTheme(currentTheme);
    });
  }

  function setTheme(theme) {
    htmlEl.setAttribute("data-theme", theme);
    localStorage.setItem("kb-theme", theme);
    if (themeToggleBtn) {
      themeToggleBtn.setAttribute("aria-label", `Switch to ${theme === "dark" ? "light" : "dark"} mode`);
      const icon = themeToggleBtn.querySelector(".theme-icon");
      const text = themeToggleBtn.querySelector(".theme-text");
      if (icon && text) {
        icon.textContent = theme === "dark" ? "🌙" : "☀️";
        text.textContent = theme === "dark" ? "Dark" : "Light";
      }
    }
  }

  // 2. Expand / Collapse Sidebar Tree with localStorage persistence
  const savedOpenNodes = JSON.parse(localStorage.getItem("kb-open-nodes") || "null");

  if (savedOpenNodes && Array.isArray(savedOpenNodes)) {
    document.querySelectorAll(".tree-node").forEach(node => {
      if (savedOpenNodes.includes(node.id)) {
        node.open = true;
      }
    });
  }

  // Always ensure the active page's category remains open
  document.querySelectorAll(".tree-node").forEach(node => {
    if (node.querySelector("a.active")) {
      node.open = true;
    }
  });

  document.querySelectorAll(".tree-node").forEach(node => {
    node.addEventListener("toggle", () => {
      const openIds = Array.from(document.querySelectorAll(".tree-node[open]")).map(n => n.id);
      localStorage.setItem("kb-open-nodes", JSON.stringify(openIds));
    });
  });

  const expandBtn = document.getElementById("expand-all-btn");
  const collapseBtn = document.getElementById("collapse-all-btn");

  if (expandBtn && collapseBtn) {
    expandBtn.addEventListener("click", () => {
      document.querySelectorAll(".tree-node").forEach(node => node.open = true);
      const allIds = Array.from(document.querySelectorAll(".tree-node")).map(n => n.id);
      localStorage.setItem("kb-open-nodes", JSON.stringify(allIds));
    });
    collapseBtn.addEventListener("click", () => {
      document.querySelectorAll(".tree-node").forEach(node => {
        if (!node.querySelector("a.active")) {
          node.open = false;
        }
      });
      const remainingOpen = Array.from(document.querySelectorAll(".tree-node[open]")).map(n => n.id);
      localStorage.setItem("kb-open-nodes", JSON.stringify(remainingOpen));
    });
  }

  // 3. Mobile Sidebar Drawer Toggle, Backdrop & Scroll Position Persistence
  const menuBtn = document.getElementById("menu-toggle");
  const sidebar = document.getElementById("sidebar");

  // Ensure a backdrop exists (injected once per page load)
  let backdrop = document.getElementById("sidebar-backdrop");
  if (!backdrop) {
    backdrop = document.createElement("div");
    backdrop.id = "sidebar-backdrop";
    backdrop.className = "sidebar-backdrop";
    document.body.appendChild(backdrop);
  }

  function closeSidebar() {
    if (sidebar) sidebar.classList.remove("open");
    document.body.classList.remove("sidebar-open");
  }

  if (sidebar) {
    const savedScrollPos = localStorage.getItem("kb-sidebar-scroll");
    if (savedScrollPos !== null) {
      sidebar.scrollTop = parseInt(savedScrollPos, 10);
    } else {
      const activeLink = sidebar.querySelector("a.active");
      if (activeLink) {
        activeLink.scrollIntoView({ block: "center" });
      }
    }

    sidebar.addEventListener("scroll", () => {
      localStorage.setItem("kb-sidebar-scroll", sidebar.scrollTop.toString());
    }, { passive: true });
  }

  if (menuBtn && sidebar) {
    menuBtn.addEventListener("click", () => {
      const isOpen = sidebar.classList.toggle("open");
      document.body.classList.toggle("sidebar-open", isOpen);
    });
  }

  backdrop.addEventListener("click", closeSidebar);

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape") closeSidebar();
  });

  // 4. Keyboard Shortcut (Cmd+K / Ctrl+K) to focus Search
  const searchInput = document.getElementById("global-search-input");
  const searchResultsModal = document.getElementById("search-results");

  document.addEventListener("keydown", (e) => {
    if ((e.metaKey || e.ctrlKey) && e.key === "k") {
      e.preventDefault();
      if (searchInput) searchInput.focus();
    }
    if (e.key === "Escape" && searchResultsModal) {
      searchResultsModal.style.display = "none";
    }
  });

  document.addEventListener("click", (e) => {
    if (searchResultsModal && searchInput && !searchResultsModal.contains(e.target) && e.target !== searchInput) {
      searchResultsModal.style.display = "none";
    }
  });

  // 5. Live Quick Search across Page Index
  if (searchInput) {
    let indexData = Array.isArray(window.SEARCH_INDEX) ? window.SEARCH_INDEX : [];
    const rootPrefix = searchInput.dataset.rootPrefix || "./";

    if (!indexData.length) {
      fetch(rootPrefix + "assets/search-index.json")
        .then(res => res.json())
        .then(data => { indexData = data; })
        .catch(err => console.error("Could not load search index", err));
    }

    let debounceTimer = null;
    searchInput.addEventListener("input", (e) => {
      clearTimeout(debounceTimer);
      debounceTimer = setTimeout(() => {
        const q = e.target.value.toLowerCase().trim();
        if (!q || !searchResultsModal) {
          if (searchResultsModal) searchResultsModal.style.display = "none";
          return;
        }

        const matches = indexData.filter(item =>
          item.title.toLowerCase().includes(q) ||
          (item.year && item.year.toString().includes(q)) ||
          (item.cat_name && item.cat_name.toLowerCase().includes(q)) ||
          (item.body && item.body.toLowerCase().includes(q))
        ).slice(0, 10);

        renderSearchResults(matches, rootPrefix);
      }, 120);
    });
  }

  function renderSearchResults(matches, rootPrefix) {
    if (!searchResultsModal) return;
    searchResultsModal.style.display = "block";
    if (matches.length === 0) {
      searchResultsModal.innerHTML = `<div style="padding:1rem; color:var(--muted); font-size:0.875rem;">No matching records found.</div>`;
      return;
    }

    let htmlStr = `<div class="search-dropdown"><ul class="search-list">`;
    matches.forEach(m => {
      htmlStr += `<li><a href="${rootPrefix + m.rel_url}"><span><strong>${escapeHtml(m.title)}</strong></span> <span class="badge-count">${escapeHtml(m.cat_name)}</span></a></li>`;
    });
    htmlStr += `</ul></div>`;
    searchResultsModal.innerHTML = htmlStr;
  }

  // 6. Stat Counters for Dashboard
  function initStatCounters() {
    const statNumbers = document.querySelectorAll(".stat-number[data-count]");
    if (statNumbers.length > 0) {
      const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const target = entry.target;
            const countTo = parseInt(target.getAttribute("data-count"), 10);
            if (isNaN(countTo)) return;

            let current = 0;
            const duration = 900; // ms
            const stepTime = 20;
            const steps = duration / stepTime;
            const increment = countTo / steps;

            const timer = setInterval(() => {
              current += increment;
              if (current >= countTo) {
                target.textContent = countTo;
                clearInterval(timer);
              } else {
                target.textContent = Math.floor(current);
              }
            }, stepTime);

            observer.unobserve(target);
          }
        });
      }, { threshold: 0.5 });

      statNumbers.forEach(num => observer.observe(num));
    }
  }

  initStatCounters();

  // 7. Scroll Reveal Animations
  function initReveal() {
    const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const targets = document.querySelectorAll("[data-reveal]");

    if (reduceMotion || !("IntersectionObserver" in window)) {
      targets.forEach(el => el.classList.add("revealed"));
      return;
    }

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add("revealed");
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });

    targets.forEach(el => {
      el.classList.remove("revealed");
      observer.observe(el);
    });
  }

  initReveal();

  // 8. Header Scroll State & Back-to-Top Button
  const backToTop = document.getElementById("back-to-top");
  const headerEl = document.querySelector(".app-header");

  function onScroll() {
    const y = window.scrollY || document.documentElement.scrollTop;
    if (headerEl) headerEl.classList.toggle("scrolled", y > 8);
    if (backToTop) backToTop.classList.toggle("visible", y > 480);
  }

  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  if (backToTop) {
    backToTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // 9. PJAX Seamless Client-Side Router
  function initPjax() {
    document.addEventListener("click", (e) => {
      const link = e.target.closest("a");
      if (!link) return;

      const href = link.getAttribute("href");
      const isExternalScheme = /^[a-zA-Z][a-zA-Z0-9+.-]*:/.test(href || "");
      if (!href || href.startsWith("#") || isExternalScheme || link.target === "_blank") {
        return;
      }

      e.preventDefault();
      const targetUrl = new URL(href, window.location.href).href;
      if (targetUrl === window.location.href) return;

      fetchAndSwap(targetUrl, true);
    });

    window.addEventListener("popstate", () => {
      fetchAndSwap(window.location.href, false);
    });
  }

  function fetchAndSwap(targetUrl, pushState) {
    fetch(targetUrl)
      .then(res => {
        if (!res.ok) throw new Error("HTTP error " + res.status);
        return res.text();
      })
      .then(htmlText => {
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlText, "text/html");

        // Swap main content
        const newContent = doc.querySelector(".content-inner");
        const currentContent = document.querySelector(".content-inner");
        if (newContent && currentContent) {
          currentContent.innerHTML = newContent.innerHTML;
          currentContent.style.animation = "none";
          currentContent.offsetHeight; // trigger reflow
          currentContent.style.animation = "fadeInUp 0.45s cubic-bezier(0.16, 1, 0.3, 1)";
        }

        // Update document title
        if (doc.title) document.title = doc.title;

        // Push state
        if (pushState) {
          history.pushState(null, "", targetUrl);
        }

        updateSidebarActive(targetUrl);

        // Scroll content to top
        window.scrollTo({ top: 0, behavior: "auto" });

        // Re-render KaTeX math
        if (window.renderMathInElement) {
          window.renderMathInElement(document.body, {
            delimiters: [
              {left: '$$', right: '$$', display: true},
              {left: '$', right: '$', display: false},
              {left: '\\(', right: '\\)', display: false},
              {left: '\\[', right: '\\]', display: true}
            ],
            throwOnError: false
          });
        }

        // Re-init dynamic behaviors on swapped content
        initStatCounters();
        initReveal();
        closeSidebar();
        onScroll();
      })
      .catch(err => {
        console.error("PJAX navigation error, fallback to page load", err);
        window.location.href = targetUrl;
      });
  }

  function updateSidebarActive(targetUrl) {
    const targetPath = new URL(targetUrl, window.location.href).pathname;
    document.querySelectorAll(".tree-list a").forEach(a => {
      const aPath = new URL(a.getAttribute("href"), window.location.href).pathname;
      if (aPath === targetPath) {
        a.classList.add("active");
        const parentNode = a.closest(".tree-node");
        if (parentNode) parentNode.open = true;
      } else {
        a.classList.remove("active");
      }
    });
  }

  initPjax();

  function escapeHtml(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }
});
