"""One-shot: refresh thematic pages with animated SVG hero + inline figure.

Pages affected (9): see PAGES below.
Safe to re-run; uses exact-match replacements.
"""
import re
import random
from pathlib import Path

ROOT = Path(__file__).parent

PAGES = [
    # (relative_path, image_filename, caption, images_prefix)
    ("civil-engineering-and-fire-prevention.html", "civil-engineering-and-fire.webp",
     "Fluid and thermal simulation for civil engineering and fire prevention", "/images/case-studies/"),
    ("clutches-and-brakes.html", "clutches-brakes.webp",
     "Oil and coolant flow analysis in clutch and brake systems", "/images/case-studies/"),
    ("cutting-tools.html", "cutting-tools.webp",
     "Coolant and chip transport simulation in machining operations", "/images/case-studies/"),
    ("e-motors.html", "e-motors.webp",
     "Oil cooling and thermal management in electric motor windings", "/images/case-studies/"),
    ("engines-and-pistons.html", "engines-pistons.webp",
     "Piston cooling jets and oil splash in internal combustion engines", "/images/case-studies/"),
    ("gearboxes-and-bearings.html", "gearboxes-bearings.webp",
     "Oil jet lubrication and churning losses in gearboxes and bearings", "/images/case-studies/"),
    ("mixing-and-separation.html", "mixing-separation.webp",
     "Particle-based simulation of industrial mixing and separation processes", "/images/case-studies/"),
    ("sterilization-food-and-consumer-goods.html", "sterilization-and-cleaning.webp",
     "Sterilization, cleaning and filling processes for food and consumer goods", "/images/case-studies/"),
    ("vehicle-management.html", "vehicle-management.webp",
     "Fluid management and thermal behaviour of onboard vehicle systems", "/images/case-studies/"),
    # applications/ subfolder — same content, different filenames/prefix
    ("applications/civil-engineering.html", "civil-engineering-and-fire.webp",
     "Fluid and thermal simulation for civil engineering and fire prevention", "../images/case-studies/"),
    ("applications/clutches-and-brakes.html", "clutches-brakes.webp",
     "Oil and coolant flow analysis in clutch and brake systems", "../images/case-studies/"),
    ("applications/cutting-tools.html", "cutting-tools.webp",
     "Coolant and chip transport simulation in machining operations", "../images/case-studies/"),
    ("applications/e-motors.html", "e-motors.webp",
     "Oil cooling and thermal management in electric motor windings", "../images/case-studies/"),
    ("applications/engines-and-pistons.html", "engines-pistons.webp",
     "Piston cooling jets and oil splash in internal combustion engines", "../images/case-studies/"),
    ("applications/gearboxes-and-bearings.html", "gearboxes-bearings.webp",
     "Oil jet lubrication and churning losses in gearboxes and bearings", "../images/case-studies/"),
    ("applications/mixing-and-separation.html", "mixing-separation.webp",
     "Particle-based simulation of industrial mixing and separation processes", "../images/case-studies/"),
    ("applications/sterilization-food-consumer.html", "sterilization-and-cleaning.webp",
     "Sterilization, cleaning and filling processes for food and consumer goods", "../images/case-studies/"),
    ("applications/vehicle-management.html", "vehicle-management.webp",
     "Fluid management and thermal behaviour of onboard vehicle systems", "../images/case-studies/"),
]

# --- Generate the particle field deterministically (seeded) -------------------
random.seed(42)
particles = []
for _ in range(56):
    cx = random.randint(30, 1570)
    cy = random.randint(40, 560)
    r = random.choice([1.2, 1.5, 1.8, 2, 2.2, 2.5, 3, 3.5])
    delay = round(random.uniform(0, 12), 2)
    dur = round(random.uniform(7, 13), 1)
    particles.append(
        f'<circle class="p" cx="{cx}" cy="{cy}" r="{r}" fill="url(#pgGrad)" '
        f'style="animation-delay:{delay}s;animation-duration:{dur}s"/>'
    )

# Ring of tiny bright dots along an implied curve for extra density
ring = []
for i in range(18):
    t = i / 18
    cx = int(60 + t * 1480)
    cy = int(300 + 80 * random.uniform(-1, 1))
    ring.append(
        f'<circle class="p p-bright" cx="{cx}" cy="{cy}" r="1.2" fill="#ffffff" '
        f'style="animation-delay:{round(i*0.4,2)}s;animation-duration:9s"/>'
    )

SVG = (
    '<svg class="hero-svg" viewBox="0 0 1600 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
    '<defs>'
      '<radialGradient id="pgGrad" cx="50%" cy="50%" r="50%">'
        '<stop offset="0%" stop-color="#ffffff" stop-opacity="1"/>'
        '<stop offset="60%" stop-color="#ffffff" stop-opacity="0.55"/>'
        '<stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>'
      '</radialGradient>'
      '<linearGradient id="flowGrad" x1="0" y1="0" x2="1" y2="0">'
        '<stop offset="0%" stop-color="#ffffff" stop-opacity="0"/>'
        '<stop offset="50%" stop-color="#ffffff" stop-opacity="0.4"/>'
        '<stop offset="100%" stop-color="#ffffff" stop-opacity="0"/>'
      '</linearGradient>'
    '</defs>'
    '<path class="flow flow-1" d="M -80 320 Q 380 210 820 300 T 1700 280" stroke="url(#flowGrad)" stroke-width="1.6" fill="none"/>'
    '<path class="flow flow-2" d="M -80 190 Q 520 300 960 170 T 1700 220" stroke="url(#flowGrad)" stroke-width="1.1" fill="none"/>'
    '<path class="flow flow-3" d="M -80 430 Q 480 350 920 450 T 1700 410" stroke="url(#flowGrad)" stroke-width="1.1" fill="none"/>'
    '<path class="flow flow-4" d="M -80 120 Q 600 80 1100 140 T 1700 100" stroke="url(#flowGrad)" stroke-width="0.8" fill="none"/>'
    '<g class="particles">' + ''.join(particles + ring) + '</g>'
    '</svg>'
)

