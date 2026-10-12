#!/usr/bin/env python3
"""Generate the two AI-acceleration event pages (.php + identical .html twin):

  webinar-ai-particleworks.php      45-min live webinar, Thu 26 Nov 2026
  training-ai-acceleration.php      custom 1-day training

Head, nav and footer are lifted from training.php so they stay in step with the site;
re-run after nav/footer changes.  Registration form: set WEBINAR_FORM_URL below once the
MachForm exists (until then the page shows an e-mail registration card).
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
BASE = (ROOT / "training.php").read_text(encoding="utf-8")
SITE = "https://particleworks-europe.com"

# --- MachForm -------------------------------------------------------------------------
WEBINAR_FORM_URL = None      # e.g. "https://particleworks-europe.forms-eu.com/embed.php?id=NNNNN"
WEBINAR_FORM_H = 700
CONTACT_FORM_URL = "https://particleworks-europe.forms-eu.com/embed.php?id=22527"   # = contact.php
CONTACT_FORM_H = 681
MAIL = "info@particleworks-europe.com"

head, rest = BASE.split("<main>", 1)
_, foot = rest.split("</main>", 1)

EXTRA_CSS = """
  <style>
    .ev-hero { background: linear-gradient(135deg, #0b3d5c 0%, #0088cc 55%, #25a361 120%); color:#fff; padding: 3.5rem 0 3rem; }
    .ev-hero h1 { font-weight: 800; font-size: clamp(1.9rem, 4vw, 2.9rem); line-height: 1.12; }
    .ev-hero .lead { opacity: .92; max-width: 40rem; }
    .ev-kicker { display:inline-block; background: rgba(255,255,255,.16); border:1px solid rgba(255,255,255,.3); border-radius: 999px; padding:.25rem .85rem; font-size:.78rem; font-weight:600; letter-spacing:.06em; text-transform:uppercase; margin-bottom:1rem; }
    .ev-facts { display:flex; flex-wrap:wrap; gap:.6rem; margin:1.4rem 0 0; padding:0; list-style:none; }
    .ev-facts li { background:#fff; color: var(--pw-dark); border-radius: 12px; padding:.55rem .9rem; font-size:.88rem; font-weight:600; box-shadow:0 6px 20px rgba(0,0,0,.14); }
    .ev-facts i { color: var(--pw-blue); margin-right:.4rem; }
    .ev-card { background:#fff; color:var(--pw-dark); border-radius:16px; padding:1.4rem; box-shadow:0 14px 40px rgba(0,0,0,.2); }
    .ev-card h2 { font-size:1.15rem; font-weight:700; }
    .ev-sec { padding: 3.5rem 0; }
    .ev-sec.alt { background: var(--pw-light); }
    .ev-sec h2.sec { font-weight:800; font-size:1.7rem; margin-bottom:.4rem; }
    .ev-sec .sub { color: var(--pw-gray); margin-bottom:2rem; max-width:44rem; }
    .agenda { position:relative; margin:0; padding:0; list-style:none; }
    .agenda > li { display:grid; grid-template-columns: 4rem 1fr; gap:1.9rem; padding:0 0 1.8rem; position:relative; }
    .agenda > li::before { content:""; position:absolute; left:5.3rem; top:.4rem; bottom:-.4rem; width:2px; background:#dbe7ee; }
    .agenda > li:last-child::before { display:none; }
    .agenda .t { text-align:right; font-weight:700; color:var(--pw-blue-dark); font-size:.95rem; padding-top:.15rem; }
    .agenda .t small { display:block; color:var(--pw-gray); font-weight:500; font-size:.74rem; }
    .agenda .dot { position:absolute; left:5.0rem; top:.45rem; width:.65rem; height:.65rem; border-radius:50%; background:var(--pw-blue); box-shadow:0 0 0 4px #fff, 0 0 0 5px #bcd9e8; }
    .agenda .b { background:#fff; border:1px solid #e3ecf1; border-radius:14px; padding:1.1rem 1.2rem; box-shadow:0 4px 16px rgba(0,0,0,.04); }
    .agenda .b h3 { font-size:1.08rem; font-weight:700; margin:0 0 .35rem; }
    .agenda .b p { margin:0; color:#4a5562; font-size:.93rem; }
    .agenda .num { color:var(--pw-green); font-weight:800; margin-right:.35rem; }
    .agenda .qa .b { background:linear-gradient(135deg, rgba(0,136,204,.07), rgba(37,163,97,.07)); border-style:dashed; }
    .gifbox { margin-top:.9rem; border-radius:12px; overflow:hidden; background:#101820; display:inline-block; max-width:100%; line-height:0; }
    .gifbox img { max-width:100%; height:auto; max-height:300px; width:auto; display:block; }
    .gifcap { display:block; line-height:1.35; font-size:.76rem; color:#6c757d; margin-top:.35rem; }
    .chips span { display:inline-block; background:#eef6fb; color:var(--pw-blue-dark); border-radius:999px; padding:.15rem .65rem; font-size:.74rem; font-weight:600; margin:.5rem .3rem 0 0; }
    .tick { list-style:none; padding:0; margin:0; }
    .tick li { padding-left:1.7rem; position:relative; margin-bottom:.6rem; }
    .tick li::before { content:"\\F26A"; font-family:"bootstrap-icons"; position:absolute; left:0; top:0; color:var(--pw-green); }
    .req { border-left:4px solid var(--pw-blue); background:#fff; border-radius:0 14px 14px 0; padding:1.2rem 1.4rem; box-shadow:0 4px 16px rgba(0,0,0,.05); }
    .req .tool { display:flex; gap:.8rem; align-items:flex-start; margin-bottom:.8rem; }
    .req .tool i { font-size:1.4rem; color:var(--pw-blue); }
    .daycard { background:#fff; border:1px solid #e3ecf1; border-radius:16px; padding:1.4rem; height:100%; box-shadow:0 4px 16px rgba(0,0,0,.04); }
    .daycard .when { font-size:.78rem; font-weight:700; letter-spacing:.06em; text-transform:uppercase; color:var(--pw-green); }
    .daycard h3 { font-weight:800; font-size:1.25rem; margin:.2rem 0 1rem; }
    .gifgrid figure { margin:0; background:#fff; border:1px solid #e3ecf1; border-radius:14px; overflow:hidden; height:100%; box-shadow:0 4px 16px rgba(0,0,0,.04); }
    .gifgrid img { width:100%; height:240px; object-fit:cover; background:#101820; display:block; }
    .gifgrid figcaption { padding:.8rem 1rem 1rem; font-size:.86rem; color:#4a5562; }
    .gifgrid figcaption b { display:block; color:var(--pw-dark); margin-bottom:.15rem; }
    .ev-cta { background:linear-gradient(135deg,#0b3d5c,#0088cc); color:#fff; border-radius:18px; padding:2rem; }
    .take { background:#fff; border:1px solid #e3ecf1; border-top:4px solid var(--pw-blue); border-radius:14px; padding:1.4rem; height:100%; box-shadow:0 4px 16px rgba(0,0,0,.04); }
    .take i { font-size:1.7rem; color:var(--pw-blue); }
    .take h3 { font-size:1.15rem; font-weight:800; margin:.5rem 0 .3rem; }
    .take p { margin:0; color:#4a5562; font-size:.92rem; }
    .ins { display:flex; gap:1rem; background:#fff; border:1px solid #e3ecf1; border-radius:14px; padding:1.1rem 1.2rem; height:100%; }
    .ins span { flex:0 0 2rem; height:2rem; border-radius:50%; background:var(--pw-green); color:#fff; font-weight:800; display:grid; place-items:center; }
    .ins h3 { font-size:1rem; font-weight:700; margin:0 0 .2rem; }
    .ins p { margin:0; font-size:.9rem; color:#4a5562; }
    .agenda .b { display:flex; gap:1.2rem; align-items:flex-start; justify-content:space-between; }
    .agenda .bt { flex:1 1 auto; }
    .agenda .am { flex:0 0 220px; }
    .agenda .gifbox { margin:0; }
    .agenda .gifbox img { max-height:150px; }
    @media (max-width: 767px) { .agenda .b { flex-direction:column; align-items:flex-start; } .agenda .am { flex-basis:auto; } }
    @media (max-width: 575px) {
      .agenda > li { grid-template-columns: 1fr; gap:.3rem; }
      .agenda > li::before, .agenda .dot { display:none; }
      .agenda .t { text-align:left; }
    }
  </style>
"""


def machform(url, height, title):
    return f"""<div id="mf_placeholder"
     data-formurl="{url}"
     data-formheight="{height}"
     data-formtitle="{title}"
     data-paddingbottom="10">
</div>
<script>
  (function(f,o,r,m){{
    r=f.createElement('script');r.async=1;r.src=o+'js/mf.js';
    m=f.getElementById('mf_placeholder'); m.parentNode.insertBefore(r, m);
  }})(document,'https://assets.forms-eu.com/');
</script>"""


def make_head(fname, title, desc):
    h = head
    url = f"{SITE}/{fname}.php"
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*"', rf'\g<1>{desc}"', h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*"', rf'\g<1>{url}"', h)
    h = re.sub(r'(<meta property="og:title" content=")[^"]*"', rf'\g<1>{title}"', h)
    h = re.sub(r'(<meta property="og:description" content=")[^"]*"', rf'\g<1>{desc}"', h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*"', rf'\g<1>{url}"', h)
    h = re.sub(r'(<meta name="twitter:title" content=")[^"]*"', rf'\g<1>{title}"', h)
    h = re.sub(r'(<meta name="twitter:description" content=")[^"]*"', rf'\g<1>{desc}"', h)
    h = h.replace("</head>", EXTRA_CSS + "</head>", 1)
    return h


def gif(src, alt, cap):
    return (f'<div><div class="gifbox"><img src="images/events/{src}" alt="{alt}" loading="lazy"></div>'
            f'<span class="gifcap">{cap}</span></div>')


# ============================ 1. WEBINAR =====================================================
TAKE = [
    ("bi-gear-wide-connected", "Gearbox, scripted",
     "Churning run, loss torque, heat-transfer map and thermal model chained in one script."),
    ("bi-grid-3x3-gap", "DoE that finishes",
     "rpm &times; oil matrices that launch, resume and compare themselves."),
    ("bi-bar-chart-line", "Post-processing on autopilot",
     "Torque, averaged windows, figures and report &mdash; same output for every run."),
]


def takeaways():
    return '<div class="row g-3">' + ''.join(
        f'<div class="col-md-4"><div class="take"><i class="bi {ic}"></i><h3>{h}</h3><p>{p}</p></div></div>'
        for ic, h, p in TAKE) + '</div>'


INSIGHTS = [
    ("Short runs lie", "Below ~0.5 s the fluctuation is as large as the mean. Average over the developed window, not the whole run."),
    ("No heat in an adiabatic run", "A churning run with adiabatic walls holds no heat-transfer coefficient. The thermal map needs a real re-run."),
    ("Scripted defaults bite", "A scene built from scratch can default to a 1 m coarse distance. Pin it, and check it before spending GPU time."),
    ("Resume, never re-run", "Re-launching a batch to &ldquo;continue&rdquo; wipes the finished runs. Resume them."),
]


def insights():
    return '<div class="row g-3">' + ''.join(
        f'<div class="col-md-6"><div class="ins"><span>{i+1}</span><div><h3>{h}</h3><p>{p}</p></div></div></div>'
        for i, (h, p) in enumerate(INSIGHTS)) + '</div>'


if WEBINAR_FORM_URL:
    reg = machform(WEBINAR_FORM_URL, WEBINAR_FORM_H, "Register for the webinar")
else:
    reg = f"""<p class="small text-muted">Free of charge &middot; live on-line &middot; recording sent to all registrants.</p>
<a class="btn btn-primary w-100 mb-2" href="mailto:{MAIL}?subject=Webinar%20registration%20%E2%80%93%20AI-accelerated%20Particleworks%20(26%20Nov%202026)&amp;body=Name%3A%0ACompany%3A%0AJob%20title%3A%0ACountry%3A%0A">
  <i class="bi bi-envelope-paper me-1"></i> Register by e-mail</a>
<p class="small mb-0 text-muted">We reply with the connection link. Or write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>"""


WEB_AGENDA = [
    ("15:00", "10 min", "Gearbox, end to end",
     "Churning-loss run, loss torque, heat-transfer map, steady thermal model &mdash; one chain instead of four manual steps.", "", ""),
    ("15:10", "8 min", "DoE without babysitting",
     "A speed &times; oil matrix as a single study: launch, monitor, resume, compare.",
     "fsi-flexible-array.gif", "A study array set up and run from one script."),
    ("15:18", "8 min", "Post-processing, automated",
     "Torque curves, steady-state windows, renders and the report, generated the same way every time.",
     "ai-omelette-pour.gif", "Scene, solve and render driven by script."),
    ("15:26", "8 min", "Engineering insights",
     "The checks that separate a plausible result from a correct one. Four of them, from real studies.",
     "ai-chemistry-mixing.gif", "A solver extended from Python: hydration computed per particle."),
    ("15:34", "6 min", "Beyond gearboxes",
     "Fluid&ndash;structure interaction, multi-phase, CFD + DEM and refinement: what to take from the workshop.",
     "multiphase-viscous-pour.gif", "Two non-Newtonian fluids on a shared surface."),
]


def web_item(i, t, dur, h, p, g, cap):
    media = (f'<div class="am"><div class="gifbox"><img src="images/events/{g}" alt="{cap}" loading="lazy"></div>'
             f'<span class="gifcap">{cap}</span></div>') if g else ''
    return f"""
        <li><div class="t">{t}<small>{dur}</small></div><span class="dot"></span>
          <div class="b"><div class="bt"><h3><span class="num">{i:02d}</span>{h}</h3><p>{p}</p></div>{media}</div></li>"""


web_body = f"""
<main>
  <section class="ev-hero">
    <div class="container"><div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <span class="ev-kicker"><i class="bi bi-broadcast me-1"></i> Live webinar &middot; 45 min</span>
        <h1>Particleworks, accelerated by AI</h1>
        <p class="lead mt-3">What we showed at the Experience 2026 workshop, in 45 minutes: gearbox studies, DoE and post-processing automated, and the engineering checks that keep results honest.</p>
        <ul class="ev-facts">
          <li><i class="bi bi-calendar-event"></i>Thu 26 November 2026</li>
          <li><i class="bi bi-clock"></i>15:00 &ndash; 15:45 CET</li>
          <li><i class="bi bi-camera-video"></i>Online</li>
        </ul>
      </div>
      <div class="col-lg-5">
        <div class="ev-card" id="register">
          <h2>Save your seat</h2>
          {reg}
        </div>
      </div>
    </div></div>
  </section>

  <section class="ev-sec pb-0">
    <div class="container">
      <h2 class="sec">Three take-homes</h2>
      <div class="mt-4">{takeaways()}</div>
    </div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <h2 class="sec">Agenda</h2>
      <ol class="agenda mt-4">
{''.join(web_item(i + 1, *a) for i, a in enumerate(WEB_AGENDA))}
        <li class="qa"><div class="t">15:40<small>5 min</small></div><span class="dot"></span>
          <div class="b"><div class="bt"><h3><i class="bi bi-chat-dots me-2 text-success"></i>Q&amp;A</h3><p>Bring your own case.</p></div></div></li>
      </ol>
    </div>
  </section>

  <section class="ev-sec alt">
    <div class="container">
      <h2 class="sec">Four checks worth the 45 minutes</h2>
      <p class="sub">A taste of the engineering insights section.</p>
      {insights()}
    </div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <div class="ev-cta"><div class="row align-items-center g-3">
        <div class="col-lg-8"><h2 class="h3 fw-bold mb-1">Want it on your own cases?</h2>
          <p class="mb-0 opacity-90">One-day custom training: the method in the morning, your scripts in the afternoon.</p></div>
        <div class="col-lg-4 text-lg-end"><a class="btn btn-light fw-semibold" href="training-ai-acceleration.php">Custom AI training <i class="bi bi-arrow-right ms-1"></i></a></div>
      </div></div>
      <p class="small text-muted mt-4 mb-0">Based on the <a href="experience/workshop.php">Particleworks Experience 2026 workshop</a>. Presented by Michele Merelli, Particleworks Europe / EnginSoft.</p>
    </div>
  </section>
</main>
"""

# ============================ 2. TRAINING ====================================================
TOOLS = [
    ("bi-terminal", "Claude Code Desktop (Anthropic)", ""),
    ("bi-code-slash", "Codex (OpenAI)", ""),
    ("bi-cpu", "Any other AI tool installed locally", " &mdash; local models included."),
]
MORNING = [
    "<b>Gearbox workflow</b> &mdash; churning run to loss torque to thermal model",
    "<b>DoE</b> &mdash; study matrices that launch, resume and compare",
    "<b>Post-processing</b> &mdash; torque, windows, figures, report",
    "<b>Engineering insights</b> &mdash; the checks that catch silent errors",
]
AFTERNOON = [
    "<b>Your model</b> &mdash; we start from a case you bring",
    "<b>Your scripts</b> &mdash; set-up, study sweep and post-processing built together",
    "<b>Hand-over</b> &mdash; documented scripts that stay with you",
]
SHOW = [
    ("fsi-flexible-array.gif", "DoE from one script", "A configuration array launched and run together."),
    ("ai-omelette-pour.gif", "Set-up to render", "Scene, solve and render driven by script."),
    ("ai-chemistry-mixing.gif", "Solver extended", "Physics added from Python, per particle."),
]

train_body = f"""
<main>
  <section class="ev-hero">
    <div class="container"><div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <span class="ev-kicker"><i class="bi bi-mortarboard me-1"></i> Custom training &middot; 1 day</span>
        <h1>AI acceleration of Particleworks</h1>
        <p class="lead mt-3">The workshop method in the morning. Scripts and automation for your own simulations in the afternoon.</p>
        <ul class="ev-facts">
          <li><i class="bi bi-calendar-check"></i>1 day</li>
          <li><i class="bi bi-people"></i>Tailored to your team</li>
          <li><i class="bi bi-laptop"></i>Hands-on</li>
        </ul>
        <a class="btn btn-light fw-semibold mt-4" href="#request"><i class="bi bi-send me-1"></i> Request this training</a>
      </div>
      <div class="col-lg-5">
        <div class="gifgrid"><figure><img src="images/events/ai-omelette-pour.gif" alt="Automated Particleworks pour simulation rendered end to end" style="height:auto;max-height:330px;">
          <figcaption><b>Set-up to render</b>Driven by script.</figcaption></figure></div>
      </div>
    </div></div>
  </section>

  <section class="ev-sec pb-0">
    <div class="container">
      <h2 class="sec">Three take-homes</h2>
      <div class="mt-4">{takeaways()}</div>
    </div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <h2 class="sec">The day</h2>
      <div class="row g-4 mt-1">
        <div class="col-lg-6"><div class="daycard">
          <div class="when">Morning &middot; method</div>
          <h3>From the workshop</h3>
          <ul class="tick">{''.join(f'<li>{x}</li>' for x in MORNING)}</ul>
        </div></div>
        <div class="col-lg-6"><div class="daycard">
          <div class="when">Afternoon &middot; your cases</div>
          <h3>Custom scripts &amp; automation</h3>
          <ul class="tick">{''.join(f'<li>{x}</li>' for x in AFTERNOON)}</ul>
        </div></div>
      </div>
    </div>
  </section>

  <section class="ev-sec alt">
    <div class="container">
      <h2 class="sec">Checks you will not forget</h2>
      <p class="sub">Four of the engineering insights from the morning.</p>
      {insights()}
    </div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <h2 class="sec">Automations, running</h2>
      <div class="row g-4 gifgrid mt-1">
{''.join(f'''        <div class="col-md-4"><figure><img src="images/events/{s}" alt="{h}" loading="lazy"><figcaption><b>{h}</b>{c}</figcaption></figure></div>
''' for s, h, c in SHOW)}      </div>
    </div>
  </section>

  <section class="ev-sec alt">
    <div class="container"><div class="row g-4">
      <div class="col-lg-6">
        <h2 class="sec">Bring</h2>
        <div class="req mt-3">
          <p class="fw-semibold mb-2">One AI tool, installed locally</p>
          {''.join(f'<div class="tool"><i class="bi {ic}"></i><div><b>{n}</b>{x}</div></div>' for ic, n, x in TOOLS)}
          <p class="fw-semibold mb-1 mt-3">Particleworks on the same machine</p>
          <p class="small mb-0 text-muted">So scripts can be tested live. Unsure about your set-up? Ask below.</p>
        </div>
      </div>
      <div class="col-lg-6">
        <h2 class="sec">Good fit if</h2>
        <ul class="tick mt-3">
          <li>You run many similar Particleworks cases</li>
          <li>You want a scripted workflow, not manual set-up</li>
          <li>You want scripts and know-how to stay in-house</li>
        </ul>
        <p class="small text-muted mt-3">Want a taste first? <a href="webinar-ai-particleworks.php">45-minute webinar, 26 November</a>.</p>
      </div>
    </div></div>
  </section>

  <section class="ev-sec" id="request">
    <div class="container"><div class="row g-4">
      <div class="col-lg-5">
        <h2 class="sec">Request this training</h2>
        <p class="sub">Tell us your team, cases and preferred period. Mention <b>&ldquo;AI acceleration training&rdquo;</b> and your AI tool.</p>
        <p class="small">Or write to <a href="mailto:{MAIL}?subject=Custom%20training%20%E2%80%93%20AI%20acceleration%20of%20Particleworks">{MAIL}</a>.</p>
      </div>
      <div class="col-lg-7"><div class="ev-card" style="box-shadow:0 8px 30px rgba(0,0,0,.08);border:1px solid #e3ecf1">
{machform(CONTACT_FORM_URL, CONTACT_FORM_H, "Request a custom training")}
      </div></div>
    </div></div>
  </section>
</main>
"""

PAGES = [
    ("webinar-ai-particleworks",
     "Webinar: AI-accelerated Particleworks – 26 November 2026 – Particleworks Europe",
     "45-minute live webinar on 26 November 2026: AI and scripting, FSI, multi-phase, CFD+DEM, refinement and CHT in Particleworks – the Experience 2026 workshop in one session.",
     web_body),
    ("training-ai-acceleration",
     "Custom training: AI acceleration of Particleworks – Particleworks Europe",
     "One-day custom training on AI acceleration of Particleworks: workshop content in the morning, custom scripts and automation on your cases in the afternoon.",
     train_body),
]

for fname, title, desc, body in PAGES:
    html = make_head(fname, title, desc) + body + foot
    for ext in ("php", "html"):
        (ROOT / f"{fname}.{ext}").write_text(html, encoding="utf-8", newline="\n")
    print(fname, len(html), "bytes")
