#!/usr/bin/env python3
"""Generate the two AI-acceleration landing pages (.php + static .html twin):

  webinar-ai-particleworks.php      45-min live webinar, Thu 26 Nov 2026
  training-ai-acceleration.php      custom 1-day training

Design source of truth: design/ai-events/*.dc.html (the Design canvas artboards).
This script lifts each artboard's CSS and body, drops the mock top bar and footer, renames the
classes that clash with Bootstrap, and wraps the result in the site's own head, nav and footer
(taken from training.php).

The .php files are real PHP: `$machform_url` at the top feeds the MachForm card in the hero. Empty =
e-mail fallback. The .html twin (GitHub Pages) is static with the same default resolved.
"""
import re
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT / "design" / "ai-events"
BASE = (ROOT / "training.php").read_text(encoding="utf-8")
SITE = "https://particleworks-europe.com"
MAIL = "info@particleworks-europe.com"

head, rest = BASE.split("<main>", 1)
_, foot = rest.split("</main>", 1)

# slot key -> (default MachForm embed URL, height, embed title, mailto subject, placeholder label)
FORMS = {
    "webinar-form": ("", 700, "Register for the webinar",
                     "Webinar%20registration%20%E2%80%93%20AI-accelerated%20Particleworks%20(26%20Nov%202026)",
                     "Registration form<br>loads here"),
    "contact-form": ("https://particleworks-europe.forms-eu.com/embed.php?id=22527", 681, "Request a custom training",
                     "Custom%20training%20%E2%80%93%20AI%20acceleration%20of%20Particleworks",
                     "Request form<br>loads here"),
}


def embed(url, height, title):
    return (f'<div id="mf_placeholder" data-formurl="{url}" data-formheight="{height}" '
            f'data-formtitle="{title}" data-paddingbottom="10"></div>\n'
            "<script>\n"
            "  (function(f,o,r,m){\n"
            "    r=f.createElement('script');r.async=1;r.src=o+'js/mf.js';\n"
            "    m=f.getElementById('mf_placeholder'); m.parentNode.insertBefore(r, m);\n"
            "  })(document,'https://assets.forms-eu.com/');\n"
            "</script>")


def fallback(subject, label):
    return (f'<div class="slot">{label}</div>'
            f'<a class="ev-btn btn-p" style="width:100%;margin-top:14px" href="mailto:{MAIL}?subject={subject}'
            '&amp;body=Name%3A%0ACompany%3A%0AJob%20title%3A%0ACountry%3A%0A">Or write to us by e-mail</a>')


def slot_html(key, php):
    url, h, title, subj, label = FORMS[key]
    if php:
        return ("<?php if ($machform_url !== ''): ?>\n"
                + embed("<?= htmlspecialchars($machform_url) ?>", "<?= (int)$machform_height ?>", title)
                + "\n<?php else: ?>\n" + fallback(subj, label) + "\n<?php endif; ?>")
    return embed(url, h, title) if url else fallback(subj, label)


def php_header(key):
    url, h = FORMS[key][:2]
    return ("<?php\n"
            "// MachForm embed URL for the form in the top-right card.\n"
            "// Paste the form's embed URL between the quotes; leave empty to show the e-mail fallback.\n"
            f"$machform_url = '{url}';\n"
            f"$machform_height = {h};\n"
            "?>\n")


def lift(dc_name):
    s = (SRC / dc_name).read_text(encoding="utf-8")
    css = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    body = re.search(r'(<div class="ev">.*?)\n</x-dc>', s, re.S).group(1)
    body = re.sub(r'<header class="ev-top">.*?</header>\s*', "", body, flags=re.S)
    body = re.sub(r'<footer class="foot">.*?</footer>\s*', "", body, flags=re.S)
    body = re.sub(r' src="/_blob/[0-9a-f]+"', "", body)                      # artboard blob -> site file
    body = re.sub(r'data-site="([^"]+)"', r'src="\1" loading="lazy"', body)
    body = re.sub(r'<div class="slot" data-site-slot="([^"]+)">[^<]*</div>', r"@@SLOT:\1@@", body)
    css = re.sub(r"\.btn(?![\w-])", ".ev-btn", css)                          # Bootstrap clashes
    css = re.sub(r"\.card(?![\w-])", ".ev-card", css)
    body = re.sub(r'class="btn(?=[ "])', 'class="ev-btn', body)
    body = body.replace('class="card"', 'class="ev-card"').replace('class="card ', 'class="ev-card ')
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
    key = re.search(r"@@SLOT:([\w-]+)@@", body).group(1)
    page = make_head(fname, title, desc, css) + "<main>\n" + body + "\n</main>" + foot
    for ext in ("php", "html"):
        out = page.replace(f"@@SLOT:{key}@@", slot_html(key, ext == "php"))
        if ext == "php":
            out = php_header(key) + out
        (ROOT / f"{fname}.{ext}").write_text(out, encoding="utf-8", newline="\n")
    print(fname, len(out), "bytes")
