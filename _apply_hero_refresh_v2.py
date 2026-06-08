"""v2: per-theme animated SVG + dropdown nav + All Applications grid.

Run after v1 has already injected figure + shared SVG.
Idempotent: safe to re-run.
"""
import re
import random
from pathlib import Path

ROOT = Path(__file__).parent

# (path, image_file, caption, images_prefix, theme_key)
PAGES = [
    ("civil-engineering-and-fire-prevention.html", "civil-engineering-and-fire.webp",
     "Fluid and thermal simulation for civil engineering and fire prevention", "/images/case-studies/", "fire"),
    ("clutches-and-brakes.html", "clutches-brakes.webp",
     "Oil and coolant flow analysis in clutch and brake systems", "/images/case-studies/", "disc"),
    ("cutting-tools.html", "cutting-tools.webp",
     "Coolant and chip transport simulation in machining operations", "/images/case-studies/", "cutter"),
    ("e-motors.html", "e-motors.webp",
     "Oil cooling and thermal management in electric motor windings", "/images/case-studies/", "stator"),
    ("engines-and-pistons.html", "engines-pistons.webp",
     "Piston cooling jets and oil splash in internal combustion engines", "/images/case-studies/", "piston"),
    ("gearboxes-and-bearings.html", "gearboxes-bearings.webp",
     "Oil jet lubrication and churning losses in gearboxes and bearings", "/images/case-studies/", "gear"),
    ("mixing-and-separation.html", "mixing-separation.webp",
     "Particle-based simulation of industrial mixing and separation processes", "/images/case-studies/", "vortex"),
    ("sterilization-food-and-consumer-goods.html", "sterilization-and-cleaning.webp",
     "Sterilization, cleaning and filling processes for food and consumer goods", "/images/case-studies/", "drops"),
    ("vehicle-management.html", "vehicle-management.webp",
     "Fluid management and thermal behaviour of onboard vehicle systems", "/images/case-studies/", "road"),
    ("applications/civil-engineering.html", "civil-engineering-and-fire.webp",
     "Fluid and thermal simulation for civil engineering and fire prevention", "../images/case-studies/", "fire"),
    ("applications/clutches-and-brakes.html", "clutches-brakes.webp",
     "Oil and coolant flow analysis in clutch and brake systems", "../images/case-studies/", "disc"),
    ("applications/cutting-tools.html", "cutting-tools.webp",
     "Coolant and chip transport simulation in machining operations", "../images/case-studies/", "cutter"),
    ("applications/e-motors.html", "e-motors.webp",
     "Oil cooling and thermal management in electric motor windings", "../images/case-studies/", "stator"),
    ("applications/engines-and-pistons.html", "engines-pistons.webp",
     "Piston cooling jets and oil splash in internal combustion engines", "../images/case-studies/", "piston"),
    ("applications/gearboxes-and-bearings.html", "gearboxes-bearings.webp",
     "Oil jet lubrication and churning losses in gearboxes and bearings", "../images/case-studies/", "gear"),
    ("applications/mixing-and-separation.html", "mixing-separation.webp",
     "Particle-based simulation of industrial mixing and separation processes", "../images/case-studies/", "vortex"),
    ("applications/sterilization-food-consumer.html", "sterilization-and-cleaning.webp",
     "Sterilization, cleaning and filling processes for food and consumer goods", "../images/case-studies/", "drops"),
    ("applications/vehicle-management.html", "vehicle-management.webp",
     "Fluid management and thermal behaviour of onboard vehicle systems", "../images/case-studies/", "road"),
]

# Applications list used for dropdown + grid (icons, titles)
APPLICATIONS = [
    ("e-motors", "E-Motors", "bi-lightning-charge", "Oil-cooled electric drives"),
    ("engines-and-pistons", "Engines & Pistons", "bi-fuel-pump", "Combustion engine thermal"),
    ("gearboxes-and-bearings", "Gearboxes & Bearings", "bi-gear-wide-connected", "Oil jet lubrication"),
    ("clutches-and-brakes", "Clutches & Brakes", "bi-disc", "Disc cooling flows"),
    ("cutting-tools", "Cutting Tools", "bi-scissors", "Machining coolant"),
    ("mixing-and-separation", "Mixing & Separation", "bi-hurricane", "Industrial processes"),
    ("sterilization-food-and-consumer-goods", "Sterilization & Consumer Goods", "bi-droplet-half", "Food and cleaning"),
    ("vehicle-management", "Vehicle Management", "bi-truck", "Onboard fluid systems"),
    ("civil-engineering-and-fire-prevention", "Civil Engineering & Fire", "bi-fire", "Safety and infrastructure"),
]

