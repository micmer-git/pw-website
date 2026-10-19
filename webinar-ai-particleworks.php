<?php
// MachForm embed URL for the form in the top-right card.
// Paste the form's embed URL between the quotes; leave empty to show the e-mail fallback.
$machform_url = '';
$machform_height = 700;
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="favicon.ico">
  <title>Webinar: AI-accelerated Particleworks – 26 November 2026 – Particleworks Europe</title>
  <meta name="description" content="45-minute live webinar, 26 November 2026: gearbox thermal chains, DoE on materials, automatic post-processing and Blender renders, driven by script and AI agents.">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
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

    :root {
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
    .btn-primary:hover { background: var(--pw-blue-dark); border-color: var(--pw-blue-dark); }
  </style>
<!-- === SEO head (auto-generated, matches backup website_now) === -->
  <link rel="canonical" href="https://particleworks-europe.com/webinar-ai-particleworks.php">
  <meta name="author" content="Particleworks Europe">
  <meta name="keywords" content="Particleworks, Particleworks Europe, Granuleworks, technologies, simulation">
  <meta name="google-site-verification" content="13JcLKtEM_c2bcIc8ZMrIKncMjxxmwN5nmfLLs8WLQA">
  <meta property="og:site_name" content="Particleworks Europe">
  <meta property="og:title" content="Webinar: AI-accelerated Particleworks – 26 November 2026 – Particleworks Europe">
  <meta property="og:description" content="45-minute live webinar, 26 November 2026: gearbox thermal chains, DoE on materials, automatic post-processing and Blender renders, driven by script and AI agents.">
  <meta property="og:url" content="https://particleworks-europe.com/webinar-ai-particleworks.php">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Webinar: AI-accelerated Particleworks – 26 November 2026 – Particleworks Europe">
  <meta name="twitter:description" content="45-minute live webinar, 26 November 2026: gearbox thermal chains, DoE on materials, automatic post-processing and Blender renders, driven by script and AI agents.">
  <script type="text/javascript" src="https://embeds.iubenda.com/widgets/6c5fe0b3-dfc8-4f17-b2ec-91c28fe04e7c.js"></script>
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-58D7FHDF');</script>
<!-- === /SEO head === -->
  <style>
body{margin:0}
.ev{--ink:#0a1f33;--blue:#0088cc;--blue-d:#006da3;--green:#25a361;--paper:#f4f8fb;--text:#1b2733;--mute:#566574;--line:#dce6ee;font-family:'Inter',system-ui,sans-serif;color:var(--text);background:#fff;line-height:1.5}
.ev *{box-sizing:border-box}
.ev h1,.ev h2,.ev h3,.ev p{margin:0}
.ev a{text-decoration:none}
.ev .wrap{max-width:1160px;margin:0 auto;padding:0 24px}
.ev-top{position:sticky;top:0;z-index:5;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line)}
.ev-top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;height:60px}
.ev-logo{font-weight:800;font-size:17px;letter-spacing:-.01em;color:var(--ink)}
.ev-logo b{color:var(--blue)}
.ev-top .when{font-size:13px;color:var(--mute);font-weight:500}
.ev-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;min-height:44px;padding:0 22px;border-radius:10px;font-weight:700;font-size:15px;border:2px solid transparent}
.btn-p{background:var(--blue);color:#fff}
.btn-p:hover{background:var(--blue-d)}
.btn-g{background:transparent;color:#fff;border-color:rgba(255,255,255,.4)}
.btn-g:hover{border-color:#fff}
.btn-w{background:#fff;color:var(--ink)}
.hero{background:var(--ink);color:#fff;position:relative;overflow:hidden;padding:72px 0 80px;background-image:radial-gradient(rgba(127,208,255,.22) 1.4px,transparent 1.6px);background-size:28px 28px}
.hero .wrap{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:56px;align-items:center}
.kick{display:inline-flex;gap:10px;align-items:center;font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:#7fd0ff}
.kick i{width:8px;height:8px;border-radius:50%;background:#3ddc84;display:inline-block}
.hero h1{font-size:clamp(36px,5.2vw,64px);line-height:1.04;font-weight:800;letter-spacing:-.025em;margin-top:18px}
.hero h1 em{font-style:normal;color:#7fd0ff}
.hero .lead{font-size:19px;color:#c4d4e2;margin-top:20px;max-width:34em}
.facts{display:flex;flex-wrap:wrap;gap:10px 28px;margin:28px 0 0;padding:0;list-style:none}
.facts li{font-weight:700;font-size:15px}
.facts small{display:block;font-weight:500;font-size:12px;color:#8fa6ba;letter-spacing:.06em;text-transform:uppercase}
.cta{display:flex;flex-wrap:wrap;gap:12px;margin-top:32px}
.shot{margin:0;border-radius:18px;overflow:hidden;background:#000;box-shadow:0 30px 70px rgba(0,0,0,.45);border:1px solid rgba(255,255,255,.12)}
.shot img{display:block;width:100%;height:auto}
.shot figcaption{padding:12px 16px;font-size:13px;color:#c4d4e2;background:#10283f}
.sec{padding:84px 0}
.sec.alt{background:var(--paper)}
.eyebrow{font-size:12.5px;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--green)}
.sec h2{font-size:clamp(28px,3.4vw,42px);line-height:1.1;font-weight:800;letter-spacing:-.02em;margin-top:10px;max-width:20em}
.sec .sub{color:var(--mute);font-size:17px;margin-top:14px;max-width:40em}
.tiles{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:44px}
.tile{background:#fff;border:1px solid var(--line);border-radius:16px;padding:26px;display:flex;flex-direction:column;gap:10px}
.tile .n{font-size:13px;font-weight:800;color:var(--blue);letter-spacing:.06em}
.tile h3{font-size:20px;font-weight:700;letter-spacing:-.01em}
.tile p{color:var(--mute);font-size:15px}
.tile .proof{margin-top:auto;padding-top:14px;border-top:1px dashed var(--line);font-size:13.5px;font-weight:600;color:var(--ink)}
.tile.hot{background:var(--ink);border-color:var(--ink);color:#fff}
.tile.hot .n{color:#7fd0ff}
.tile.hot p{color:#c4d4e2}
.tile.hot .proof{color:#fff;border-color:rgba(255,255,255,.25)}
.agenda{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:56px;align-items:start;margin-top:44px}
.agenda ol{list-style:none;margin:0;padding:0}
.agenda li{display:grid;grid-template-columns:76px 1fr;gap:20px;padding:20px 0;border-top:1px solid var(--line)}
.agenda li:last-child{border-bottom:1px solid var(--line)}
.agenda .t{font-weight:800;font-size:18px;color:var(--blue-d)}
.agenda .t small{display:block;font-size:12px;font-weight:600;color:var(--mute)}
.agenda h3{font-size:18px;font-weight:700}
.agenda p{color:var(--mute);font-size:15px;margin-top:4px}
.agenda .qa h3{color:var(--green)}
.agenda .side{position:sticky;top:84px;display:grid;gap:20px}
.agenda .shot{box-shadow:0 18px 44px rgba(10,31,51,.18);border-color:var(--line)}
.agenda .shot figcaption{background:#fff;color:var(--mute)}
.stats{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:20px;margin-top:44px}
.stat{border-top:4px solid var(--blue);padding-top:18px}
.stat b{display:block;font-size:clamp(44px,5vw,68px);line-height:1;font-weight:800;letter-spacing:-.03em;color:var(--ink)}
.stat h3{font-size:17px;font-weight:700;margin-top:12px}
.stat p{color:var(--mute);font-size:15px;margin-top:6px}
.note{font-size:13px;color:var(--mute);margin-top:28px}
.reg{background:var(--ink);color:#fff;padding:84px 0;background-image:radial-gradient(rgba(127,208,255,.18) 1.4px,transparent 1.6px);background-size:28px 28px}
.reg .wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:56px;align-items:center}
.reg h2{font-size:clamp(30px,4vw,48px);line-height:1.08;font-weight:800;letter-spacing:-.02em}
.reg p{color:#c4d4e2;font-size:17px;margin-top:14px}
.ev-card{background:#fff;color:var(--text);border-radius:18px;padding:28px;box-shadow:0 30px 70px rgba(0,0,0,.4)}
.ev-card h3{font-size:20px;font-weight:700}
.ev-card .slot{margin-top:16px;border:2px dashed var(--line);border-radius:12px;padding:28px;text-align:center;color:var(--mute);font-size:14px}
.ev-card .mini{font-size:13px;color:var(--mute);margin-top:14px}
.ev-card .mini a{color:var(--blue-d);font-weight:600}
.next{padding:36px 0;background:var(--paper)}
.next .wrap{display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between}
.next p{font-size:17px;font-weight:600}
.next p span{color:var(--mute);font-weight:500}
.next .ev-btn{border-color:var(--ink);color:var(--ink)}
.foot{padding:26px 0;font-size:13px;color:var(--mute)}
@media (max-width:900px){
.hero .wrap,.agenda,.reg .wrap{grid-template-columns:minmax(0,1fr);gap:36px}
.tiles,.stats{grid-template-columns:minmax(0,1fr)}
.agenda .side{position:static}
.ev-top .when{display:none}
.sec,.reg{padding:56px 0}
.hero{padding:48px 0 56px}
}
  </style>
</head>
<body>
  <!-- Google Tag Manager (noscript) -->
  <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-58D7FHDF" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
  <!-- End Google Tag Manager (noscript) -->

  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="index.html"><img src="images/PW_Europe_logo_small.png" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-lg-center gap-1">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Products</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="particleworks.html"><i class="bi bi-droplet"></i><span><div class="dd-t">Particleworks</div><div class="dd-s">Meshfree CFD fluid solver</div></span></a></li>
              <li><a class="dropdown-item" href="granuleworks.html"><i class="bi bi-circle-fill"></i><span><div class="dd-t">Granuleworks</div><div class="dd-s">DEM granular simulation</div></span></a></li>
              <li><a class="dropdown-item" href="particleworksforansys.html"><i class="bi bi-plug"></i><span><div class="dd-t">Particleworks for Ansys</div><div class="dd-s">Native Workbench integration</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Applications</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="e-motors.html"><i class="bi bi-lightning-charge"></i><span><div class="dd-t">E-Motors</div><div class="dd-s">Oil-cooled electric drives</div></span></a></li>
              <li><a class="dropdown-item" href="engines-and-pistons.html"><i class="bi bi-fuel-pump"></i><span><div class="dd-t">Engines &amp; Pistons</div><div class="dd-s">Combustion thermal</div></span></a></li>
              <li><a class="dropdown-item" href="gearboxes-and-bearings.html"><i class="bi bi-gear-wide-connected"></i><span><div class="dd-t">Gearboxes &amp; Bearings</div><div class="dd-s">Oil jet lubrication</div></span></a></li>
              <li><a class="dropdown-item" href="clutches-and-brakes.html"><i class="bi bi-disc"></i><span><div class="dd-t">Clutches &amp; Brakes</div><div class="dd-s">Disc cooling flows</div></span></a></li>
              <li><a class="dropdown-item" href="cutting-tools.html"><i class="bi bi-scissors"></i><span><div class="dd-t">Cutting Tools</div><div class="dd-s">Machining coolant</div></span></a></li>
              <li><a class="dropdown-item" href="mixing-and-separation.html"><i class="bi bi-hurricane"></i><span><div class="dd-t">Mixing &amp; Separation</div><div class="dd-s">Industrial processes</div></span></a></li>
              <li><a class="dropdown-item" href="sterilization-food-and-consumer-goods.html"><i class="bi bi-droplet-half"></i><span><div class="dd-t">Sterilization &amp; Consumer Goods</div><div class="dd-s">Food and cleaning</div></span></a></li>
              <li><a class="dropdown-item" href="vehicle-management.html"><i class="bi bi-truck"></i><span><div class="dd-t">Vehicle Management</div><div class="dd-s">Onboard fluid systems</div></span></a></li>
              <li><a class="dropdown-item" href="civil-engineering-and-fire-prevention.html"><i class="bi bi-fire"></i><span><div class="dd-t">Civil Engineering &amp; Fire</div><div class="dd-s">Safety and infrastructure</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="case-studies.html">Case Studies</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Resources</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="resources.html"><i class="bi bi-file-earmark-pdf"></i><span><div class="dd-t">Resources &amp; Whitepapers</div><div class="dd-s">Technical documents</div></span></a></li>
              <li><a class="dropdown-item" href="SPH-MPS.html"><i class="bi bi-braces"></i><span><div class="dd-t">FVM vs SPH vs MPS</div><div class="dd-s">Method comparison</div></span></a></li>
              <li><a class="dropdown-item" href="glossary.html"><i class="bi bi-book"></i><span><div class="dd-t">Glossary</div><div class="dd-s">Meshfree CFD terminology</div></span></a></li>
              <li><a class="dropdown-item active" href="training.html"><i class="bi bi-mortarboard"></i><span><div class="dd-t">Training</div><div class="dd-s">Courses &amp; workshops</div></span></a></li>
              <li><a class="dropdown-item" href="support.html"><i class="bi bi-life-preserver"></i><span><div class="dd-t">Support</div><div class="dd-s">Technical help</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Company</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="company.html"><i class="bi bi-building"></i><span><div class="dd-t">About Particleworks Europe</div><div class="dd-s">Who we are</div></span></a></li>
              <li><a class="dropdown-item" href="resellers.html"><i class="bi bi-globe-europe-africa"></i><span><div class="dd-t">Resellers</div><div class="dd-s">Global partner network</div></span></a></li>
              <li><a class="dropdown-item" href="careers.html"><i class="bi bi-person-plus"></i><span><div class="dd-t">Careers</div><div class="dd-s">Join the team</div></span></a></li>
              <li><a class="dropdown-item" href="consulting.html"><i class="bi bi-briefcase"></i><span><div class="dd-t">Consulting &amp; Services</div><div class="dd-s">Engineering support</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="contact.html">Contact</a></li>
          <li class="nav-item ms-lg-1"><a class="nav-link" href="https://www.linkedin.com/company/particleworks-europe/" target="_blank" rel="noopener" aria-label="LinkedIn" style="color:var(--pw-blue);font-size:1.15rem;"><i class="bi bi-linkedin"></i></a></li>
        </ul>
      </div>
    </div>
  </nav>

  <main>
<div class="ev">

<section class="hero"><div class="wrap">
  <div>
    <span class="kick"><i></i>Live webinar · 45 minutes</span>
    <h1>Let an AI agent <em>run</em> your Particleworks studies</h1>
    <p class="lead">From the Experience 2026 workshop: gearbox thermal chains, DoE on materials, automatic post-processing and Blender renders, all driven from a script. Plus the SDK route to extend the solver itself.</p>
    <ul class="facts">
      <li><small>Date</small>Thu 26 November 2026</li>
      <li><small>Time</small>15:00 – 15:45 CET</li>
      <li><small>Where</small>Online · free</li>
    </ul>
    <div class="cta">
      <a class="ev-btn btn-p" href="#register">Save my seat</a>
      <a class="ev-btn btn-g" href="#agenda">See the agenda</a>
    </div>
  </div>
  <div class="ev-card" id="register">
    <h3>Save your seat</h3>
    <p class="mini">Thu 26 Nov 2026 · 15:00–15:45 CET · online · free</p>
    <?php if ($machform_url !== ''): ?>
<div id="mf_placeholder" data-formurl="<?= htmlspecialchars($machform_url) ?>" data-formheight="<?= (int)$machform_height ?>" data-formtitle="Register for the webinar" data-paddingbottom="10"></div>
<script>
  (function(f,o,r,m){
    r=f.createElement('script');r.async=1;r.src=o+'js/mf.js';
    m=f.getElementById('mf_placeholder'); m.parentNode.insertBefore(r, m);
  })(document,'https://assets.forms-eu.com/');
</script>
<?php else: ?>
<div class="slot">Registration form<br>loads here</div><a class="ev-btn btn-p" style="width:100%;margin-top:14px" href="mailto:info@particleworks-europe.com?subject=Webinar%20registration%20%E2%80%93%20AI-accelerated%20Particleworks%20(26%20Nov%202026)&amp;body=Name%3A%0ACompany%3A%0AJob%20title%3A%0ACountry%3A%0A">Or write to us by e-mail</a>
<?php endif; ?>
    <p class="mini">Recording sent to every registrant.</p>
  </div>
</div></section>

<section class="sec" id="can"><div class="wrap">
  <span class="eyebrow">What you will see</span>
  <h2>Six things Particleworks can do when it is scripted</h2>
  <p class="sub">All shown on real runs from the workshop, none needs custom training data.</p>
  <div class="tiles">
    <article class="tile"><span class="n">01</span><h3>Gearbox, end to end</h3><p>Churning run, heat-transfer map and steady thermal model chained in one command. Every step is gated before it spends GPU time.</p><div class="proof">9.2 h of GPU condensed into a 20 s thermal solve</div></article>
    <article class="tile"><span class="n">02</span><h3>DoE on materials</h3><p>16 fluids across the rheology map, Newtonian to Bingham, shear-thinning and shear-thickening, against 9 obstacle shapes.</p><div class="proof">144 cases from one study definition</div></article>
    <article class="tile"><span class="n">03</span><h3>Post-processing on autopilot</h3><p>Wetting maps, peak forces, torque, HTC and the report, produced the same way for every run.</p><div class="proof">A plausibility gate rejects bad fields before you see them</div></article>
    <article class="tile"><span class="n">04</span><h3>Blender in the loop</h3><p>Particles to surface to cinematic frames. Colour and translucency can follow each particle's own history.</p><div class="proof">Beauty renders without leaving the pipeline</div></article>
    <article class="tile"><span class="n">05</span><h3>Complex workflows</h3><p>The omelette: pour, swirl, cooking history integrated per particle, then compared against the no-swirl case.</p><div class="proof">Swirl cuts thickness variation 0.31 → 0.22</div></article>
    <article class="tile hot"><span class="n">06</span><h3>Beyond the GUI</h3><p>Scripted motions, custom viscosity laws, and the SDK to hook into the solver and add physics that did not exist.</p><div class="proof">Viscosity as a function of temperature, per particle</div></article>
  </div>
</div></section>

<section class="sec alt" id="agenda"><div class="wrap">
  <span class="eyebrow">Agenda · 45 min</span>
  <h2>Five blocks, one live Q&amp;A</h2>
  <div class="agenda">
    <ol>
      <li><div class="t">15:00<small>7 min</small></div><div><h3>From script to agent</h3><p>Four levels of control: your own Python, AI chat with the API in context, agents that run the machine, and the SDK.</p></div></li>
      <li><div class="t">15:07<small>10 min</small></div><div><h3>Gearbox, end to end</h3><p>Churning loss, HTC map, steady CHT. What was automated, what was machine-checked, what the temperatures really mean.</p></div></li>
      <li><div class="t">15:17<small>9 min</small></div><div><h3>DoE on materials, plus post-processing</h3><p>16 fluids × 9 shapes, wetting and force maps, and the Blender renders generated from the same script.</p></div></li>
      <li><div class="t">15:26<small>9 min</small></div><div><h3>Complex workflows</h3><p>The omelette: temperature-driven viscosity, per-particle history, and what it takes to prepare such a case.</p></div></li>
      <li><div class="t">15:35<small>5 min</small></div><div><h3>Engineering insights</h3><p>The checks that separate a plausible result from a correct one.</p></div></li>
      <li class="qa"><div class="t">15:40<small>5 min</small></div><div><h3>Live Q&amp;A</h3><p>Bring your own case.</p></div></li>
    </ol>
    <div class="side">
      <figure class="shot">
        <img src="images/events/ai-omelette-pour.gif" loading="lazy" alt="Simulated egg pour into a pan, rendered from Particleworks particles" width="520" height="293">
        <figcaption>An omelette, simulated and rendered end to end from a script. Viscosity follows temperature.</figcaption>
      </figure>
      <figure class="shot">
        <img src="images/events/fsi-flexible-array.gif" loading="lazy" alt="Array of four flexible sheets deforming under falling liquid" width="560" height="394">
        <figcaption>A study array launched, monitored and compared from one script.</figcaption>
      </figure>
    </div>
  </div>
</div></section>

<section class="sec" id="insights"><div class="wrap">
  <span class="eyebrow">Engineering insights</span>
  <h2>Three numbers from the gearbox report</h2>
  <div class="stats">
    <div class="stat"><b>2.1×</b><h3>ISO over-predicts the churning loss</h3><p>118 W by ISO/TR 14179-2 against 55 W simulated. ISO has no term for gears fed by thrown oil, which is most of this box.</p></div>
    <div class="stat"><b>3–6×</b><h3>Gears cool harder than the housing</h3><p>Mean HTC 214 W/m²K on a gear against 36 on the housing. Relative velocity drives it, not how wet the surface is.</p></div>
    <div class="stat"><b>0</b><h3>HTC in an adiabatic run</h3><p>Zero non-zero values over 670,920 triangles. The thermal map needed a real re-run, not a post-process.</p></div>
  </div>
  <p class="note">Demonstration gearbox, Particleworks 8.2, 375 k particles, 2 s run. No customer data.</p>
</div></section>

<section class="reg"><div class="wrap">
  <div>
    <span class="kick"><i></i>Free · live online</span>
    <h2>Thu 26 November, 15:00 CET. Bring a case.</h2>
    <p>45 minutes, presented by Michele Merelli, Particleworks Europe / EnginSoft. To attend you only need a browser. To reproduce the workflow on your own machine afterwards, a local install of an AI tool (Claude Code Desktop, Codex) is required. Prefer e-mail? <a href="mailto:info@particleworks-europe.com" style="color:#7fd0ff;font-weight:600">info@particleworks-europe.com</a></p>
  </div>
  <div class="cta" style="margin:0;justify-content:flex-end"><a class="ev-btn btn-p" href="#register">Save my seat</a></div>
</div></section>

<section class="next"><div class="wrap">
  <p>Want this on your own cases? <span>One-day custom training: method in the morning, your scripts in the afternoon.</span></p>
  <a class="ev-btn" href="training-ai-acceleration.php">See the custom training</a>
</div></section>

</div>
</main>

  <footer class="py-5 mt-5" style="background:#1a1a1a;color:#adb5bd;">
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4">
          <img src="images/PWEurope_negativ-logo.png" alt="Particleworks Europe" style="height:34px;">
          <p class="small mt-3" style="max-width:320px;">European competence center for meshfree CFD simulation with Particleworks and Granuleworks technologies.</p>
          <div class="d-flex gap-2 mt-3"><a href="https://www.linkedin.com/company/particleworks-europe/" class="text-white" target="_blank" style="font-size:1.2rem;"><i class="bi bi-linkedin"></i></a></div>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Products</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="particleworks.html" class="text-reset">Particleworks</a></li><li class="mb-2"><a href="granuleworks.html" class="text-reset">Granuleworks</a></li></ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Services</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="consulting.html" class="text-reset">Consulting</a></li><li class="mb-2"><a href="training.html" class="text-reset">Training</a></li><li class="mb-2"><a href="support.html" class="text-reset">Support</a></li></ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Resources</h6>
          <ul class="list-unstyled small"><li class="mb-2"><a href="case-studies.html" class="text-reset">Case Studies</a></li><li class="mb-2"><a href="resources.html" class="text-reset">Resources</a></li><li class="mb-2"><a href="glossary.html" class="text-reset">Glossary</a></li></ul>
        </div>
        <div class="col-lg-2">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Contact</h6>
          <ul class="list-unstyled small"><li class="mb-2"><i class="bi bi-telephone me-1"></i> +39 0461 915391</li><li class="mb-2"><a href="mailto:info@particleworks-europe.com" class="text-reset"><i class="bi bi-envelope me-1"></i> info@particleworks-europe.com</a></li></ul>
        </div>
      </div>
      <hr class="my-4" style="border-color:#2a2a2a;">
      <div class="d-flex flex-wrap justify-content-between align-items-center">
        <p class="small mb-0">&copy; 2026 Particleworks Europe. All rights reserved.</p>
        <p class="small mb-0"><a href="privacy.html" class="text-reset me-3">Privacy</a>Meshfree CFD simulation technology</p>
      </div>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>window.addEventListener('scroll', function() { document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30); });</script>
</body>
</html>
