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
    url = f"{SITE}/{fname}.html"
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
if WEBINAR_FORM_URL:
    reg = machform(WEBINAR_FORM_URL, WEBINAR_FORM_H, "Register for the webinar")
else:
    reg = f"""<p class="small text-muted">Free of charge &middot; live on-line &middot; recording sent to all registrants.</p>
<a class="btn btn-primary w-100 mb-2" href="mailto:{MAIL}?subject=Webinar%20registration%20%E2%80%93%20AI-accelerated%20Particleworks%20(26%20Nov%202026)&amp;body=Name%3A%0ACompany%3A%0AJob%20title%3A%0ACountry%3A%0A">
  <i class="bi bi-envelope-paper me-1"></i> Register by e-mail</a>
<p class="small mb-0 text-muted">We reply with the connection link. Or write to <a href="mailto:{MAIL}">{MAIL}</a>.</p>"""

WEB_AGENDA = [
    ("15:00", "10 min", "AI and scripting as a simulation engine",
     "How an AI coding agent drives Particleworks through its Python API: scene set-up, pre-processing, batch runs, "
     "monitoring and automatic reporting &mdash; and where AI genuinely adds value in a meshless CFD workflow.",
     ["AI agents", "Python API", "DoE"],
     gif("ai-chemistry-mixing.gif", "Pasta-dough mixing with water content computed on every particle",
         "Scripted solver extension: hydration computed on every particle and fed back into the flow.")),
    ("15:10", "8 min", "Fluid&ndash;structure interaction",
     "Deformable bodies under fluid action: how the pressure load is passed to a structural model and the deformed "
     "shape returned to the flow, step after step.",
     ["Two-way coupling", "Flexible walls"],
     gif("fsi-flexible-array.gif", "Four flexible sheets deforming under a falling liquid",
         "Flexible sheets deforming under impact &mdash; a parametric array run from one script.")),
    ("15:18", "8 min", "Multi-phase flow: air and liquid",
     "Methods for air&ndash;liquid flows and free-surface problems, with practical use cases and the modelling choices "
     "that decide whether a result can be trusted.",
     ["Air &amp; liquid", "Non-Newtonian", "Free surface"],
     gif("multiphase-viscous-pour.gif", "Two viscous sauces pouring onto stuffed pasta",
         "Two non-Newtonian fluids pouring and mixing on a shared surface.")),
    ("15:26", "7 min", "CFD + DEM: fluid meets granular media",
     "Coupling fluid flow with particles and powders &mdash; where the two solvers exchange momentum and how to set up "
     "a coupled case without losing the physics.",
     ["Particleworks", "Granuleworks", "Coupling"], ""),
    ("15:33", "7 min", "Multi-level resolution and conjugate heat transfer",
     "Particle refinement where it matters, plus what's new for conjugate heat transfer in Particleworks 9.0 "
     "and the applications it opens.",
     ["Refinement", "CHT", "Version 9.0"], ""),
]


def web_item(i, t, dur, h, p, chips, g):
    return f"""
        <li><div class="t">{t}<small>{dur}</small></div><span class="dot"></span>
          <div class="b"><h3><span class="num">{i:02d}</span>{h}</h3><p>{p}</p>
            <div class="chips">{''.join(f'<span>{c}</span>' for c in chips)}</div>
            {g}</div></li>"""