# For applications/ subfolder, slugs are slightly different
SUB_SLUG_MAP = {
    "civil-engineering-and-fire-prevention": "civil-engineering",
    "sterilization-food-and-consumer-goods": "sterilization-food-consumer",
}

# -------- shared particle field (deterministic) --------
random.seed(42)
_particles = []
for _ in range(56):
    cx = random.randint(30, 1570)
    cy = random.randint(40, 560)
    r = random.choice([1.2, 1.5, 1.8, 2, 2.2, 2.5, 3, 3.5])
    delay = round(random.uniform(0, 12), 2)
    dur = round(random.uniform(7, 13), 1)
    _particles.append(
        f'<circle class="p" cx="{cx}" cy="{cy}" r="{r}" fill="url(#pgGrad)" '
        f'style="animation-delay:{delay}s;animation-duration:{dur}s"/>'
    )
_ring = []
for i in range(18):
    t = i / 18
    cx = int(60 + t * 1480)
    cy = int(300 + 80 * random.uniform(-1, 1))
    _ring.append(
        f'<circle class="p p-bright" cx="{cx}" cy="{cy}" r="1.2" fill="#ffffff" '
        f'style="animation-delay:{round(i*0.4,2)}s;animation-duration:9s"/>'
    )
PARTICLE_FIELD = ''.join(_particles + _ring)

SHARED_DEFS = (
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
      '<filter id="pwGlow" x="-50%" y="-50%" width="200%" height="200%">'
        '<feGaussianBlur stdDeviation="2"/>'
      '</filter>'
    '</defs>'
)

SHARED_FLOWS = (
    '<path class="flow flow-1" d="M -80 320 Q 380 210 820 300 T 1700 280" stroke="url(#flowGrad)" stroke-width="1.6" fill="none" stroke-linecap="round"/>'
    '<path class="flow flow-2" d="M -80 190 Q 520 300 960 170 T 1700 220" stroke="url(#flowGrad)" stroke-width="1.1" fill="none" stroke-linecap="round"/>'
    '<path class="flow flow-3" d="M -80 430 Q 480 350 920 450 T 1700 410" stroke="url(#flowGrad)" stroke-width="1.1" fill="none" stroke-linecap="round"/>'
)

# ---------- per-theme motifs ----------

def motif_fire():
    # Rising wavy flame paths
    flames = [
        (220, 1.6, 9), (360, 1.3, 11), (500, 1.4, 8),
        (1000, 1.3, 12), (1160, 1.5, 10), (1320, 1.4, 13),
    ]
    paths = []
    for i, (x, w, dur) in enumerate(flames):
        d = f"M {x} 600 C {x-18} 500 {x+22} 420 {x} 340 C {x-14} 280 {x+18} 220 {x} 140"
        paths.append(
            f'<path class="flame f{i}" d="{d}" stroke="url(#flowGrad)" stroke-width="{w}" '
            f'fill="none" stroke-linecap="round" style="animation-duration:{dur}s"/>'
        )
    return '<g class="motif motif-fire">' + ''.join(paths) + '</g>'

