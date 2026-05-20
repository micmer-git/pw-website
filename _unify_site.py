"""One-shot script to unify nav, inject favicon link, normalize paths.
Idempotent: safe to re-run.
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

EXCLUDE_DIRS = {"website_now", "8.2_inputs"}
EXCLUDE_FILES = {"index.html"}  # has special nav with search modal + CTA

def collect_html():
    out = []
    for d, dirs, fs in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in EXCLUDE_DIRS and not x.startswith('.')]
        for f in fs:
            if f.endswith('.html') and f not in EXCLUDE_FILES:
                out.append(os.path.join(d, f))
    return out

def page_prefix(html_path):
    rel = os.path.relpath(html_path, ROOT).replace('\\', '/')
    depth = rel.count('/')
    return '../' * depth

def build_nav(prefix: str, active: str | None = None) -> str:
    """Canonical navbar with dropdowns. `active` is the current page filename (no prefix)."""
    def cls(href):
        base = href.split('#')[0]
        return ' active' if active and base == active else ''
    return f'''  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="{prefix}index.html"><img src="{prefix}images/PW_Europe_logo_small.png" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-lg-center gap-1">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Products</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item{cls('particleworks.html')}" href="{prefix}particleworks.html"><i class="bi bi-droplet"></i><span><div class="dd-t">Particleworks</div><div class="dd-s">Meshfree CFD fluid solver</div></span></a></li>
              <li><a class="dropdown-item{cls('granuleworks.html')}" href="{prefix}granuleworks.html"><i class="bi bi-circle-fill"></i><span><div class="dd-t">Granuleworks</div><div class="dd-s">DEM granular simulation</div></span></a></li>
              <li><a class="dropdown-item{cls('particleworksforansys.html')}" href="{prefix}particleworksforansys.html"><i class="bi bi-plug"></i><span><div class="dd-t">Particleworks for Ansys</div><div class="dd-s">Native Workbench integration</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Applications</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item{cls('e-motors.html')}" href="{prefix}e-motors.html"><i class="bi bi-lightning-charge"></i><span><div class="dd-t">E-Motors</div><div class="dd-s">Oil-cooled electric drives</div></span></a></li>
              <li><a class="dropdown-item{cls('engines-and-pistons.html')}" href="{prefix}engines-and-pistons.html"><i class="bi bi-fuel-pump"></i><span><div class="dd-t">Engines &amp; Pistons</div><div class="dd-s">Combustion thermal</div></span></a></li>
              <li><a class="dropdown-item{cls('gearboxes-and-bearings.html')}" href="{prefix}gearboxes-and-bearings.html"><i class="bi bi-gear-wide-connected"></i><span><div class="dd-t">Gearboxes &amp; Bearings</div><div class="dd-s">Oil jet lubrication</div></span></a></li>
              <li><a class="dropdown-item{cls('clutches-and-brakes.html')}" href="{prefix}clutches-and-brakes.html"><i class="bi bi-disc"></i><span><div class="dd-t">Clutches &amp; Brakes</div><div class="dd-s">Disc cooling flows</div></span></a></li>
              <li><a class="dropdown-item{cls('cutting-tools.html')}" href="{prefix}cutting-tools.html"><i class="bi bi-scissors"></i><span><div class="dd-t">Cutting Tools</div><div class="dd-s">Machining coolant</div></span></a></li>
              <li><a class="dropdown-item{cls('mixing-and-separation.html')}" href="{prefix}mixing-and-separation.html"><i class="bi bi-hurricane"></i><span><div class="dd-t">Mixing &amp; Separation</div><div class="dd-s">Industrial processes</div></span></a></li>
              <li><a class="dropdown-item{cls('sterilization-food-and-consumer-goods.html')}" href="{prefix}sterilization-food-and-consumer-goods.html"><i class="bi bi-droplet-half"></i><span><div class="dd-t">Sterilization &amp; Consumer Goods</div><div class="dd-s">Food and cleaning</div></span></a></li>
              <li><a class="dropdown-item{cls('vehicle-management.html')}" href="{prefix}vehicle-management.html"><i class="bi bi-truck"></i><span><div class="dd-t">Vehicle Management</div><div class="dd-s">Onboard fluid systems</div></span></a></li>
              <li><a class="dropdown-item{cls('civil-engineering-and-fire-prevention.html')}" href="{prefix}civil-engineering-and-fire-prevention.html"><i class="bi bi-fire"></i><span><div class="dd-t">Civil Engineering &amp; Fire</div><div class="dd-s">Safety and infrastructure</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link{cls('case-studies.html')}" href="{prefix}case-studies.html">Case Studies</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Resources</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item{cls('resources.html')}" href="{prefix}resources.html"><i class="bi bi-file-earmark-pdf"></i><span><div class="dd-t">Resources &amp; Whitepapers</div><div class="dd-s">Technical documents</div></span></a></li>
              <li><a class="dropdown-item{cls('SPH-MPS.html')}" href="{prefix}SPH-MPS.html"><i class="bi bi-braces"></i><span><div class="dd-t">FVM vs SPH vs MPS</div><div class="dd-s">Method comparison</div></span></a></li>
              <li><a class="dropdown-item{cls('glossary.html')}" href="{prefix}glossary.html"><i class="bi bi-book"></i><span><div class="dd-t">Glossary</div><div class="dd-s">Meshfree CFD terminology</div></span></a></li>
              <li><a class="dropdown-item{cls('training.html')}" href="{prefix}training.html"><i class="bi bi-mortarboard"></i><span><div class="dd-t">Training</div><div class="dd-s">Courses &amp; workshops</div></span></a></li>
              <li><a class="dropdown-item{cls('support.html')}" href="{prefix}support.html"><i class="bi bi-life-preserver"></i><span><div class="dd-t">Support</div><div class="dd-s">Technical help</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Company</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item{cls('company.html')}" href="{prefix}company.html"><i class="bi bi-building"></i><span><div class="dd-t">About Particleworks Europe</div><div class="dd-s">Who we are</div></span></a></li>
              <li><a class="dropdown-item{cls('resellers.html')}" href="{prefix}resellers.html"><i class="bi bi-globe-europe-africa"></i><span><div class="dd-t">Resellers</div><div class="dd-s">Global partner network</div></span></a></li>
              <li><a class="dropdown-item{cls('careers.html')}" href="{prefix}careers.html"><i class="bi bi-person-plus"></i><span><div class="dd-t">Careers</div><div class="dd-s">Join the team</div></span></a></li>
              <li><a class="dropdown-item{cls('consulting.html')}" href="{prefix}consulting.html"><i class="bi bi-briefcase"></i><span><div class="dd-t">Consulting &amp; Services</div><div class="dd-s">Engineering support</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link{cls('contact.html')}" href="{prefix}contact.html">Contact</a></li>
          <li class="nav-item ms-lg-1"><a class="nav-link" href="https://www.linkedin.com/company/particleworks-europe/" target="_blank" rel="noopener" aria-label="LinkedIn" style="color:var(--pw-blue);font-size:1.15rem;"><i class="bi bi-linkedin"></i></a></li>
        </ul>
      </div>
    </div>
  </nav>'''

# Self-contained CSS to inject (only if missing). Uses CSS vars that exist on all pages.
NAV_CSS = """
    /* --- unified nav dropdown styles (auto-injected) --- */
    .navbar .dropdown-menu { border: 1px solid rgba(0,0,0,0.06); border-radius: 14px; box-shadow: 0 12px 40px rgba(0,0,0,0.10); padding: 0.6rem; margin-top: 0.4rem !important; min-width: 280px; }
    .navbar .dropdown-menu .dropdown-item { border-radius: 10px; padding: 0.55rem 0.75rem; font-size: 0.88rem; font-weight: 500; color: var(--pw-dark, #1a1a2e); display: flex; align-items: center; gap: 0.7rem; transition: background 0.15s, color 0.15s; white-space: normal; }
    .navbar .dropdown-menu .dropdown-item i { color: var(--pw-blue, #0088cc); font-size: 1.05rem; width: 20px; text-align: center; flex-shrink: 0; }
    .navbar .dropdown-menu .dropdown-item:hover,
    .navbar .dropdown-menu .dropdown-item:focus,
    .navbar .dropdown-menu .dropdown-item.active { background: linear-gradient(135deg, rgba(0,136,204,0.08), rgba(37,163,97,0.06)); color: var(--pw-blue-dark, #006da3); }
    .navbar .dropdown-menu .dd-t { font-size: 0.88rem; font-weight: 600; }
    .navbar .dropdown-menu .dd-s { font-size: 0.72rem; color: #8993a3; font-weight: 400; }
    @media (min-width: 992px) {
      .navbar .dropdown-menu { opacity: 0; visibility: hidden; transform: translateY(4px); transition: opacity 0.18s ease, transform 0.18s ease, visibility 0.18s; display: block; }
      .navbar .dropdown:hover > .dropdown-menu, .navbar .dropdown-menu.show { opacity: 1; visibility: visible; transform: translateY(0); }
    }
"""

NAV_RE = re.compile(r'(\s*)<nav class="navbar[^>]*>.*?</nav>', re.DOTALL)
HEAD_VIEWPORT_RE = re.compile(r'(<meta name="viewport"[^>]*>)')
FAVICON_RE = re.compile(r'<link rel="icon"[^>]*>')
STYLE_OPEN_RE = re.compile(r'<style\b[^>]*>')

def process(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()
    text = original
    changes = []

    prefix = page_prefix(path)
    active = os.path.basename(path)

    # 1) Replace nav block
    new_nav = build_nav(prefix, active)
    if NAV_RE.search(text):
        text = NAV_RE.sub(lambda m: m.group(1) + new_nav.lstrip(), text, count=1)
        # remove any *additional* old navs in same file (defensive: index has only one)
        changes.append('nav')

    # 2) Inject dropdown CSS into first <style> block if missing
    if '.navbar .dropdown-menu' not in text and STYLE_OPEN_RE.search(text):
        text = STYLE_OPEN_RE.sub(lambda m: m.group(0) + NAV_CSS, text, count=1)
        changes.append('css')

    # 3) Inject favicon link
    fav_href = f'{prefix}favicon.ico'
    fav_link = f'<link rel="icon" type="image/png" href="{fav_href}">'
    if not FAVICON_RE.search(text):
        text = HEAD_VIEWPORT_RE.sub(lambda m: m.group(0) + '\n  ' + fav_link, text, count=1)
        changes.append('favicon')
    else:
        # normalize existing favicon href to canonical
        text = FAVICON_RE.sub(fav_link, text, count=1)

    # 4) Normalize root-leading paths for root-level pages only
    if prefix == '':
        # href="/x" -> href="x"
        text = re.sub(r'href="/(?!/)', 'href="', text)
        text = re.sub(r"href='/(?!/)", "href='", text)
        # src="/x" -> src="x"
        text = re.sub(r'src="/(?!/)', 'src="', text)
        text = re.sub(r"src='/(?!/)", "src='", text)
        # poster="/x"
        text = re.sub(r'poster="/(?!/)', 'poster="', text)
        if text != original:
            if 'paths' not in changes: changes.append('paths')

    if text != original:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
    return {'path': os.path.relpath(path, ROOT), 'changes': changes}

def main():
    files = collect_html()
    print(f'Found {len(files)} HTML files')
    results = []
    for fp in files:
        r = process(fp)
        results.append(r)
    summary = {}
    for r in results:
        for c in r['changes']:
            summary[c] = summary.get(c, 0) + 1
    print('Summary:', summary)
    for r in results:
        if r['changes']:
            print(f"  {r['path']}: {','.join(r['changes'])}")

if __name__ == '__main__':
    main()
