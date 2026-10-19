#!/usr/bin/env python3
"""Build blog/pw-experience-2026.html (+ .php twin) from the 2025 post's chrome. Edit the talks / prose below, not the output.
Slide images: blog/images/pwe2026/slide-NN.jpg (rendered from the speakers' released PDFs); speaker photos: experience/speakers/."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'blog' / 'pw-experience-2025.html').read_text(encoding='utf8')

head = src[:src.index('<!-- Hero -->')]
head = re.sub(r'<title>.*?</title>', '<title>PW Experience 2026 — What Modena Taught Us About Heat, Air and Wear | Particleworks Europe</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Particleworks Experience 2026, Modena: six talks on closing thermal balances, calibrating aeration against optical measurements and predicting wear with meshless CFD, with the slides, quotes and moments that matter.">', head, count=1, flags=re.S)
CSS = '''
    /* --- PWEXP26 talk blocks --- */
    .talk-intro { display:flex; gap:1rem; align-items:center; background:linear-gradient(135deg,#fff6f3,#fdeeec); border:1px solid rgba(192,31,36,0.15); border-left:5px solid #c01f24; border-radius:14px; padding:1rem 1.2rem; margin:1.8rem 0 1.1rem; }
    .talk-intro img { width:68px; height:68px; border-radius:50%; object-fit:cover; border:3px solid #fff; box-shadow:0 3px 12px rgba(143,22,27,0.2); flex-shrink:0; }
    .talk-intro .t-time { font-size:0.72rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:#c01f24; }
    .talk-intro h3 { font-size:1.08rem; font-weight:800; line-height:1.3; margin:0.15rem 0 0.2rem; color:var(--pw-dark,#1a1a2e); }
    .talk-intro .t-who { font-size:0.85rem; color:#6c757d; }
    .keypoints { background:#f4f8fc; border:1px solid rgba(0,136,204,0.18); border-radius:14px; padding:1rem 1.3rem 0.6rem; margin:1.1rem 0; }
    .keypoints h5 { font-size:0.72rem; font-weight:800; letter-spacing:1.3px; text-transform:uppercase; color:#006da3; margin:0 0 0.6rem; }
    .keypoints ul { padding-left:1.1rem; margin:0; }
    .keypoints li { font-size:0.92rem; line-height:1.55; margin-bottom:0.45rem; }
    .eng-note { border-left:4px solid #25a361; background:#f3faf6; border-radius:0 12px 12px 0; padding:0.8rem 1.1rem; margin:1.1rem 0; font-size:0.9rem; line-height:1.6; }
    .eng-note b { color:#1e8a51; }
    figure.slide { margin:1.2rem 0 1.6rem; }
    figure.slide img { width:100%; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.10); border:1px solid rgba(0,0,0,0.06); }
    figure.slide figcaption { font-size:0.8rem; color:#6c757d; margin-top:0.5rem; line-height:1.5; }
    html { scroll-behavior:smooth; }
    .article-content { font-size:1.02rem; line-height:1.75; }
    .article-content h2 { margin-top:0.4rem; }
    .sec-eyebrow { display:inline-flex; align-items:center; gap:0.45rem; font-size:0.74rem; font-weight:800; letter-spacing:1.6px; text-transform:uppercase; color:#c01f24; margin:2.6rem 0 0.3rem; }
    .sec-eyebrow::before { content:''; width:26px; height:3px; border-radius:3px; background:linear-gradient(90deg,#d9503f,#8f161b); }
    .sec-lead { font-size:1.08rem; color:#3a4150; margin-bottom:0.4rem; }
    .toc { display:flex; flex-wrap:wrap; gap:0.5rem; margin:1.2rem 0 0.4rem; }
    .toc a { font-size:0.8rem; font-weight:600; text-decoration:none; color:#8f161b; border:1px solid rgba(192,31,36,0.3); border-radius:50px; padding:0.3rem 0.85rem; background:#fff; }
    .toc a:hover { background:#c01f24; color:#fff; }
    .toc small { color:#6c757d; font-weight:500; }
    .standfirst { font-size:1.12rem; line-height:1.6; font-weight:600; color:var(--pw-dark,#1a1a2e); margin:0 0 0.9rem; }
    mark.hl { background:linear-gradient(transparent 55%, rgba(255,196,0,0.38) 55%); color:inherit; padding:0 0.1em; font-weight:600; }
    .statstrip { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:0.7rem; margin:0.4rem 0 1.1rem; }
    .stat { background:#fff; border:1px solid rgba(0,0,0,0.08); border-top:3px solid #c01f24; border-radius:12px; padding:0.7rem 0.9rem; }
    .stat b { display:block; font-size:1.45rem; line-height:1.15; font-weight:800; letter-spacing:-0.5px; color:#8f161b; }
    .stat span { display:block; font-size:0.78rem; color:#5d6670; margin-top:0.2rem; line-height:1.35; }
    .daystats { margin:1.4rem 0 0.4rem; }
    .moments-blog { display:flex; flex-wrap:wrap; gap:0.4rem; align-items:center; margin:-0.6rem 0 1.4rem; }
    .moments-blog .lbl { font-size:0.72rem; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; color:#6c757d; margin-right:0.2rem; }
    .moments-blog a { font-size:0.78rem; font-weight:600; text-decoration:none; color:#c01f24; border:1px solid rgba(192,31,36,0.3); border-radius:50px; padding:0.22rem 0.7rem 0.22rem 0.5rem; background:#fff; }
    .moments-blog a:hover { background:#c01f24; color:#fff; }
    .moments-blog a i { vertical-align:-1px; }
    .blk-label { font-size:0.72rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:#006da3; margin:1.8rem 0 0.5rem; display:flex; align-items:center; gap:0.6rem; }
    .blk-label::after { content:''; flex:1; height:1px; background:rgba(0,136,204,0.22); }
    .finding { display:grid; grid-template-columns:2.1rem 1fr; gap:0.85rem; margin:1.15rem 0; }
    .finding .fn { width:2.1rem; height:2.1rem; border-radius:50%; background:#c01f24; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:0.95rem; margin-top:0.15rem; }
    .finding h4 { font-size:1.05rem; font-weight:800; margin:0 0 0.25rem; color:var(--pw-dark,#1a1a2e); }
    .finding p { margin:0; }
    blockquote.pq { margin:1.5rem 0; padding:1.1rem 1.4rem 0.9rem 1.6rem; background:#fff8e6; border-left:5px solid #ffc400; border-radius:0 14px 14px 0; }
    blockquote.pq p { font-size:1.12rem; line-height:1.55; font-weight:600; font-style:italic; color:#2b2f3a; margin:0 0 0.5rem; }
    blockquote.pq .pqf { font-size:0.82rem; color:#6c757d; display:flex; flex-wrap:wrap; gap:0.4rem 1rem; align-items:center; }
    blockquote.pq .pqf a { font-weight:700; color:#c01f24; text-decoration:none; }
    .pair { display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin:1.2rem 0 1.6rem; }
    .pair figure.slide { margin:0; }
    .chart-card { background:#fff; border:1px solid rgba(0,0,0,0.09); border-radius:14px; padding:1rem 1.2rem 0.7rem; margin:1.3rem 0; box-shadow:0 2px 12px rgba(0,0,0,0.05); }
    .chart-t { font-weight:800; font-size:0.98rem; color:#1a1a2e; }
    .chart-s { font-size:0.8rem; color:#6c757d; margin-bottom:0.4rem; }
    svg.chart { width:100%; height:auto; display:block; }
    svg.chart .cl { font-size:12.5px; fill:#3a4150; font-family:inherit; }
    svg.chart .cv { font-size:12.5px; font-weight:700; fill:#1a1a2e; font-family:inherit; }
    .chart-leg { display:flex; flex-wrap:wrap; gap:0.3rem 1.2rem; font-size:0.78rem; color:#5d6670; margin-top:0.2rem; }
    .chart-leg i { display:inline-block; width:11px; height:11px; border-radius:3px; margin-right:0.35rem; vertical-align:-1px; }
    .chart-two { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    .qa { padding:0.7rem 0; border-top:1px solid rgba(0,0,0,0.08); }
    .qa b { display:block; color:#1a1a2e; } .qa span { display:block; color:#4a5260; font-size:0.95rem; margin-top:0.15rem; }
    @media(max-width:700px){ .pair, .chart-two { grid-template-columns:1fr; } }
    @media(max-width:560px){ .talk-intro { flex-direction:column; text-align:center; } }
  </style>'''
head = head.replace('</style>', CSS, 1)

tail = src[src.index('<!-- Related Content -->'):]
tail = tail.replace('''<a href="pw-experience-2024.html" class="related-card">
                <h5>PW Experience 2024</h5>
                <p>Eleven presentations from Munich 2024 — meshless CFD goes mainstream.</p>''',
'''<a href="pw-experience-2025.html" class="related-card">
                <h5>PW Experience 2025</h5>
                <p>Munich 2025 — from validation to virtual prototyping.</p>''')
tail = tail.replace('''<a href="particleworks-82.html" class="related-card">
                <h5>Particleworks v8.2 Release</h5>
                <p>EIMPS solver, LBM coupling, anisotropic thermal and more.</p>''',
'''<a href="../experience/proceedings2026.php" class="related-card">
                <h5>Proceedings 2026</h5>
                <p>Slides and key findings of every released talk.</p>''')



import sys
sys.path.insert(0, str(root))
from _pwexp26_content import TALKS, ORDER, TAKEAWAYS, SKF_SPHERE, TRK_ERR, DFL_AIR, BRG_SEP


def mm(t):
    return f'{t // 60}:{t % 60:02d}'


def hl(x):
    return f'<mark class="hl">{x}</mark>'


def md(t):
    """**x** -> highlight"""
    return re.sub(r'\*\*(.+?)\*\*', lambda m: hl(m.group(1)), t)


def link(tid, t):
    return f'../experience/proceedings2026.php?talk={tid}&amp;t={t}#talk-{tid}'


# ---------- small SVG charts (no libs) ----------
RED, BLUE, GREEN, GREY, AMBER = '#c01f24', '#0088cc', '#25a361', '#8a94a0', '#d98a00'


def hbars(title, sub, items, unit, ref=None, vmax=None, colors=None):
    """horizontal bars. items: (label, value, kind) kind in ref/bad/mid/good/plain"""
    vmax = vmax or max(v for _, v, *_ in items) * 1.12
    W, lw, rw, rh = 640, 300, 60, 30
    H = 22 + rh * len(items) + 14
    cmap = colors or {'ref': '#1a1a2e', 'bad': RED, 'mid': AMBER, 'good': GREEN, 'plain': BLUE}
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="{title}" class="chart">']
    bw = W - lw - rw
    for i, it in enumerate(items):
        lab, v, k = it[0], it[1], (it[2] if len(it) > 2 else 'plain')
        y = 10 + i * rh
        out.append(f'<text x="{lw - 8}" y="{y + 17}" text-anchor="end" class="cl">{lab}</text>')
        out.append(f'<rect x="{lw}" y="{y + 3}" width="{bw * v / vmax:.1f}" height="19" rx="4" fill="{cmap[k]}"/>')
        out.append(f'<text x="{lw + bw * v / vmax + 6:.1f}" y="{y + 18}" class="cv">{v:g}{unit}</text>')
    if ref is not None:
        x = lw + bw * ref / vmax
        out.append(f'<line x1="{x:.1f}" y1="4" x2="{x:.1f}" y2="{H - 8}" stroke="#1a1a2e" stroke-dasharray="4 3" stroke-width="1.4"/>')
    out.append('</svg>')
    return f'<div class="chart-card"><div class="chart-t">{title}</div><div class="chart-s">{sub}</div>{"".join(out)}</div>'


def chart_sphere():
    return hbars('One sphere, nine answers', 'Surface-average heat-transfer coefficient, W/m²K. Dashed line: Whitaker correlation, 184.',
                 SKF_SPHERE, '', ref=184, vmax=215)


def chart_trk():
    cases = TRK_ERR['cases']; items = TRK_ERR['items']
    W, H, x0, y0, bh = 640, 40 + 28 * len(items) * 2 // 1, 150, 24, 10
    rows = len(items)
    H = 40 + rows * 34
    sc = 14  # px per %
    zero = x0 + 12 * sc / 2 + 70
    zero = 330
    out = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Error against bench test" class="chart">']
    out.append(f'<line x1="{zero}" y1="8" x2="{zero}" y2="{H - 22}" stroke="#1a1a2e" stroke-width="1.2"/>')
    for g in (-10, -5, 5, 10):
        out.append(f'<text x="{zero + g * 14}" y="{H - 6}" text-anchor="middle" class="cl" fill="#8a94a0">{g:+d}%</text>')
        out.append(f'<line x1="{zero + g * 14}" y1="8" x2="{zero + g * 14}" y2="{H - 22}" stroke="#e5e9ee"/>')
    for i, (lab, e1, e2) in enumerate(items):
        y = 12 + i * 34
        out.append(f'<text x="{zero - 12 * 14 - 12}" y="{y + 17}" text-anchor="end" class="cl">{lab}</text>')
        for j, (e, col) in enumerate(((e1, RED), (e2, GREEN))):
            yy = y + j * 13
            x = zero + min(e, 0) * 14
            out.append(f'<rect x="{x:.1f}" y="{yy}" width="{abs(e) * 14:.1f}" height="11" rx="3" fill="{col}"/>')
            tx = zero + e * 14 + (6 if e >= 0 else -6)
            out.append(f'<text x="{tx:.1f}" y="{yy + 10}" text-anchor="{"start" if e >= 0 else "end"}" class="cv">{e:+.1f}%</text>')
    out.append('</svg>')
    leg = f'<div class="chart-leg"><span><i style="background:{RED}"></i>Case 1</span><span><i style="background:{GREEN}"></i>Case 2 (higher speed, lower load)</span></div>'
    return f'<div class="chart-card"><div class="chart-t">Error against the bench test, component by component</div><div class="chart-s">Simulated minus measured temperature, in % (TrackOne, slides 18–19).</div>{"".join(out)}{leg}</div>'


def chart_dfl():
    a = hbars('Air content in the gearbox', 'Percent of oil volume.', [(l, v, 'bad' if i == 0 else 'good' if i == 1 else 'ref') for i, (l, v) in enumerate(DFL_AIR['air'])], ' %', vmax=0.55)
    b = hbars('Average bubble diameter', 'Micrometres.', [(l, v, 'bad' if i == 0 else 'good' if i == 1 else 'ref') for i, (l, v) in enumerate(DFL_AIR['bub'])], ' µm', vmax=900)
    return f'<div class="chart-two">{a}{b}</div>'


def chart_brg():
    return hbars('Sand that leaves through the clean outlet', 'Percent of the sand fed, from the simulation (Börger / EnginSoft).', [(l, v, 'good' if i == 0 else 'bad') for i, (l, v) in enumerate(BRG_SEP)], ' %', vmax=30)


CHARTS = {'sphere': chart_sphere, 'trk': chart_trk, 'dfl': chart_dfl, 'brg': chart_brg}


# ---------- blocks ----------
def label(t):
    return f'<div class="blk-label">{t}</div>'


def fig(f, cap, title):
    return f'<figure class="slide"><img src="images/pwe2026/{f}.jpg" alt="{title} — slide" loading="lazy"><figcaption><b>Slide.</b> {cap}</figcaption></figure>'


def figpair(items, title):
    ims = ''.join(f'<figure class="slide"><img src="images/pwe2026/{f}.jpg" alt="{title} — slide" loading="lazy"><figcaption>{cap}</figcaption></figure>' for f, cap in items)
    return f'<div class="pair">{ims}</div>'


def quote(tid, q, who, t):
    return (f'<blockquote class="pq"><p>“{q}”</p><div class="pqf">{who} <a href="{link(tid, t)}"><i class="bi bi-play-fill"></i> {mm(t)} Watch the moment</a></div></blockquote>')


def finding(n, head, text):
    return f'<div class="finding"><span class="fn">{n}</span><div><h4>{head}</h4><p>{md(text)}</p></div></div>'


def talk(tid):
    d = TALKS[tid]
    parts = [f'<div class="talk-intro" id="talk-{tid}"><img src="../experience/speakers/{d["photo"][0]}" alt="{d["photo"][1]}"><div><div class="t-time">{d["tag"]} · {d["time"]}</div><h3>{d["title"]}</h3><div class="t-who">{d["who"]}</div></div></div>',
             f'<p class="standfirst">{md(d["lead"])}</p>',
             label('The context')]
    parts += [f'<p>{md(p)}</p>' for p in d['context']]
    parts.append(fig(*d['slideA'], d['title']))
    parts.append(label('What they found'))
    qpos = dict(zip(d['quote_pos'], d['quotes']))
    for i, (h, t) in enumerate(d['findings']):
        parts.append(finding(i + 1, h, t))
        if i in qpos:
            q = qpos[i]; parts.append(quote(tid, q[0], q[1], q[2]))
        if d.get('chart') and i == d.get('chart_after', 1):
            parts.append(CHARTS[d['chart']]())
    if d.get('pair'):
        parts.append(figpair(d['slidesB'], d['title']))
    elif len(d['slidesB']) == 2:
        parts.append(figpair(d['slidesB'], d['title']))
    else:
        for f, cap in d['slidesB']:
            parts.append(fig(f, cap, d['title']))
    if d.get('note'):
        parts.append(f'<div class="eng-note"><b>Engineering note.</b> {d["note"]}</div>')
    parts.append(f'<div class="keypoints"><h5>In short</h5><ul>{"".join(f"<li>{md(k)}</li>" for k in d["keys"])}</ul></div>')
    mo = ''.join(f'<a href="{link(tid, t)}"><i class="bi bi-play-fill"></i> {mm(t)} {lab}</a>' for t, lab in d['moments'])
    parts.append(f'<div class="moments-blog"><span class="lbl">Watch the moment</span>{mo}</div>')
    return '\n            '.join(parts)


def sec(eyebrow, h2, lead):
    return f'\n            <div class="sec-eyebrow">{eyebrow}</div>\n            <h2>{h2}</h2>\n            <p class="sec-lead">{lead}</p>'


SECT = {
    '04': sec('01 · Heat', 'From side effect to deliverable', 'Three talks treated temperature as a result to deliver. They share one trick: ' + hl('never run oil and metal on the same clock.') + ' The oil is simulated briefly, its heat-transfer map is handed to a steady solution of the solids, and the result is checked against something physical.'),
    '07': sec('02 · Air', 'Measure it before you simulate it', 'Aeration changes viscosity, density, film thickness and oxidation. The afternoon showed how to put a measured number on it before the model is asked to predict it.'),
    '05': sec('03 · Wear', 'Simulating what breaks', 'Two very different machines, one question: can a particle simulation say where, and how fast, the hardware will wear?'),
}
HR = '\n\n            <hr class="section-rule">\n'
body_talks = ''
for tid in ['04', '06', '10', '07', '05', '11']:
    if tid in SECT:
        body_talks += HR + SECT[tid]
    body_talks += '\n            ' + talk(tid) + '\n'

stat = lambda v, l: f'<div class="stat"><b>{v}</b><span>{l}</span></div>'
QA = [
    ('How many manual iterations does the pump model take?', 'Three to five, and a steady CHT converges in minutes on a GPU. “Sometimes the setup is longer than the simulation itself.” (R&amp;D CFD)'),
    ('Does an aeration calibration transfer?', 'Across geometry yes, across speed by scaling, across additives no: the same base oil with another additive package needs a new one, and the temperature trend can flip sign. (deepfluid)'),
    ('Why start from such basic verification cases?', 'Because once a bearing rotates there is no good reference model; complexity is added step by step. (SKF)'),
    ('What do owners want from a Pelton simulation?', 'Not newtons: what 2&nbsp;% of efficiency lost to one flood costs over a year, and when to refurbish. (HES-SO)'),
]
toc = ''.join(f'<a href="#talk-{t}">{TALKS[t]["tag"]} · {TALKS[t]["short_org"]} <small>{TALKS[t]["topic"]}</small></a>' for t in ['04', '06', '10', '07', '05', '11'])
BODY = '''
  <!-- Hero -->
  <section class="blog-hero">
    <div class="container">
      <div class="version-badge"><i class="bi bi-calendar-event me-1"></i> PW Experience 2026</div>
      <h1>What Modena Taught Us About Heat, Air and Wear</h1>
      <p class="lead">Modena, October 7, 2026 — six talks: the context, what they found, the sentence worth quoting and the moment to watch</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 18 min read</span>
        <span><i class="bi bi-tag"></i> Conference Highlights</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p class="standfirst">On October 7, Particleworks users filled the BPER FORUM Monzani in Modena for a day built around three questions: ''' + hl('where does the heat go, where does the air go, and where does the material wear?') + '''</p>

            <p>Speakers from a bearing maker, a pump manufacturer, a hydropower research project and several engineering firms answered them with the same discipline. Each put simulation next to a thermocouple, an optical sensor or a worn prototype, and said plainly how well they agreed. Each talk below starts with its context, then what was found, with the slides that carry it and a sentence taken straight from the recording. Every “Watch the moment” link opens the video at that second on the <a href="../experience/proceedings2026.php">proceedings page</a>.</p>

            <div class="statstrip daystats">
              ''' + stat('1.5 h', 'per case for a pump thermal model, once the model exists') + stat('66 → 169', 'W/m²K: the same sphere, read at the wall or 1.5&nbsp;mm away (target 184)') + stat('0.45 vs 0.43 %', 'simulated vs measured air in a gearbox, after calibration') + stat('10 → 25 %', 'sand lost when the separator flow rate is doubled') + '''
            </div>

            <div class="toc">''' + toc + '''</div>

            <hr class="section-rule">
''' + body_talks + '''
            <hr class="section-rule">

            <div class="sec-eyebrow">From the floor</div>
            <h2>The questions that mattered</h2>
            ''' + ''.join(f'<div class="qa"><b>{q}</b><span>{a}</span></div>' for q, a in QA) + '''

            <hr class="section-rule">

            <div class="sec-eyebrow">Take-home</div>
            <h2>What we take home</h2>

            <div class="keypoints"><h5>Four things the day showed</h5><ul>
              ''' + ''.join(f'<li><strong>{h}.</strong> {t}</li>' for h, t in TAKEAWAYS) + '''
            </ul></div>

            <p>Meshless CFD in Modena looked less like a promise and more like a tool with a known price, and with speakers who were exact about it.</p>

            <div class="cta-box">
              <h3>Get the Modena proceedings</h3>
              <p>Slides, recordings and the key findings of each released presentation, free after a short form.</p>
              <a href="../experience/proceedings2026.php" class="btn-pw"><i class="bi bi-unlock me-2"></i>Open the proceedings</a>
            </div>

          </article>
        </div>
      </div>
    </div>
  </section>

  '''

html = head + BODY.lstrip('\n') + tail
(root / 'blog' / 'pw-experience-2026.html').write_text(html, encoding='utf8')
php = re.sub(r'href="((?:\.\./)?[A-Za-z0-9_\-/]+)\.html', r'href="\1.php', html)
(root / 'blog' / 'pw-experience-2026.php').write_text(php, encoding='utf8')
art = html[html.index('<article'):html.index('</article>')]
txt = re.sub(r'<svg.*?</svg>', ' ', art, flags=re.S)
print('words in article:', len(re.sub(r'<[^>]+>', ' ', txt).split()))
