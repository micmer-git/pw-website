#!/usr/bin/env python3
"""Build blog/pw-experience-2026.html (+ .php twin) from the 2025 post's chrome. Edit the talks / prose below, not the output.
Slide images: blog/images/pwe2026/slide-NN.jpg (rendered from the speakers' released PDFs); speaker photos: experience/speakers/."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'blog' / 'pw-experience-2025.html').read_text(encoding='utf8')

head = src[:src.index('<!-- Hero -->')]
head = re.sub(r'<title>.*?</title>', '<title>PW Experience 2026 — What Modena Taught Us About Heat, Air and Wear | Particleworks Europe</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Particleworks Experience 2026, Modena: seven talks on closing thermal balances, calibrating aeration against optical measurements and predicting wear with meshless CFD, with the key slide of each.">', head, count=1, flags=re.S)
CSS = '''
    /* --- PWEXP26 talk blocks --- */
    .talk-intro { display:flex; gap:1rem; align-items:center; background:linear-gradient(135deg,#fff6f3,#fdeeec); border:1px solid rgba(192,31,36,0.15); border-left:5px solid #c01f24; border-radius:14px; padding:1rem 1.2rem; margin:1.8rem 0 1.1rem; }
    .talk-intro img { width:68px; height:68px; border-radius:50%; object-fit:cover; border:3px solid #fff; box-shadow:0 3px 12px rgba(143,22,27,0.2); flex-shrink:0; }
    .talk-intro .t-time { font-size:0.72rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:#c01f24; }
    .talk-intro h3 { font-size:1.08rem; font-weight:800; line-height:1.3; margin:0.15rem 0 0.2rem; color:var(--pw-dark,#1a1a2e); }
    .talk-intro .t-who { font-size:0.85rem; color:#6c757d; }
    .keypoints { background:#f4f8fc; border:1px solid rgba(0,136,204,0.18); border-radius:14px; padding:1rem 1.3rem 0.6rem; margin:1.1rem 0; }
    .keypoints h5 { font-size:0.72rem; font-weight:800; letter-spacing:1.3px; text-transform:uppercase; color:#006da3; margin:0 0 0.6rem; }
    .keypoints ul { padding-left:1.1rem; margin:0; }
    .keypoints li { font-size:0.92rem; line-height:1.55; margin-bottom:0.45rem; }
    .eng-note { border-left:4px solid #25a361; background:#f3faf6; border-radius:0 12px 12px 0; padding:0.8rem 1.1rem; margin:1.1rem 0; font-size:0.9rem; line-height:1.6; }
    .eng-note b { color:#1e8a51; }
    figure.slide { margin:1.2rem 0 1.6rem; }
    figure.slide img { width:100%; border-radius:12px; box-shadow:0 4px 20px rgba(0,0,0,0.10); border:1px solid rgba(0,0,0,0.06); }
    figure.slide figcaption { font-size:0.8rem; color:#6c757d; margin-top:0.5rem; line-height:1.5; }
    html { scroll-behavior:smooth; }
    .article-content { font-size:1.02rem; line-height:1.75; }
    .article-content h2 { margin-top:0.4rem; }
    .sec-eyebrow { display:inline-flex; align-items:center; gap:0.45rem; font-size:0.74rem; font-weight:800; letter-spacing:1.6px; text-transform:uppercase; color:#c01f24; margin:2.6rem 0 0.3rem; }
    .sec-eyebrow::before { content:''; width:26px; height:3px; border-radius:3px; background:linear-gradient(90deg,#d9503f,#8f161b); }
    .sec-lead { font-size:1.08rem; color:#3a4150; margin-bottom:0.4rem; }
    .toc { display:flex; flex-wrap:wrap; gap:0.5rem; margin:1.2rem 0 0.4rem; }
    .toc a { font-size:0.8rem; font-weight:600; text-decoration:none; color:#8f161b; border:1px solid rgba(192,31,36,0.3); border-radius:50px; padding:0.3rem 0.85rem; background:#fff; }
    .toc a:hover { background:#c01f24; color:#fff; }
    .toc small { color:#6c757d; font-weight:500; }
    .standfirst { font-size:1.12rem; line-height:1.6; font-weight:600; color:var(--pw-dark,#1a1a2e); margin:0 0 0.9rem; }
    mark.hl { background:linear-gradient(transparent 55%, rgba(255,196,0,0.38) 55%); color:inherit; padding:0 0.1em; font-weight:600; }
    .statstrip { display:grid; grid-template-columns:repeat(auto-fit,minmax(150px,1fr)); gap:0.7rem; margin:0.4rem 0 1.1rem; }
    .stat { background:#fff; border:1px solid rgba(0,0,0,0.08); border-top:3px solid #c01f24; border-radius:12px; padding:0.7rem 0.9rem; }
    .stat b { display:block; font-size:1.45rem; line-height:1.15; font-weight:800; letter-spacing:-0.5px; color:#8f161b; }
    .stat span { display:block; font-size:0.78rem; color:#5d6670; margin-top:0.2rem; line-height:1.35; }
    .daystats { margin:1.4rem 0 0.4rem; }
    .moments-blog { display:flex; flex-wrap:wrap; gap:0.4rem; align-items:center; margin:-0.6rem 0 1.4rem; }
    .moments-blog .lbl { font-size:0.72rem; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; color:#6c757d; margin-right:0.2rem; }
    .moments-blog a { font-size:0.78rem; font-weight:600; text-decoration:none; color:#c01f24; border:1px solid rgba(192,31,36,0.3); border-radius:50px; padding:0.22rem 0.7rem 0.22rem 0.5rem; background:#fff; }
    .moments-blog a:hover { background:#c01f24; color:#fff; }
    .moments-blog a i { vertical-align:-1px; }
    @media(max-width:560px){ .talk-intro { flex-direction:column; text-align:center; } }
  </style>'''
head = head.replace('</style>', CSS, 1)

tail = src[src.index('<!-- Related Content -->'):]
tail = tail.replace('''<a href="pw-experience-2024.html" class="related-card">
                <h5>PW Experience 2024</h5>
                <p>Eleven presentations from Munich 2024 — meshless CFD goes mainstream.</p>''',
'''<a href="pw-experience-2025.html" class="related-card">
                <h5>PW Experience 2025</h5>
                <p>Munich 2025 — from validation to virtual prototyping.</p>''')
tail = tail.replace('''<a href="particleworks-82.html" class="related-card">
                <h5>Particleworks v8.2 Release</h5>
                <p>EIMPS solver, LBM coupling, anisotropic thermal and more.</p>''',
'''<a href="../experience/proceedings2026.php" class="related-card">
                <h5>Proceedings 2026</h5>
                <p>Slides and key findings of every released talk.</p>''')



def mm(t):
    return f'{t // 60}:{t % 60:02d}'


def talk(tid, time, title, who, photo, lead, stats, paras, points, slide, caption, moments, note_html=''):
    st = ''.join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in stats)
    ps = ''.join(f'\n            <p>{p}</p>' for p in paras)
    mo = ''.join(f'<a href="../experience/proceedings2026.php?talk={tid}&amp;t={t}#talk-{tid}"><i class="bi bi-play-fill"></i> {mm(t)} {lab}</a>' for t, lab in moments)
    nt = f'\n            <div class="eng-note"><b>Engineering note.</b> {note_html}</div>' if note_html else ''
    return f'''
            <div class="talk-intro" id="talk-{tid}"><img src="../experience/speakers/{photo[0]}" alt="{photo[1]}"><div><div class="t-time">{time}</div><h3>{title}</h3><div class="t-who">{who}</div></div></div>
            <p class="standfirst">{lead}</p>
            <div class="statstrip">{st}</div>{ps}{nt}
            <div class="keypoints"><h5>Key points</h5><ul>{''.join(f'<li>{p}</li>' for p in points)}</ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-{slide}.jpg" alt="{title} — key slide" loading="lazy"><figcaption><b>Key slide.</b> {caption}</figcaption></figure>
            <div class="moments-blog"><span class="lbl">Watch the moment</span>{mo}</div>'''


def sec(eyebrow, h2, lead):
    return f'\n            <div class="sec-eyebrow">{eyebrow}</div>\n            <h2>{h2}</h2>\n            <p class="sec-lead">{lead}</p>'


def hl(x):
    return f'<mark class="hl">{x}</mark>'



RD = ('04', '11:45–12:15', 'CHT Analysis of a Reciprocating Pump', 'Leonardo Lanciotti — R&amp;D CFD S.R.L. – Comet S.p.A. (IT)', ('leonardo-lanciotti.jpg', 'Leonardo Lanciotti'))
SKF = ('06', '12:45–13:15', 'Integrating Particleworks into SKF Engineering Tools: Part I', 'Lijun Cao &amp; Fabrizio Mandrile — SKF (NL)', ('lijun-cao.jpg', 'Lijun Cao'))
TRK = ('10', '16:30–17:00', 'Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method', 'Leonardo Tiberi — Track One SRL – Unimore (IT)', ('leonardo-tiberi.jpg', 'Leonardo Tiberi'))
DFL = ('07', '14:30–15:00', 'Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems', 'Dr. Lukas Hafner — deepfluid (DE), with Gianluca Parma — EnginSoft', ('lukas-hafner.jpg', 'Lukas Hafner'))
HES = ('05', '12:15–12:45', 'Moving Particle Simulation of Eroded Pelton Runners', 'Jean Decaix — HES-SO Valais/Wallis (CH)', ('jean-decaix.jpg', 'Jean Decaix'))
BRG = ('11', '17:00–17:30', 'Simulation of Sand Separation and Wear in the Börger FlowSep', 'Bernd Valtwies — Börger GmbH (DE) &amp; Riccardo Sala — EnginSoft (IT)', ('bernd-valtwies.jpg', 'Bernd Valtwies'))

BODY = '''
  <!-- Hero -->
  <section class="blog-hero">
    <div class="container">
      <div class="version-badge"><i class="bi bi-calendar-event me-1"></i> PW Experience 2026</div>
      <h1>What Modena Taught Us About Heat, Air and Wear</h1>
      <p class="lead">Modena, October 7, 2026 — six talks, the key slide of each, and the moment to watch</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 12 min read</span>
        <span><i class="bi bi-tag"></i> Conference Highlights</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p class="standfirst">On October 7, Particleworks users filled the BPER FORUM Monzani in Modena for a day built around three questions: ''' + hl('where does the heat go, where does the air go, and where does the material wear?') + '''</p>

            <p>Speakers from a bearing maker, a pump manufacturer, a hydropower research project and several engineering firms answered them with the same discipline. Each put simulation next to a thermocouple, an optical sensor or a worn prototype, and said plainly how well they agreed. This post follows six of the talks, each introduced by its speaker, with the engineering that mattered, the one slide that carries the most information, and a link to the exact moment in the recording. The slides are in the <a href="../experience/proceedings2026.php">proceedings</a>.</p>

            <div class="statstrip daystats">
              <div class="stat"><b>3–5</b><span>manual iterations to close a pump's thermal balance</span></div>
              <div class="stat"><b>&lt; 7 %</b><span>error against the bench test on a carrier roller</span></div>
              <div class="stat"><b>0.45 vs 0.43 %</b><span>simulated vs measured air in a gearbox after calibration</span></div>
              <div class="stat"><b>10 → 25 %</b><span>badly separated sand when the flow rate goes up</span></div>
            </div>

            <div class="toc">
              <a href="#talk-04">Heat · R&amp;D CFD <small>pump</small></a>
              <a href="#talk-06">Heat · SKF <small>bearings</small></a>
              <a href="#talk-10">Heat · Track One <small>roller</small></a>
              <a href="#talk-07">Air · deepfluid <small>gear oil</small></a>
              <a href="#talk-05">Wear · HES-SO <small>Pelton</small></a>
              <a href="#talk-11">Wear · Börger <small>separator</small></a>
            </div>

            <hr class="section-rule">
''' + sec('01 · Heat', 'From side effect to deliverable', 'Three talks treated temperature as the result to deliver. They share one trick: ' + hl('never run the oil and the solid together in time.') + ' Oil reaches its flow pattern in seconds, metal needs hours. So the oil is simulated briefly, its heat-transfer coefficient (HTC) and near-wall temperature are handed to a steady conjugate-heat-transfer (CHT) solution, and the two are iterated until nothing moves.') + talk(*RD,
    lead='A pump lubricated by oil sloshing, cooled by natural convection, and a thermal model that is closed by physics, not by fitting.',
    stats=[('3–5', 'manual iterations'), ('≈ 1.5 h', 'per case, once the model exists'), ('5.4 °C', 'worst thermocouple gap')],
    paras=['The case was a volumetric water pump with 3.7 kW at the shaft and 85–90% mechanical efficiency, so roughly ' + hl('0.4–0.55 kW') + ' of heat to dissipate, oil at 63 °C, ambient 22 °C. A fully coupled unsteady run would need double precision and a transient far too long, so a few seconds of sloshing give the HTC map and a steady CHT converges in minutes.',
           'The delicate input is where the heat is born. Loads on the kinematic pairs were not available, so instead of trial and error the team ran a dynamic analysis of the pump, took friction coefficients from the literature and split the power between contacts. Each source is a local volumetric heat source in a thin slice of CAD next to the contact.',
           'The results show where the model is right and where it is not. The shaft sits at 70–80 °C as in the test, and a ' + hl('hot spot at the piston–seal contact') + ' appears exactly where seals degrade in service. The small bearing comes out hotter than the large one, contrary to experiment: a sign that sloshing needs a particle refinement there.'],
    note_html='Convergence is not judged on temperatures alone. The oil is not a heat sink, so the heat it takes from the shaft must equal the heat it gives to the housing: <code>Q&#775;<sub>shaft&rarr;oil</sub> = &Sigma; HTC<sub>i</sub>(T<sub>i</sub>&minus;T<sub>oil</sub>)A<sub>i</sub> = &Sigma; HTC<sub>j</sub>(T<sub>oil</sub>&minus;T<sub>j</sub>)A<sub>j</sub></code>, on a uniform surface mesh built from the HTC map. If it is not zero, scale the thermal power, the oil temperature or the external HTC and iterate.',
    points=['Sloshing is decoupled from CHT: seconds of oil flow, minutes of steady CHT.', 'Six of seven thermocouples within 3.1 °C of the test; the worst, the open-side bearing, 5.4 °C.', 'The seal hot spot is predicted where seals fail in practice.', 'The setup can take longer than the run: the iteration itself is cheap.'],
    slide='04', caption='Simulation versus experimental thermocouples, with the difference in °C for each position (R&amp;D CFD).',
    moments=[(370, 'Why decouple sloshing and CHT'), (432, 'Power split'), (863, 'Results'), (1208, 'Q&amp;A: how many iterations?')]) + talk(*SKF,
    lead='Before trusting a heat-transfer coefficient inside a bearing tool, verify it on the simplest cases that exist, and report the spread honestly.',
    stats=[('−7 … +28 %', 'Particleworks HTC vs correlation'), ('−8 … +17 %', 'conventional CFD vs correlation'), ('4', 'radius-ratio / speed cases')],
    paras=['SKF framed thermal analysis as a ladder: lumped networks, finite-element thermal models, FE with CFD-derived HTCs one way, then fully coupled CFD. Each step buys fidelity and costs time. Their plan is the one-way rung inside the ' + hl('BEAST bearing simulation tool') + ': BEAST provides dynamics and heat sources, Particleworks provides the HTCs.',
           'The verification used a sphere in a uniform flow and oil between concentric cylinders, the inner one rotating. Against the Aoki correlation the two numerical methods scatter by similar amounts, which is the honest message: the correlation is not truth either. The vortex pattern appeared with ' + hl('mostly default settings') + ', with one caution: watch the velocity (Courant) limiter.',
           'The roadmap is concrete: a segmented bearing first, ideally with a ' + hl('cyclic boundary condition') + ', which SKF has asked for, otherwise a full bearing with strong local refinement.'],
    points=['Concentric cylinders, bearing oil, radius ratio 0.5 and 0.83, 1,500 and 3,000 rpm.', 'Particleworks HTC 352–554 W/m²K against 312–531 from the correlation.', 'Once a bearing rotates there is no good reference model, so complexity is added step by step.', 'Request to the roadmap: cyclic boundary condition for bearing segments.'],
    slide='06', caption='HTC results for the concentric-cylinders model: Particleworks, correlation and conventional CFD (SKF).',
    moments=[(904, 'BEAST + Particleworks'), (1177, 'Two verification models'), (2343, 'Results and the limiter'), (2602, 'Wish: cyclic boundary')]) + talk(*TRK,
    lead='A rotating carrier roller, a two-phase iterative CHT, and a bench test that agrees to within 7%.',
    stats=[('< 7 %', 'error vs bench test'), ('3–4', 'iterations'), ('1 day', 'per case')],
    paras=['A carrier roller holds the track chain of an excavator: the shell rotates, the shaft stays fixed, and the internal temperature decides whether the seals survive. Track One modelled every component with its own motion and material, and added the thermal boundaries a real roller has: two heat-generating surfaces (seal and bushing), a heat sink at the chain contact and on the circumferential surface, and convection to air.',
           'The iterative steady-state CHT has two phases. ' + hl('Phase 1') + ' runs the oil alone with the solids frozen and extracts averaged HTC and near-wall temperature maps: a few hours. ' + hl('Phase 2') + ' maps them on the solids and solves the new steady temperature field: a few minutes. The loop stops when the solid field no longer changes, here after three to four passes. Oil viscosity follows an Arrhenius–Vogel law, so temperature feeds back on the flow at every pass.'],
    note_html='Because the roller rotates, the contact patch that sees the chain is not fixed; a naive contact resistance would overestimate heat dissipation. Track One divides it by the footprint-to-contact area ratio &tau;: <code>R&Prime;<sub>c,eq</sub> = R&Prime;<sub>c,real</sub> / &tau;</code>. Air convection used <code>HTC<sub>air</sub> = 5.7 + 3.8&middot;v</code>.',
    points=['Phase 1 (oil only, hours) and phase 2 (solid mapping, minutes) alternate until the solid field is stable.', 'Bench test: laser sensors outside, a probe in the oil, load and speed applied through the wheels.', 'Next: oil rheology evolution, FEM coupling for deformation, critical operating conditions.'],
    slide='10', caption='Case 1: simulated against measured temperatures on collar, cover, shell, shaft and oil (Track One).',
    moments=[(466, 'Viscosity follows temperature'), (661, 'Equivalent contact resistance'), (726, 'Phase 1 / phase 2'), (850, 'Results vs bench')]) + '''

            <hr class="section-rule">
''' + sec('02 · Air', 'Measure it before you simulate it', 'Aeration changes viscosity, density, film thickness and oxidation. The afternoon showed how to put a measured number on it before the model is asked to predict it.') + talk(*DFL,
    lead='Two oils with the same air content can behave very differently, so the aeration model has to be calibrated on bubbles, not on a percentage.',
    stats=[('0.65 %', 'same air: 132 µm vs 68 µm bubbles'), ('18 → 32 m²', 'oil–air contact surface'), ('0.45 vs 0.43 %', 'simulated vs measured, after calibration')],
    paras=['An optical inline sensor sees what a single air-content number hides. In one oil, ' + hl('361 bubbles of 132 µm') + ' offered 18 m² of oil–air contact surface; in the other, ' + hl('1,289 bubbles of 68 µm') + ' offered 32 m². Same percentage, almost double the interface, so very different oxidation, cavitation and compressibility behaviour.',
           'For simulation this means calibrating the Particleworks aeration model on two things: the total air generated and the bubble size distribution. The demonstration was a differential gear at 130 rpm with 1.4 litres of oil and 2.7 million particles of 0.8 mm. Before calibration the model returned 0.12% air with 800 µm bubbles, simply the particle size. After calibration with deepfluid data: ' + hl('0.45% air and 186 µm') + ', against measured 0.43% and 180 µm.',
           'The caveat came from the room. A calibration belongs to an oil and its additive package; change the additives and it must be repeated. Coefficients can be scaled with speed from a reference speed, but the temperature dependence is still an open point.'],
    points=['Same air content can hide very different bubble populations.', 'Calibrate generation rate and size distribution: 0.12% / 800 µm becomes 0.45% / 186 µm.', 'A calibration is specific to an oil and additive package.', 'Temperature scaling of the coefficients: open point.'],
    slide='07', caption='Quantitative comparison before and after calibration: air content and bubble-size distribution against the measurement (deepfluid).',
    moments=[(325, 'Same air, different bubbles'), (732, 'Calibrating the model'), (1157, 'Before vs after'), (1316, 'Q&amp;A: new additive'), (1500, 'Temperature: open point')]) + '''

            <hr class="section-rule">
''' + sec('03 · Wear', 'Simulating what breaks', 'Two very different machines, one question: can a particle simulation say where the hardware will wear before it does?') + talk(*HES,
    lead='A Pelton runner, a single jet, and the efficiency lost to erosion computed on a GPU.',
    stats=[('5 min → 1.5 d', 'run time, coarse to fine, one L40S'), ('2–3 days', 'production lost per runner inspection'), ('3 stages', 'new, 3 years, 5 years')],
    paras=['The context is ReHydro, a Horizon Europe project of 18 partners and about 12 million euros that runs to 2028. Europe’s hydropower fleet is 50–55 years old and now balances wind and solar, so runners see sediment and cavitation erosion. Inspecting one means two or three days without production, which is why a ' + hl('prediction of the efficiency loss') + ' has real value.',
           'The set-up is lean: a single jet, imposed rotation, viscosity neglected, time step near 10<sup>&minus;6</sup> s and a Courant limiter of 0.2. Several revolutions are feasible, where a finite-volume code takes more than a week. For a new runner, dimensionless torque approaches 1 as the particle size drops from 5 to 0.5 mm, and a ' + hl('linear extrapolation to zero size') + ' lands close to it.',
           'For eroded runners, artificial erosion (flat or rounded splitter, enlarged cut-out, worn tip) was compared with analytical and published efficiency drops. Then came real runners: new, after three years and after five, when the owner decided to refurbish. The torque decrease was ' + hl('predicted accurately') + '.'],
    points=['Single jet, imposed speed, CFL limiter 0.2: 5 minutes to 1.5 days on an NVIDIA L40S.', 'Flat-splitter efficiency drop follows the analytical trend, closer with finer particles.', 'Next: let the runner speed respond to load rejection, which needs the shaft-line inertia.', 'Longer term: a brick of a digital twin for owners who ask what 2% of efficiency costs them.'],
    slide='05', caption='Dimensionless torque of three physically eroded runners (T-1 to T-3) against the erosion parameter (HES-SO).',
    moments=[(70, 'ReHydro: why erosion matters'), (443, 'Set-up and run times'), (549, 'Extrapolating to zero size'), (689, 'New, 3 and 5 years'), (1196, 'Q&amp;A: load rejection')]) + talk(*BRG,
    lead='A sand separator for biogas plants, simulated before the second prototype, and a wear map that the hardware confirmed.',
    stats=[('< 10 %', 'mass-flow deviation vs tests'), ('10 → 25 %', 'badly separated at higher flow rate'), ('≈ 6 months', '24/7 until visible wear')],
    paras=['Biogas plants are moving from maize silage to manure, which brings stones, sand and soil. Sand settles in the final storage tank (about 1.9 m after 36 months in the case shown), blocks pipes and tankers and shrinks usable volume. The FlowSep is a cyclone-like stage that sends the heavy phase to output 1 and a clean thin phase to output 2. Sand is only about 1% of the material, in fractions of 0.4–0.5, 0.3–0.4 and under 0.3 mm.',
           'Börger measured flows, densities and the ash content (800 °C burns off the organics) and EnginSoft built the Granuleworks–Particleworks model. The reference case deviated by ' + hl('less than 10% in mass flow') + ' from the tests. About 10% of the sand leaves through the wrong outlet, and it is the small particles: large ones are centrifuged radially, as intended.',
           'Then the surprise. Börger’s instinct was to raise the flow rate. The simulation showed ' + hl('the opposite') + ': at the higher flow rate the coarse fraction reaches the clean output and the badly separated share rises from about 10% to about 25%. Better to go slower and separate better.',
           'Finally, wear. The model flagged high interaction at the back plate and near the blades, and the prototype wore exactly there after roughly half a year of round-the-clock operation.'],
    note_html='Wall interaction was read from the particle number density within 1 mm of the wall, combined with velocity. With version 9, the force acting on the wall from the particles is the more direct indicator.',
    points=['Evaluation parameter: number of fraction-1 particles in the clean output.', 'Higher flow rate loses separation efficiency, against the first intuition.', 'Simulated wear zones match the prototype: back plate and bending edge.', 'Use: decide whether to widen the radius or lengthen the unit before the next prototype.'],
    slide='11', caption='Wear in the prototype housing: “the wear pattern corresponds to simulation” (Börger).',
    moments=[(330, 'The sand problem'), (619, 'How the FlowSep works'), (1364, 'Who leaks'), (1495, 'Higher flow rate'), (1661, 'Prototype wear'), (1811, 'With 9.0: wall force')]) + '''

            <hr class="section-rule">

            <div class="sec-eyebrow">From the floor</div>
            <h2>The questions that mattered</h2>

            <ul>
              <li><strong>How much effort is the manual iteration?</strong> Three to five passes, and a steady CHT takes minutes on a GPU (R&amp;D CFD).</li>
              <li><strong>Does a calibration transfer between lubricants?</strong> No: the same base oil with other additives needs a new one, and the temperature trend can flip sign (deepfluid).</li>
              <li><strong>Why such a basic first verification?</strong> Because once a bearing rotates there is no good reference model; complexity is added step by step (SKF).</li>
              <li><strong>Why dimensionless results?</strong> Owners ask what 2% of efficiency lost to a single flood costs them over a year, not for newtons (HES-SO).</li>
            </ul>

            <hr class="section-rule">

            <div class="sec-eyebrow">Take-home</div>
            <h2>What we take home</h2>

            <div class="keypoints"><h5>Three habits</h5><ul>
              <li><strong>Trust comes from a check that does not depend on the model:</strong> an oil balance at zero, a thermocouple, a bubble sensor, a worn prototype.</li>
              <li><strong>Cost was stated, not hidden:</strong> three to five iterations, a day per case, minutes for a steady solution, a particle size you can extrapolate away.</li>
              <li><strong>The physics is split on purpose:</strong> fast flow in particles, slow heat in a steady solid, measured air as calibration data.</li>
            </ul></div>

            <p>Meshless CFD in Modena looked less like a promise and more like a tool with a known price.</p>

            <div class="cta-box">
              <h3>Get the Modena proceedings</h3>
              <p>Slides, recordings and the key findings of each released presentation, free after a short form.</p>
              <a href="../experience/proceedings2026.php" class="btn-pw"><i class="bi bi-unlock me-2"></i>Open the proceedings</a>
            </div>

          </article>
        </div>
      </div>
    </div>
  </section>

  '''

html = head + BODY.lstrip('\n') + tail
(root / 'blog' / 'pw-experience-2026.html').write_text(html, encoding='utf8')
php = re.sub(r'href="((?:\.\./)?[A-Za-z0-9_\-/]+)\.html', r'href="\1.php', html)
(root / 'blog' / 'pw-experience-2026.php').write_text(php, encoding='utf8')
art = html[html.index('<article'):html.index('</article>')]
print('words in article:', len(re.sub(r'<[^>]+>', ' ', art).split()))
