#!/usr/bin/env python3
"""
SEO sync: align pw-website new HTML site with backup (website_now PHP site)
so that particleworks-europe.com URLs map 1:1 to backup slugs.

Strategy (per Michele's decision 2026-04-17):
- Canonical base domain: https://particleworks-europe.com
- Create root-level ALIAS HTML for each backup PHP page, duplicating the
  content of the matching nested new HTML page.
- Alias page owns the canonical (self). Nested page points canonical -> alias.
- Inject on EVERY HTML (alias + nested + top-level): OG tags, GTM,
  google-site-verification, keywords, author, Iubenda, self-canonical.
- Emit sitemap.xml + robots.txt matching backup structure.
"""
import os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
BACKUP = ROOT / "website_now"
DOMAIN = "https://particleworks-europe.com"
GTM_ID = "GTM-58D7FHDF"
GSV_TOKEN = "13JcLKtEM_c2bcIc8ZMrIKncMjxxmwN5nmfLLs8WLQA"
IUBENDA_ID = "6c5fe0b3-dfc8-4f17-b2ec-91c28fe04e7c"

# ---------- Mapping: new HTML path -> backup PHP basename ----------
NEW_TO_BACKUP = {
    # Top-level (same filename)
    "index.html": "index.php",
    "particleworks.html": "particleworks.php",
    "granuleworks.html": "granuleworks.php",
    # Applications
    "applications/civil-engineering.html": "civil-engineering-and-fire-prevention.php",
    "applications/clutches-and-brakes.html": "clutches-and-brakes.php",
    "applications/cutting-tools.html": "cutting-tools.php",
    "applications/e-motors.html": "e-motors.php",
    "applications/engines-and-pistons.html": "engines-and-pistons.php",
    "applications/gearboxes-and-bearings.html": "gearboxes-and-bearings.php",
    "applications/mixing-and-separation.html": "mixing-and-separation.php",
    "applications/sterilization-food-consumer.html": "sterilization-food-and-consumer-goods.php",
    "applications/vehicle-management.html": "vehicle-management.php",
    # Cases
    "cases/comer-high-speed.html": "ComerIndustries-HighSpeedTransmissions.php",
    "cases/comer-oil-flow.html": "comer-oil-flow-rate.php",
    "cases/comer-oil-splashing.html": "ComerIndustries-Oilsplashing.php",
    "cases/dana.html": "DanaMotionSystems-AxialPistonPump.php",
    "cases/drive-system-design.html": "DriveSystemDesign-edrivecooling.php",
    "cases/ducati.html": "Ducati-corse-racing-piston.php",
    "cases/emotors.html": "EMOTORS-Optimizing-spray-cooling-edrives.php",
    "cases/fire-simulation.html": "simulating-fire-for-historical-buildings.php",
    "cases/gima.html": "GIMATransmissionTechnology-Gearoiljetlubrication.php",
    "cases/gkn.html": "GKNDriveline-Gearboxlubrication.php",
    "cases/hitachi.html": "HitachiAutomotive-Pistonoiljetsimulation.php",
    "cases/hpe.html": "HPECoxa_oil-pistoncooling-jets.php",
    "cases/hyundai.html": "HyundaiMotorGroup-Churningoilpath.php",
    "cases/iav.html": "IAV-edrivecooling.php",
    "cases/lion.html": "LIONCorporation-Liquiddetergent.php",
    "cases/lixil.html": "LIXIL-water-technology.php",
    "cases/marelli.html": "MarelliMotori-Oillubricatedbearings.php",
    "cases/ricardo.html": "Ricardo-Oil-cooled-emotor.php",
    "cases/royal-enfield.html": "RoyalEnfield-Pistoncooling.php",
    "cases/spm.html": "SPM-vertical-axis-washing-machine.php",
    "cases/total-energies.html": "TotalEnergies_Electric-motor-cooling-simulation.php",
    "cases/unitn.html": "UniTN_stand-up-pouch-filling-process.php",
    "cases/univance.html": "Univance-ChainLubrication.php",
    "cases/wfinland.html": "WFinland-Pistontemperaturevalidation.php",
    "cases/zeco.html": "ZECO-Peltonturbine.php",
}

# Blog pages: new content, no backup match. Self-canonical under /blog/.
BLOG_DIR = ROOT / "blog"

# ---------- Extract title/description from backup PHP ----------
TOP_RE = re.compile(
    r'top\s*\(\s*"([^"]*)"\s*,\s*"([^"]*)"\s*,\s*"([^"]*)"\s*\)', re.S
)