def motif_disc():
    ticks = ''.join([
        f'<line x1="0" y1="-175" x2="0" y2="-156" stroke="#fff" stroke-opacity="0.55" stroke-width="1.4" transform="rotate({i*15})"/>'
        for i in range(24)
    ])
    inner_ticks = ''.join([
        f'<line x1="0" y1="-110" x2="0" y2="-98" stroke="#fff" stroke-opacity="0.35" stroke-width="1" transform="rotate({i*30 + 7.5})"/>'
        for i in range(12)
    ])
    return (
        '<g class="motif motif-disc" transform="translate(1300 300)">'
          '<circle r="185" fill="none" stroke="#fff" stroke-opacity="0.12" stroke-width="1"/>'
          '<circle r="140" fill="none" stroke="#fff" stroke-opacity="0.22" stroke-width="1"/>'
          '<circle r="90" fill="none" stroke="#fff" stroke-opacity="0.32" stroke-width="1.1"/>'
          '<circle r="38" fill="none" stroke="#fff" stroke-opacity="0.5" stroke-width="1.2"/>'
          '<circle r="8" fill="#fff" fill-opacity="0.55"/>'
          f'<g class="spin spin-cw">{ticks}</g>'
          f'<g class="spin spin-ccw">{inner_ticks}</g>'
        '</g>'
    )

def motif_cutter():
    # 6 radial blades rotating + chip sparks
    blades = ''.join([
        f'<path d="M 0 -160 Q 18 -100 0 -40 Q -18 -100 0 -160 Z" fill="#fff" fill-opacity="0.18" transform="rotate({i*60})"/>'
        for i in range(6)
    ])
    sparks = ''.join([
        f'<circle class="spark" cx="{int(200*1.1*__cos(i*60))}" cy="{int(200*1.1*__sin(i*60))}" r="2" fill="#fff" style="animation-delay:{round(i*0.25,2)}s"/>'
        for i in range(12)
    ])
    return (
        '<g class="motif motif-cutter" transform="translate(320 310)">'
          '<circle r="170" fill="none" stroke="#fff" stroke-opacity="0.15" stroke-width="1"/>'
          '<circle r="45" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="1.2"/>'
          f'<g class="spin spin-fast">{blades}</g>'
          f'{sparks}'
        '</g>'
    )

def __cos(deg):
    import math
    return math.cos(math.radians(deg))
def __sin(deg):
    import math
    return math.sin(math.radians(deg))

def motif_stator():
    # Stator = outer ring with trapezoidal slot teeth pointing inward
    teeth = ''
    for i in range(18):
        # Trapezoid tooth pointing inward at angle i*20
        teeth += (
            f'<path d="M -11 -150 L 11 -150 L 7 -112 L -7 -112 Z" '
            f'fill="#fff" fill-opacity="0.22" transform="rotate({i*20})"/>'
        )
    # Rotor field lines
    field = ''.join([
        f'<line x1="0" y1="-82" x2="0" y2="-60" stroke="#fff" stroke-opacity="0.45" stroke-width="1.5" transform="rotate({i*45})"/>'
        for i in range(8)
    ])
    return (
        '<g class="motif motif-stator" transform="translate(1290 300)">'
          '<circle r="168" fill="none" stroke="#fff" stroke-opacity="0.15" stroke-width="1"/>'
          '<circle r="100" fill="none" stroke="#fff" stroke-opacity="0.18" stroke-width="1"/>'
          '<circle r="55" fill="none" stroke="#fff" stroke-opacity="0.3" stroke-width="1"/>'
          f'{teeth}'
          f'<g class="spin spin-cw">{field}</g>'
          '<circle r="7" fill="#fff" fill-opacity="0.6"/>'
        '</g>'
    )

def motif_piston():
    # 4 cylinders with pistons sliding + droplets
    cyls = []
    drops = []
    xs = [210, 540, 1060, 1390]
    for i, x in enumerate(xs):
        # Cylinder outline
        cyls.append(
            f'<g class="cylinder" transform="translate({x} 120)">'
              f'<rect x="-45" y="0" width="90" height="360" fill="none" stroke="#fff" stroke-opacity="0.22" stroke-width="1.2" rx="4"/>'
              f'<rect x="-42" y="0" width="84" height="60" fill="#fff" fill-opacity="0.04"/>'
              f'<g class="piston-inner" style="animation-delay:{i*0.5}s">'
                f'<rect x="-40" y="90" width="80" height="32" fill="#fff" fill-opacity="0.28" rx="3"/>'
                f'<line x1="-40" y1="100" x2="40" y2="100" stroke="#fff" stroke-opacity="0.5" stroke-width="0.8"/>'
                f'<line x1="-40" y1="114" x2="40" y2="114" stroke="#fff" stroke-opacity="0.5" stroke-width="0.8"/>'
              f'</g>'
            f'</g>'
        )
        # Oil jet droplets above each cylinder
        for j in range(4):
            drops.append(
                f'<circle class="drop" cx="{x}" cy="90" r="1.8" fill="#fff" fill-opacity="0.7" '
                f'style="animation-delay:{round(i*0.6 + j*0.5, 2)}s"/>'
            )
    return '<g class="motif motif-piston">' + ''.join(cyls) + ''.join(drops) + '</g>'

