#!/usr/bin/env python3
"""
Generate the 14 non-event pages missing from the new site but present in backup.
Repurposes backup PHP body content, wraps it in the new-site shell, injects SEO head.

Pages (skipping events/webinars per Michele):
  careers, case-studies, company, consulting, contact, glossary,
  particleworksforansys, privacy, privacy-conference, resellers, resources,
  SPH-MPS, support, training
"""
import re
from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).parent.resolve()
BACKUP = ROOT / "website_now"
DOMAIN = "https://particleworks-europe.com"
GTM_ID = "GTM-58D7FHDF"
GSV_TOKEN = "13JcLKtEM_c2bcIc8ZMrIKncMjxxmwN5nmfLLs8WLQA"
IUBENDA_ID = "6c5fe0b3-dfc8-4f17-b2ec-91c28fe04e7c"

PAGES = [
    "careers.php",
    "case-studies.php",
    "company.php",
    "consulting.php",
    "contact.php",
    "glossary.php",
    "particleworksforansys.php",
    "privacy.php",
    "privacy-conference.php",
    "resellers.php",
    "resources.php",
    "SPH-MPS.php",
    "support.php",
    "training.php",
]

TOP_RE = re.compile(
    r'top\s*\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)', re.S
)

def backup_meta(php_name: str):
    p = BACKUP / php_name
    txt = p.read_text(encoding="utf-8", errors="ignore")
    m = TOP_RE.search(txt)
    return (m.group(1), m.group(3)) if m else ("", "")

def extract_body(php_name: str) -> str:
    """Return PHP body stripped of all <?php ?> blocks and rewritten for root."""
    p = BACKUP / php_name
    txt = p.read_text(encoding="utf-8", errors="ignore")
    # Remove all <?php ... ?> blocks
    txt = re.sub(r"<\?php.*?\?>", "", txt, flags=re.S)
    # Remove stray footer/top/menu calls if any survived
    txt = re.sub(r"<\?=.*?\?>", "", txt, flags=re.S)
    # Rewrite relative asset paths to root-relative
    txt = re.sub(r'(\b(?:src|href)=")images/', r'\1/images/', txt)
    txt = re.sub(r'(\b(?:src|href)=")assets/', r'\1/assets/', txt)
    # .php self-refs -> .html
    txt = re.sub(
        r'(\b(?:href)=")([A-Za-z0-9_\-]+)\.php(["#?])',
        lambda m: f'{m.group(1)}{m.group(2)}.html{m.group(3)}',
        txt,
    )
    # Common internal links
    txt = txt.replace('href="index.php"', 'href="/index.html"')
    txt = txt.replace('href="contact.php"', 'href="/contact.html"')
    return txt.strip()

def seo_head_block(canonical: str, title: str, description: str) -> str:
    def esc(s): return s.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    t = esc(title); d = esc(description)
    return f"""  <link rel="canonical" href="{canonical}">
  <meta name="author" content="Particleworks Europe">
  <meta name="keywords" content="Particleworks, Particleworks Europe, Granuleworks, technologies, simulation">
  <meta name="google-site-verification" content="{GSV_TOKEN}">
  <meta property="og:site_name" content="Particleworks Europe">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <script type="text/javascript" src="https://embeds.iubenda.com/widgets/{IUBENDA_ID}.js"></script>
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>"""

NAVBAR = """<nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="/index.html"><img src="/images/PW_Europe_logo_small.png" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-center gap-1">
          <li class="nav-item"><a class="nav-link" href="/index.html">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="/particleworks.html">Particleworks</a></li>
          <li class="nav-item"><a class="nav-link" href="/granuleworks.html">Granuleworks</a></li>
          <li class="nav-item"><a class="nav-link" href="/case-studies.html">Case Studies</a></li>
          <li class="nav-item"><a class="nav-link" href="/company.html">Company</a></li>
          <li class="nav-item"><a class="nav-link" href="/contact.html">Contact</a></li>
          <li class="nav-item"><a class="nav-link" href="https://www.linkedin.com/company/particleworks-europe/" target="_blank"><i class="bi bi-linkedin"></i></a></li>
        </ul>
      </div>
    </div>
  </nav>"""

FOOTER = """<footer class="py-5 mt-5" style="background:#1a1a1a;color:#adb5bd;">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4">
          <img src="/images/PWEurope_negativ-logo.png" alt="Particleworks Europe" style="height:34px;">
          <p class="small mt-3" style="max-width:320px;">European competence center for meshfree CFD simulation with Particleworks and Granuleworks technologies.</p>
          <div class="d-flex gap-2 mt-3"><a href="https://www.linkedin.com/company/particleworks-europe/" class="text-white" target="_blank" style="font-size:1.2rem;"><i class="bi bi-linkedin"></i></a></div>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Products</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="/particleworks.html" class="text-reset">Particleworks</a></li><li class="mb-2"><a href="/granuleworks.html" class="text-reset">Granuleworks</a></li></ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Services</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="/consulting.html" class="text-reset">Consulting</a></li><li class="mb-2"><a href="/training.html" class="text-reset">Training</a></li><li class="mb-2"><a href="/support.html" class="text-reset">Support</a></li></ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Resources</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="/case-studies.html" class="text-reset">Case Studies</a></li><li class="mb-2"><a href="/resources.html" class="text-reset">Resources</a></li><li class="mb-2"><a href="/glossary.html" class="text-reset">Glossary</a></li></ul>
        </div>
        <div class="col-lg-2">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Contact</h6>
          <ul class="list-unstyled small"><li class="mb-2"><i class="bi bi-telephone me-1"></i> +39 0461 915391</li><li class="mb-2"><a href="mailto:info@particleworks-europe.com" class="text-reset"><i class="bi bi-envelope me-1"></i> info@particleworks-europe.com</a></li></ul>
        </div>
      </div>
      <hr class="my-4" style="border-color:#2a2a2a;">
      <div class="d-flex flex-wrap justify-content-between align-items-center">
        <p class="small mb-0">&copy; 2026 Particleworks Europe. All rights reserved.</p>
        <p class="small mb-0"><a href="/privacy.html" class="text-reset me-3">Privacy</a>Meshfree CFD simulation technology</p>
      </div>
    </div>
  </footer>"""