web_body = f"""
<main>
  <section class="ev-hero">
    <div class="container"><div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <span class="ev-kicker"><i class="bi bi-broadcast me-1"></i> Live webinar &middot; 45 minutes</span>
        <h1>AI-accelerated Particleworks: the workshop, in 45 minutes</h1>
        <p class="lead mt-3">The key results from our Particleworks Experience 2026 workshop &mdash; AI and scripting, fluid&ndash;structure
          interaction, multi-phase flow, CFD&nbsp;+&nbsp;DEM, refinement and heat transfer &mdash; condensed into one live session.</p>
        <ul class="ev-facts">
          <li><i class="bi bi-calendar-event"></i>Thursday 26 November 2026</li>
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

  <section class="ev-sec">
    <div class="container">
      <h2 class="sec">Agenda</h2>
      <p class="sub">Five focused topics and a short Q&amp;A. Every topic comes from a talk of the workshop; simulations shown are real Particleworks runs.</p>
      <ol class="agenda">
{''.join(web_item(i + 1, *a) for i, a in enumerate(WEB_AGENDA))}
        <li class="qa"><div class="t">15:40<small>5 min</small></div><span class="dot"></span>
          <div class="b"><h3><i class="bi bi-chat-dots me-2 text-success"></i>Live Q&amp;A</h3><p>Bring your own case: we answer on the spot.</p></div></li>
      </ol>
    </div>
  </section>

  <section class="ev-sec alt">
    <div class="container"><div class="row g-4">
      <div class="col-lg-6">
        <h2 class="sec">Who should attend</h2>
        <ul class="tick mt-3">
          <li>CFD and simulation engineers already using, or evaluating, Particleworks</li>
          <li>Team leaders who want to see where AI and automation save real simulation time</li>
          <li>Anyone who missed the workshop in Modena and wants the essentials</li>
        </ul>
      </div>
      <div class="col-lg-6">
        <h2 class="sec">What you take home</h2>
        <ul class="tick mt-3">
          <li>A clear picture of what AI-driven Particleworks workflows can do today</li>
          <li>The modelling choices behind coupled FSI, multi-phase and CFD&nbsp;+&nbsp;DEM cases</li>
          <li>The recording and the slides, sent to every registrant</li>
        </ul>
      </div>
    </div></div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <div class="ev-cta"><div class="row align-items-center g-3">
        <div class="col-lg-8"><h2 class="h3 fw-bold mb-1">Want to go deeper?</h2>
          <p class="mb-0 opacity-90">Take the one-day custom training on AI acceleration of Particleworks &mdash; the workshop content, plus scripts and automation built around your own cases.</p></div>
        <div class="col-lg-4 text-lg-end"><a class="btn btn-light fw-semibold" href="training-ai-acceleration.html">Custom AI training <i class="bi bi-arrow-right ms-1"></i></a></div>
      </div></div>
      <p class="small text-muted mt-4 mb-0">Based on the <a href="experience/workshop.html">Particleworks Experience 2026 workshop</a>. Presented by Michele Merelli, Particleworks Europe / EnginSoft.</p>
    </div>
  </section>
</main>
"""

# ============================ 2. TRAINING ====================================================
TOOLS = [
    ("bi-terminal", "Claude Code Desktop (Anthropic)", ""),
    ("bi-code-slash", "Codex (OpenAI)", ""),
    ("bi-cpu", "Any other AI coding tool installed on your local machine", " &mdash; including local models."),
]
MORNING = [
    "<b>AI as a simulation engine</b> &mdash; what to delegate to an agent, what to keep, and how to brief it",
    "<b>Python API in practice</b> &mdash; scenes, pre-processing, GPU solve and post-processing, headless",
    "<b>Parametric studies &amp; DoE</b> &mdash; batches that run, resume and report on their own",
    "<b>Advanced physics from a script</b> &mdash; fluid&ndash;structure interaction, multi-phase, CFD&nbsp;+&nbsp;DEM, refinement and heat transfer",
    "<b>Automatic reporting</b> &mdash; from raw results to figures and a readable summary",
]
AFTERNOON = [
    "<b>Your case, your scripts</b> &mdash; we start from a model you bring and automate its set-up and runs",
    "<b>Custom automation</b> &mdash; post-processing, reports and study sweeps tailored to your workflow",
    "<b>Hands-on, side by side</b> &mdash; you drive the AI tool, we steer and unblock",
    "<b>Hand-over</b> &mdash; the scripts stay with you, documented, ready to reuse",
]
SHOW = [
    ("ai-chemistry-mixing.gif", "Solver extended from Python",
     "Pasta-dough hydration computed on every particle and fed back into the flow &mdash; a physics model added by script."),
    ("ai-omelette-pour.gif", "Scene to render, end to end",
     "A pour built, solved and rendered through an automated pipeline driven by an AI agent."),
    ("fsi-flexible-array.gif", "A study array from one script",
     "Several flexible-sheet configurations set up, run and post-processed together."),
]

