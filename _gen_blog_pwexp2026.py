#!/usr/bin/env python3
"""Build blog/pw-experience-2026.html (+ .php twin) from the 2025 post's chrome. Edit the BODY below, not the output."""
import re, pathlib
root = pathlib.Path(__file__).parent
src = (root / 'blog' / 'pw-experience-2025.html').read_text(encoding='utf8')

head = src[:src.index('<!-- Hero -->')]
head = re.sub(r'<title>.*?</title>', '<title>PW Experience 2026 — What Modena Taught Us About Heat, Air and Wear | Particleworks Europe</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Particleworks Experience 2026, Modena: how industrial users now close thermal balances, calibrate aeration against optical measurements and predict wear with meshless CFD.">', head, count=1, flags=re.S)
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
                <p>Slides, recordings and key findings of every released talk.</p>''')

BODY = '''
  <!-- Hero -->
  <section class="blog-hero">
    <div class="container">
      <div class="version-badge"><i class="bi bi-calendar-event me-1"></i> PW Experience 2026</div>
      <h1>What Modena Taught Us About Heat, Air and Wear</h1>
      <p class="lead">Modena, October 7, 2026</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 6 min read</span>
        <span><i class="bi bi-tag"></i> Conference Highlights</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p>On October 7, Particleworks users filled the BPER FORUM Monzani in Modena for a day that opened with the release of Particleworks 9.0 and Granuleworks 4.0 and closed, nine hours later, with a group photo. In between, speakers from bearing makers, e-drive engineers, a hydropower research project, a pump manufacturer and several engineering firms kept returning to three questions: where does the heat go, where does the air go, and where does the material wear?</p>

            <p>None of them was a software demo. Each talk put simulation next to a thermocouple, an optical sensor or a worn prototype, and said plainly how well they agreed.</p>

            <hr class="section-rule">

            <h2>Heat: from side effect to deliverable</h2>

            <p>Three talks treated temperature as the result to deliver, not a by-product. At R&amp;D CFD, a team simulating the lubrication of a reciprocating pump separated the two time scales: a few seconds of oil sloshing produce the heat-transfer map, and a steady conjugate-heat-transfer solution on that map converges in minutes on a GPU. The loop is closed by a plain physical check: the oil is not a heat sink, so its thermal balance must come out at zero. Three to five iterations, done by hand, were enough, and the temperatures landed within about 5 °C of the thermocouples, with the remaining mismatch at the open-side bearing pointing to where a local particle refinement should go.</p>

            <p>SKF approached the same physics from the other end. Before trusting a heat transfer coefficient inside their bearing tools, they verified it on the simplest case that exists, oil between a rotating and a fixed cylinder. Particleworks reproduced the vortex pattern with mostly default settings and landed in the same range as a literature correlation and a conventional CFD code. The one warning: mind the velocity limiter. Their wish list for what comes next, a cyclic boundary condition so that a bearing segment can stand in for the whole bearing, is the kind of request that shapes a roadmap.</p>

            <p>Track One then showed the industrial end of the chain: an iterative steady CHT model of a carrier roller, within 7% of the bench test on every thermocouple and on the oil, at about one day per case.</p>

            <hr class="section-rule">

            <h2>Air: measure it before you simulate it</h2>

            <p>The afternoon was about bubbles. deepfluid showed what an optical air-in-oil sensor sees that a single number hides: two oils with the same 0.65% air content can carry bubbles of 132 µm or 68 µm, and the difference changes the oil&ndash;air contact surface, hence oxidation, cavitation behaviour and compressibility. The consequence for simulation is direct. The aeration model has to be calibrated twice, on the total amount of air generated and on the bubble size distribution, and a calibration belongs to one oil and one additive package: change the additives and the temperature trend can even flip sign. Temperature scaling of the coefficients is, honestly, still an open point.</p>

            <p>IAV took the coupled Particleworks&ndash;Granuleworks approach to an electric three-speed commercial-vehicle transmission and followed the air from formation to dissolution, counting bubbles by source with their Particle Explorer tool. A simple oil guide on the lower intermediate shaft cut the splash that creates the air. The settings were close to best practice, with the Courant number raised from 0.2 to 0.3. And in the discussion, the speaker was candid that the measures are on their way to manufacturing but not yet confirmed on a bench. That candour is what made the case persuasive.</p>

            <hr class="section-rule">

            <h2>Wear: simulating what breaks</h2>

            <p>For a Pelton turbine, inspecting the runner means stopping production for two or three days. In the European ReHydro project, HES-SO Valais/Wallis used Particleworks to compute the torque of artificially eroded runners, with flat and rounded splitters and enlarged cut-outs, and found the loss of torque predicted accurately. A simulation that takes five minutes at coarse resolution and 1.5 days at fine resolution can tell an owner what a given erosion costs in efficiency, and whether it is worth another year of running. The next step, letting the runner speed respond to load rejection, needs the inertia of the whole shaft line and is not trivial.</p>

            <p>Börger tested the same idea on a very different machine: a separator that removes sand from biogas manure. The simulation, with Granuleworks, compared separation at two flow rates and three particle sizes, and, more tellingly, predicted where sand hits the housing. The prototype later wore exactly there, at the back plate and along the bending edge, after roughly half a year of round-the-clock operation. The wall-interaction indicator was the particle number density within a millimetre of the wall, combined with velocity; with version 9, the force acting on the walls becomes the more direct choice.</p>

            <hr class="section-rule">

            <h2>Under the hood: Particleworks 9.0</h2>

            <p>The release itself explains why these workflows are getting faster to set up. Multi-level resolution lets particles be refined where it matters without abrupt size jumps; an elastic-body model, a stabilised LSMPS scheme and the promotion of the liquid-film heat transfer model to a full feature widen the physics. On the Granuleworks side, multi-GPU DEM delivered a 3.5&times; speed-up on four A100 cards for a 16-million-particle ribbon mixer. A DEM&ndash;MPS&ndash;CHT thermal coupling and tetrahedral CHT meshes complete the picture. Asked about AI, the Prometech team pointed to the Python API, which already lets an AI agent drive the solver, and asked users how they would like AI tools to look in 9.1.</p>

            <hr class="section-rule">

            <h2>What we take home</h2>

            <p>Two habits ran through every talk. First, a result earns trust by closing a check that does not depend on the model: an oil balance at zero, a thermocouple, a worn prototype. Second, the people who got the most from the method were precise about cost: three to five iterations, a day per case, minutes for a steady solution. Meshless CFD in Modena looked less like a promise and more like a tool with a known price.</p>

            <p>Slides, recordings and short summaries of the talks the speakers released are in the proceedings.</p>

            <div class="cta-box">
              <h3>Get the Modena proceedings</h3>
              <p>Slides, one video per talk and the key findings of each presentation, free after a short form.</p>
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
php = html.replace('proceedings2026.php', 'proceedings2026.php')
# local twin links
php = re.sub(r'href="((?:\.\./)?[A-Za-z0-9_\-/]+)\.html', r'href="\1.php', php)
(root / 'blog' / 'pw-experience-2026.php').write_text(php, encoding='utf8')
words = len(re.sub(r'<[^>]+>', ' ', BODY[BODY.index('<article'):BODY.index('</article>')]).split())
print('words in article:', words)