STYLE = """:root {
      --pw-blue: #0088cc;
      --pw-blue-dark: #006da3;
      --pw-green: #25a361;
      --pw-dark: #333333;
      --pw-gray: #6c757d;
      --pw-light: #f8f9fa;
    }
    * { font-family: 'Inter', sans-serif; }
    html { scroll-behavior: smooth; }
    body { color: var(--pw-dark); overflow-x: hidden; padding-top: 70px; }
    .navbar { background: rgba(255,255,255,0.97); backdrop-filter: blur(12px); box-shadow: 0 1px 0 rgba(0,0,0,0.06); padding: 0.6rem 0; transition: box-shadow 0.3s; }
    .navbar.scrolled { box-shadow: 0 2px 20px rgba(0,0,0,0.08); }
    .navbar-brand img { height: 38px; }
    .navbar .nav-link { font-size: 0.88rem; font-weight: 500; color: var(--pw-dark); padding: 0.5rem 0.75rem !important; transition: color 0.2s; }
    .navbar .nav-link:hover { color: var(--pw-blue); }
    .main_section { padding: 4rem 0; background: var(--pw-green); color: #fff; }
    .main_section h1 { font-weight: 700; }
    .background_gray { background: var(--pw-light); padding: 3rem 0; }
    .background-green { background: linear-gradient(135deg, #1e8a51 0%, #25a361 100%); }
    .featurette-heading { font-weight: 700; }
    .text-muted { color: var(--pw-gray) !important; }
    .text-justify { text-align: justify; }
    .small { font-size: 0.88rem; }
    img.img-fluid { max-width: 100%; height: auto; }
    .shadow { box-shadow: 0 6px 20px rgba(0,0,0,0.08) !important; }
    .border-gray { border: 1px solid #e9ecef; }
    .card { border: 1px solid #e9ecef; border-radius: 10px; }
    h1,h2,h3,h4 { letter-spacing: -0.01em; }
    a { color: var(--pw-blue); text-decoration: none; }
    a:hover { color: var(--pw-blue-dark); }
    .btn-primary { background: var(--pw-blue); border-color: var(--pw-blue); }
    .btn-primary:hover { background: var(--pw-blue-dark); border-color: var(--pw-blue-dark); }"""

def build_page(php_name: str) -> str:
    title, description = backup_meta(php_name)
    body = extract_body(php_name)
    basename = php_name[:-4]  # drop .php
    canonical = f"{DOMAIN}/{basename}.html"

    # Fallbacks for empty metadata
    if not title:
        title = f"{basename.replace('-', ' ').title()} — Particleworks Europe"
    if not description:
        description = "Particleworks Europe — meshfree CFD simulation with the Moving Particle Simulation method."

    desc_attr = description.replace('"', '&quot;')
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{desc_attr}">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    {STYLE}
  </style>
<!-- === SEO head (auto-generated, matches backup website_now) === -->
{seo_head_block(canonical, title, description)}
<!-- === /SEO head === -->
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  {NAVBAR}

  <main>
    {body}
  </main>

  {FOOTER}

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>window.addEventListener('scroll', function() {{ document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30); }});</script>
</body>
</html>
"""

def update_sitemap(new_pages: list[str]):
    """Append new URLs to existing sitemap.xml."""
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    today = datetime.now().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    additions = []
    for p in new_pages:
        loc = f"{DOMAIN}/{p[:-4]}.html"
        if loc in text:  # skip duplicates
            continue
        additions += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{today}</lastmod>",
            "    <priority>0.80</priority>",
            "  </url>",
        ]
    if additions:
        text = text.replace("</urlset>", "\n".join(additions) + "\n</urlset>")
        sitemap.write_text(text, encoding="utf-8")
    return len(additions) // 5

def main():
    report = []
    for php in PAGES:
        out_name = php[:-4] + ".html"
        out_path = ROOT / out_name
        html = build_page(php)
        out_path.write_text(html, encoding="utf-8")
        report.append(f"WROTE {out_name} ({len(html):,} bytes)")
    added = update_sitemap(PAGES)
    report.append(f"SITEMAP: +{added} URLs")
    print("\n".join(report))
    print(f"\nTOTAL: {len(PAGES)} pages generated")

if __name__ == "__main__":
    main()
