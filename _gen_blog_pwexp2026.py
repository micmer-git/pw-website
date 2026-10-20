#!/usr/bin/env python3
"""Build blog/pw-experience-2026.html (+ .php twin) from the 2025 post's chrome. Edit the talks / prose below, not the output.
Slide images: blog/images/pwe2026/slide-NN.jpg (rendered from the speakers' released PDFs); speaker photos: experience/speakers/."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'blog' / 'pw-experience-2025.html').read_text(encoding='utf8')

head = src[:src.index('<!-- Hero -->')]
head = re.sub(r'<title>.*?</title>', '<title>Heat, air and wear: six talks from Particleworks Experience 2026 | Particleworks Europe</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Six talks from Particleworks Experience 2026 in Modena: thermal models checked against thermocouples, an aeration model calibrated on measured bubbles, and wear predicted for a Pelton runner and a sand separator. With slides, quotes and video.">', head, count=1, flags=re.S)
CSS = '''
    /* --- PWEXP26 talk blocks --- */
    .talk-intro { display:flex; gap:1rem; align-items:center; background:linear-gradient(135deg,#fff6f3,#fdeeec); border:1px solid rgba(192,31,36,0.15); border-left:5px solid #c01f24; border-radius:14px; padding:1rem 1.2rem; margin:1.8rem 0 1.1rem; }
    .talk-intro img { width:68px; height:68px; border-radius:50%; object-fit:cover; border:3px solid #fff; box-shadow:0 3px 12px rgba(143,22,27,0.2); flex-shrink:0; }
    .talk-intro .t-time { font-size:0.72rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:#c01f24; }
    .talk-intro h3 { font-size:1.08rem; font-weight:800; line-height:1.3; margin:0.15rem 0 0.2rem; color:var(--pw-dark,#1a1a2e); }
    .talk-intro .t-who { font-size:0.85rem; color:#6c757d; }
    .keypoints { background:#fff6f1; border:1px solid rgba(192,31,36,0.16); border-radius:14px; padding:1rem 1.3rem 0.6rem; margin:1.1rem 0; }
    .keypoints h5 { font-size:0.72rem; font-weight:800; letter-spacing:1.3px; text-transform:uppercase; color:#8f161b; margin:0 0 0.6rem; }
    .keypoints ul { padding-left:1.1rem; margin:0; }
    .keypoints li { font-size:0.92rem; line-height:1.55; margin-bottom:0.45rem; }
    .eng-note { border-left:4px solid #c01f24; background:linear-gradient(135deg,#fff3ea,#ffe9df); border-radius:0 14px 14px 0; padding:1rem 1.3rem 1.05rem; margin:1.4rem 0; font-size:0.94rem; line-height:1.6; }
    .eng-note .en-h { font-size:0.72rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:#b4421f; margin:0 0 0.45rem; }
    .eng-note p { margin:0 0 0.7rem; }
    .eq-list { display:grid; gap:0.5rem; margin:0.2rem 0 0.1rem; }
    .eq { display:grid; grid-template-columns:minmax(7.5rem,10rem) 1fr; gap:0.2rem 1rem; align-items:baseline; background:rgba(255,255,255,0.7); border:1px solid rgba(192,31,36,0.14); border-radius:10px; padding:0.55rem 0.9rem; }
    .eq-l { font-size:0.74rem; font-weight:700; letter-spacing:0.4px; text-transform:uppercase; color:#8f161b; }
    .eq-m { font-family:"Cambria Math","STIX Two Math","Latin Modern Math",Cambria,Georgia,serif; font-size:1.12rem; color:#2b2f3a; overflow-x:auto; white-space:nowrap; }
    .eq-m var { font-style:italic; }
    .eq-m sub, .eq-m sup { font-size:0.68em; line-height:0; }
    .eq-m .sum { font-size:1.25em; }
    .eq-m .n { font-style:normal; }
    @media(max-width:560px){ .eq { grid-template-columns:1fr; } }
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
    mark.hl { background:linear-gradient(transparent 62%, rgba(217,80,63,0.22) 62%); color:inherit; padding:0 0.05em; font-weight:inherit; }
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
    .blk-label { font-size:0.72rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:#8f161b; margin:1.8rem 0 0.5rem; display:flex; align-items:center; gap:0.6rem; }
    .blk-label::after { content:''; flex:1; height:1px; background:rgba(192,31,36,0.22); }
    .finding { display:grid; grid-template-columns:2.1rem 1fr; gap:0.85rem; margin:1.15rem 0; }
    .finding .fn { width:2.1rem; height:2.1rem; border-radius:50%; background:#c01f24; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:0.95rem; margin-top:0.15rem; }
    .finding h4 { font-size:1.05rem; font-weight:800; margin:0 0 0.25rem; color:var(--pw-dark,#1a1a2e); }
    .finding p { margin:0; }
    blockquote.pq { margin:1.5rem 0; padding:1.1rem 1.4rem 0.9rem 1.6rem; background:#fff4ec; border-left:5px solid #d9503f; border-radius:0 14px 14px 0; }
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
    /* --- Modena palette (the experience microsite red, no blue) --- */
    :root { --pw-blue:#c01f24; --pw-blue-dark:#8f161b; --pw-green:#d9503f; --pw-green-dark:#b4421f;
            --pw-gradient:linear-gradient(135deg,#d9503f,#8f161b); --pw-gradient-dark:linear-gradient(135deg,#8f161b,#c01f24 60%,#d9503f); }
    .blog-hero { background:linear-gradient(135deg, rgba(217,80,63,0.85), rgba(143,22,27,0.93)), url('../images/experience2026/theme-bg.jpg') center/cover no-repeat; }
    .blog-hero::before { background:radial-gradient(ellipse 80% 60% at 15% 85%, rgba(255,190,120,0.20) 0%, transparent 60%), radial-gradient(ellipse 60% 50% at 85% 15%, rgba(255,255,255,0.12) 0%, transparent 60%); }
    .blog-hero h1 { max-width:780px; }
    .version-badge { background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.32); color:#ffe6dd; }
    /* --- click-to-watch links and the floating player --- */
    .article-content a { color:#c01f24; }
    .article-content a:hover { color:#8f161b; }
    .article-content a.yt { cursor:pointer; }
    .fp { position:fixed; right:1.1rem; bottom:1.1rem; width:min(380px, calc(100vw - 2.2rem)); z-index:1080; background:#1a0f10; color:#fff; border-radius:14px; box-shadow:0 18px 50px rgba(70,8,8,0.45); overflow:hidden; border:1px solid rgba(255,255,255,0.14); }
    .fp[hidden] { display:none; }
    .fp-bar { display:flex; align-items:center; gap:0.5rem; padding:0.5rem 0.4rem 0.5rem 0.8rem; background:linear-gradient(135deg,#c01f24,#8f161b); }
    .fp-t { flex:1; min-width:0; line-height:1.25; }
    .fp-t b { display:block; font-size:0.78rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    .fp-t span { display:block; font-size:0.7rem; opacity:0.8; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }
    .fp-bar button { border:0; background:transparent; color:#fff; width:30px; height:30px; border-radius:8px; font-size:0.95rem; cursor:pointer; }
    .fp-bar button:hover { background:rgba(255,255,255,0.18); }
    .fp-body { position:relative; aspect-ratio:16/9; background:#000; }
    .fp-body iframe, .fp-body #fp-yt { position:absolute; inset:0; width:100%; height:100%; border:0; }
    .fp.min .fp-body { display:none; }
    @media(max-width:600px){ .fp { right:0; left:0; bottom:0; width:100%; border-radius:14px 14px 0 0; } }
  </style>'''
head = head.replace('</style>', CSS, 1)
def _warm(x):
    x = x.replace('rgba(0,136,204,', 'rgba(192,31,36,').replace('rgba(0,68,102,', 'rgba(143,22,27,').replace('rgba(37,163,97,', 'rgba(217,80,63,')
    return x.replace('#0088cc', '#c01f24').replace('#006da3', '#8f161b').replace('#004466', '#8f161b').replace('#25a361', '#d9503f')
head = _warm(head)

tail = _warm(src[src.index('<!-- Related Content -->'):])
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


YTID = {'04': 'qVtrBzDs-co', '05': 'lef8A75FZ5k', '06': '7ITTalQNChs', '07': 'Ip6wCIB_bSM', '10': 'uFIH9fnBhh4', '11': 'X9gMb70HHJ8'}


def ytlink(tid, t, inner, cls=''):
    """real link to the YouTube moment; the page script opens it in the floating player instead"""
    return f'<a class="yt {cls}" href="https://youtu.be/{YTID[tid]}?t={t}" data-talk="{tid}" data-t="{t}" target="_blank" rel="noopener">{inner}</a>'


# ---------- small SVG charts (no libs) ----------
RED, BLUE, GREEN, GREY, AMBER = '#c01f24', '#e07a3c', '#25a361', '#8a94a0', '#d98a00'


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
    return (f'<blockquote class="pq"><p>“{q}”</p><div class="pqf">{who} {ytlink(tid, t, f'<i class="bi bi-play-fill"></i> {mm(t)} Watch this moment')}</div></blockquote>')


def finding(n, head, text):
    return f'<div class="finding"><span class="fn">{n}</span><div><h4>{head}</h4><p>{md(text)}</p></div></div>'


def talk(tid):
    d = TALKS[tid]
    parts = [f'<div class="talk-intro" id="talk-{tid}"><img src="../experience/speakers/{d["photo"][0]}" alt="{d["photo"][1]}"><div><div class="t-time">{d["tag"]} · {d["time"]}</div><h3>{d["title"]}</h3><div class="t-who">{d["who"].replace(" — ", " · ")}</div></div></div>',
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
        n = d['note']
        eqs = ''.join(f'<div class="eq"><span class="eq-l">{l}</span><span class="eq-m">{m}</span></div>' for l, m in n['eqs'])
        parts.append(f'<div class="eng-note"><div class="en-h">Engineering note</div><p>{n["text"]}</p><div class="eq-list">{eqs}</div></div>')
    parts.append(f'<div class="keypoints"><h5>In short</h5><ul>{"".join(f"<li>{md(k)}</li>" for k in d["keys"])}</ul></div>')
    mo = ''.join(ytlink(tid, t, f'<i class="bi bi-play-fill"></i> {mm(t)} {lab}') for t, lab in d['moments'])
    parts.append(f'<div class="moments-blog"><span class="lbl">Jump to</span>{mo}</div>')
    return '\n            '.join(parts)


def sec(eyebrow, h2, lead):
    return f'\n            <div class="sec-eyebrow">{eyebrow}</div>\n            <h2>{h2}</h2>\n            <p class="sec-lead">{lead}</p>'


SECT = {
    '04': sec('01 · Heat', 'Closing the thermal model', 'Two talks closed a thermal model with the same trick: oil and metal never run on the same clock. The oil is simulated briefly, its heat-transfer map goes into a steady solution of the solids, and the result is compared with measurements. The SKF talk, in between, tests the heat-transfer coefficient such models rely on.'),
    '07': sec('02 · Air', 'Measure it before you simulate it', 'Aeration changes viscosity, density, film thickness and oxidation rate. The afternoon showed how to get a measured number for it before asking the model to predict it.'),
    '05': sec('03 · Wear', 'Where it wears, and what that costs', 'Two very different machines, one question: can a particle simulation say where the hardware wears and how much performance it loses?'),
}
HR = '\n\n            <hr class="section-rule">\n'
body_talks = ''
for tid in ['04', '06', '10', '07', '05', '11']:
    if tid in SECT:
        body_talks += HR + SECT[tid]
    body_talks += '\n            ' + talk(tid) + '\n'

QA = [
    ('How many manual iterations does the pump model take?', 'Three to five, and a steady CHT converges in minutes on a GPU. “Sometimes the setup is longer than the simulation itself.” (R&amp;D CFD)'),
    ('Does an aeration calibration transfer?', 'Across geometry yes, across speed by scaling, across additives no: the same base oil with another additive package needs a new one, and the temperature trend can flip sign. (deepfluid)'),
    ('Why start from such basic verification cases?', 'Once a bearing rotates there is no good reference model, so SKF adds complexity step by step. (SKF)'),
    ('What do owners want from a Pelton simulation?', 'What 2&nbsp;% of efficiency lost to one flood costs over a year, and when to refurbish. (HES-SO)'),
]
toc = ''.join(f'<a href="#talk-{t}">{TALKS[t]["tag"]} · {TALKS[t]["short_org"]} <small>{TALKS[t]["topic"]}</small></a>' for t in ['04', '06', '10', '07', '05', '11'])
BODY = '''
  <!-- Hero -->
  <section class="blog-hero">
    <div class="container">
      <div class="version-badge"><i class="bi bi-calendar-event me-1"></i> PW Experience 2026</div>
      <h1>Heat, air and wear: six talks from Modena</h1>
      <p class="lead">Particleworks Experience, October 7, 2026. For each talk: the context, what the speakers found, the slide that shows it and a sentence from the recording.</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 18 min read</span>
        <span><i class="bi bi-tag"></i> Conference report</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p class="standfirst">On October 7 the BPER FORUM Monzani in Modena hosted the Particleworks Experience. Six talks with recordings asked three questions: where does the heat go, where does the air go, and where does the material wear?</p>

            <p>The speakers came from a bearing maker, a pump manufacturer, a hydropower research project and several engineering firms. Each put the simulation next to a thermocouple, an optical sensor or a worn prototype, and stated the gap. Every “Watch this moment” link plays the recording at that second in a floating player. The full slides are on the <a href="../experience/proceedings2026.php">proceedings page</a>.</p>

            <div class="toc">''' + toc + '''</div>

            <hr class="section-rule">
''' + body_talks + '''
            <hr class="section-rule">

            <div class="sec-eyebrow">Also on the programme</div>
            <h2>Three talks with slides only</h2>
            <p>These speakers released their slides but not a recording, so there are no quotes here. Each is in the <a href="../experience/proceedings2026.php">proceedings</a>.</p>
            <ul>
              <li><strong>Prometech Software</strong> (Issei Masaie and Iori Saigo) presented the Particleworks 9.0 and Granuleworks 4.0 releases. The new features get their own article.</li>
              <li><strong>IAV</strong> (René Kockisch) followed air bubbles in the gear oil of an electric 3-speed commercial-vehicle drivetrain: formation, transport, coalescence and dissolution, measured with the IAV Particle Explorer.</li>
              <li><strong>Univance</strong> (Naohiro Fujita) showed gearbox lubrication studies in early design, and early R&amp;D on how airflow changes the oil distribution.</li>
            </ul>

            <hr class="section-rule">

            <div class="sec-eyebrow">From the floor</div>
            <h2>The questions that mattered</h2>
            ''' + ''.join(f'<div class="qa"><b>{q}</b><span>{a}</span></div>' for q, a in QA) + '''

            <hr class="section-rule">

            <div class="sec-eyebrow">Take-home</div>
            <h2>What the day showed</h2>

            <div class="keypoints"><h5>Four findings</h5><ul>
              ''' + ''.join(f'<li><strong>{h}.</strong> {t}</li>' for h, t in TAKEAWAYS) + '''
            </ul></div>

            <p>No talk claimed a perfect match. The useful part was the stated gap: about 5–6 °C at worst on the pump, about 12 % on the roller oil, a factor of 2.5 on a sphere depending on where the HTC was read.</p>

            <div class="cta-box">
              <h3>Get the Modena proceedings</h3>
              <p>Slides, recordings and key findings of each released talk. Free, after a short form.</p>
              <a href="../experience/proceedings2026.php" class="btn-pw"><i class="bi bi-arrow-right me-2"></i>Get the proceedings</a>
            </div>

          </article>
        </div>
      </div>
    </div>
  </section>

  '''

PLAYER_TPL = r"""
  <aside class="fp" id="fp" hidden aria-label="Video player">
    <div class="fp-bar"><div class="fp-t"><b id="fp-title"></b><span id="fp-who"></span></div>
      <button type="button" id="fp-min" aria-label="Minimise the player"><i class="bi bi-dash-lg"></i></button>
      <button type="button" id="fp-x" aria-label="Close the player"><i class="bi bi-x-lg"></i></button></div>
    <div class="fp-body"><div id="fp-yt"></div></div>
  </aside>
  <script>
  (function () {
    var VID = __VID__;
    var fp = document.getElementById('fp'), box = fp.querySelector('.fp-body'), frame = null, cur = null;
    function label(id) { var w = VID[id].who.split(' — '); document.getElementById('fp-title').textContent = VID[id].title; document.getElementById('fp-who').textContent = w[0] + (w[1] ? ' · ' + w[1] : ''); }
    function cmd(fn, args) { frame.contentWindow.postMessage(JSON.stringify({ event: 'command', func: fn, args: args || [] }), '*'); }
    function open(id, t) {
      label(id); fp.hidden = false; fp.classList.remove('min');
      if (frame && cur === id) { cmd('seekTo', [t, true]); cmd('playVideo'); return; }   // same talk: seek, no reload
      if (!frame) { frame = document.createElement('iframe'); frame.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; frame.allowFullscreen = true; frame.title = 'Recording'; box.innerHTML = ''; box.appendChild(frame); }
      frame.src = 'https://www.youtube-nocookie.com/embed/' + VID[id].id + '?autoplay=1&rel=0&modestbranding=1&playsinline=1&enablejsapi=1&start=' + t;
      cur = id;
    }
    document.addEventListener('click', function (ev) {
      var a = ev.target.closest && ev.target.closest('a.yt'); if (!a) return;
      ev.preventDefault(); open(a.dataset.talk, parseInt(a.dataset.t, 10) || 0);
    });
    document.getElementById('fp-min').addEventListener('click', function () { fp.classList.toggle('min'); });
    document.getElementById('fp-x').addEventListener('click', function () { if (frame) { frame.src = 'about:blank'; frame = null; cur = null; } fp.hidden = true; });
  })();
  </script>
"""
import json
PLAYER = PLAYER_TPL.replace('__VID__', json.dumps({k: dict(id=YTID[k], title=TALKS[k]['title'], who=TALKS[k]['who'].replace('&amp;', '&')) for k in YTID}))
html = head + BODY.lstrip('\n') + PLAYER + tail
(root / 'blog' / 'pw-experience-2026.html').write_text(html, encoding='utf8')
php = re.sub(r'href="((?:\.\./)?[A-Za-z0-9_\-/]+)\.html', r'href="\1.php', html)
(root / 'blog' / 'pw-experience-2026.php').write_text(php, encoding='utf8')
art = html[html.index('<article'):html.index('</article>')]
txt = re.sub(r'<svg.*?</svg>', ' ', art, flags=re.S)
print('words in article:', len(re.sub(r'<[^>]+>', ' ', txt).split()))
