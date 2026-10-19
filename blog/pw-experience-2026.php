<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="../favicon.ico">
  <title>PW Experience 2026 — What Modena Taught Us About Heat, Air and Wear | Particleworks Europe</title>
  <meta name="description" content="Particleworks Experience 2026, Modena: seven talks on closing thermal balances, calibrating aeration against optical measurements and predicting wear with meshless CFD, with the key slide of each.">
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
      --pw-green-dark: #1e8a51;
      --pw-dark: #333333;
      --pw-gray: #6c757d;
      --pw-light: #f8f9fa;
      --pw-gradient: linear-gradient(135deg, #0088cc 0%, #25a361 100%);
      --pw-gradient-dark: linear-gradient(135deg, #004466 0%, #0088cc 50%, #1a7a4a 100%);
    }
    * { font-family: 'Inter', sans-serif; }
    html { scroll-behavior: smooth; }
    body { color: var(--pw-dark); overflow-x: hidden; }

    /* Navbar */
    .navbar {
      background: rgba(255,255,255,0.97);
      backdrop-filter: blur(12px);
      box-shadow: 0 1px 0 rgba(0,0,0,0.06);
      padding: 0.6rem 0;
      transition: box-shadow 0.3s;
    }
    .navbar.scrolled { box-shadow: 0 2px 20px rgba(0,0,0,0.08); }
    .navbar-brand img { height: 38px; }
    .navbar .nav-link {
      font-size: 0.88rem;
      font-weight: 500;
      color: var(--pw-dark);
      padding: 0.5rem 0.75rem !important;
      transition: color 0.2s;
    }
    .navbar .nav-link:hover { color: var(--pw-blue); }

    /* Hero */
    .blog-hero {
      position: relative;
      padding: 9rem 0 4rem;
      background: var(--pw-gradient-dark);
      overflow: hidden;
    }
    .blog-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 80% 60% at 20% 80%, rgba(37,163,97,0.15) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 20%, rgba(0,136,204,0.2) 0%, transparent 60%);
    }
    .blog-hero .container { position: relative; z-index: 2; }
    .blog-hero h1 {
      font-size: clamp(2rem, 4.5vw, 3rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.5px;
      line-height: 1.15;
      max-width: 720px;
    }
    .blog-hero .lead {
      font-size: 1.15rem;
      color: rgba(255,255,255,0.8);
      max-width: 620px;
      line-height: 1.7;
      margin-top: 1.25rem;
    }
    .version-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(0,136,204,0.25);
      color: #fff;
      border: 1px solid rgba(0,136,204,0.5);
      padding: 0.3rem 0.9rem;
      border-radius: 50px;
      font-size: 0.78rem;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      margin-bottom: 1.2rem;
    }
    .hero-meta {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      margin-top: 1.75rem;
      color: rgba(255,255,255,0.6);
      font-size: 0.88rem;
    }
    .hero-meta span { display: inline-flex; align-items: center; gap: 0.35rem; }

    /* Article body */
    .blog-body {
      padding: 4rem 0 3rem;
    }
    .article-content {
      max-width: 740px;
    }
    .article-content h2 {
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--pw-dark);
      margin-top: 3rem;
      margin-bottom: 1rem;
      letter-spacing: -0.3px;
      line-height: 1.3;
    }
    .article-content h2:first-of-type {
      margin-top: 0;
    }
    .article-content p {
      font-size: 1.05rem;
      line-height: 1.85;
      color: #444;
      margin-bottom: 1.25rem;
    }
    .article-content ul {
      margin-bottom: 1.5rem;
      padding-left: 0;
      list-style: none;
    }
    .article-content ul li {
      position: relative;
      padding-left: 1.5rem;
      margin-bottom: 0.75rem;
      font-size: 1.02rem;
      line-height: 1.75;
      color: #444;
    }
    .article-content ul li::before {
      content: '';
      position: absolute;
      left: 0;
      top: 0.65rem;
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: var(--pw-blue);
    }
    .article-content strong {
      color: var(--pw-dark);
      font-weight: 600;
    }

    /* Sub-headers within sections */
    .article-content h3 {
      font-size: 1.1rem;
      font-weight: 700;
      color: var(--pw-blue);
      text-transform: uppercase;
      letter-spacing: 0.5px;
      margin-top: 2rem;
      margin-bottom: 0.75rem;
    }

    /* Section divider */
    .section-rule {
      border: none;
      height: 1px;
      background: linear-gradient(90deg, transparent, rgba(0,136,204,0.2), transparent);
      margin: 3rem 0;
    }

    /* CTA box */
    .cta-box {
      background: linear-gradient(135deg, #f0f9ff 0%, #f0fdf4 100%);
      border: 1px solid rgba(0,136,204,0.15);
      border-radius: 16px;
      padding: 2.5rem;
      margin-top: 3rem;
    }
    .cta-box h3 {
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--pw-dark);
      text-transform: none;
      letter-spacing: -0.2px;
      margin-top: 0;
      margin-bottom: 0.5rem;
    }
    .cta-box p {
      color: var(--pw-gray);
      font-size: 0.98rem;
      margin-bottom: 1.5rem;
    }

    /* Buttons */
    .btn-pw {
      background: var(--pw-blue);
      color: #fff;
      border: none;
      padding: 0.75rem 2rem;
      border-radius: 50px;
      font-weight: 600;
      font-size: 0.95rem;
      transition: all 0.3s;
      display: inline-block;
      text-decoration: none;
    }
    .btn-pw:hover { background: var(--pw-blue-dark); color: #fff; transform: translateY(-2px); box-shadow: 0 8px 25px rgba(0,136,204,0.3); }
    .btn-pw-outline {
      background: transparent;
      color: var(--pw-blue);
      border: 2px solid var(--pw-blue);
      padding: 0.65rem 1.8rem;
      border-radius: 50px;
      font-weight: 600;
      font-size: 0.9rem;
      transition: all 0.3s;
      display: inline-block;
      text-decoration: none;
    }
    .btn-pw-outline:hover { background: var(--pw-blue); color: #fff; transform: translateY(-2px); }

    /* Related links */
    .related-section {
      padding: 3rem 0 4rem;
      border-top: 1px solid rgba(0,0,0,0.06);
    }
    .related-card {
      display: block;
      background: #fff;
      border: 1px solid rgba(0,0,0,0.06);
      border-radius: 12px;
      padding: 1.5rem;
      text-decoration: none;
      transition: all 0.25s;
      height: 100%;
    }
    .related-card:hover {
      border-color: var(--pw-blue);
      box-shadow: 0 6px 20px rgba(0,136,204,0.1);
      transform: translateY(-2px);
    }
    .related-card h5 {
      font-size: 1rem;
      font-weight: 600;
      color: var(--pw-dark);
      margin-bottom: 0.4rem;
    }
    .related-card p {
      font-size: 0.88rem;
      color: var(--pw-gray);
      margin-bottom: 0;
      line-height: 1.5;
    }
    .related-card .card-arrow {
      color: var(--pw-blue);
      font-size: 1.1rem;
      margin-top: 0.75rem;
      display: block;
    }

    /* Footer */
    footer {
      background: #1a1a2e;
      color: rgba(255,255,255,0.7);
      padding: 3.5rem 0 1.5rem;
    }
    footer a { color: rgba(255,255,255,0.7); text-decoration: none; transition: color 0.2s; }
    footer a:hover { color: #fff; }
    footer .footer-brand img { height: 34px; margin-bottom: 1rem; }
    footer .footer-divider { border-top: 1px solid rgba(255,255,255,0.08); margin: 2rem 0 1.5rem; }
    footer .social-link {
      width: 40px;
      height: 40px;
      border-radius: 10px;
      background: rgba(255,255,255,0.06);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      transition: all 0.3s;
    }
    footer .social-link:hover { background: var(--pw-blue); color: #fff; }
  
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
  </style>

<!-- === SEO head (auto-generated, matches backup website_now) === -->
  <link rel="canonical" href="https://particleworks-europe.com/blog/pw-experience-2025.html">
  <meta name="author" content="Particleworks Europe">
  <meta name="keywords" content="Particleworks, Particleworks Europe, Granuleworks, technologies, simulation">
  <meta name="google-site-verification" content="13JcLKtEM_c2bcIc8ZMrIKncMjxxmwN5nmfLLs8WLQA">
  <meta property="og:site_name" content="Particleworks Europe">
  <meta property="og:title" content="PW Experience 2025 — From Validation to Virtual Prototyping">
  <meta property="og:description" content="PW Experience 2025 in Munich featured twelve presentations with hard correlation data from SADEN, TotalEnergies, SKF, ZF, DSD and more — proving meshless CFD has reached production-grade accuracy.">
  <meta property="og:url" content="https://particleworks-europe.com/blog/pw-experience-2025.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="PW Experience 2025 — From Validation to Virtual Prototyping">
  <meta name="twitter:description" content="PW Experience 2025 in Munich featured twelve presentations with hard correlation data from SADEN, TotalEnergies, SKF, ZF, DSD and more — proving meshless CFD has reached production-grade accuracy.">
  <!-- Iubenda -->
  <script type="text/javascript" src="https://embeds.iubenda.com/widgets/6c5fe0b3-dfc8-4f17-b2ec-91c28fe04e7c.js"></script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-58D7FHDF');</script>
  <!-- End Google Tag Manager -->
<!-- === /SEO head === -->
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-58D7FHDF"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->


  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="../index.php"><img src="../images/PW_Europe_logo_small.png" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="navbarNav">
        <ul class="navbar-nav align-items-lg-center gap-1">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Products</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="../particleworks.php"><i class="bi bi-droplet"></i><span><div class="dd-t">Particleworks</div><div class="dd-s">Meshfree CFD fluid solver</div></span></a></li>
              <li><a class="dropdown-item" href="../granuleworks.php"><i class="bi bi-circle-fill"></i><span><div class="dd-t">Granuleworks</div><div class="dd-s">DEM granular simulation</div></span></a></li>
              <li><a class="dropdown-item" href="../particleworksforansys.php"><i class="bi bi-plug"></i><span><div class="dd-t">Particleworks for Ansys</div><div class="dd-s">Native Workbench integration</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Applications</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="../e-motors.php"><i class="bi bi-lightning-charge"></i><span><div class="dd-t">E-Motors</div><div class="dd-s">Oil-cooled electric drives</div></span></a></li>
              <li><a class="dropdown-item" href="../engines-and-pistons.php"><i class="bi bi-fuel-pump"></i><span><div class="dd-t">Engines &amp; Pistons</div><div class="dd-s">Combustion thermal</div></span></a></li>
              <li><a class="dropdown-item" href="../gearboxes-and-bearings.php"><i class="bi bi-gear-wide-connected"></i><span><div class="dd-t">Gearboxes &amp; Bearings</div><div class="dd-s">Oil jet lubrication</div></span></a></li>
              <li><a class="dropdown-item" href="../clutches-and-brakes.php"><i class="bi bi-disc"></i><span><div class="dd-t">Clutches &amp; Brakes</div><div class="dd-s">Disc cooling flows</div></span></a></li>
              <li><a class="dropdown-item" href="../cutting-tools.php"><i class="bi bi-scissors"></i><span><div class="dd-t">Cutting Tools</div><div class="dd-s">Machining coolant</div></span></a></li>
              <li><a class="dropdown-item" href="../mixing-and-separation.php"><i class="bi bi-hurricane"></i><span><div class="dd-t">Mixing &amp; Separation</div><div class="dd-s">Industrial processes</div></span></a></li>
              <li><a class="dropdown-item" href="../sterilization-food-and-consumer-goods.php"><i class="bi bi-droplet-half"></i><span><div class="dd-t">Sterilization &amp; Consumer Goods</div><div class="dd-s">Food and cleaning</div></span></a></li>
              <li><a class="dropdown-item" href="../vehicle-management.php"><i class="bi bi-truck"></i><span><div class="dd-t">Vehicle Management</div><div class="dd-s">Onboard fluid systems</div></span></a></li>
              <li><a class="dropdown-item" href="../civil-engineering-and-fire-prevention.php"><i class="bi bi-fire"></i><span><div class="dd-t">Civil Engineering &amp; Fire</div><div class="dd-s">Safety and infrastructure</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="../case-studies.php">Case Studies</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Resources</a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="../resources.php"><i class="bi bi-file-earmark-pdf"></i><span><div class="dd-t">Resources &amp; Whitepapers</div><div class="dd-s">Technical documents</div></span></a></li>
              <li><a class="dropdown-item" href="../SPH-MPS.php"><i class="bi bi-braces"></i><span><div class="dd-t">FVM vs SPH vs MPS</div><div class="dd-s">Method comparison</div></span></a></li>
              <li><a class="dropdown-item" href="../glossary.php"><i class="bi bi-book"></i><span><div class="dd-t">Glossary</div><div class="dd-s">Meshfree CFD terminology</div></span></a></li>
              <li><a class="dropdown-item" href="../training.php"><i class="bi bi-mortarboard"></i><span><div class="dd-t">Training</div><div class="dd-s">Courses &amp; workshops</div></span></a></li>
              <li><a class="dropdown-item" href="../support.php"><i class="bi bi-life-preserver"></i><span><div class="dd-t">Support</div><div class="dd-s">Technical help</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Company</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="../company.php"><i class="bi bi-building"></i><span><div class="dd-t">About Particleworks Europe</div><div class="dd-s">Who we are</div></span></a></li>
              <li><a class="dropdown-item" href="../resellers.php"><i class="bi bi-globe-europe-africa"></i><span><div class="dd-t">Resellers</div><div class="dd-s">Global partner network</div></span></a></li>
              <li><a class="dropdown-item" href="../careers.php"><i class="bi bi-person-plus"></i><span><div class="dd-t">Careers</div><div class="dd-s">Join the team</div></span></a></li>
              <li><a class="dropdown-item" href="../consulting.php"><i class="bi bi-briefcase"></i><span><div class="dd-t">Consulting &amp; Services</div><div class="dd-s">Engineering support</div></span></a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="../contact.php">Contact</a></li>
          <li class="nav-item ms-lg-1"><a class="nav-link" href="https://www.linkedin.com/company/particleworks-europe/" target="_blank" rel="noopener" aria-label="LinkedIn" style="color:var(--pw-blue);font-size:1.15rem;"><i class="bi bi-linkedin"></i></a></li>
        </ul>
      </div>
    </div>
  </nav>

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

            <div class="talk-intro"><img src="../experience/speakers/iori-saigo.jpg" alt="Iori Saigo"><div><div class="t-time">09:00–10:00</div><h3>Particleworks 9.0 &amp; Granuleworks 4.0</h3><div class="t-who">Issei Masaie &amp; Iori Saigo — Prometech Software (JP)</div></div></div>
            <p>The morning keynote did not walk through a feature list; it showed what the new capabilities do on real geometries. The most concrete number came from a ribbon mixer with 16 million particles solved with a double-precision DEM solver: one, two and four A100 GPUs gave speed-ups of 1.00, 1.96 and 3.49, which is about 87% parallel efficiency at four cards. That is what turns a day-long powder run into an overnight one.</p>

            <p>The same logic applied to structures. DEM can now output the force distribution on walls, until now an MPS-only quantity, and the example was shot peening, where the contour of the summed force shows directly where a component takes the load. For heat, a two-way DEM&ndash;MPS&ndash;CHT coupling solves fluid, powder and wall temperatures together, with a temperature for each powder particle; the case shown was a plastic-pellet cooling silo, where powder volume and uneven distribution locally change the heat transfer.</p>
            <div class="keypoints"><h5>Key points</h5><ul><li>Multi-GPU DEM: <strong>3.49&times; on 4 A100</strong> for 16 M particles in double precision.</li><li>DEM wall-force output makes wear and load visible on structures (shot-peening example).</li><li>DEM&ndash;MPS&ndash;CHT: per-particle powder temperature coupled both ways with fluid and wall.</li><li>Elastic-body model: a valve with fixed edges under flow and screen printing coupled with MPS; the liquid-film HTC model now flags regions of higher heat transfer than the conventional model.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-01.jpg" alt="Particleworks 9.0 &amp; Granuleworks 4.0 — key slide" loading="lazy"><figcaption>Multi-GPU support for DEM: speed-up of the ribbon-mixer case on 1, 2 and 4 A100 GPUs (Prometech).</figcaption></figure>

            <hr class="section-rule">

            <h2>Heat: from side effect to deliverable</h2>

            <p>Three talks treated temperature as the result to deliver. They share one trick: <strong>never run the oil and the solid together in time.</strong> Oil reaches its flow pattern in seconds; metal needs hours. So the oil is simulated briefly, its heat-transfer coefficient (HTC) and near-wall temperature are handed to a steady conjugate-heat-transfer (CHT) solution, and the two are iterated until nothing moves.</p>

            <div class="talk-intro"><img src="../experience/speakers/leonardo-lanciotti.jpg" alt="Leonardo Lanciotti"><div><div class="t-time">11:45–12:15</div><h3>CHT Analysis of a Reciprocating Pump</h3><div class="t-who">Leonardo Lanciotti — R&amp;D CFD S.R.L. – Comet S.p.A. (IT)</div></div></div>
            <p>The case was a volumetric water pump lubricated by oil sloshing in the crankcase, with heat leaving by natural convection: 3.7 kW at the shaft and 85&ndash;90% mechanical efficiency, so roughly 0.4&ndash;0.55 kW to dissipate, with the oil at 63 °C and ambient at 22 °C. A fully coupled unsteady model would need double precision and a thermal transient far too long to run, so the team used a few seconds of sloshing to get the HTC map and then a steady CHT that converges in minutes.</p>

            <p>The delicate input is where the heat is born. Loads on the kinematic pairs were not available, so instead of trial and error the team ran a dynamic analysis of the pump, took friction coefficients from the literature and split the power between contacts; each source is applied as a local volumetric heat source in a thin slice of CAD next to the contact. The results show where the model is right and where it is not: the shaft sits at 70&ndash;80 °C as in the test, a hot spot appears at the piston&ndash;seal contact, which is exactly where seals degrade in service, while the small bearing comes out hotter than the large one, contrary to experiment, a sign that sloshing needs a particle refinement there.</p>
            <div class="eng-note"><b>Engineering note.</b> Convergence is not judged on temperatures alone. The oil is not a heat sink, so the heat it takes from the shaft must equal the heat it gives to the housing: <code>Q&#775;<sub>shaft&rarr;oil</sub> = &Sigma; HTC<sub>i</sub>(T<sub>i</sub>&minus;T<sub>oil</sub>)A<sub>i</sub> = &Sigma; HTC<sub>j</sub>(T<sub>oil</sub>&minus;T<sub>j</sub>)A<sub>j</sub></code>, evaluated on a uniform surface mesh from the Particleworks HTC map. If it is not zero, scale the thermal power, the oil temperature or the external HTC and iterate.</div>
            <div class="keypoints"><h5>Key points</h5><ul><li>Sloshing is decoupled from CHT: seconds of oil flow, minutes of steady CHT.</li><li>Six of seven thermocouples within 3.1 °C of the test; the worst, the open-side bearing, is off by 5.4 °C.</li><li>The seal hot spot is predicted where seals fail in practice.</li><li><strong>3&ndash;5 manual iterations, about 1.5 hours per case</strong> once the model exists; the setup can take longer than the run.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-04.jpg" alt="CHT Analysis of a Reciprocating Pump — key slide" loading="lazy"><figcaption>Simulation versus experimental thermocouples on the pump, with the difference in °C for each position (R&amp;D CFD).</figcaption></figure>
            <div class="talk-intro"><img src="../experience/speakers/lijun-cao.jpg" alt="Lijun Cao"><div><div class="t-time">12:45–13:15</div><h3>Integrating Particleworks into SKF Engineering Tools: Part I</h3><div class="t-who">Lijun Cao &amp; Fabrizio Mandrile — SKF (NL)</div></div></div>
            <p>SKF framed the problem as a ladder: lumped thermal networks, finite-element thermal models, then FE with CFD-derived HTCs one way, then fully coupled CFD. Each step buys fidelity and costs time. Their plan is the one-way rung inside the BEAST bearing simulation tool: BEAST provides the dynamics and heat sources, Particleworks provides the HTCs, and the combination shortens iteration cycles. Before trusting it, they verified the HTC on two textbook cases, a sphere in a uniform flow and oil between concentric cylinders, the inner one rotating.</p>

            <p>The result is instructive because it is not flattering to anyone. Against the Aoki correlation, Particleworks lay between &minus;7% and +28% over four combinations of radius ratio and speed, and the conventional CFD code between &minus;8% and +17%: the two numerical methods scatter around the correlation by similar amounts. What mattered to SKF is that the vortex pattern appeared with mostly default settings, and the one caution was to watch the velocity (Courant) limiter. The roadmap is concrete: a segmented bearing model first, ideally with a cyclic boundary condition, which SKF has asked for, otherwise a full bearing with strong local refinement.</p>
            <div class="keypoints"><h5>Key points</h5><ul><li>One-way coupling: BEAST dynamics and heat sources, Particleworks HTC, FE thermal solution.</li><li>Concentric cylinders, bearing oil, radius ratio 0.5 and 0.83, 1,500 and 3,000 rpm: <strong>HTC of 352&ndash;554 W/m&sup2;K</strong> against 312&ndash;531 from the correlation.</li><li>Mostly default settings reproduced the vortex pattern; mind the velocity limiter.</li><li>Request to the roadmap: cyclic boundary condition for bearing segments.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-06.jpg" alt="Integrating Particleworks into SKF Engineering Tools: Part I — key slide" loading="lazy"><figcaption>HTC results for the concentric-cylinders model: Particleworks, correlation and conventional CFD (SKF).</figcaption></figure>
            <div class="talk-intro"><img src="../experience/speakers/leonardo-tiberi.jpg" alt="Leonardo Tiberi"><div><div class="t-time">16:30–17:00</div><h3>Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method</h3><div class="t-who">Leonardo Tiberi — Track One SRL – Unimore (IT)</div></div></div>
            <p>A carrier roller holds the track chain of an excavator: the shell rotates, the shaft stays fixed, and the internal temperature decides whether the seals survive. Track One modelled every component with its own motion and material and added the thermal boundaries a real roller has: two heat-generating surfaces (seal and bushing), a heat sink at the chain contact and the circumferential surface, and convection to air.</p>

            <p>The iterative steady-state CHT has two phases. Phase 1 runs the oil alone with the solids frozen and extracts averaged HTC and near-wall temperature maps, a few hours of simulation; phase 2 maps them onto the solids and solves the new steady temperature field, a few minutes. The loop stops when the solid field no longer changes within a tolerance, which here took three to four iterations. Oil viscosity follows an Arrhenius&ndash;Vogel law, so oil temperature feeds back on the flow at every pass.</p>
            <div class="eng-note"><b>Engineering note.</b> Because the roller rotates, the contact patch that sees the chain is not fixed; a naive contact resistance would overestimate heat dissipation. Track One divides it by the footprint-to-contact area ratio &tau;: <code>R&Prime;<sub>c,eq</sub> = R&Prime;<sub>c,real</sub> / &tau;</code>. Air convection used <code>HTC<sub>air</sub> = 5.7 + 3.8&middot;v</code>.</div>
            <div class="keypoints"><h5>Key points</h5><ul><li>Phase 1 (oil only, hours) and phase 2 (solid mapping, minutes) alternate until the solid field is stable.</li><li><strong>3&ndash;4 iterations</strong>; about one day per case.</li><li>Errors against the bench test below 7% on thermocouples and oil in both load cases (laser sensors outside, probe in the oil).</li><li>Next: oil rheology evolution, FEM coupling for deformation, critical operating conditions.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-10.jpg" alt="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method — key slide" loading="lazy"><figcaption>Case 1: simulated against measured temperatures on collar, cover, shell, shaft and oil (Track One).</figcaption></figure>

            <hr class="section-rule">

            <h2>Air: measure it before you simulate it</h2>

            <div class="talk-intro"><img src="../experience/speakers/lukas-hafner.jpg" alt="Lukas Hafner"><div><div class="t-time">14:30–15:00</div><h3>Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems</h3><div class="t-who">Dr. Lukas Hafner — deepfluid (DE), with Gianluca Parma — EnginSoft</div></div></div>
            <p>An optical inline sensor sees what a single air-content number hides. The slide that opened the measurement part showed two oils at the same 0.65% air: in one, 361 bubbles of 132 µm average diameter offering 18 m&sup2; of oil&ndash;air contact surface; in the other, 1,289 bubbles of 68 µm and 32 m&sup2;. Same percentage, almost double the interface, so very different oxidation, cavitation and compressibility behaviour. Hafner added that cavitation maps correlate with both air content and bubble size.</p>

            <p>For simulation this means calibrating the Particleworks aeration model on two things, the total air generated and the bubble size distribution, and then using it also away from the calibration point. The demonstration was a differential gear at 130 rpm with 1.4 litres of oil and 2.7 million particles of 0.8 mm. Before calibration the model returned 0.12% air with 800 µm bubbles, simply the particle size. After calibration with deepfluid data it returned <strong>0.45% air and 186 µm bubbles against measured values of 0.43% and 180 µm</strong>.</p>
            <div class="keypoints"><h5>Key points</h5><ul><li>Same air content can hide very different bubble populations: 132 µm / 18 m&sup2; versus 68 µm / 32 m&sup2;.</li><li>Calibrate both generation rate and size distribution: 0.12% / 800 µm becomes 0.45% / 186 µm (measured 0.43% / 180 µm).</li><li>A calibration belongs to an oil and its additive package: change the additives and it must be repeated.</li><li>Coefficients can be scaled with speed from a reference speed; the temperature dependence is an open point.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-07.jpg" alt="Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems — key slide" loading="lazy"><figcaption>Quantitative comparison before and after calibration: air content and bubble-size distribution against the measurement (deepfluid).</figcaption></figure>

            <hr class="section-rule">

            <h2>Wear: simulating what breaks</h2>

            <div class="talk-intro"><img src="../experience/speakers/jean-decaix.jpg" alt="Jean Decaix"><div><div class="t-time">12:15–12:45</div><h3>Moving Particle Simulation of Eroded Pelton Runners</h3><div class="t-who">Jean Decaix — HES-SO Valais/Wallis (CH)</div></div></div>
            <p>The context is ReHydro, a Horizon Europe project of 18 partners and about 12 million euros that runs to 2028. Europe&rsquo;s hydropower fleet is 50&ndash;55 years old and must now balance wind and solar, so runners see sediment and cavitation erosion that costs efficiency, and inspecting one means two or three days without production. HES-SO&rsquo;s question was whether MPS can compute the torque, and the torque loss, of an eroded Pelton runner.</p>

            <p>The setup is lean: a single jet, imposed rotation, viscosity neglected, a time step near 10<sup>&minus;6</sup> s and a Courant limiter of 0.2, from 5 minutes (coarse) to 1.5 days (fine) on an NVIDIA L40S. Several full revolutions are feasible, which Decaix noted a finite-volume code takes more than a week to do. For a new runner, dimensionless torque rises as the particle size goes from 5 to 0.5 mm, and a linear extrapolation to zero size lands close to 1. For eroded runners, he first used artificial erosion (a flat or rounded splitter, an enlarged cut-out, a worn tip) to compare the efficiency drop with analytical and published results, then real runners at three stages: new, after three years and after five, when the owner decided to refurbish.</p>
            <div class="keypoints"><h5>Key points</h5><ul><li>Single jet, imposed speed, CFL limiter 0.2: 5 minutes to 1.5 days on an L40S.</li><li>Torque converges towards the target as particle size shrinks; extrapolating to zero size gives a cheap estimate.</li><li>Efficiency drop from a flat splitter follows the analytical trend, closer with finer particles.</li><li><strong>Torque loss from real erosion is predicted accurately</strong>; next, letting the runner speed respond to load rejection, which needs the shaft-line inertia.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-05.jpg" alt="Moving Particle Simulation of Eroded Pelton Runners — key slide" loading="lazy"><figcaption>Dimensionless torque of three physically eroded runners (T-1 to T-3) against the erosion parameter (HES-SO).</figcaption></figure>
            <div class="talk-intro"><img src="../experience/speakers/bernd-valtwies.jpg" alt="Bernd Valtwies"><div><div class="t-time">17:00–17:30</div><h3>Simulation of Sand Separation and Wear in the Börger FlowSep</h3><div class="t-who">Bernd Valtwies — Börger GmbH (DE) &amp; Riccardo Sala — EnginSoft (IT)</div></div></div>
            <p>Biogas plants are moving from maize silage to manure, which brings stones, sand and soil. Sand settles in the final storage tank (about 1.9 m of it after 36 months in the case shown), blocks pipes and tankers and shrinks usable volume. The FlowSep is a cyclone-like stage behind Börger&rsquo;s BioSelect that sends the heavy phase to output 1 and a clean thin phase to output 2. Sand is only about 1% of the material, split in fractions of 0.4&ndash;0.5, 0.3&ndash;0.4 and under 0.3 mm, and in the thin phase of the real machine the coarsest fraction is completely gone.</p>

            <p>Börger measured flows, densities and the ash content (heating to 800 °C burns off the organics) and EnginSoft built the Granuleworks&ndash;Particleworks model. The reference case deviated by <strong>less than 10% in mass flow</strong> from the tests, and the particle sizes in the thin phase matched exactly. The model then compared two flow rates and showed more particles of the first fraction reaching the clean output at the higher one, before the question turned to wear: the predicted high-wear zones, at the back plate and along the bending edge, are where the prototype wore after roughly half a year of round-the-clock operation.</p>
            <div class="eng-note"><b>Engineering note.</b> Wall interaction was read from the particle number density within 1 mm of the wall, together with velocity. With version 9, the force acting on the wall from the particles is the more direct indicator, and it is now available for DEM too.</div>
            <div class="keypoints"><h5>Key points</h5><ul><li>Evaluation parameter: number of fraction-1 particles in the clean output; <strong>deviation under 10%</strong> from the tests.</li><li>Higher flow rate sends more of the coarse fraction into the clean phase.</li><li>Simulated wear zones match the prototype: back plate and bending edge, after ~6 months of 24/7 operation.</li><li>Use: decide whether to widen the radius or lengthen the unit before building the next prototype.</li></ul></div>
            <figure class="slide"><img src="images/pwe2026/slide-11.jpg" alt="Simulation of Sand Separation and Wear in the Börger FlowSep — key slide" loading="lazy"><figcaption>Wear in the prototype housing: &ldquo;the wear pattern corresponds to simulation&rdquo; (Börger).</figcaption></figure>

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

  <!-- Related Content -->
  <section class="related-section">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <h5 class="fw-bold mb-3" style="font-size: 0.85rem; text-transform: uppercase; letter-spacing: 0.5px; color: var(--pw-gray);">Related Content</h5>
          <div class="row g-3">
            <div class="col-md-4">
              <a href="pw-experience-2025.php" class="related-card">
                <h5>PW Experience 2025</h5>
                <p>Munich 2025 — from validation to virtual prototyping.</p>
                <span class="card-arrow"><i class="bi bi-arrow-right"></i></span>
              </a>
            </div>
            <div class="col-md-4">
              <a href="../experience/proceedings2026.php" class="related-card">
                <h5>Proceedings 2026</h5>
                <p>Slides and key findings of every released talk.</p>
                <span class="card-arrow"><i class="bi bi-arrow-right"></i></span>
              </a>
            </div>
            <div class="col-md-4">
              <a href="../index.php#demo" class="related-card">
                <h5>Request a Demo</h5>
                <p>See Particleworks in action with a personalized walkthrough.</p>
                <span class="card-arrow"><i class="bi bi-arrow-right"></i></span>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4">
          <div class="footer-brand">
            <img src="../images/PWEurope_negativ-logo.png" alt="Particleworks Europe">
          </div>
          <p class="small" style="max-width:300px;">European competence center for meshfree CFD simulation with Particleworks and Granuleworks technologies.</p>
          <div class="d-flex gap-2 mt-3">
            <a href="https://www.linkedin.com/company/particleworks-europe/" class="social-link" target="_blank"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Products</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="../index.php">Particleworks</a></li>
            <li class="mb-2"><a href="../index.php">Granuleworks</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Services</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="../index.php">Consulting</a></li>
            <li class="mb-2"><a href="../index.php">Training</a></li>
            <li class="mb-2"><a href="../index.php">Support</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Resources</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="../index.php#case-studies">Case Studies</a></li>
          </ul>
        </div>
        <div class="col-lg-2">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Contact</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><i class="bi bi-telephone me-1"></i> +39 0461 915391</li>
            <li class="mb-2"><a href="mailto:info@particleworks-europe.com"><i class="bi bi-envelope me-1"></i> info@particleworks-europe.com</a></li>
          </ul>
        </div>
      </div>
      <div class="footer-divider"></div>
      <div class="d-flex flex-wrap justify-content-between align-items-center">
        <p class="small mb-0">&copy; 2026 Particleworks Europe. All rights reserved.</p>
        <p class="small mb-0">Meshfree CFD simulation technology</p>
      </div>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    window.addEventListener('scroll', function() {
      document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30);
    });
  </script>
</body>
</html>