def motif_gear():
    # Simple stroked "gear" look via radial teeth circles
    def gear_shape(cx, cy, R, teeth_n, cls, dir_):
        out = [f'<g class="motif-gear-wrap {cls}" transform="translate({cx} {cy})">']
        out.append(f'<g class="spin spin-{dir_}">')
        out.append(f'<circle r="{R-12}" fill="none" stroke="#fff" stroke-opacity="0.35" stroke-width="1.6"/>')
        for i in range(teeth_n):
            out.append(
                f'<rect x="-6" y="-{R+2}" width="12" height="18" fill="#fff" fill-opacity="0.35" '
                f'transform="rotate({i * (360/teeth_n)})"/>'
            )
        out.append(f'<circle r="18" fill="none" stroke="#fff" stroke-opacity="0.55" stroke-width="1.2"/>')
        out.append(f'<circle r="4" fill="#fff" fill-opacity="0.6"/>')
        out.append('</g>')
        out.append('</g>')
        return ''.join(out)
    return '<g class="motif motif-gear">' + gear_shape(1100, 260, 92, 14, 'gear-a', 'cw') + gear_shape(1310, 360, 72, 12, 'gear-b', 'ccw') + '</g>'

def motif_vortex():
    # Archimedean spiral from center outward
    import math
    pts = []
    for t in range(0, 720, 4):
        a = math.radians(t)
        r = 6 + t * 0.24
        x = r * math.cos(a)
        y = r * math.sin(a)
        pts.append(f"{x:.1f},{y:.1f}")
    path = 'M ' + ' L '.join(pts)
    # Orbiting particles
    orbits = ''
    for i in range(8):
        r = 30 + i*18
        dur = 6 + i*1.2
        dir_ = 'cw' if i % 2 == 0 else 'ccw'
        orbits += (
            f'<g class="spin spin-{dir_}" style="animation-duration:{dur}s">'
              f'<circle cx="{r}" cy="0" r="{1.8 + i*0.1}" fill="#fff" fill-opacity="{0.7 - i*0.05}"/>'
            f'</g>'
        )
    return (
        '<g class="motif motif-vortex" transform="translate(1290 300)">'
          f'<path d="{path}" stroke="url(#flowGrad)" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
          f'{orbits}'
          '<circle r="6" fill="#fff" fill-opacity="0.7"/>'
        '</g>'
    )

def motif_drops():
    # Falling droplet columns
    cols = ''
    xs = [180, 340, 500, 700, 900, 1100, 1260, 1420]
    for i, x in enumerate(xs):
        # Stream line
        cols += (
            f'<line x1="{x}" y1="20" x2="{x}" y2="560" stroke="#fff" stroke-opacity="0.08" stroke-width="0.8"/>'
        )
        for k in range(4):
            cols += (
                f'<circle class="drop-fall" cx="{x}" cy="-20" r="{2 - k*0.2}" fill="#fff" fill-opacity="0.65" '
                f'style="animation-delay:{round(i*0.3 + k*1.1, 2)}s;animation-duration:{round(5.5 + (i%3)*0.4, 1)}s"/>'
            )
    return '<g class="motif motif-drops">' + cols + '</g>'