def backup_meta(php_name: str):
    p = BACKUP / php_name
    if not p.exists():
        return None
    txt = p.read_text(encoding="utf-8", errors="ignore")
    m = TOP_RE.search(txt)
    if not m:
        return None
    return {"title": m.group(1), "description": m.group(3)}

# ---------- SEO head block builder ----------
def seo_head(canonical_url: str, title: str, description: str) -> str:
    # Escape HTML quotes minimally; values already plain text.
    def esc(s): return s.replace('"', '&quot;').replace('<', '&lt;').replace('>', '&gt;')
    t = esc(title)
    d = esc(description)
    return f"""<!-- === SEO head (auto-generated, matches backup website_now) === -->
  <link rel="canonical" href="{canonical_url}">
  <meta name="author" content="Particleworks Europe">
  <meta name="keywords" content="Particleworks, Particleworks Europe, Granuleworks, technologies, simulation">
  <meta name="google-site-verification" content="{GSV_TOKEN}">
  <meta property="og:site_name" content="Particleworks Europe">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{canonical_url}">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <!-- Iubenda -->
  <script type="text/javascript" src="https://embeds.iubenda.com/widgets/{IUBENDA_ID}.js"></script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
}})(window,document,'script','dataLayer','{GTM_ID}');</script>
  <!-- End Google Tag Manager -->
<!-- === /SEO head === -->"""

GTM_NOSCRIPT = f"""<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->"""

# ---------- HTML patchers ----------
SEO_MARK_START = "<!-- === SEO head (auto-generated"
SEO_MARK_END   = "<!-- === /SEO head === -->"
GTM_NOSCRIPT_MARK = "<!-- Google Tag Manager (noscript) -->"

TITLE_RE = re.compile(r"<title>.*?</title>", re.S | re.I)
DESC_RE  = re.compile(r'<meta\s+name="description"\s+content="[^"]*"\s*/?>', re.I)
HEAD_CLOSE_RE = re.compile(r"</head>", re.I)
BODY_OPEN_RE = re.compile(r"<body[^>]*>", re.I)

def patch_html(
    html: str,
    canonical_url: str,
    title: str | None,
    description: str | None,
) -> str:
    # Replace <title> and meta description if override provided
    if title:
        html = TITLE_RE.sub(f"<title>{title}</title>", html, count=1)
    if description:
        # Escape double quotes inside description for safe attribute
        d_attr = description.replace('"', '&quot;')
        if DESC_RE.search(html):
            html = DESC_RE.sub(
                f'<meta name="description" content="{d_attr}">', html, count=1
            )
        else:
            # Insert after <title>
            html = TITLE_RE.sub(
                lambda m: m.group(0) + f'\n  <meta name="description" content="{d_attr}">',
                html, count=1
            )

    # Remove previously-injected SEO block (idempotency)
    html = re.sub(
        re.escape(SEO_MARK_START) + r".*?" + re.escape(SEO_MARK_END),
        "",
        html, flags=re.S,
    )
    # Remove previously-injected GTM noscript (idempotency)
    html = re.sub(
        re.escape(GTM_NOSCRIPT_MARK) + r".*?<!-- End Google Tag Manager \(noscript\) -->",
        "",
        html, flags=re.S,
    )

    # Extract the title/description NOW for the SEO head block
    t_m = TITLE_RE.search(html)
    d_m = DESC_RE.search(html)
    cur_title = re.sub(r"</?title>", "", t_m.group(0)) if t_m else "Particleworks Europe"
    cur_desc = re.search(r'content="([^"]*)"', d_m.group(0)).group(1) if d_m else ""

    # Inject SEO head before </head>
    head_block = seo_head(canonical_url, cur_title, cur_desc)
    if HEAD_CLOSE_RE.search(html):
        html = HEAD_CLOSE_RE.sub(head_block + "\n</head>", html, count=1)

    # Inject GTM noscript right after <body ...>
    if BODY_OPEN_RE.search(html):
        html = BODY_OPEN_RE.sub(lambda m: m.group(0) + "\n" + GTM_NOSCRIPT, html, count=1)

    return html

def rewrite_internal_links_for_alias(html: str) -> str:
    """
    Nested pages use '../images/...', '../cases/...', '../index.html'.
    When served at root (alias), ../ resolves above site root and breaks.
    Rewrite the specific '../X/' prefixes we know exist. Conservative:
    leaves everything else (https://, #anchor, mailto:, siblings) untouched.
    """
    for prefix in ("images/", "assets/", "blog/", "cases/", "applications/"):
        html = html.replace(f'../{prefix}', f'/{prefix}')
    html = html.replace('"../index.html', '"/index.html')
    html = html.replace("'../index.html", "'/index.html")
    return html

