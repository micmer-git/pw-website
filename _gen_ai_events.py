#!/usr/bin/env python3
"""Generate the two AI-acceleration landing pages (.php + identical .html twin):

  webinar-ai-particleworks.php      45-min live webinar, Thu 26 Nov 2026
  training-ai-acceleration.php      custom 1-day training

The design source of truth is design/ai-events/*.dc.html (the Design canvas artboards).
This script lifts each artboard's CSS and body, drops the mock top bar and footer, renames the
classes that clash with Bootstrap, swaps the form placeholders for real embeds and wraps the result in
the site's own head, nav and footer (taken from training.php).

Registration form: set WEBINAR_FORM_URL once the MachForm exists (until then an e-mail card is shown).
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "design" / "ai-events"
BASE = (ROOT / "training.php").read_text(encoding="utf-8")
SITE = "https://particleworks-europe.com"

WEBINAR_FORM_URL = None      # e.g. "https://particleworks-europe.forms-eu.com/embed.php?id=NNNNN"
WEBINAR_FORM_H = 700
CONTACT_FORM_URL = "https://particleworks-europe.forms-eu.com/embed.php?id=22527"   # = contact.php
CONTACT_FORM_H = 681
MAIL = "info@particleworks-europe.com"

head, rest = BASE.split("<main>", 1)
_, foot = rest.split("</main>", 1)


def machform(url, height, title):
    return f"""<div id="mf_placeholder" data-formurl="{url}" data-formheight="{height}" data-formtitle="{title}" data-paddingbottom="10"></div>
<script>
  (function(f,o,r,m){{
    r=f.createElement('script');r.async=1;r.src=o+'js/mf.js';
    m=f.getElementById('mf_placeholder'); m.parentNode.insertBefore(r, m);
  }})(document,'https://assets.forms-eu.com/');
</script>"""


def webinar_slot():
    if WEBINAR_FORM_URL:
        return machform(WEBINAR_FORM_URL, WEBINAR_FORM_H, "Register for the webinar")
    return (f'<p class="mini" style="margin:14px 0 16px">Free of charge · live online · recording sent to every registrant.</p>'
            f'<a class="ev-btn btn-p" style="width:100%" href="mailto:{MAIL}?subject=Webinar%20registration%20%E2%80%93%20AI-accelerated%20Particleworks%20(26%20Nov%202026)'
            f'&amp;body=Name%3A%0ACompany%3A%0AJob%20title%3A%0ACountry%3A%0A">Register by e-mail</a>')


SLOTS = {
    "webinar-form": webinar_slot,
    "contact-form": lambda: machform(CONTACT_FORM_URL, CONTACT_FORM_H, "Request a custom training"),
}


def lift(dc_name):
    s = (SRC / dc_name).read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    body = re.search(r'(<div class="ev">.*?)\n</x-dc>', s, re.S).group(1)
    body = re.sub(r'<header class="ev-top">.*?</header>\s*', "", body, flags=re.S)
    body = re.sub(r'<footer class="foot">.*?</footer>\s*', "", body, flags=re.S)
    # image: artboard blob url -> site file
    body = re.sub(r' src="/_blob/[0-9a-f]+"', "", body)
    body = re.sub(r'data-site="([^"]+)"', r'src="\1" loading="lazy"', body)
    # form placeholders
    body = re.sub(r'<div class="slot" data-site-slot="([^"]+)">[^<]*</div>',
                  lambda m: SLOTS[m.group(1)](), body)
    # Bootstrap clashes
    css = re.sub(r"\.btn(?![\w-])", ".ev-btn", css)
    css = re.sub(r"\.card(?![\w-])", ".ev-card", css)
    body = re.sub(r'class="btn(?=[ "])', 'class="ev-btn', body)
    body = body.replace('class="card"', 'class="ev-card"')
    return css.strip(), body


def make_head(fname, title, desc, css):
    h = head
    url = f"{SITE}/{fname}.php"
    h = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", h, flags=re.S)
    h = re.sub(r'(<meta name="description" content=")[^"]*"', rf'\g<1>{desc}"', h)
    h = re.sub(r'(<link rel="canonical" href=")[^"]*"', rf'\g<1>{url}"', h)
    for key in ("og:title", "twitter:title"):
        h = re.sub(rf'(<meta (?:property|name)="{key}" content=")[^"]*"', rf'\g<1>{title}"', h)
    for key in ("og:description", "twitter:description"):
        h = re.sub(rf'(<meta (?:property|name)="{key}" content=")[^"]*"', rf'\g<1>{desc}"', h)
    h = re.sub(r'(<meta property="og:url" content=")[^"]*"', rf'\g<1>{url}"', h)
    return h.replace("</head>", f"  <style>\n{css}\n  </style>\n</head>", 1)


PAGES = [
    ("webinar-ai-particleworks", "Main.dc.html",
     "Webinar: AI-accelerated Particleworks – 26 November 2026 – Particleworks Europe",
     "45-minute live webinar, 26 November 2026: gearbox thermal chains, DoE on materials, automatic post-processing and Blender renders, driven by script and AI agents."),
    ("training-ai-acceleration", "Training.dc.html",
     "Custom training: AI acceleration of Particleworks – Particleworks Europe",
     "One-day custom training: the workshop method in the morning, custom scripts and automation on your own Particleworks cases in the afternoon."),
]

for fname, dc, title, desc in PAGES:
    css, body = lift(dc)
    html = make_head(fname, title, desc, css) + "<main>\n" + body + "\n</main>" + foot
    for ext in ("php", "html"):
        (ROOT / f"{fname}.{ext}").write_text(html, encoding="utf-8", newline="\n")
    print(fname, len(html), "bytes")