CSS_EXTRA = '''
    /* --- Hero SVG particle field --- */
    .app-hero .hero-svg { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
    .app-hero .hero-svg .flow { stroke-dasharray: 4 9; animation: pwFlowDash 18s linear infinite; opacity: 0.85; }
    .app-hero .hero-svg .flow-2 { animation-duration: 26s; animation-direction: reverse; opacity: 0.55; }
    .app-hero .hero-svg .flow-3 { animation-duration: 22s; opacity: 0.6; }
    .app-hero .hero-svg .flow-4 { animation-duration: 30s; animation-direction: reverse; opacity: 0.4; }
    .app-hero .hero-svg .p { opacity: 0; animation-name: pwParticleRise; animation-iteration-count: infinite; animation-timing-function: ease-in-out; }
    .app-hero .hero-svg .p-bright { animation-name: pwParticleTwinkle; }
    @keyframes pwFlowDash { to { stroke-dashoffset: -260; } }
    @keyframes pwParticleRise {
      0%   { opacity: 0; transform: translateY(0); }
      15%  { opacity: 1; }
      85%  { opacity: 0.9; }
      100% { opacity: 0; transform: translateY(-90px); }
    }
    @keyframes pwParticleTwinkle {
      0%,100% { opacity: 0; }
      50%     { opacity: 0.9; }
    }
    @media (prefers-reduced-motion: reduce) {
      .app-hero .hero-svg .flow,
      .app-hero .hero-svg .p { animation: none; opacity: 0.5; }
    }
    .app-hero .container { position: relative; z-index: 2; }

    /* --- Inline post figure (was hero background) --- */
    .app-figure { margin: 2.75rem auto 2.25rem; max-width: 740px; border-radius: 16px; overflow: hidden; box-shadow: 0 14px 45px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); background: #fff; }
    .app-figure img { width: 100%; height: auto; display: block; }
    .app-figure figcaption { padding: 0.85rem 1.25rem; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #64748b; font-size: 0.85rem; font-style: italic; border-top: 1px solid rgba(0,136,204,0.08); letter-spacing: 0.1px; }
'''

# Replacement for the old `.app-hero::before { ... url(...) ... }` rule.
HERO_BEFORE_NEW = (
    ".app-hero::before { content: ''; position: absolute; inset: 0; "
    "background: "
    "radial-gradient(ellipse at 18% 25%, rgba(255,255,255,0.10), transparent 55%), "
    "radial-gradient(ellipse at 82% 75%, rgba(255,255,255,0.07), transparent 55%); }"
)

HERO_BEFORE_PATTERN = re.compile(
    r"\.app-hero::before\s*\{[^{}]*url\([^)]*\)[^{}]*\}",
    re.DOTALL,
)

SECTION_OPEN = '<section class="app-hero">'
FIRST_SECTION_RULE = '<hr class="section-rule">'

def transform(html: str, image: str, caption: str, prefix: str) -> str:
    # 1. Replace the hero::before block that contained the webp URL
    new_html, n = HERO_BEFORE_PATTERN.subn(HERO_BEFORE_NEW, html, count=1)
    if n == 0:
        raise RuntimeError("hero::before url block not found")

    # 2. Skip if already transformed (idempotency)
    if '.hero-svg' in new_html and 'pwParticleRise' in new_html:
        return new_html

    # 3. Inject extra CSS just before first </style>
    new_html = new_html.replace('</style>', CSS_EXTRA + '\n  </style>', 1)

    # 4. Inject SVG right after the opening hero <section>
    new_html = new_html.replace(SECTION_OPEN, SECTION_OPEN + '\n    ' + SVG, 1)

    # 5. Insert the inline figure right before the first section-rule hr
    figure_html = (
        f'<figure class="app-figure">'
        f'<img src="{prefix}{image}" alt="{caption}" loading="lazy">'
        f'<figcaption>{caption}</figcaption>'
        f'</figure>\n\n          '
    )
    new_html = new_html.replace(FIRST_SECTION_RULE, figure_html + FIRST_SECTION_RULE, 1)
    return new_html

def main():
    for filename, image, caption, prefix in PAGES:
        path = ROOT / filename
        html = path.read_text(encoding='utf-8')
        try:
            new_html = transform(html, image, caption, prefix)
        except RuntimeError as e:
            print(f"SKIP {filename}: {e}")
            continue
        if new_html != html:
            path.write_text(new_html, encoding='utf-8')
            print(f"updated {filename}")
        else:
            print(f"unchanged {filename}")

if __name__ == '__main__':
    main()