def motif_road():
    # Horizontal dashed lanes (like highways)
    lanes = ''
    ys = [170, 260, 360, 450]
    for i, y in enumerate(ys):
        lanes += (
            f'<line class="lane l{i}" x1="-80" y1="{y}" x2="1700" y2="{y}" '
            f'stroke="#fff" stroke-opacity="0.4" stroke-width="2" stroke-linecap="round" '
            f'stroke-dasharray="24 36" style="animation-duration:{round(8 + i*2, 1)}s"/>'
        )
    # Moving "vehicles" (small horizontal bars)
    bars = ''
    for i, y in enumerate(ys):
        bars += (
            f'<g class="vehicle" style="animation-delay:{round(i*1.2, 1)}s;animation-duration:{round(12 + i*2, 1)}s">'
              f'<rect x="0" y="{y-6}" width="44" height="12" fill="#fff" fill-opacity="0.35" rx="3"/>'
            f'</g>'
        )
    return '<g class="motif motif-road">' + lanes + bars + '</g>'

MOTIFS = {
    'fire': motif_fire,
    'disc': motif_disc,
    'cutter': motif_cutter,
    'stator': motif_stator,
    'piston': motif_piston,
    'gear': motif_gear,
    'vortex': motif_vortex,
    'drops': motif_drops,
    'road': motif_road,
}

def build_svg(theme: str) -> str:
    motif_svg = MOTIFS[theme]()
    return (
        '<svg class="hero-svg" viewBox="0 0 1600 600" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false">'
        + SHARED_DEFS
        + SHARED_FLOWS
        + motif_svg
        + '<g class="particles">' + PARTICLE_FIELD + '</g>'
        + '</svg>'
    )

# ---------- CSS (base + motif-specific) ----------

