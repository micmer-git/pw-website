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


def talk(time, title, who, photo, body_html, points, slide, caption):
    return f'''
            <div class="talk-intro"><img src="../experience/speakers/{photo[0]}" alt="{photo[1]}"><div><div class="t-time">{time}</div><h3>{title}</h3><div class="t-who">{who}</div></div></div>
{body_html}
            <div class="keypoints"><h5>Key points</h5><ul>{''.join(f'<li>{p}</li>' for p in points)}</ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-{slide}.jpg" alt="{title} — key slide" loading="lazy"><figcaption>{caption}</figcaption></figure>'''


def note(html):
    return f'\n            <div class="eng-note"><b>Engineering note.</b> {html}</div>'


BODY = '''
  <!-- Hero -->
  <section class="blog-hero">
    <div class="container">
      <div class="version-badge"><i class="bi bi-calendar-event me-1"></i> PW Experience 2026</div>
      <h1>What Modena Taught Us About Heat, Air and Wear</h1>
      <p class="lead">Modena, October 7, 2026 — seven talks, the key slide of each</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 11 min read</span>
        <span><i class="bi bi-tag"></i> Conference Highlights</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p>On October 7, Particleworks users filled the BPER FORUM Monzani in Modena for a day that opened with the release of Particleworks 9.0 and Granuleworks 4.0 and closed, nine hours later, with a group photo. In between, speakers from bearing makers, e-drive engineers, a hydropower research project, a pump manufacturer and several engineering firms kept returning to three questions: <strong>where does the heat go, where does the air go, and where does the material wear?</strong></p>

            <p>None of the talks was a software demo. Each put simulation next to a thermocouple, an optical sensor or a worn prototype, and said plainly how well they agreed. Below, the seven talks that the speakers released for sharing, each with the one slide that carries the most information. The full slides are in the <a href="../experience/proceedings2026.php">proceedings</a>.</p>

            <hr class="section-rule">

            <h2>The release, seen through industrial cases</h2>
''' + talk('09:00–10:00', 'Particleworks 9.0 &amp; Granuleworks 4.0', 'Issei Masaie &amp; Iori Saigo — Prometech Software (JP)',
    ('iori-saigo.jpg', 'Iori Saigo'),
    '''            <p>The morning keynote did not walk through a feature list; it showed what the new capabilities do on real geometries. The most concrete number came from a ribbon mixer with 16 million particles solved with a double-precision DEM solver: one, two and four A100 GPUs gave speed-ups of 1.00, 1.96 and 3.49, which is about 87% parallel efficiency at four cards. That is what turns a day-long powder run into an overnight one.</p>

            <p>The same logic applied to structures. DEM can now output the force distribution on walls, until now an MPS-only quantity, and the example was shot peening, where the contour of the summed force shows directly where a component takes the load. For heat, a two-way DEM&ndash;MPS&ndash;CHT coupling solves fluid, powder and wall temperatures together, with a temperature for each powder particle; the case shown was a plastic-pellet cooling silo, where powder volume and uneven distribution locally change the heat transfer.</p>''',
    ['Multi-GPU DEM: <strong>3.49&times; on 4 A100</strong> for 16 M particles in double precision.',
     'DEM wall-force output makes wear and load visible on structures (shot-peening example).',
     'DEM&ndash;MPS&ndash;CHT: per-particle powder temperature coupled both ways with fluid and wall.',
     'Elastic-body model: a valve with fixed edges under flow and screen printing coupled with MPS; the liquid-film HTC model now flags regions of higher heat transfer than the conventional model.'],
    '01', 'Multi-GPU support for DEM: speed-up of the ribbon-mixer case on 1, 2 and 4 A100 GPUs (Prometech).') + '''

            <hr class="section-rule">

            <h2>Heat: from side effect to deliverable</h2>

            <p>Three talks treated temperature as the result to deliver. They share one trick: <strong>never run the oil and the solid together in time.</strong> Oil reaches its flow pattern in seconds; metal needs hours. So the oil is simulated briefly, its heat-transfer coefficient (HTC) and near-wall temperature are handed to a steady conjugate-heat-transfer (CHT) solution, and the two are iterated until nothing moves.</p>
''' + talk('11:45–12:15', 'CHT Analysis of a Reciprocating Pump', 'Leonardo Lanciotti — R&amp;D CFD S.R.L. – Comet S.p.A. (IT)',
    ('leonardo-lanciotti.jpg', 'Leonardo Lanciotti'),
    '''            <p>The case was a volumetric water pump lubricated by oil sloshing in the crankcase, with heat leaving by natural convection: 3.7 kW at the shaft and 85&ndash;90% mechanical efficiency, so roughly 0.4&ndash;0.55 kW to dissipate, with the oil at 63 °C and ambient at 22 °C. A fully coupled unsteady model would need double precision and a thermal transient far too long to run, so the team used a few seconds of sloshing to get the HTC map and then a steady CHT that converges in minutes.</p>

            <p>The delicate input is where the heat is born. Loads on the kinematic pairs were not available, so instead of trial and error the team ran a dynamic analysis of the pump, took friction coefficients from the literature and split the power between contacts; each source is applied as a local volumetric heat source in a thin slice of CAD next to the contact. The results show where the model is right and where it is not: the shaft sits at 70&ndash;80 °C as in the test, a hot spot appears at the piston&ndash;seal contact, which is exactly where seals degrade in service, while the small bearing comes out hotter than the large one, contrary to experiment, a sign that sloshing needs a particle refinement there.</p>''' + note('Convergence is not judged on temperatures alone. The oil is not a heat sink, so the heat it takes from the shaft must equal the heat it gives to the housing: <code>Q&#775;<sub>shaft&rarr;oil</sub> = &Sigma; HTC<sub>i</sub>(T<sub>i</sub>&minus;T<sub>oil</sub>)A<sub>i</sub> = &Sigma; HTC<sub>j</sub>(T<sub>oil</sub>&minus;T<sub>j</sub>)A<sub>j</sub></code>, evaluated on a uniform surface mesh from the Particleworks HTC map. If it is not zero, scale the thermal power, the oil temperature or the external HTC and iterate.'),
    ['Sloshing is decoupled from CHT: seconds of oil flow, minutes of steady CHT.',
     'Six of seven thermocouples within 3.1 °C of the test; the worst, the open-side bearing, is off by 5.4 °C.',
     'The seal hot spot is predicted where seals fail in practice.',
     '<strong>3&ndash;5 manual iterations, about 1.5 hours per case</strong> once the model exists; the setup can take longer than the run.'],
    '04', 'Simulation versus experimental thermocouples on the pump, with the difference in °C for each position (R&amp;D CFD).') + talk('12:45–13:15', 'Integrating Particleworks into SKF Engineering Tools: Part I', 'Lijun Cao &amp; Fabrizio Mandrile — SKF (NL)',
    ('lijun-cao.jpg', 'Lijun Cao'),
    '''            <p>SKF framed the problem as a ladder: lumped thermal networks, finite-element thermal models, then FE with CFD-derived HTCs one way, then fully coupled CFD. Each step buys fidelity and costs time. Their plan is the one-way rung inside the BEAST bearing simulation tool: BEAST provides the dynamics and heat sources, Particleworks provides the HTCs, and the combination shortens iteration cycles. Before trusting it, they verified the HTC on two textbook cases, a sphere in a uniform flow and oil between concentric cylinders, the inner one rotating.</p>

            <p>The result is instructive because it is not flattering to anyone. Against the Aoki correlation, Particleworks lay between &minus;7% and +28% over four combinations of radius ratio and speed, and the conventional CFD code between &minus;8% and +17%: the two numerical methods scatter around the correlation by similar amounts. What mattered to SKF is that the vortex pattern appeared with mostly default settings, and the one caution was to watch the velocity (Courant) limiter. The roadmap is concrete: a segmented bearing model first, ideally with a cyclic boundary condition, which SKF has asked for, otherwise a full bearing with strong local refinement.</p>''',
    ['One-way coupling: BEAST dynamics and heat sources, Particleworks HTC, FE thermal solution.',
     'Concentric cylinders, bearing oil, radius ratio 0.5 and 0.83, 1,500 and 3,000 rpm: <strong>HTC of 352&ndash;554 W/m&sup2;K</strong> against 312&ndash;531 from the correlation.',
     'Mostly default settings reproduced the vortex pattern; mind the velocity limiter.',
     'Request to the roadmap: cyclic boundary condition for bearing segments.'],
    '06', 'HTC results for the concentric-cylinders model: Particleworks, correlation and conventional CFD (SKF).') + talk('16:30–17:00', 'Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method', 'Leonardo Tiberi — Track One SRL – Unimore (IT)',
    ('leonardo-tiberi.jpg', 'Leonardo Tiberi'),
    '''            <p>A carrier roller holds the track chain of an excavator: the shell rotates, the shaft stays fixed, and the internal temperature decides whether the seals survive. Track One modelled every component with its own motion and material and added the thermal boundaries a real roller has: two heat-generating surfaces (seal and bushing), a heat sink at the chain contact and the circumferential surface, and convection to air.</p>

            <p>The iterative steady-state CHT has two phases. Phase 1 runs the oil alone with the solids frozen and extracts averaged HTC and near-wall temperature maps, a few hours of simulation; phase 2 maps them onto the solids and solves the new steady temperature field, a few minutes. The loop stops when the solid field no longer changes within a tolerance, which here took three to four iterations. Oil viscosity follows an Arrhenius&ndash;Vogel law, so oil temperature feeds back on the flow at every pass.</p>''' + note('Because the roller rotates, the contact patch that sees the chain is not fixed; a naive contact resistance would overestimate heat dissipation. Track One divides it by the footprint-to-contact area ratio &tau;: <code>R&Prime;<sub>c,eq</sub> = R&Prime;<sub>c,real</sub> / &tau;</code>. Air convection used <code>HTC<sub>air</sub> = 5.7 + 3.8&middot;v</code>.'),
    ['Phase 1 (oil only, hours) and phase 2 (solid mapping, minutes) alternate until the solid field is stable.',
     '<strong>3&ndash;4 iterations</strong>; about one day per case.',
     'Errors against the bench test below 7% on thermocouples and oil in both load cases (laser sensors outside, probe in the oil).',
     'Next: oil rheology evolution, FEM coupling for deformation, critical operating conditions.'],
    '10', 'Case 1: simulated against measured temperatures on collar, cover, shell, shaft and oil (Track One).') + '''

            <hr class="section-rule">

            <h2>Air: measure it before you simulate it</h2>
''' + talk('14:30–15:00', 'Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems', 'Dr. Lukas Hafner — deepfluid (DE), with Gianluca Parma — EnginSoft',
    ('lukas-hafner.jpg', 'Lukas Hafner'),
    '''            <p>An optical inline sensor sees what a single air-content number hides. The slide that opened the measurement part showed two oils at the same 0.65% air: in one, 361 bubbles of 132 µm average diameter offering 18 m&sup2; of oil&ndash;air contact surface; in the other, 1,289 bubbles of 68 µm and 32 m&sup2;. Same percentage, almost double the interface, so very different oxidation, cavitation and compressibility behaviour. Hafner added that cavitation maps correlate with both air content and bubble size.</p>

            <p>For simulation this means calibrating the Particleworks aeration model on two things, the total air generated and the bubble size distribution, and then using it also away from the calibration point. The demonstration was a differential gear at 130 rpm with 1.4 litres of oil and 2.7 million particles of 0.8 mm. Before calibration the model returned 0.12% air with 800 µm bubbles, simply the particle size. After calibration with deepfluid data it returned <strong>0.45% air and 186 µm bubbles against measured values of 0.43% and 180 µm</strong>.</p>''',
    ['Same air content can hide very different bubble populations: 132 µm / 18 m&sup2; versus 68 µm / 32 m&sup2;.',
     'Calibrate both generation rate and size distribution: 0.12% / 800 µm becomes 0.45% / 186 µm (measured 0.43% / 180 µm).',
     'A calibration belongs to an oil and its additive package: change the additives and it must be repeated.',
     'Coefficients can be scaled with speed from a reference speed; the temperature dependence is an open point.'],
    '07', 'Quantitative comparison before and after calibration: air content and bubble-size distribution against the measurement (deepfluid).') + '''

            <hr class="section-rule">

            <h2>Wear: simulating what breaks</h2>
''' + talk('12:15–12:45', 'Moving Particle Simulation of Eroded Pelton Runners', 'Jean Decaix — HES-SO Valais/Wallis (CH)',
    ('jean-decaix.jpg', 'Jean Decaix'),
    '''            <p>The context is ReHydro, a Horizon Europe project of 18 partners and about 12 million euros that runs to 2028. Europe&rsquo;s hydropower fleet is 50&ndash;55 years old and must now balance wind and solar, so runners see sediment and cavitation erosion that costs efficiency, and inspecting one means two or three days without production. HES-SO&rsquo;s question was whether MPS can compute the torque, and the torque loss, of an eroded Pelton runner.</p>

            <p>The setup is lean: a single jet, imposed rotation, viscosity neglected, a time step near 10<sup>&minus;6</sup> s and a Courant limiter of 0.2, from 5 minutes (coarse) to 1.5 days (fine) on an NVIDIA L40S. Several full revolutions are feasible, which Decaix noted a finite-volume code takes more than a week to do. For a new runner, dimensionless torque rises as the particle size goes from 5 to 0.5 mm, and a linear extrapolation to zero size lands close to 1. For eroded runners, he first used artificial erosion (a flat or rounded splitter, an enlarged cut-out, a worn tip) to compare the efficiency drop with analytical and published results, then real runners at three stages: new, after three years and after five, when the owner decided to refurbish.</p>''',
    ['Single jet, imposed speed, CFL limiter 0.2: 5 minutes to 1.5 days on an L40S.',
     'Torque converges towards the target as particle size shrinks; extrapolating to zero size gives a cheap estimate.',
     'Efficiency drop from a flat splitter follows the analytical trend, closer with finer particles.',
     '<strong>Torque loss from real erosion is predicted accurately</strong>; next, letting the runner speed respond to load rejection, which needs the shaft-line inertia.'],
    '05', 'Dimensionless torque of three physically eroded runners (T-1 to T-3) against the erosion parameter (HES-SO).') + talk('17:00–17:30', 'Simulation of Sand Separation and Wear in the Börger FlowSep', 'Bernd Valtwies — Börger GmbH (DE) &amp; Riccardo Sala — EnginSoft (IT)',
    ('bernd-valtwies.jpg', 'Bernd Valtwies'),
    '''            <p>Biogas plants are moving from maize silage to manure, which brings stones, sand and soil. Sand settles in the final storage tank (about 1.9 m of it after 36 months in the case shown), blocks pipes and tankers and shrinks usable volume. The FlowSep is a cyclone-like stage behind Börger&rsquo;s BioSelect that sends the heavy phase to output 1 and a clean thin phase to output 2. Sand is only about 1% of the material, split in fractions of 0.4&ndash;0.5, 0.3&ndash;0.4 and under 0.3 mm, and in the thin phase of the real machine the coarsest fraction is completely gone.</p>

            <p>Börger measured flows, densities and the ash content (heating to 800 °C burns off the organics) and EnginSoft built the Granuleworks&ndash;Particleworks model. The reference case deviated by <strong>less than 10% in mass flow</strong> from the tests, and the particle sizes in the thin phase matched exactly. The model then compared two flow rates and showed more particles of the first fraction reaching the clean output at the higher one, before the question turned to wear: the predicted high-wear zones, at the back plate and along the bending edge, are where the prototype wore after roughly half a year of round-the-clock operation.</p>''' + note('Wall interaction was read from the particle number density within 1 mm of the wall, together with velocity. With version 9, the force acting on the wall from the particles is the more direct indicator, and it is now available for DEM too.'),
    ['Evaluation parameter: number of fraction-1 particles in the clean output; <strong>deviation under 10%</strong> from the tests.',
     'Higher flow rate sends more of the coarse fraction into the clean phase.',
     'Simulated wear zones match the prototype: back plate and bending edge, after ~6 months of 24/7 operation.',
     'Use: decide whether to widen the radius or lengthen the unit before building the next prototype.'],
    '11', 'Wear in the prototype housing: &ldquo;the wear pattern corresponds to simulation&rdquo; (Börger).') + '''

            <hr class="section-rule">

            <h2>From the floor</h2>

            <p>Some of the best material was in the questions. Asked how much effort the manual iteration costs, R&amp;D CFD answered that three to five passes were enough and that a steady CHT takes minutes on a GPU. Asked whether a calibration transfers between lubricants, deepfluid was clear: the same base oil with different additives needs a new calibration, and the temperature trend can even flip sign. SKF explained why the first verification is so basic: once a bearing rotates there is simply no good reference model, so they start with the simplest one that exists and add complexity step by step. And HES-SO reminded everyone why the dimensionless form matters: owners do not ask for newtons, they ask what 2% of efficiency lost to a single flood costs them over a year.</p>

            <hr class="section-rule">

            <h2>What we take home</h2>

            <p><strong>Trust comes from a check that does not depend on the model:</strong> an oil balance at zero, a thermocouple, a bubble sensor, a worn prototype. <strong>Cost was stated, not hidden:</strong> three to five iterations, a day per case, minutes for a steady solution, a particle size you can extrapolate away. And <strong>the physics is being split on purpose</strong>: fast flow in particles, slow heat in a steady solid, measured air as calibration data. Meshless CFD in Modena looked less like a promise and more like a tool with a known price.</p>

            <div class="cta-box">
              <h3>Get the Modena proceedings</h3>
              <p>Slides and the key findings of each released presentation, free after a short form.</p>
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
