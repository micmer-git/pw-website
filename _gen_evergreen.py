#!/usr/bin/env python3
# Rebuild evergreen pages: extract body from website_now/*.php backup,
# wrap in the current unified template (head+nav+footer from company.html).
# Writes both .html and an identical .php twin (exact-URL preservation).
import re, sys, os

TEMPLATE_SRC = "company.html"

def load_shell():
    html = open(TEMPLATE_SRC, encoding="utf-8").read()
    # HEAD+NAV = start .. end of </nav>
    nav_end = html.index("</nav>") + len("</nav>")
    head = html[:nav_end]
    # FOOTER+scripts = from "<!-- FOOTER -->" to EOF
    foot = html[html.index("<!-- FOOTER -->"):]
    return head, foot

def extract_body(php_path):
    src = open(php_path, encoding="utf-8").read()
    # content = after first "?>" .. before footer marker
    start = src.index("?>") + 2
    # cut at footer marker (several variants)
    end = len(src)
    for marker in ("<!-- FOOTER -->", "<?php footer", "<?php bottom", "footer();"):
        i = src.find(marker, start)
        if i != -1:
            end = min(end, i)
    body = src[start:end].strip()
    # title / description from top("title","section","desc")
    m = re.search(r'top\(\s*"([^"]*)"\s*,\s*"[^"]*"\s*,\s*"([^"]*)"', src)
    title = m.group(1) if m else "Particleworks Europe"
    desc = m.group(2) if m else ""
    return title, desc, body

def customize_head(head, title, desc, out_html):
    h = head
    h = h.replace("Particleworks Europe - company", title)
    h = h.replace("Particleworks is a CAE software for the simulation of liquid flows based on the Moving Particle Simulation method.", desc or "Particleworks is a CAE software for the simulation of liquid flows based on the Moving Particle Simulation method.")
    h = h.replace("company.html", out_html)
    # drop stale active highlight on Company>About
    h = h.replace("dropdown-item active", "dropdown-item")
    return h

def build(php_path, out_base):
    head, foot = load_shell()
    title, desc, body = extract_body(php_path)
    out_html = out_base + ".html"
    page = customize_head(head, title, desc, out_html) + "\n\n  <main>\n" + body + "\n  </main>\n\n  " + foot
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(page)
    # identical .php twin
    with open(out_base + ".php", "w", encoding="utf-8") as f:
        f.write(page)
    # report internal .php/.html links that don't resolve
    links = set(re.findall(r'href="([a-zA-Z0-9._-]+\.(?:php|html))"', body))
    missing = [l for l in links if not os.path.exists(l) and not os.path.exists(l.rsplit('.',1)[0]+'.html')]
    print(f"  {out_html:50s} title='{title[:40]}'  internal-link-misses={sorted(missing)}")

if __name__ == "__main__":
    jobs = [
        ("website_now/recorded-webinars.php", "recorded-webinars"),
        ("website_now/single-speed-transmission-webinar.php", "single-speed-transmission-webinar"),
        ("website_now/thank-you-page.php", "thank-you-page"),
    ]
    for php, base in jobs:
        build(php, base)
    print("done")