BASE_CSS = '''
    /* === HERO SVG PARTICLE SYSTEM (v2) === */
    .app-hero { padding-top: 9rem; }
    .app-hero .hero-svg { position: absolute; inset: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
    .app-hero .hero-svg .flow { stroke-dasharray: 4 9; animation: pwFlowDash 18s linear infinite; opacity: 0.85; }
    .app-hero .hero-svg .flow-2 { animation-duration: 26s; animation-direction: reverse; opacity: 0.55; }
    .app-hero .hero-svg .flow-3 { animation-duration: 22s; opacity: 0.6; }
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
    .app-hero .hero-svg .spin { transform-box: fill-box; transform-origin: center; animation-iteration-count: infinite; animation-timing-function: linear; }
    .app-hero .hero-svg .spin-cw  { animation-name: pwSpin;     animation-duration: 26s; }
    .app-hero .hero-svg .spin-ccw { animation-name: pwSpinRev; animation-duration: 32s; }
    .app-hero .hero-svg .spin-fast{ animation-name: pwSpin;     animation-duration: 11s; }
    @keyframes pwSpin    { to { transform: rotate(360deg); } }
    @keyframes pwSpinRev { to { transform: rotate(-360deg); } }

    /* motif: fire */
    .motif-fire .flame { stroke-dasharray: 6 10; animation-name: pwFlowDash; animation-iteration-count: infinite; animation-timing-function: linear; opacity: 0.75; }

    /* motif: cutter sparks */
    .motif-cutter .spark { opacity: 0; animation: pwSparkPulse 2.4s ease-out infinite; transform-box: fill-box; transform-origin: center; }
    @keyframes pwSparkPulse {
      0%, 20% { opacity: 0; transform: scale(0.4); }
      40%     { opacity: 1; transform: scale(1); }
      100%    { opacity: 0; transform: scale(1.6); }
    }

    /* motif: piston movement */
    .motif-piston .piston-inner { transform-box: fill-box; transform-origin: center; animation: pwPistonStroke 1.6s ease-in-out infinite; }
    @keyframes pwPistonStroke {
      0%,100% { transform: translateY(0); }
      50%     { transform: translateY(200px); }
    }
    .motif-piston .drop { opacity: 0; animation: pwDropFall 2.4s ease-in infinite; transform-box: fill-box; transform-origin: center; }
    @keyframes pwDropFall {
      0%   { opacity: 0; transform: translateY(0); }
      15%  { opacity: 1; }
      100% { opacity: 0; transform: translateY(90px); }
    }

    /* motif: drops rain */
    .motif-drops .drop-fall { opacity: 0; animation-name: pwRainFall; animation-iteration-count: infinite; animation-timing-function: ease-in; transform-box: fill-box; transform-origin: center; }
    @keyframes pwRainFall {
      0%   { opacity: 0; transform: translateY(0); }
      10%  { opacity: 0.9; }
      90%  { opacity: 0.9; }
      100% { opacity: 0; transform: translateY(580px); }
    }

    /* motif: road lanes + vehicles */
    .motif-road .lane { stroke-dashoffset: 0; animation-name: pwLaneScroll; animation-iteration-count: infinite; animation-timing-function: linear; }
    @keyframes pwLaneScroll { to { stroke-dashoffset: -240; } }
    .motif-road .vehicle { transform-box: fill-box; transform-origin: center; animation-name: pwVehicleSlide; animation-iteration-count: infinite; animation-timing-function: linear; }
    @keyframes pwVehicleSlide {
      0%   { transform: translateX(-100px); }
      100% { transform: translateX(1700px); }
    }

    @media (prefers-reduced-motion: reduce) {
      .app-hero .hero-svg * { animation: none !important; }
      .app-hero .hero-svg .flow { opacity: 0.5; }
    }

    .app-hero .container { position: relative; z-index: 2; }

    /* === INLINE FIGURE === */
    .app-figure { margin: 2.75rem auto 2.25rem; max-width: 740px; border-radius: 16px; overflow: hidden; box-shadow: 0 14px 45px rgba(0,0,0,0.08); border: 1px solid rgba(0,0,0,0.05); background: #fff; }
    .app-figure img { width: 100%; height: auto; display: block; }
    .app-figure figcaption { padding: 0.85rem 1.25rem; background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%); color: #64748b; font-size: 0.85rem; font-style: italic; border-top: 1px solid rgba(0,136,204,0.08); letter-spacing: 0.1px; }

    /* === DROPDOWN NAV === */
    .navbar .dropdown-menu { border: 1px solid rgba(0,0,0,0.06); border-radius: 14px; box-shadow: 0 12px 40px rgba(0,0,0,0.10); padding: 0.6rem; margin-top: 0.4rem !important; min-width: 280px; }
    .navbar .dropdown-menu .dropdown-item { border-radius: 10px; padding: 0.55rem 0.75rem; font-size: 0.88rem; font-weight: 500; color: var(--pw-dark); display: flex; align-items: center; gap: 0.7rem; transition: background 0.15s, color 0.15s; }
    .navbar .dropdown-menu .dropdown-item i { color: var(--pw-blue); font-size: 1.05rem; width: 20px; text-align: center; }
    .navbar .dropdown-menu .dropdown-item:hover,
    .navbar .dropdown-menu .dropdown-item:focus { background: linear-gradient(135deg, rgba(0,136,204,0.08), rgba(37,163,97,0.06)); color: var(--pw-blue-dark); }
    .navbar .dropdown-menu .dd-caption { font-size: 0.72rem; color: #8993a3; font-weight: 400; margin-left: auto; }
    @media (min-width: 992px) { .navbar .dropdown-menu { opacity: 0; visibility: hidden; transform: translateY(4px); transition: opacity 0.18s ease, transform 0.18s ease, visibility 0.18s; display: block; } .navbar .dropdown:hover > .dropdown-menu, .navbar .dropdown-menu.show { opacity: 1; visibility: visible; transform: translateY(0); } }

    /* === ALL APPLICATIONS GRID === */
    .all-apps-section { padding: 4rem 0 3rem; background: #fbfcfd; border-top: 1px solid rgba(0,0,0,0.04); }
    .all-apps-section .apps-eyebrow { font-size: 0.72rem; font-weight: 700; letter-spacing: 2px; color: var(--pw-blue); text-transform: uppercase; margin-bottom: 0.5rem; }
    .all-apps-section h3 { font-size: 1.65rem; font-weight: 800; color: var(--pw-dark); margin-bottom: 0.35rem; letter-spacing: -0.4px; }
    .all-apps-section .apps-sub { color: var(--pw-gray); font-size: 0.97rem; margin-bottom: 2rem; }
    .app-tile { display: flex; align-items: center; gap: 0.85rem; padding: 1rem 1.15rem; background: #fff; border: 1px solid rgba(0,0,0,0.06); border-radius: 14px; text-decoration: none; color: var(--pw-dark); transition: all 0.22s; height: 100%; }
    .app-tile:hover { border-color: var(--pw-blue); transform: translateY(-3px); box-shadow: 0 10px 30px rgba(0,136,204,0.12); color: var(--pw-dark); }
    .app-tile .tile-icon { flex: 0 0 42px; height: 42px; width: 42px; border-radius: 12px; background: linear-gradient(135deg, rgba(0,136,204,0.1), rgba(37,163,97,0.1)); display: flex; align-items: center; justify-content: center; color: var(--pw-blue); font-size: 1.15rem; }
    .app-tile .tile-title { font-size: 0.92rem; font-weight: 600; margin: 0; line-height: 1.25; }
    .app-tile .tile-sub { font-size: 0.76rem; color: var(--pw-gray); margin: 0; }
    .app-tile.current { background: linear-gradient(135deg, rgba(0,136,204,0.05), rgba(37,163,97,0.05)); border-color: rgba(0,136,204,0.25); }
'''

