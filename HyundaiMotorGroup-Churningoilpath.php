<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="favicon.ico">
  <title>Moving Particle Simulation: the case studies of Particleworks Europe</title>
  <meta name="description" content="Case study: Churning oil path optimization process development - Application of Moving Particle Simulation Method to Design Process">
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

    .case-hero {
      position: relative;
      padding: 8rem 0 4rem;
      background: var(--pw-gradient-dark);
      overflow: hidden;
    }
    .case-hero::before {
      content: '';
      position: absolute;
      inset: 0;
      background:
        radial-gradient(ellipse 80% 60% at 20% 80%, rgba(37,163,97,0.2) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 20%, rgba(0,136,204,0.25) 0%, transparent 60%);
    }
    .case-hero .container { position: relative; z-index: 2; }
    .case-hero h1 {
      font-size: clamp(1.8rem, 4vw, 2.8rem);
      font-weight: 800;
      color: #fff;
      letter-spacing: -0.5px;
      line-height: 1.2;
      max-width: 800px;
    }
    .industry-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: #fd7e1422;
      color: #fff;
      border: 1px solid #fd7e1466;
      padding: 0.35rem 1rem;
      border-radius: 50px;
      font-size: 0.82rem;
      font-weight: 600;
      margin-bottom: 1.2rem;
    }
    .case-meta {
      color: rgba(255,255,255,0.75);
      font-size: 0.95rem;
      margin-top: 1.5rem;
    }
    .case-meta strong { color: #fff; }

    .case-content { padding: 4rem 0; }
    .case-image {
      border-radius: 16px;
      overflow: hidden;
      box-shadow: 0 12px 40px rgba(0,0,0,0.1);
      margin-bottom: 2rem;
    }
    .case-image img {
      width: 100%;
      height: auto;
      display: block;
    }
    .abstract-text {
      font-size: 1.08rem;
      line-height: 1.85;
      color: #444;
    }
    .info-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: linear-gradient(135deg, rgba(0,136,204,0.1), rgba(37,163,97,0.1));
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--pw-blue);
      font-size: 1.1rem;
      flex-shrink: 0;
      margin-right: 1rem;
    }

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
    .btn-pw-green {
      background: var(--pw-green);
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
    .btn-pw-green:hover { background: var(--pw-green-dark); color: #fff; transform: translateY(-2px); box-shadow: 0 8px 25px rgba(37,163,97,0.3); }
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

    .quote-section {
      background: var(--pw-gradient);
      color: #fff;
      padding: 4rem 0;
    }
    .quote-section blockquote {
      font-size: clamp(1.15rem, 2.5vw, 1.5rem);
      font-weight: 300;
      line-height: 1.65;
      max-width: 750px;
      margin: 0 auto;
    }
    .quote-section cite {
      font-size: 1rem;
      opacity: 0.8;
      font-style: normal;
      font-weight: 500;
    }

    .sidebar-card {
      background: #fff;
      border-radius: 16px;
      border: 1px solid rgba(0,0,0,0.06);
      padding: 2rem;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    }

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
  </style>



<!-- === SEO head (auto-generated, matches backup website_now) === -->
  <link rel="canonical" href="https://particleworks-europe.com/HyundaiMotorGroup-Churningoilpath.html">
  <meta name="author" content="Particleworks Europe">
  <meta name="keywords" content="Particleworks, Particleworks Europe, Granuleworks, technologies, simulation">
  <meta name="google-site-verification" content="13JcLKtEM_c2bcIc8ZMrIKncMjxxmwN5nmfLLs8WLQA">
  <meta property="og:site_name" content="Particleworks Europe">
  <meta property="og:title" content="Moving Particle Simulation: the case studies of Particleworks Europe">
  <meta property="og:description" content="Case study: Churning oil path optimization process development - Application of Moving Particle Simulation Method to Design Process">
  <meta property="og:url" content="https://particleworks-europe.com/HyundaiMotorGroup-Churningoilpath.html">
  <meta property="og:type" content="website">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Moving Particle Simulation: the case studies of Particleworks Europe">
  <meta name="twitter:description" content="Case study: Churning oil path optimization process development - Application of Moving Particle Simulation Method to Design Process">
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
              <li><a class="dropdown-item" href="training.html"><i class="bi bi-mortarboard"></i><span><div class="dd-t">Training</div><div class="dd-s">Courses &amp; workshops</div></span></a></li>
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

  <section class="case-hero">
    <div class="container">
      <div class="industry-badge"><i class="bi-gear"></i> Transmissions & Gearboxes</div>
      <h1>Churning oil path optimization process development &mdash; Application of MPS to Design Process</h1>
      <div class="case-meta">
        <strong><i class="bi bi-people me-1"></i> Chulmin Ahn, Hyundai Motor Group R&amp;D Division</strong>
        <span class="mx-2">|</span>
        <span><i class="bi bi-building me-1"></i> Hyundai Motor Group</span>
      </div>
    </div>
  </section>

  <section class="case-content">
    <div class="container">
      <div class="row g-5">
        <div class="col-lg-8">
          <div class="case-image">
            <img src="images/case-studies/Hyundai_01.png" alt="Churning oil path optimization process development &mdash; Application of MPS to Design Process">
          </div>
          <h3 class="fw-bold mb-3">Abstract</h3>
          <p class="abstract-text">Moving Particle Simulation method applied to reduce computing time and remove mesh work for transmission efficiency optimization. Correlation with bench tests done on different gear speed and temperature.</p>
        </div>
        <div class="col-lg-4">
          <div class="sidebar-card mb-4">
            <h5 class="fw-bold mb-3">Case Study Details</h5>
            <div class="d-flex align-items-center mb-3">
              <div class="info-icon"><i class="bi bi-building"></i></div>
              <div>
                <small class="text-muted d-block">Company</small>
                <span class="fw-medium">Hyundai Motor Group</span>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <div class="info-icon"><i class="bi-gear"></i></div>
              <div>
                <small class="text-muted d-block">Industry</small>
                <span class="fw-medium">Transmissions & Gearboxes</span>
              </div>
            </div>
            <div class="d-flex align-items-center mb-3">
              <div class="info-icon"><i class="bi bi-cpu"></i></div>
              <div>
                <small class="text-muted d-block">Software</small>
                <span class="fw-medium">Particleworks (MPS)</span>
              </div>
            </div>
          </div>

          <div class="sidebar-card">
            <h5 class="fw-bold mb-3">Access Full Paper</h5>
            <div class="d-grid gap-2">
              <a href="images/case-studies/Hyundai-VDI-conference.pdf" class="btn btn-pw me-3 mb-2" target="_blank">
                <i class="bi bi-file-earmark-pdf me-2"></i>Download PDF
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="mt-5 pt-4 border-top">
        <a href="index.html#case-studies" class="btn-pw-outline">
          <i class="bi bi-arrow-left me-2"></i>Back to all case studies
        </a>
      </div>
    </div>
  </section>

  <footer>
    <div class="container">
      <div class="row g-4">
        <div class="col-lg-4">
          <div class="footer-brand">
            <img src="images/PWEurope_negativ-logo.png" alt="Particleworks Europe">
          </div>
          <p class="small" style="max-width:300px;">European competence center for meshfree CFD simulation with Particleworks and Granuleworks technologies.</p>
          <div class="d-flex gap-2 mt-3">
            <a href="https://www.linkedin.com/company/particleworks-europe/" class="social-link" target="_blank"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Products</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="index.html">Particleworks</a></li>
            <li class="mb-2"><a href="index.html">Granuleworks</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Services</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="index.html">Consulting</a></li>
            <li class="mb-2"><a href="index.html">Training</a></li>
            <li class="mb-2"><a href="index.html">Support</a></li>
          </ul>
        </div>
        <div class="col-lg-2 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Resources</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="index.html#case-studies">Case Studies</a></li>
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
        <p class="small mb-0">&copy; 2025 Particleworks Europe. All rights reserved.</p>
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