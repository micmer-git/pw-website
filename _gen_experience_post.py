#!/usr/bin/env python3
"""Post-event Experience microsite: landing page that leads to the proceedings form, Program and Registration retired
(redirect stubs), Technical Session page kept but without registration CTAs. Run after _gen_proceedings2026.py's inputs are in place:
    python _gen_experience_post.py && python _gen_proceedings2026.py
Sources frozen on first run (so the originals survive being replaced): _templates/experience-registration.html (head/css/nav/footer
used by the proceedings page) and _pwexp26_abstracts.json (public abstracts copied from the old program page)."""
import re, json, pathlib
root = pathlib.Path(__file__).parent
exp = root / 'experience'
import sys; sys.path.insert(0, str(root))
from _experience_chrome import fix_nav, fix_footer
from _pwexp26_content import TALKS, TAKEAWAYS

tpl = root / '_templates' / 'experience-registration.html'
if not tpl.exists():
    tpl.parent.mkdir(exist_ok=True)
    tpl.write_text((exp / 'registration.html').read_text(encoding='utf8'), encoding='utf8')
ab = root / '_pwexp26_abstracts.json'
if not ab.exists():
    prog = (exp / 'program.html').read_text(encoding='utf8')
    KEY = {'04': 'Lanciotti', '06': 'Lijun Cao', '10': 'Tiberi', '07': 'Hafner', '05': 'Decaix', '11': 'Valtwies', '02': 'Raimondo'}
    out = {}
    for a in prog.split('<article class="talk"')[1:]:
        for k, name in KEY.items():
            if name in a and '<div class="abs">' in a and k not in out:
                x = a[a.index('<div class="abs">') + 17:]
                out[k] = ''.join(re.findall(r'<p>.*?</p>', x[:x.index('<div class="authors">')], flags=re.S))
    ab.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding='utf8')

# ---------------------------------------------------------------- landing
old = (exp / 'index.html').read_text(encoding='utf8')
if 'post-event' not in old:
    head = old[:old.index('<section class="hero">')]
    head = re.sub(r'<title>.*?</title>', '<title>Particleworks Experience 2026 — Thank you, Modena | Proceedings now online</title>', head, flags=re.S)
    head = re.sub(r'<meta name="description" content=".*?">', '<meta name="description" content="Particleworks Experience 2026, Modena, October 6–7: thank you. Slides, recordings and key findings of the released talks are online.">', head, flags=re.S)
    head = fix_nav(head).replace('</style>', '''
    /* post-event */
    .take-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:1rem; }
    .take { background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:18px; padding:1.3rem 1.4rem; }
    .take .n { width:34px; height:34px; border-radius:10px; background:var(--ev-accent); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.8rem; }
    .take b { display:block; margin-bottom:0.3rem; } .take p { margin:0; font-size:0.9rem; color:#445; line-height:1.55; }
    .tag { display:inline-block; font-size:0.68rem; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; color:var(--ev-crimson); margin-bottom:0.15rem; }
  </style>''', 1)
    FLAG = {'04': '🇮🇹', '05': '🇨🇭', '06': '🇳🇱', '07': '🇩🇪', '10': '🇮🇹', '11': '🇩🇪'}
    ICON = {'04': 'thermometer-half', '05': 'water', '06': 'record-circle', '07': 'camera', '10': 'truck', '11': 'funnel'}
    cards = ''.join(
        f'''<div class="col-md-6 col-lg-5"><a href="proceedings2026.php#talks" class="text-decoration-none text-reset"><div class="topic">
            <div class="ic"><i class="bi bi-{ICON[k]}"></i></div>
            <div><span class="tag">{TALKS[k]["tag"]}</span><h4>{TALKS[k]["title"] if len(TALKS[k]["title"]) < 95 else "Direct Optical Air-in-Oil Measurement for Gearings &amp; Hydraulics"}</h4><div class="org">{TALKS[k]["org"].replace("&", "&amp;")} {FLAG[k]}</div></div>
          </div></a></div>''' for k in ['04', '06', '10', '07', '05', '11'])
    take = ''.join(f'<div class="take"><div class="n">{i + 1}</div><b>{h}</b><p>{t}</p></div>' for i, (h, t) in enumerate(TAKEAWAYS))
    body = f'''<!-- post-event landing -->
  <section class="hero">
    <div class="container">
      <div class="badge-year"><i class="bi bi-heart-fill"></i> Thank you, Modena</div>
      <h1 class="sr-only">Particleworks Experience 2026 — European Edition, Modena, October 6–7: proceedings now online</h1>
      <div class="hero-banner"><img src="../images/experience2026/banner-2026.jpg" alt="Particleworks Experience 2026 — European Edition · October 6-7, 2026 · Modena, Italy"></div>
      <p class="lead">Two days with the meshless CFD community in Modena. The <strong>proceedings are online</strong>: slides, recordings and the key findings of every talk the speakers released.</p>
      <div class="hero-meta">
        <span class="m"><i class="bi bi-calendar-event"></i> October 6–7, 2026</span>
        <span class="m"><i class="bi bi-geo-alt"></i> BPER FORUM Monzani, Modena · Italy</span>
      </div>
      <div class="hero-cta">
        <a href="proceedings2026.php" class="btn-pw"><i class="bi bi-unlock"></i> Get the proceedings</a>
        <a href="../blog/pw-experience-2026.php" class="btn-ghost"><i class="bi bi-journal-text"></i> Read the story of the day</a>
      </div>
    </div>
  </section>

  <section class="topics">
    <div class="container">
      <div class="sec-head">
        <div class="kick">Conference Day · October 7</div>
        <h2>What the day showed</h2>
        <p>Heat, air and wear, seen through meshless simulation.</p>
      </div>
      <div class="take-grid">{take}</div>
    </div>
  </section>

  <section class="topics" style="padding-top:2rem">
    <div class="container">
      <div class="sec-head">
        <div class="kick">The talks</div>
        <h2>Six talks with slides and recordings</h2>
        <p>Abstracts of all eleven talks are open. Slides, recordings and key findings open after a short form. The Prometech, IAV and Univance talks are slides only.</p>
      </div>
      <div class="row g-3 justify-content-center">{cards}
        <div class="col-md-6 col-lg-5 d-flex">
          <a href="proceedings2026.php" class="btn-pw w-100 justify-content-center align-self-stretch" style="border-radius:16px;"><i class="bi bi-file-earmark-text"></i> Fill in the form</a>
        </div>
      </div>
    </div>
  </section>

  <section class="days" style="padding-top:2rem">
    <div class="container">
      <div class="row g-4 justify-content-center">
        <div class="col-lg-7">
          <a href="workshop.php" class="day-card conf">
            <span class="ribbon"><i class="bi bi-arrow-right-circle"></i> Look back</span>
            <div class="date-row"><span class="dnum">06</span><span class="dmon">October 2026 · Tuesday</span></div>
            <h3>Technical Session</h3>
            <p>What's new in <strong>Particleworks 9.0</strong>, advanced modeling techniques and use cases — AI-driven automation, CHT, multi-phase, FSI, CFD+DEM.</p>
            <span class="go">See the six topics <i class="bi bi-arrow-right"></i></span>
          </a>
        </div>
      </div>
    </div>
  </section>

  <section class="cta-final" id="proceedings">
    <div class="container text-center">
      <h2>Get the slides and recordings</h2>
      <p>One short form gives access to every released talk. This browser keeps the access for 7 days. Earlier editions stay online.</p>
      <div class="hero-cta justify-content-center">
        <a href="proceedings2026.php" class="btn-pw"><i class="bi bi-unlock"></i> Get the proceedings</a>
        <a href="https://particleworks-europe.com/experience/proceedings2025.php" class="btn-ghost"><i class="bi bi-calendar3"></i> Proceedings 2025</a>
      </div>
    </div>
  </section>

  '''
    foot = old[old.index('<!-- Footer -->'):]
    (exp / 'index.html').write_text(head + body + fix_footer(foot), encoding='utf8')
    (exp / 'index.php').write_text(head + body + fix_footer(foot), encoding='utf8')