# ---------- navbar builder ----------

def build_nav(prefix: str, current_slug: str) -> str:
    """prefix: '' for root pages, '../' for applications/ pages.
       Relative paths so the site works both at domain root
       (particleworks-europe.com) and in a subfolder
       (micmer-git.github.io/pw-website/)."""
    dropdown_items = ''
    for slug, title, icon, sub in APPLICATIONS:
        if prefix == '':
            href = f'{slug}.html'
        else:
            sub_slug = SUB_SLUG_MAP.get(slug, slug)
            href = f'{sub_slug}.html'
        active = ' active' if slug == current_slug else ''
        dropdown_items += (
            f'<li><a class="dropdown-item{active}" href="{href}">'
            f'<i class="bi {icon}"></i>'
            f'<span><div class="tile-title" style="font-size:0.88rem;font-weight:600;">{title}</div>'
            f'<div class="dd-caption-inline" style="font-size:0.73rem;color:#8993a3;font-weight:400;">{sub}</div></span>'
            f'</a></li>'
        )
    home = f'{prefix}index.html'
    pw = f'{prefix}particleworks.html'
    gw = f'{prefix}granuleworks.html'
    cases = f'{prefix}case-studies.html'
    company = f'{prefix}company.html'
    contact = f'{prefix}contact.html'
    logo = f'{prefix}images/PW_Europe_logo_small.png'
    return f'''<nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="{home}"><img src="{logo}" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-lg-center gap-1">
          <li class="nav-item"><a class="nav-link" href="{home}">Home</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Products</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="{pw}"><i class="bi bi-droplet"></i><span><div style="font-size:0.88rem;font-weight:600;">Particleworks</div><div style="font-size:0.73rem;color:#8993a3;">Meshfree CFD fluid solver</div></span></a></li>
              <li><a class="dropdown-item" href="{gw}"><i class="bi bi-circle-fill"></i><span><div style="font-size:0.88rem;font-weight:600;">Granuleworks</div><div style="font-size:0.73rem;color:#8993a3;">DEM granular simulation</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Applications</a>
            <ul class="dropdown-menu dropdown-menu-end">
              {dropdown_items}
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="{cases}">Case Studies</a></li>
          <li class="nav-item"><a class="nav-link" href="{company}">Company</a></li>
          <li class="nav-item"><a class="nav-link" href="{contact}">Contact</a></li>
          <li class="nav-item"><a class="nav-link" href="https://www.linkedin.com/company/particleworks-europe/" target="_blank" aria-label="LinkedIn"><i class="bi bi-linkedin"></i></a></li>
        </ul>
      </div>
    </div>
  </nav>'''

# ---------- All Applications grid ----------

