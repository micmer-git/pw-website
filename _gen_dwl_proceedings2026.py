#!/usr/bin/env python3
"""experience/dwl-proceedings-2026.php — the OPEN download page of the 2026 proceedings, same job and same block markup as
dwl-proceedings-2024/2025.php (which the customer portal scrapes): one `row bg-light` block per talk with photo, 'Org | Speaker', title,
abstract, PDF download and the YouTube embed. Unlisted (noindex); the gated page is proceedings2026.php.
PDFs are NOT in git: they sit in /experience/2026/proceedings/ on the web host (see the deploy bundle)."""
import re, json, pathlib, sys
root = pathlib.Path(__file__).parent
sys.path.insert(0, str(root))
from _pwexp26_content import TALKS
TALKS['09'] = dict(short_org='Univance', org='Univance Corporation (JP)', speaker='Naohiro Fujita', photo=('naohiro-fujita.jpg', 'Naohiro Fujita'), title='Application of Particleworks to Gear Lubrication Analysis and Its Expansion to R&amp;D on Airflow Effects', pdf='09.UNIVANCE-NAOHIRO-FUJITA.pdf')
from _experience_chrome import fix_nav, fix_footer

YT = {'04': 'qVtrBzDs-co', '05': 'lef8A75FZ5k', '06': '7ITTalQNChs', '07': 'Ip6wCIB_bSM', '10': 'uFIH9fnBhh4', '11': 'X9gMb70HHJ8'}
AB = json.loads((root / '_pwexp26_abstracts.json').read_text(encoding='utf8'))
reg = (root / '_templates' / 'experience-registration.html').read_text(encoding='utf8')
head = reg[:reg.index('</style>')]
head = re.sub(r'<title>.*?</title>', '<title>2026 Proceedings — Particleworks Experience | Modena, October 7</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Presentations and recordings of Particleworks Experience 2026, Modena.">', head, flags=re.S)
head = head.replace('<head>', '<head>\n  <meta name="robots" content="noindex,nofollow">', 1)
nav = fix_nav(reg[reg.index('<!-- Navbar -->'):reg.index('<!-- Hero -->')])
foot = fix_footer(reg[reg.index('<!-- Footer -->'):])
css = '''
    .dwl-hero { padding:8.5rem 0 3.5rem; background:linear-gradient(135deg, rgba(217,80,63,0.88), rgba(143,22,27,0.95)); text-align:center; }
    .dwl-hero h1 { color:#fff; font-weight:900; font-size:clamp(2.2rem,5vw,3.4rem); letter-spacing:-1px; }
    .dwl-hero p { color:rgba(255,255,255,0.85); font-size:1.1rem; margin:0.6rem 0 0; }
    .dwl-list { padding:3rem 0 4rem; background:#f6fafd; }
    .dwl-list .row.bg-light { border:1px solid rgba(0,0,0,0.07); border-radius:18px; margin:0 0 1.4rem; align-items:flex-start; background:#fff !important; }
    .dwl-list img.rounded-circle { width:150px; height:150px; object-fit:cover; border:5px solid #fff; box-shadow:0 6px 18px rgba(143,22,27,0.18); }
    .dwl-list h5 { font-size:0.82rem; font-weight:700; letter-spacing:0.5px; text-transform:uppercase; color:#6c757d; }
    .dwl-list h4 { font-size:1.12rem; font-weight:800; color:#c01f24; line-height:1.3; }
    .dwl-list p { font-size:0.92rem; line-height:1.6; color:#334; }
    .dwl-list .btn-primary { background:#c01f24; border-color:#c01f24; border-radius:50px; font-weight:600; font-size:0.9rem; }
    .dwl-list .ratio iframe { border:0; border-radius:12px; }
'''
def video(k, d):
    if k not in YT: return '<p class="small text-muted">Slides only: no recording of this talk.</p>'
    return f'<div class="ratio ratio-16x9"><iframe src="https://www.youtube.com/embed/{YT[k]}" title="{d["short_org"]} presentation" loading="lazy" allowfullscreen></iframe></div>'
order = ['04', '05', '06', '07', '09', '10', '11']
blocks = ''
for k in order:
    d = TALKS[k]
    pdf = '/experience/2026/proceedings/' + d['pdf']
    org = d['org'].split(' (')[0].replace('&', '&amp;')
    blocks += f'''
      <!-- {d["short_org"]} -->
      <div class="row bg-light p-3 align-items-start">
        <div class="col-lg-3 col-md-4 text-center">
          <img alt="{d["photo"][1]}" class="rounded-circle border border-5 img-fluid mb-3" src="speakers/{d["photo"][0]}" />
          <p><a href="{pdf}" target="_blank" rel="noopener" class="btn btn-primary"><i class="bi bi-file-earmark-pdf me-2"></i>Download presentation</a></p>
        </div>
        <div class="col-lg-5 col-md-8">
          <h5>{org} | {d["speaker"].replace("&", "&amp;")}</h5>
          <h4>{d["title"].replace("&", "&amp;") if "&amp;" not in d["title"] else d["title"]}</h4>
          {AB.get(k, "")}
        </div>
        <div class="col-lg-4">{video(k, d)}
        </div>
      </div>'''
body = f'''
  <section class="dwl-hero"><div class="container"><h1>2026 Proceedings</h1><p>Particleworks Experience 2026 · Modena · October 7 — presentations and recordings</p></div></section>
  <section class="dwl-list"><div class="container">{blocks}
    <p class="text-center mt-4"><a href="../blog/pw-experience-2026.php">Read the story of the day</a> · <a href="proceedings2025.php">Proceedings 2025</a> · <a href="proceedings2024.php">Proceedings 2024</a></p>
  </div></section>
'''
out = head + css + '  </style>\n</head>\n<body>\n\n  ' + nav + '\n' + body + '\n  ' + foot
for ext in ('php', 'html'):
    (root / 'experience' / f'dwl-proceedings-2026.{ext}').write_text(out, encoding='utf8')
print('dwl-proceedings-2026 written', len(out))
