import re, json, pathlib, sys
from concurrent.futures import ThreadPoolExecutor
import fitz

root = pathlib.Path('.')
targets = list((root/'raw_sources').rglob('*.pdf')) + list((root/'raw_sources').rglob('*.md')) + list((root/'wiki'/'papers').rglob('*.md'))
url_re = re.compile(r'https?://[^\s\)\]\}>"\']+', re.I)
terms = re.compile(r'(?i)(dataset|data set|data availability|data source|download|repository|github|gitlab|zenodo|kaggle|open data|portal|ACN|Pecan Street|Elaad|Belib|Palo Alto|Boulder|Perth|Dundee|Paris|Caltech|EV charging|electric vehicle charging|smart meter|mobility data)')
def scan(p):
    try:
        if p.suffix.lower()=='.pdf':
            doc = fitz.open(p)
            text = '\n'.join(page.get_text() for page in doc)
            doc.close()
        else:
            text = p.read_text(encoding='utf-8', errors='ignore')
        urls = sorted(set(u.rstrip('.,;:') for u in url_re.findall(text)))
        hits = []
        for m in terms.finditer(text):
            a = max(0, m.start()-220)
            b = min(len(text), m.end()+420)
            snippet = re.sub(r'\s+', ' ', text[a:b]).strip()
            if snippet not in hits:
                hits.append(snippet)
        if urls or hits:
            return {'file': str(p).replace('\\', '/'), 'urls': urls, 'hits': hits[:80]}
        return None
    except Exception as e:
        return {'file': str(p).replace('\\', '/'), 'error': repr(e)}

with ThreadPoolExecutor(max_workers=8) as ex:
    out = [r for r in ex.map(scan, sorted(targets)) if r]

(root/'scan_results.json').write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'scanned={len(targets)} matches={len(out)}')