train_body = f"""
<main>
  <section class="ev-hero">
    <div class="container"><div class="row g-4 align-items-center">
      <div class="col-lg-7">
        <span class="ev-kicker"><i class="bi bi-mortarboard me-1"></i> Custom training &middot; 1 day</span>
        <h1>AI acceleration of Particleworks</h1>
        <p class="lead mt-3">A one-day training built on what we presented at the Particleworks Experience 2026 workshop:
          the morning gives you the method, the afternoon turns it into scripts and automation for <em>your</em> simulations.</p>
        <ul class="ev-facts">
          <li><i class="bi bi-calendar-check"></i>1 day &middot; dates agreed with you</li>
          <li><i class="bi bi-people"></i>Tailored to your team</li>
          <li><i class="bi bi-laptop"></i>Hands-on</li>
        </ul>
        <a class="btn btn-light fw-semibold mt-4" href="#request"><i class="bi bi-send me-1"></i> Request this training</a>
      </div>
      <div class="col-lg-5">
        <div class="gifgrid"><figure><img src="images/events/ai-omelette-pour.gif" alt="Automated Particleworks pour simulation rendered end to end" style="height:auto;max-height:330px;">
          <figcaption><b>Automation in action</b>Set-up, solve and render, driven by script.</figcaption></figure></div>
      </div>
    </div></div>
  </section>

  <section class="ev-sec">
    <div class="container">
      <h2 class="sec">One day, two halves</h2>
      <p class="sub">Method in the morning, your own automation in the afternoon.</p>
      <div class="row g-4">
        <div class="col-lg-6"><div class="daycard">
          <div class="when">Morning &middot; the workshop content</div>
          <h3>AI-driven Particleworks</h3>
          <ul class="tick">{''.join(f'<li>{x}</li>' for x in MORNING)}</ul>
        </div></div>
        <div class="col-lg-6"><div class="daycard">
          <div class="when">Afternoon &middot; custom scripts &amp; automation</div>
          <h3>Built around your cases</h3>
          <ul class="tick">{''.join(f'<li>{x}</li>' for x in AFTERNOON)}</ul>
        </div></div>
      </div>
    </div>
  </section>

  <section class="ev-sec alt">
    <div class="container">
      <h2 class="sec">What the automations look like</h2>
      <p class="sub">Real Particleworks runs produced with the same approach you will learn.</p>
      <div class="row g-4 gifgrid">
{''.join(f'''        <div class="col-md-4"><figure><img src="images/events/{s}" alt="{h}" loading="lazy"><figcaption><b>{h}</b>{c}</figcaption></figure></div>
''' for s, h, c in SHOW)}      </div>
    </div>
  </section>

  <section class="ev-sec">
    <div class="container"><div class="row g-4">
      <div class="col-lg-6">
        <h2 class="sec">Requirements</h2>
        <p class="sub mb-3">Please bring a laptop or workstation with:</p>
        <div class="req">
          <p class="fw-semibold mb-2">One AI coding tool, installed locally</p>
          {''.join(f'<div class="tool"><i class="bi {ic}"></i><div><b>{n}</b>{x}</div></div>' for ic, n, x in TOOLS)}
          <p class="fw-semibold mb-1 mt-3">Particleworks, on the same machine</p>
          <p class="small mb-0 text-muted">So scripts can be tested live. Not sure your set-up qualifies? Ask us in the request below.</p>
        </div>
      </div>
      <div class="col-lg-6">
        <h2 class="sec">Who it is for</h2>
        <ul class="tick mt-3">
          <li>Simulation engineers who run many similar Particleworks cases</li>
          <li>Teams that want a repeatable, scripted workflow instead of manual set-up</li>
          <li>Companies that want the scripts and know-how to stay in-house</li>
        </ul>
        <p class="small text-muted mt-3">Prefer a short introduction first? Join the <a href="webinar-ai-particleworks.html">45-minute webinar on 26 November</a>.</p>
      </div>
    </div></div>
  </section>

  <section class="ev-sec alt" id="request">
    <div class="container"><div class="row g-4">
      <div class="col-lg-5">
        <h2 class="sec">Request this training</h2>
        <p class="sub">Tell us about your team, your cases and your preferred period. In the message, please mention <b>&ldquo;AI acceleration training&rdquo;</b> and the AI tool you plan to use. We come back with a proposal.</p>
        <p class="small">Or write directly to <a href="mailto:{MAIL}?subject=Custom%20training%20%E2%80%93%20AI%20acceleration%20of%20Particleworks">{MAIL}</a>.</p>
      </div>
      <div class="col-lg-7"><div class="ev-card">
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