def build_all_apps_grid(prefix: str, current_slug: str) -> str:
    tiles = ''
    for slug, title, icon, sub in APPLICATIONS:
        if prefix == '':
            href = f'{slug}.html'
        else:
            sub_slug = SUB_SLUG_MAP.get(slug, slug)
            href = f'{sub_slug}.html'
        is_current = slug == current_slug
        cls = 'app-tile current' if is_current else 'app-tile'
        marker = '<span class="badge bg-light text-muted ms-auto" style="font-size:0.65rem;font-weight:600;letter-spacing:0.4px;">VIEWING</span>' if is_current else ''
        tiles += f'''
            <div class="col-lg-4 col-md-6">
              <a href="{href}" class="{cls}">
                <span class="tile-icon"><i class="bi {icon}"></i></span>
                <div>
                  <p class="tile-title">{title}</p>
                  <p class="tile-sub">{sub}</p>
                </div>
                {marker}
              </a>
            </div>'''
    return f'''  <section class="all-apps-section" id="all-applications">
    <div class="container">
      <div class="text-center">
        <p class="apps-eyebrow">Explore</p>
        <h3>All Industry Applications</h3>
        <p class="apps-sub">Discover how Particleworks powers simulation across sectors.</p>
      </div>
      <div class="row g-3">{tiles}
      </div>
    </div>
  </section>

'''

# ---------- transformations ----------

SVG_PATTERN = re.compile(r'<svg class="hero-svg"[\s\S]*?</svg>', re.DOTALL)
CSS_BLOCK_PATTERN = re.compile(
    r'\n\s*/\* --- Hero SVG particle field --- \*/[\s\S]*?\.app-figure figcaption\s*\{[^}]*\}',
    re.DOTALL,
)
CSS_BLOCK_V2_PATTERN = re.compile(
    r'\n\s*/\* === HERO SVG PARTICLE SYSTEM \(v2\) === \*/[\s\S]*?\.app-tile\.current\s*\{[^}]*\}',
    re.DOTALL,
)
NAV_PATTERN = re.compile(r'<nav class="navbar navbar-expand-lg fixed-top">[\s\S]*?</nav>', re.DOTALL)
CTA_OPEN = '<section class="cta-section">'
ALL_APPS_MARKER = 'id="all-applications"'

def transform(html: str, theme: str, prefix: str, current_slug: str) -> str:
    # 1) Replace hero SVG with per-theme version
    new_svg = build_svg(theme)
    html, n = SVG_PATTERN.subn(new_svg, html, count=1)
    if n == 0:
        raise RuntimeError("hero-svg not found")

    # 2) Replace v1 or v2 CSS block with new BASE_CSS
    if CSS_BLOCK_V2_PATTERN.search(html):
        html = CSS_BLOCK_V2_PATTERN.sub('\n' + BASE_CSS.rstrip(), html, count=1)
    else:
        html = CSS_BLOCK_PATTERN.sub('\n' + BASE_CSS.rstrip(), html, count=1)

    # 3) Replace navbar
    new_nav = build_nav(prefix, current_slug)
    html = NAV_PATTERN.sub(new_nav, html, count=1)

    # 4) Insert All Applications grid before CTA section (or replace existing)
    grid_html = build_all_apps_grid(prefix, current_slug)
    if ALL_APPS_MARKER in html:
        # Replace existing grid section to keep idempotent
        html = re.sub(
            r'  <section class="all-apps-section" id="all-applications">[\s\S]*?</section>\s*\n\s*\n',
            grid_html,
            html, count=1
        )
    else:
        html = html.replace(CTA_OPEN, grid_html + '  ' + CTA_OPEN, 1)

    return html

def main():
    for filename, image, caption, img_prefix, theme in PAGES:
        path = ROOT / filename
        html = path.read_text(encoding='utf-8')
        # Current slug for the grid (root slug, matching APPLICATIONS list)
        root_slug = Path(filename).stem
        # Map applications/ subfolder slugs back to root slugs for "current" highlight
        reverse_sub = {v: k for k, v in SUB_SLUG_MAP.items()}
        current_slug = reverse_sub.get(root_slug, root_slug)
        # nav prefix
        nav_prefix = '../' if filename.startswith('applications/') else ''
        try:
            new_html = transform(html, theme, nav_prefix, current_slug)
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