# ---------- Main passes ----------
def process():
    report = []

    # 1. Patch every mapped "nested" page: canonical points to ALIAS URL
    for new_rel, php_name in NEW_TO_BACKUP.items():
        new_path = ROOT / new_rel
        if not new_path.exists():
            report.append(f"MISSING NEW: {new_rel}")
            continue
        meta = backup_meta(php_name)
        alias_basename = php_name[:-4] + ".html"  # drop .php add .html
        canonical_url = f"{DOMAIN}/{alias_basename}"

        # For top-level files (index.html, particleworks.html, granuleworks.html):
        # alias IS the same file. For homepage, canonical base domain only.
        if "/" not in new_rel:
            if new_rel == "index.html":
                canonical_url = f"{DOMAIN}/"
            else:
                canonical_url = f"{DOMAIN}/{new_rel}"

        html = new_path.read_text(encoding="utf-8")
        t = meta["title"] if meta else None
        d = meta["description"] if meta else None
        patched = patch_html(html, canonical_url, t, d)
        new_path.write_text(patched, encoding="utf-8")
        report.append(f"PATCHED NESTED: {new_rel} -> canonical {canonical_url}")

    # 2. Create ALIAS at root for each mapping (nested only; skip top-level self)
    for new_rel, php_name in NEW_TO_BACKUP.items():
        if "/" not in new_rel:
            continue
        new_path = ROOT / new_rel
        if not new_path.exists():
            continue
        alias_basename = php_name[:-4] + ".html"
        alias_path = ROOT / alias_basename
        # Load the (now-patched) nested file
        html = new_path.read_text(encoding="utf-8")

        # Rewrite asset/link paths to root-relative so alias served from / works
        html = rewrite_internal_links_for_alias(html)

        # Set canonical to self (the alias is the indexed URL)
        meta = backup_meta(php_name)
        canonical_url = f"{DOMAIN}/{alias_basename}"
        t = meta["title"] if meta else None
        d = meta["description"] if meta else None
        # patch again to overwrite canonical block
        html = patch_html(html, canonical_url, t, d)

        alias_path.write_text(html, encoding="utf-8")
        report.append(f"CREATED ALIAS: {alias_basename}")

        # Nested page: point canonical -> alias (overwriting self-canonical from pass 1)
        nested_html = new_path.read_text(encoding="utf-8")
        nested_html = patch_html(nested_html, canonical_url, t, d)
        new_path.write_text(nested_html, encoding="utf-8")

    # 3. Blog pages: self-canonical under /blog/
    if BLOG_DIR.exists():
        for blog_file in BLOG_DIR.glob("*.html"):
            canonical_url = f"{DOMAIN}/blog/{blog_file.name}"
            html = blog_file.read_text(encoding="utf-8")
            html = patch_html(html, canonical_url, None, None)
            blog_file.write_text(html, encoding="utf-8")
            report.append(f"PATCHED BLOG: blog/{blog_file.name}")

    # 4. robots.txt
    robots = f"""User-agent: *
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")
    report.append("WROTE robots.txt")

    # 5. sitemap.xml
    urls = []
    # Homepage
    urls.append((f"{DOMAIN}/", "1.00"))
    # Top-level mapped
    urls.append((f"{DOMAIN}/particleworks.html", "0.80"))
    urls.append((f"{DOMAIN}/granuleworks.html", "0.80"))
    # Alias URLs (root-level, matching backup basenames)
    for new_rel, php_name in NEW_TO_BACKUP.items():
        if "/" not in new_rel:
            continue
        alias_basename = php_name[:-4] + ".html"
        # Applications & cases get 0.64 like backup
        prio = "0.64"
        urls.append((f"{DOMAIN}/{alias_basename}", prio))
    # Blog pages
    if BLOG_DIR.exists():
        for blog_file in sorted(BLOG_DIR.glob("*.html")):
            urls.append((f"{DOMAIN}/blog/{blog_file.name}", "0.51"))

    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    from datetime import datetime
    today = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S+00:00")
    for loc, prio in urls:
        sm += [
            "  <url>",
            f"    <loc>{loc}</loc>",
            f"    <lastmod>{today}</lastmod>",
            f"    <priority>{prio}</priority>",
            "  </url>",
        ]
    sm.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(sm) + "\n", encoding="utf-8")
    report.append(f"WROTE sitemap.xml ({len(urls)} URLs)")

    return report

if __name__ == "__main__":
    rep = process()
    print("\n".join(rep))
    print(f"\nTOTAL OPS: {len(rep)}")
