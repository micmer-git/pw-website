<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="../favicon.ico">
  <title>Register — Particleworks Experience 2026 | Modena, October 6-7</title>
  <meta name="description" content="Register for Particleworks Experience 2026 — Modena, October 6-7. Reserve your seat for the technical workshop and conference day, including the release of Particleworks 9.0.">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {
      --pw-blue:#0088cc; --pw-blue-dark:#006da3; --pw-green:#25a361; --pw-green-dark:#1e8a51;
      --pw-dark:#1a1a2e; --pw-gray:#6c757d; --pw-light:#f8f9fa;
      --pw-gradient:linear-gradient(135deg,#0088cc 0%,#25a361 100%);
      --pw-gradient-dark:linear-gradient(135deg,#04243a 0%,#0a3a5c 45%,#0d4a3a 100%);
      --ev-red:#d9503f; --ev-red-deep:#b51e23; --ev-red-dark:#8f161b; --ev-blue:#1983d0;
      --ev-crimson:#c01f24; --ev-vivid:#e0382a; --ev-coral:#ef5c43;
      --ev-gradient:linear-gradient(135deg,#d9503f 0%,#b51e23 58%,#8f161b 100%);
      --ev-accent:linear-gradient(135deg,#ef5c43 0%,#b51e23 100%);
    }
    * { font-family:'Inter',sans-serif; }
    html { scroll-behavior:smooth; }
    body { color:var(--pw-dark); overflow-x:hidden; background:#fff; }

    .navbar { background:rgba(255,255,255,0.97); backdrop-filter:blur(12px); box-shadow:0 1px 0 rgba(0,0,0,0.06); padding:0.6rem 0; transition:box-shadow .3s; }
    .navbar.scrolled { box-shadow:0 2px 20px rgba(0,0,0,0.08); }
    .navbar-brand img { height:38px; }
    .navbar .nav-link { font-size:0.88rem; font-weight:500; color:var(--pw-dark); padding:0.5rem 0.85rem !important; transition:color .2s; }
    .navbar .nav-link:hover { color:var(--pw-blue); }
    .nav-register { background:var(--pw-blue); color:#fff !important; border-radius:50px; padding:0.5rem 1.3rem !important; font-weight:600; }
    .nav-register:hover { background:var(--pw-blue-dark); color:#fff !important; }
    .navbar .dropdown-toggle::after { margin-left:0.35rem; vertical-align:0.1em; }
    .navbar .dropdown-menu { border:1px solid rgba(0,0,0,0.06); border-radius:12px; box-shadow:0 12px 40px rgba(0,0,0,0.10); padding:0.5rem; margin-top:0.4rem; min-width:210px; }
    .navbar .dropdown-item { border-radius:8px; padding:0.5rem 0.7rem; font-size:0.86rem; font-weight:500; color:var(--pw-dark); display:flex; align-items:center; gap:0.6rem; }
    .navbar .dropdown-item i { color:var(--ev-crimson); font-size:0.95rem; }
    .navbar .dropdown-item:hover, .navbar .dropdown-item:focus { background:linear-gradient(135deg, rgba(217,80,63,0.10), rgba(143,22,27,0.06)); color:var(--ev-crimson); }

    /* Hero */
    .reg-hero { position:relative; padding:8.5rem 0 4rem; background:linear-gradient(135deg, rgba(217,80,63,0.85), rgba(143,22,27,0.93)), url('img/theme-bg.jpg') center/cover no-repeat; overflow:hidden; }
    .reg-hero::before { content:''; position:absolute; inset:0; background:
        radial-gradient(ellipse 70% 60% at 12% 92%, rgba(255,180,150,0.18) 0%, transparent 60%),
        radial-gradient(ellipse 60% 55% at 88% 8%, rgba(255,255,255,0.12) 0%, transparent 60%); }
    .reg-hero .container { position:relative; z-index:3; }
    .hero-particles { position:absolute; inset:0; z-index:1; opacity:0.35; }
    .eyebrow { display:inline-flex; align-items:center; gap:0.5rem; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.32); color:#ffe6dd; padding:0.4rem 1rem; border-radius:50px; font-size:0.78rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:1.4rem; }
    .reg-hero h1 { font-size:clamp(2.2rem,5.2vw,3.6rem); font-weight:900; color:#fff; letter-spacing:-1px; line-height:1.08; }
    .reg-hero h1 .accent { background:linear-gradient(120deg,#fff,#ffd9c2); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
    .reg-hero .lead { font-size:1.15rem; color:rgba(255,255,255,0.85); max-width:620px; line-height:1.7; margin-top:1.2rem; }
    .hero-facts { display:flex; flex-wrap:wrap; gap:0.7rem; margin-top:2rem; }
    .hero-fact { display:inline-flex; align-items:center; gap:0.5rem; background:rgba(255,255,255,0.10); border:1px solid rgba(255,255,255,0.20); color:#fff5f1; padding:0.55rem 1.05rem; border-radius:12px; font-size:0.9rem; font-weight:500; }
    .hero-fact i { color:#ffd9c2; font-size:1.05rem; }

    /* Form section */
    .reg-section { padding:3.5rem 0 4.5rem; background:linear-gradient(180deg,#fff,#f6fafd); }
    .reg-card { background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:24px; box-shadow:0 18px 50px rgba(7,40,70,0.08); overflow:hidden; }
    .reg-card-head { padding:1.6rem 1.9rem; border-bottom:1px solid rgba(0,0,0,0.06); display:flex; align-items:center; gap:0.8rem; background:linear-gradient(135deg,#fff6f3,#fdeeec); }
    .reg-card-head .ic { flex-shrink:0; width:46px; height:46px; border-radius:12px; background:var(--ev-accent); display:flex; align-items:center; justify-content:center; color:#fff; font-size:1.3rem; }
    .reg-card-head h2 { font-size:1.2rem; font-weight:800; margin:0; letter-spacing:-0.3px; }
    .reg-card-head p { margin:0.15rem 0 0; font-size:0.88rem; color:var(--pw-gray); }
    .reg-embed-wrap { position:relative; }
    .reg-embed { display:block; width:100%; min-height:1180px; border:0; }
    .reg-fallback { text-align:center; font-size:0.88rem; color:var(--pw-gray); padding:1.1rem 1.5rem; border-top:1px solid rgba(0,0,0,0.06); }
    .reg-fallback a { color:var(--ev-crimson); font-weight:600; }

    .aside-card { background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:18px; padding:1.6rem 1.7rem; height:100%; }
    .aside-card h3 { font-size:1rem; font-weight:800; letter-spacing:-0.2px; margin-bottom:1rem; }
    .aside-list { list-style:none; padding:0; margin:0; }
    .aside-list li { display:flex; gap:0.7rem; align-items:flex-start; font-size:0.92rem; line-height:1.5; color:#445; margin-bottom:0.9rem; }
    .aside-list li i { color:var(--ev-crimson); font-size:1.05rem; margin-top:0.1rem; flex-shrink:0; }
    .aside-list li b { color:var(--pw-dark); font-weight:600; display:block; }
    .btn-ghost-red { background:transparent; color:var(--ev-crimson); border:1.5px solid rgba(192,31,36,0.4); padding:0.6rem 1.3rem; border-radius:50px; font-weight:600; font-size:0.9rem; transition:all .3s; display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; }
    .btn-ghost-red:hover { background:var(--ev-crimson); color:#fff; }

    footer { background:#11111e; color:rgba(255,255,255,0.7); padding:3.5rem 0 1.5rem; }
    footer a { color:rgba(255,255,255,0.7); text-decoration:none; transition:color .2s; }
    footer a:hover { color:#fff; }
    footer .footer-brand img { height:34px; margin-bottom:1rem; }
    footer .footer-divider { border-top:1px solid rgba(255,255,255,0.08); margin:2rem 0 1.5rem; }
    .social-link { width:40px; height:40px; border-radius:10px; background:rgba(255,255,255,0.06); display:inline-flex; align-items:center; justify-content:center; font-size:1.1rem; transition:all .3s; }
    .social-link:hover { background:var(--pw-blue); color:#fff; }
  </style>
</head>
<body>

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg fixed-top">
    <div class="container">
      <a class="navbar-brand" href="https://particleworks-europe.com/"><img src="../images/PW_Europe_logo_small.png" alt="Particleworks Europe"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#nav" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
      <div class="collapse navbar-collapse justify-content-end" id="nav">
        <ul class="navbar-nav align-items-lg-center gap-1">
          <li class="nav-item"><a class="nav-link" href="index.html">Experience 2026</a></li>
          <li class="nav-item"><a class="nav-link" href="program.html">Program</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Past editions</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2025.php"><i class="bi bi-calendar3"></i> Proceedings 2025</a></li>
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2024.php"><i class="bi bi-calendar3"></i> Proceedings 2024</a></li>
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2023.php"><i class="bi bi-calendar3"></i> Proceedings 2023</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="https://particleworks-europe.com/experience/contact.php">Contact</a></li>
          <li class="nav-item ms-lg-2"><a class="nav-link nav-register" href="registration.html">Register</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Hero -->
  <section class="reg-hero">
    <svg class="hero-particles" preserveAspectRatio="xMidYMid slice" viewBox="0 0 1200 500" aria-hidden="true">
      <g fill="#ffe2d4">
        <circle cx="120" cy="80" r="3"><animate attributeName="cy" values="80;120;80" dur="7s" repeatCount="indefinite"/></circle>
        <circle cx="300" cy="200" r="2.4" opacity="0.7"><animate attributeName="cy" values="200;160;200" dur="9s" repeatCount="indefinite"/></circle>
        <circle cx="540" cy="100" r="3.4" opacity="0.6"><animate attributeName="cy" values="100;140;100" dur="6s" repeatCount="indefinite"/></circle>
        <circle cx="820" cy="240" r="2.6" opacity="0.7"><animate attributeName="cy" values="240;200;240" dur="8s" repeatCount="indefinite"/></circle>
        <circle cx="1010" cy="120" r="3" opacity="0.6"><animate attributeName="cy" values="120;170;120" dur="7.5s" repeatCount="indefinite"/></circle>
        <circle cx="700" cy="380" r="2.2" opacity="0.5"><animate attributeName="cy" values="380;340;380" dur="10s" repeatCount="indefinite"/></circle>
        <circle cx="200" cy="420" r="2.8" opacity="0.5"><animate attributeName="cy" values="420;380;420" dur="8.5s" repeatCount="indefinite"/></circle>
      </g>
    </svg>
    <div class="container">
      <div class="eyebrow"><i class="bi bi-pencil-square"></i> Registration</div>
      <h1>Save your seat for <span class="accent">Modena</span>.</h1>
      <p class="lead">Reserve your place at Particleworks Experience 2026 — the technical workshop, the release of <strong>Particleworks&nbsp;9.0</strong> and validated case studies from industry and academia.</p>
      <div class="hero-facts">
        <span class="hero-fact"><i class="bi bi-calendar-event"></i> October 6–7, 2026</span>
        <span class="hero-fact"><i class="bi bi-geo-alt"></i> BPER FORUM Monzani, Modena (IT)</span>
        <span class="hero-fact"><i class="bi bi-ticket-perforated"></i> Free to attend · seats limited</span>
      </div>
    </div>
  </section>

  <!-- Registration form -->
  <section class="reg-section" id="form">
    <div class="container">
      <div class="row g-4 justify-content-center">
        <div class="col-lg-8">
          <div class="reg-card">
            <div class="reg-card-head">
              <div class="ic"><i class="bi bi-person-check"></i></div>
              <div>
                <h2>Registration form</h2>
                <p>Fill in your details below — you'll receive a confirmation by email.</p>
              </div>
            </div>
            <div class="reg-embed-wrap">
              <iframe id="reg-form" class="reg-embed" src="https://particleworks-europe.forms-eu.com/embed.php?id=24414"
                title="Particleworks Experience 2026 registration form" loading="lazy" scrolling="yes"></iframe>
            </div>
            <div class="reg-fallback">
              Trouble loading the form? <a href="https://particleworks-europe.forms-eu.com/embed.php?id=24414" target="_blank" rel="noopener">Open it in a new tab <i class="bi bi-box-arrow-up-right"></i></a>
            </div>
          </div>
        </div>

        <div class="col-lg-4">
          <div class="aside-card">
            <h3>Good to know</h3>
            <ul class="aside-list">
              <li><i class="bi bi-calendar2-week"></i><span><b>Two days</b>Workshop on Oct 6 (14:00–18:00) and the full conference day on Oct 7 (09:00–17:00).</span></li>
              <li><i class="bi bi-geo-alt"></i><span><b>Venue</b>BPER FORUM Monzani – Sala Bossoli, Via Aristotele 33, 41126 Modena (MO), Italy.</span></li>
              <li><i class="bi bi-mic"></i><span><b>8 talks · 5 countries</b>Including the release of Particleworks 9.0 and Granuleworks 4.0.</span></li>
              <li><i class="bi bi-shield-check"></i><span><b>Your data</b>Processed in line with GDPR, solely for managing your participation.</span></li>
            </ul>
            <div class="d-flex flex-wrap gap-2 mt-3">
              <a href="program.html" class="btn-ghost-red"><i class="bi bi-calendar3"></i> View the program</a>
              <a href="https://particleworks-europe.com/experience/call-for-abstract" class="btn-ghost-red"><i class="bi bi-file-earmark-text"></i> Submit an abstract</a>
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
          <div class="footer-brand"><img src="../images/PWEurope_negativ-logo.png" alt="Particleworks Europe"></div>
          <p class="small" style="max-width:300px;">European competence center for meshfree CFD simulation with Particleworks and Granuleworks technologies.</p>
          <div class="d-flex gap-2 mt-3">
            <a href="https://www.linkedin.com/company/particleworks-europe/" class="social-link" target="_blank"><i class="bi bi-linkedin"></i></a>
          </div>
        </div>
        <div class="col-lg-3 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Experience 2026</h6>
          <ul class="list-unstyled small">
            <li class="mb-2"><a href="index.html">Conference overview</a></li>
            <li class="mb-2"><a href="program.html">Program</a></li>
            <li class="mb-2"><a href="registration.html">Registration</a></li>
          </ul>
        </div>
        <div class="col-lg-3 col-md-4">
          <h6 class="fw-semibold text-white mb-3" style="font-size:0.85rem;">Venue</h6>
          <p class="small mb-0">BPER FORUM Monzani – Sala Bossoli<br>Via Aristotele 33<br>41126 Modena (MO), Italy</p>
        </div>
        <div class="col-lg-2 col-md-4">
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
    window.addEventListener('scroll', function(){
      document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30);
    });
    // Progressive enhancement: if the embedded form posts its height, resize the iframe to fit (no inner scrollbar).
    window.addEventListener('message', function(e){
      if (typeof e.origin !== 'string' || e.origin.indexOf('forms-eu.com') === -1) return;
      var h = null, d = e.data;
      if (typeof d === 'number') h = d;
      else if (d && typeof d === 'object') h = d.height || d.frameHeight || (d.iframe && d.iframe.height);
      else if (typeof d === 'string') { var m = d.match(/(\d{3,5})/); if (m) h = parseInt(m[1], 10); }
      if (h && h > 300 && h < 20000) {
        var f = document.getElementById('reg-form');
        if (f) f.style.height = h + 'px';
      }
    }, false);
  </script>
</body>
</html>