# ---------------------------------------------------------------- workshop: keep, drop registration/program
for ext in ('html', 'php'):
    p = exp / f'workshop.{ext}'
    s = open(p, encoding='utf8', newline='').read()
    if 'registration.php' in s or 'program.php' in s:
        s = fix_footer(fix_nav(s))
        s = s.replace('href="registration.php" class="btn-pw"><i class="bi bi-pencil-square"></i> Register now</a>', 'href="proceedings2026.php" class="btn-pw"><i class="bi bi-unlock"></i> Proceedings 2026</a>')
        s = s.replace('href="registration.php" class="btn-pw"><i class="bi bi-pencil-square"></i> Register</a>', 'href="proceedings2026.php" class="btn-pw"><i class="bi bi-unlock"></i> Proceedings 2026</a>')
        s = s.replace('href="registration.php" class="btn-pw float-reg"><i class="bi bi-pencil-square"></i> Register</a>', 'href="proceedings2026.php" class="btn-pw float-reg"><i class="bi bi-unlock"></i> Proceedings 2026</a>')
        s = s.replace('href="program.php"', 'href="proceedings2026.php"')
        s = s.replace('href="registration.php"', 'href="proceedings2026.php"')
        open(p, 'w', encoding='utf8', newline='').write(s)

# ---------------------------------------------------------------- retired pages: redirect to the proceedings
STUB = '''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="https://particleworks-europe.com/experience/proceedings2026.php">
<meta http-equiv="refresh" content="0; url=proceedings2026.php"><title>Particleworks Experience 2026</title></head>
<body style="font-family:sans-serif"><p>Particleworks Experience 2026 took place on 6–7 October in Modena. <a href="proceedings2026.php">Open the proceedings</a>.</p></body></html>
'''
for n in ('program', 'registration'):
    (exp / f'{n}.html').write_text(STUB, encoding='utf8')
    (exp / f'{n}.php').write_text('<?php header("Location: proceedings2026.php", true, 301); exit; ?>\n' + STUB, encoding='utf8')
print('experience post-event pages written')
