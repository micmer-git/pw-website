<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="../favicon.ico">
  <title>PW Experience 2026 — What Modena Taught Us About Heat, Air and Wear | Particleworks Europe</title>
  <meta name="description" content="Particleworks Experience 2026, Modena: six talks on closing thermal balances, calibrating aeration against optical measurements and predicting wear with meshless CFD, with the slides, quotes and moments that matter.">
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
    .blk-label { font-size:0.72rem; font-weight:800; letter-spacing:1.5px; text-transform:uppercase; color:#006da3; margin:1.8rem 0 0.5rem; display:flex; align-items:center; gap:0.6rem; }
    .blk-label::after { content:''; flex:1; height:1px; background:rgba(0,136,204,0.22); }
    .finding { display:grid; grid-template-columns:2.1rem 1fr; gap:0.85rem; margin:1.15rem 0; }
    .finding .fn { width:2.1rem; height:2.1rem; border-radius:50%; background:#c01f24; color:#fff; font-weight:800; display:flex; align-items:center; justify-content:center; font-size:0.95rem; margin-top:0.15rem; }
    .finding h4 { font-size:1.05rem; font-weight:800; margin:0 0 0.25rem; color:var(--pw-dark,#1a1a2e); }
    .finding p { margin:0; }
    blockquote.pq { margin:1.5rem 0; padding:1.1rem 1.4rem 0.9rem 1.6rem; background:#fff8e6; border-left:5px solid #ffc400; border-radius:0 14px 14px 0; }
    blockquote.pq p { font-size:1.12rem; line-height:1.55; font-weight:600; font-style:italic; color:#2b2f3a; margin:0 0 0.5rem; }
    blockquote.pq .pqf { font-size:0.82rem; color:#6c757d; display:flex; flex-wrap:wrap; gap:0.4rem 1rem; align-items:center; }
    blockquote.pq .pqf a { font-weight:700; color:#c01f24; text-decoration:none; }
    .pair { display:grid; grid-template-columns:1fr 1fr; gap:1rem; margin:1.2rem 0 1.6rem; }
    .pair figure.slide { margin:0; }
    .chart-card { background:#fff; border:1px solid rgba(0,0,0,0.09); border-radius:14px; padding:1rem 1.2rem 0.7rem; margin:1.3rem 0; box-shadow:0 2px 12px rgba(0,0,0,0.05); }
    .chart-t { font-weight:800; font-size:0.98rem; color:#1a1a2e; }
    .chart-s { font-size:0.8rem; color:#6c757d; margin-bottom:0.4rem; }
    svg.chart { width:100%; height:auto; display:block; }
    svg.chart .cl { font-size:12.5px; fill:#3a4150; font-family:inherit; }
    svg.chart .cv { font-size:12.5px; font-weight:700; fill:#1a1a2e; font-family:inherit; }
    .chart-leg { display:flex; flex-wrap:wrap; gap:0.3rem 1.2rem; font-size:0.78rem; color:#5d6670; margin-top:0.2rem; }
    .chart-leg i { display:inline-block; width:11px; height:11px; border-radius:3px; margin-right:0.35rem; vertical-align:-1px; }
    .chart-two { display:grid; grid-template-columns:1fr 1fr; gap:1rem; }
    .qa { padding:0.7rem 0; border-top:1px solid rgba(0,0,0,0.08); }
    .qa b { display:block; color:#1a1a2e; } .qa span { display:block; color:#4a5260; font-size:0.95rem; margin-top:0.15rem; }
    @media(max-width:700px){ .pair, .chart-two { grid-template-columns:1fr; } }
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
      <p class="lead">Modena, October 7, 2026 — six talks: the context, what they found, the sentence worth quoting and the moment to watch</p>
      <div class="hero-meta">
        <span><i class="bi bi-calendar3"></i> October 2026</span>
        <span><i class="bi bi-clock"></i> 18 min read</span>
        <span><i class="bi bi-tag"></i> Conference Highlights</span>
      </div>
    </div>
  </section>

  <section class="blog-body">
    <div class="container">
      <div class="row justify-content-center">
        <div class="col-lg-9 col-xl-8">
          <article class="article-content">

            <p class="standfirst">On October 7, Particleworks users filled the BPER FORUM Monzani in Modena for a day built around three questions: <mark class="hl">where does the heat go, where does the air go, and where does the material wear?</mark></p>

            <p>Speakers from a bearing maker, a pump manufacturer, a hydropower research project and several engineering firms answered them with the same discipline. Each put simulation next to a thermocouple, an optical sensor or a worn prototype, and said plainly how well they agreed. Each talk below starts with its context, then what was found, with the slides that carry it and a sentence taken straight from the recording. Every “Watch the moment” link opens the video at that second on the <a href="../experience/proceedings2026.php">proceedings page</a>.</p>

            <div class="statstrip daystats">
              <div class="stat"><b>1.5 h</b><span>per case for a pump thermal model, once the model exists</span></div><div class="stat"><b>66 → 169</b><span>W/m²K: the same sphere, read at the wall or 1.5&nbsp;mm away (target 184)</span></div><div class="stat"><b>0.45 vs 0.43 %</b><span>simulated vs measured air in a gearbox, after calibration</span></div><div class="stat"><b>10 → 25 %</b><span>sand lost when the separator flow rate is doubled</span></div>
            </div>

            <div class="toc"><a href="#talk-04">Heat · R&D CFD <small>pump</small></a><a href="#talk-06">Heat · SKF <small>bearings</small></a><a href="#talk-10">Heat · TrackOne <small>roller</small></a><a href="#talk-07">Air · deepfluid <small>gear oil</small></a><a href="#talk-05">Wear · HES-SO <small>Pelton</small></a><a href="#talk-11">Wear · Börger <small>separator</small></a></div>

            <hr class="section-rule">


            <hr class="section-rule">

            <div class="sec-eyebrow">01 · Heat</div>
            <h2>From side effect to deliverable</h2>
            <p class="sec-lead">Three talks treated temperature as a result to deliver. They share one trick: <mark class="hl">never run oil and metal on the same clock.</mark> The oil is simulated briefly, its heat-transfer map is handed to a steady solution of the solids, and the result is checked against something physical.</p>
            <div class="talk-intro" id="talk-04"><img src="../experience/speakers/leonardo-lanciotti.jpg" alt="Leonardo Lanciotti"><div><div class="t-time">Heat · 11:45–12:15</div><h3>CHT Analysis of a Reciprocating Pump</h3><div class="t-who">Leonardo Lanciotti — R&amp;D CFD S.R.L. – Comet S.p.A. (IT)</div></div></div>
            <p class="standfirst">An industrial pump bathed in oil, no thermal data on its contacts, and a model that is declared finished only when <mark class="hl">the oil neither gains nor loses heat</mark>.</p>
            <div class="blk-label">The context</div>
            <p>Volumetric pumps for food, chemical and waste-water plants run all day at a fixed operating point. What goes wrong first is thermal: seals degrade, components overheat. Inside the pump the oil is the only link between hot and cold parts, and every watt finally leaves through natural convection. R&amp;D CFD, with its customer Comet, wanted a thermal model <mark class="hl">representative of the real operating point</mark>, and a method that can be reused on the next pump.</p>
            <p>The obvious route, a fully coupled unsteady run, does not work: it needs double precision and, because sloshing lives in seconds and heat in hours, a simulation far too long. So the problem was cut in two. A few seconds of Particleworks sloshing give the heat-transfer map; a steady conjugate-heat-transfer (CHT) solution then converges in minutes.</p>
            <figure class="slide"><img src="images/pwe2026/s04-10.jpg" alt="CHT Analysis of a Reciprocating Pump — slide" loading="lazy"><figcaption><b>Slide.</b> Why two steps: a short 3D sloshing run feeds a steady CHT, instead of days of unsteady coupling (R&amp;D CFD).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>Do not guess where the heat is born</h4><p>Loads on the contacts were not available. Trial and error was rejected as stochastic and unvalidated; a <mark class="hl">dynamic analysis of the pump</mark> with friction coefficients from the literature gave a power split instead, with far fewer free variables. The largest share sits on the piston–block pair, the contact that is also critical in the test.</p></div></div>
            <div class="finding"><span class="fn">2</span><div><h4>Two independent checks, not one</h4><p>First the thermocouples, compared one to one at the test positions. Then the oil: it is a heat carrier, not a heat sink, so the heat taken from the shaft must equal the heat given to the housing. If either fails, the power, the oil temperature or the ambient HTC is scaled and the loop restarts.</p></div></div>
            <blockquote class="pq"><p>“The oil is not a heat sink. All the heat carried by the oil should be exchanged with the other components of the pump, so the balance of the oil should be equal to zero.”</p><div class="pqf">Leonardo Lanciotti <a href="../experience/proceedings2026.php?talk=04&amp;t=1279#talk-04"><i class="bi bi-play-fill"></i> 21:19 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">3</span><div><h4>The model tells the truth about the seals</h4><p>All thermocouples align; the worst, the open-side bearing, is off by about 5–6 °C and points to a local particle refinement as the next step. The shaft sits at 70–80 °C as in the test, and a <mark class="hl">hot spot at the piston–seal contact</mark> shows up where seals degrade abnormally in service.</p></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>Cheap enough to do by hand</h4><p>Three to five iterations were enough, and a steady CHT takes minutes on a GPU. Once the model exists, a case is about <mark class="hl">an hour and a half</mark>.</p></div></div>
            <blockquote class="pq"><p>“Sometimes the setup is longer than the simulation itself. But, of course, we are talking about one hour and a half once the model is defined.”</p><div class="pqf">Leonardo Lanciotti <a href="../experience/proceedings2026.php?talk=04&amp;t=1220#talk-04"><i class="bi bi-play-fill"></i> 20:20 Watch the moment</a></div></blockquote>
            <figure class="slide"><img src="images/pwe2026/s04-28.jpg" alt="CHT Analysis of a Reciprocating Pump — slide" loading="lazy"><figcaption><b>Slide.</b> Simulated against measured thermocouples at the same positions: the gap is in °C for each one (R&amp;D CFD).</figcaption></figure>
            <div class="eng-note"><b>Engineering note.</b> The oil balance is checked on a uniform surface mesh built from the HTC map: <code>Q&#775;<sub>shaft&rarr;oil</sub> = &Sigma; HTC<sub>i</sub>(T<sub>i</sub>&minus;T<sub>oil</sub>)A<sub>i</sub> = &Sigma; HTC<sub>j</sub>(T<sub>oil</sub>&minus;T<sub>j</sub>)A<sub>j</sub></code> and must close to 0 W.</div>
            <div class="keypoints"><h5>In short</h5><ul><li>Sloshing and heat are decoupled: seconds of oil, minutes of steady CHT.</li><li>The oil balance at zero is the check that does not depend on the thermocouples.</li><li>About 1.5 h per case once the model exists; automation with Python is the natural next step.</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=04&amp;t=370#talk-04"><i class="bi bi-play-fill"></i> 6:10 Why decouple sloshing and CHT</a><a href="../experience/proceedings2026.php?talk=04&amp;t=432#talk-04"><i class="bi bi-play-fill"></i> 7:12 Power split</a><a href="../experience/proceedings2026.php?talk=04&amp;t=863#talk-04"><i class="bi bi-play-fill"></i> 14:23 Results vs thermocouples</a><a href="../experience/proceedings2026.php?talk=04&amp;t=1011#talk-04"><i class="bi bi-play-fill"></i> 16:51 Where it needs refinement</a><a href="../experience/proceedings2026.php?talk=04&amp;t=1208#talk-04"><i class="bi bi-play-fill"></i> 20:08 Q&A: how many iterations?</a></div>

            <div class="talk-intro" id="talk-06"><img src="../experience/speakers/lijun-cao.jpg" alt="Lijun Cao"><div><div class="t-time">Heat · 12:45–13:15</div><h3>Integrating Particleworks into SKF Engineering Tools: Part I</h3><div class="t-who">Lijun Cao &amp; Fabrizio Mandrile — SKF (NL)</div></div></div>
            <p class="standfirst">Before trusting a heat-transfer coefficient inside a bearing tool, SKF tested it on the simplest cases that exist, and found that <mark class="hl">the answer depends on where you read it</mark>.</p>
            <div class="blk-label">The context</div>
            <p>SKF frames the problem with one number: about <mark class="hl">20 % of the world’s energy is lost to friction</mark>. Bearings fight friction, but even a good bearing is a source of heat, and temperature then shapes everything: the lubricant film, thermal expansion and the extra load it brings, and life, because every degree more shortens the life of the lubricant and of the bearing.</p>
            <p>Thermal analysis is a ladder, from lumped networks that answer in real time, through finite elements with HTCs from analytical formulas, to CFD coupled one way and finally two ways, where answers take days or weeks. SKF’s next rung is one-way: its in-house bearing tool BEAST provides dynamics and heat sources, Particleworks provides the HTC maps. Part I of the study is the verification of those HTCs. Rolling bearings cannot be measured easily, so the references are classic cases: a sphere in a cross-flow, and two concentric cylinders.</p>
            <figure class="slide"><img src="images/pwe2026/s06-11.jpg" alt="Integrating Particleworks into SKF Engineering Tools: Part I — slide" loading="lazy"><figcaption><b>Slide.</b> The thermal-analysis ladder: from lumped networks to fully coupled CFD, trading speed for accuracy (SKF).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>One sphere, many answers</h4><p>The reference is the Whitaker correlation: 184 W/m²K. Particleworks’ local-correlation method reads the velocity of particles next to the wall, which tends to zero there, so it reports a low HTC: <mark class="hl">66 at the wall, 169 when sampled 1.5 mm away</mark>. With coarser particles the default is 85, and raising the Nusselt coefficient lifts it to 192.</p></div></div>
            <blockquote class="pq"><p>“Imagine if you apply a non-slip condition very close to the wall: the velocity is approaching zero, so you get a very low Reynolds number and therefore a very low HTC. There’s nothing wrong with it. This is just the nature of the method.”</p><div class="pqf">Lijun Cao <a href="../experience/proceedings2026.php?talk=06&amp;t=1488#talk-06"><i class="bi bi-play-fill"></i> 24:48 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">2</span><div><h4>The heat-flux method converges, at a price</h4><p>Solving the temperature field and reading the heat flux does not care about mapping distance, and improves with refinement (75 → 127 W/m²K from 0.5 to 0.25 mm, against 180 for Ansys Fluent). But a thermal particle is heavier than a flow-only one, so further refinement was too expensive. Local refinement was disappointing, and is improved in the new release.</p></div></div>
            <div class="chart-card"><div class="chart-t">One sphere, nine answers</div><div class="chart-s">Surface-average heat-transfer coefficient, W/m²K. Dashed line: Whitaker correlation, 184.</div><svg viewBox="0 0 640 306" role="img" aria-label="One sphere, nine answers" class="chart"><text x="292" y="27" text-anchor="end" class="cl">Whitaker correlation (reference)</text><rect x="300" y="13" width="239.6" height="19" rx="4" fill="#1a1a2e"/><text x="545.6" y="28" class="cv">184</text><text x="292" y="57" text-anchor="end" class="cl">PW local correlation: read at the wall</text><rect x="300" y="43" width="86.0" height="19" rx="4" fill="#c01f24"/><text x="392.0" y="58" class="cv">66</text><text x="292" y="87" text-anchor="end" class="cl">… read 0.75 mm from the wall</text><rect x="300" y="73" width="128.9" height="19" rx="4" fill="#d98a00"/><text x="434.9" y="88" class="cv">99</text><text x="292" y="117" text-anchor="end" class="cl">… read 1.5 mm from the wall</text><rect x="300" y="103" width="220.1" height="19" rx="4" fill="#25a361"/><text x="526.1" y="118" class="cv">169</text><text x="292" y="147" text-anchor="end" class="cl">1 mm particles, default settings</text><rect x="300" y="133" width="110.7" height="19" rx="4" fill="#c01f24"/><text x="416.7" y="148" class="cv">85</text><text x="292" y="177" text-anchor="end" class="cl">1 mm particles, Nusselt coefficient 0.745</text><rect x="300" y="163" width="250.0" height="19" rx="4" fill="#25a361"/><text x="556.0" y="178" class="cv">192</text><text x="292" y="207" text-anchor="end" class="cl">Heat-flux method, 0.5 mm particles</text><rect x="300" y="193" width="97.7" height="19" rx="4" fill="#c01f24"/><text x="403.7" y="208" class="cv">75</text><text x="292" y="237" text-anchor="end" class="cl">Heat-flux method, 0.25 mm particles</text><rect x="300" y="223" width="165.4" height="19" rx="4" fill="#d98a00"/><text x="471.4" y="238" class="cv">127</text><text x="292" y="267" text-anchor="end" class="cl">Ansys Fluent</text><rect x="300" y="253" width="234.4" height="19" rx="4" fill="#25a361"/><text x="540.4" y="268" class="cv">180</text><line x1="539.6" y1="4" x2="539.6" y2="298" stroke="#1a1a2e" stroke-dasharray="4 3" stroke-width="1.4"/></svg></div>
            <div class="finding"><span class="fn">3</span><div><h4>Concentric cylinders: defaults were enough</h4><p>Heat transfer here is governed by the vortex pattern, and published correlations each hold only in a parameter range. The vortices appeared <mark class="hl">with mostly default settings</mark> (watch the Courant limiter). Across four radius-ratio and speed cases Particleworks sits between −7 % and +28 % of the correlation, a spread comparable with Fluent (−8 % to +17 %).</p></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>A lucky trial in the field</h4><p>On a confidential customer case, a large oil system with spherical thrust bearings, SKF simply imported the power loss from its bearing software as a heat source and let Particleworks run. The temperature map was something the customer could relate to.</p></div></div>
            <blockquote class="pq"><p>“We never tried; we just pushed the button and saw what happens with default settings. [...] It worked. [...] Maybe we’re just being lucky in that occasion.”</p><div class="pqf">Fabrizio Mandrile <a href="../experience/proceedings2026.php?talk=06&amp;t=2700#talk-06"><i class="bi bi-play-fill"></i> 45:00 Watch the moment</a></div></blockquote>
            <figure class="slide"><img src="images/pwe2026/s06-20.jpg" alt="Integrating Particleworks into SKF Engineering Tools: Part I — slide" loading="lazy"><figcaption><b>Slide.</b> Single-sphere results: HTC fields for 0.25 mm and 1 mm particles and the numbers behind the chart (SKF).</figcaption></figure>
            <div class="keypoints"><h5>In short</h5><ul><li>Be conscious of what drives a discrepancy: mapping distance, Nusselt coefficient and refinement each moved the sphere HTC by a factor of two or more.</li><li>Next: a segmented bearing, ideally with a cyclic boundary condition (requested), then a full bearing with multi-layer refinement.</li><li>The honest message: the correlation is not truth either.</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=06&amp;t=904#talk-06"><i class="bi bi-play-fill"></i> 15:04 BEAST + Particleworks</a><a href="../experience/proceedings2026.php?talk=06&amp;t=1177#talk-06"><i class="bi bi-play-fill"></i> 19:37 The two verification models</a><a href="../experience/proceedings2026.php?talk=06&amp;t=1768#talk-06"><i class="bi bi-play-fill"></i> 29:28 HTC read at a distance</a><a href="../experience/proceedings2026.php?talk=06&amp;t=1861#talk-06"><i class="bi bi-play-fill"></i> 31:01 Defaults: 85 vs 184</a><a href="../experience/proceedings2026.php?talk=06&amp;t=2343#talk-06"><i class="bi bi-play-fill"></i> 39:03 Results and the limiter</a><a href="../experience/proceedings2026.php?talk=06&amp;t=2602#talk-06"><i class="bi bi-play-fill"></i> 43:22 Wish: cyclic boundary condition</a><a href="../experience/proceedings2026.php?talk=06&amp;t=2700#talk-06"><i class="bi bi-play-fill"></i> 45:00 The field case</a></div>

            <div class="talk-intro" id="talk-10"><img src="../experience/speakers/leonardo-tiberi.jpg" alt="Leonardo Tiberi"><div><div class="t-time">Heat · 16:30–17:00</div><h3>Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method</h3><div class="t-who">Leonardo Tiberi — TrackOne SRL – Unimore (IT)</div></div></div>
            <p class="standfirst">A sealed, partly filled oil bath that heats itself while it turns: TrackOne maps its temperatures in <mark class="hl">a day per case</mark>, and the bench test shows where the model can be trusted.</p>
            <div class="blk-label">The context</div>
            <p>The carrier roller holds up the track chain of an excavator. The chain forces the shell to rotate around a fixed shaft; seals, bushings and a partial oil fill keep metal from touching metal. Under load, the friction creates internal thermal peaks, and “if not controlled, the spikes lead to component failure”. The goal was a steady-state temperature map for a given operating case.</p>
            <p>Because the oil only partly fills the roller, it is thrown and fragmented against the walls as the shell turns. That, and the narrow passages in cover, bushing and shaft, is why TrackOne, with the Enzo Ferrari engineering department of Unimore, chose a meshless method.</p>
            <figure class="slide"><img src="images/pwe2026/s10-05.jpg" alt="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method — slide" loading="lazy"><figcaption><b>Slide.</b> The roller: shell and collars rotate with the chain, the shaft stays fixed to the chassis (TrackOne).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>Fluid and solid do not share a clock</h4><p>The oil reaches its pattern in milliseconds, the metal in hours, so a straight unsteady CHT is prohibitive. The answer is an iterative steady CHT with two phases: the <mark class="hl">oil alone</mark> produces average HTC and near-wall temperature maps (a few hours), then the <mark class="hl">solids alone</mark> are solved with those maps (a few minutes). The loop stops when the solid field no longer changes, after three to four iterations.</p></div></div>
            <blockquote class="pq"><p>“The temporal scale of the fluid was very different from the temporal scale of the solid. So we decided to use an iterative steady-state CHT.”</p><div class="pqf">Leonardo Tiberi <a href="../experience/proceedings2026.php?talk=10&amp;t=593#talk-10"><i class="bi bi-play-fill"></i> 9:53 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">2</span><div><h4>A real-life contact has to be re-written for a steady model</h4><p>The chain touches only the top of the roller shell. A steady run with that contact alone would give “an unrealistic and unbalanced temperature map”. TrackOne spreads the cooling over the whole circumference and corrects it with a scale factor τ (footprint area over contact area) and an equivalent thermal contact resistance.</p></div></div>
            <div class="finding"><span class="fn">3</span><div><h4>Good at one operating point, honest at the other</h4><p>On the bench, with sensors outside and a probe in the oil, case 1 shows good convergence with a slight underestimation of the roller shell and the oil (errors up to about 12 %). Case 2, at higher speed and lower load, is excellent: all errors below 7 %. About one day per case.</p></div></div>
            <blockquote class="pq"><p>“There is a good convergence between simulated and bench test temperature, with a slight underestimation of the roller shell and the internal oil temperature.”</p><div class="pqf">Leonardo Tiberi <a href="../experience/proceedings2026.php?talk=10&amp;t=850#talk-10"><i class="bi bi-play-fill"></i> 14:10 Watch the moment</a></div></blockquote>
            <div class="chart-card"><div class="chart-t">Error against the bench test, component by component</div><div class="chart-s">Simulated minus measured temperature, in % (TrackOne, slides 18–19).</div><svg viewBox="0 0 640 210" role="img" aria-label="Error against bench test" class="chart"><line x1="330" y1="8" x2="330" y2="188" stroke="#1a1a2e" stroke-width="1.2"/><text x="190" y="204" text-anchor="middle" class="cl" fill="#8a94a0">-10%</text><line x1="190" y1="8" x2="190" y2="188" stroke="#e5e9ee"/><text x="260" y="204" text-anchor="middle" class="cl" fill="#8a94a0">-5%</text><line x1="260" y1="8" x2="260" y2="188" stroke="#e5e9ee"/><text x="400" y="204" text-anchor="middle" class="cl" fill="#8a94a0">+5%</text><line x1="400" y1="8" x2="400" y2="188" stroke="#e5e9ee"/><text x="470" y="204" text-anchor="middle" class="cl" fill="#8a94a0">+10%</text><line x1="470" y1="8" x2="470" y2="188" stroke="#e5e9ee"/><text x="150" y="29" text-anchor="end" class="cl">Collar</text><rect x="303.4" y="12" width="26.6" height="11" rx="3" fill="#c01f24"/><text x="297.4" y="22" text-anchor="end" class="cv">-1.9%</text><rect x="264.6" y="25" width="65.4" height="11" rx="3" fill="#25a361"/><text x="258.6" y="35" text-anchor="end" class="cv">-4.7%</text><text x="150" y="63" text-anchor="end" class="cl">Cover</text><rect x="330.0" y="46" width="22.4" height="11" rx="3" fill="#c01f24"/><text x="358.4" y="56" text-anchor="start" class="cv">+1.6%</text><rect x="317.4" y="59" width="12.6" height="11" rx="3" fill="#25a361"/><text x="311.4" y="69" text-anchor="end" class="cv">-0.9%</text><text x="150" y="97" text-anchor="end" class="cl">Roller shell</text><rect x="330.0" y="80" width="147.4" height="11" rx="3" fill="#c01f24"/><text x="483.4" y="90" text-anchor="start" class="cv">+10.5%</text><rect x="330.0" y="93" width="50.1" height="11" rx="3" fill="#25a361"/><text x="386.1" y="103" text-anchor="start" class="cv">+3.6%</text><text x="150" y="131" text-anchor="end" class="cl">Shaft</text><rect x="330.0" y="114" width="46.6" height="11" rx="3" fill="#c01f24"/><text x="382.6" y="124" text-anchor="start" class="cv">+3.3%</text><rect x="330.0" y="127" width="43.7" height="11" rx="3" fill="#25a361"/><text x="379.7" y="137" text-anchor="start" class="cv">+3.1%</text><text x="150" y="165" text-anchor="end" class="cl">Oil</text><rect x="330.0" y="148" width="173.6" height="11" rx="3" fill="#c01f24"/><text x="509.6" y="158" text-anchor="start" class="cv">+12.4%</text><rect x="330.0" y="161" width="84.0" height="11" rx="3" fill="#25a361"/><text x="420.0" y="171" text-anchor="start" class="cv">+6.0%</text></svg><div class="chart-leg"><span><i style="background:#c01f24"></i>Case 1</span><span><i style="background:#25a361"></i>Case 2 (higher speed, lower load)</span></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>What is not resolved</h4><p>In the Q&A the numerics were questioned: the smallest gap, between shaft and bushing, is not resolved with particles. Next steps: oil rheology evolution, coupling with a FEM solver for deformation, and critical operating conditions.</p></div></div>
            <div class="pair"><figure class="slide"><img src="images/pwe2026/s10-18.jpg" alt="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method — slide" loading="lazy"><figcaption>Case 1: simulated against bench temperatures, with the percentage error per component (TrackOne).</figcaption></figure><figure class="slide"><img src="images/pwe2026/s10-19.jpg" alt="Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method — slide" loading="lazy"><figcaption>Case 2, higher speed and lower load: errors below 7 % (TrackOne).</figcaption></figure></div>
            <div class="eng-note"><b>Engineering note.</b> Air convection on exposed components uses an analytical law in the component velocity, <code>HTC<sub>air</sub> = 5.7 + 3.8&middot;v</code>; oil viscosity follows an Arrhenius–Vogel law with temperature.</div>
            <div class="keypoints"><h5>In short</h5><ul><li>Phase 1 (oil, hours) and phase 2 (solids, minutes) alternate until the solid field is stable.</li><li>Errors are reported component by component: up to about 12 % in case 1, below 7 % in case 2.</li><li>Next: rheology evolution, FEM coupling, critical conditions.</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=10&amp;t=304#talk-10"><i class="bi bi-play-fill"></i> 5:04 Why thermal peaks matter</a><a href="../experience/proceedings2026.php?talk=10&amp;t=466#talk-10"><i class="bi bi-play-fill"></i> 7:46 Viscosity follows temperature</a><a href="../experience/proceedings2026.php?talk=10&amp;t=593#talk-10"><i class="bi bi-play-fill"></i> 9:53 Why steady and iterative</a><a href="../experience/proceedings2026.php?talk=10&amp;t=638#talk-10"><i class="bi bi-play-fill"></i> 10:38 The contact trick</a><a href="../experience/proceedings2026.php?talk=10&amp;t=726#talk-10"><i class="bi bi-play-fill"></i> 12:06 Phase 1 / phase 2</a><a href="../experience/proceedings2026.php?talk=10&amp;t=850#talk-10"><i class="bi bi-play-fill"></i> 14:10 Results vs bench</a><a href="../experience/proceedings2026.php?talk=10&amp;t=919#talk-10"><i class="bi bi-play-fill"></i> 15:19 One day per case</a></div>


            <hr class="section-rule">

            <div class="sec-eyebrow">02 · Air</div>
            <h2>Measure it before you simulate it</h2>
            <p class="sec-lead">Aeration changes viscosity, density, film thickness and oxidation. The afternoon showed how to put a measured number on it before the model is asked to predict it.</p>
            <div class="talk-intro" id="talk-07"><img src="../experience/speakers/lukas-hafner.jpg" alt="Lukas Hafner"><div><div class="t-time">Air · 14:30–15:00</div><h3>Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems</h3><div class="t-who">Dr. Lukas Hafner — deepfluid (DE), with Gianluca Parma — EnginSoft</div></div></div>
            <p class="standfirst">Two oils with the same air content can behave very differently. <mark class="hl">The aeration model has to be calibrated on bubbles, not on a percentage.</mark></p>
            <div class="blk-label">The context</div>
            <p>Air in oil is a multi-scale problem: root causes and effects sit in different places and develop over time. A gas phase changes the density and viscosity of the oil, so efficiency drops; it brings cavitation and NVH problems; it exposes the oil to thermal and chemical stress, with oxidation in the long run; and it makes the lubricant film unreliable where the gear needs it. Particleworks has an aeration module that predicts generation, transport, coalescence and disappearance of bubbles.</p>
            <p>What was available until now was a single number, the air content. deepfluid’s optical sensors, in the laboratory, on the test bench and in the field, take snapshots of every bubble and give the bubble count, the size distribution, the mean diameter and the <mark class="hl">oil–air contact surface</mark>, with the snapshot as evidence.</p>
            <figure class="slide"><img src="images/pwe2026/s07-06.jpg" alt="Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems — slide" loading="lazy"><figcaption><b>Slide.</b> Same air content, 0.65 %, two very different bubble populations (deepfluid).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>0.65 % of air is not one situation</h4><p>In scenario A, 361 bubbles of 132 µm offer 18 m² of oil–air surface. In scenario B, 1,289 bubbles of 68 µm offer <mark class="hl">32 m²</mark> for the same volume of air. The surface is where oxidation happens, so oil aging, cavitation and compressibility differ although the percentage is identical.</p></div></div>
            <blockquote class="pq"><p>“Those 0.65 percent of air content can look very different: pretty big bubbles with a wide deviation in sizes, or very, very small bubbles all the time. And this changes your system behavior pretty much.”</p><div class="pqf">Dr. Lukas Hafner <a href="../experience/proceedings2026.php?talk=07&amp;t=325#talk-07"><i class="bi bi-play-fill"></i> 5:25 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">2</span><div><h4>Measure, calibrate, then simulate</h4><p>The aeration model has many coefficients, and two things are calibrated: the total amount of air generated and the bubble-size distribution. Simulation then gives the global picture (flow paths, recirculation, aeration hot spots) while the sensor supplies the local truth: “measured data does not replace the simulation”.</p></div></div>
            <div class="finding"><span class="fn">3</span><div><h4>A differential gear, before and after</h4><p>In a differential gear in a pool of oil, the default coefficients gave <mark class="hl">0.12 % air with 800 µm bubbles</mark>. After calibration on the measurement: 0.45 % against 0.43 % measured, and 186 µm bubbles against 180 µm. The bubble motion and the recirculation under the gear are visibly better captured.</p></div></div>
            <div class="chart-two"><div class="chart-card"><div class="chart-t">Air content in the gearbox</div><div class="chart-s">Percent of oil volume.</div><svg viewBox="0 0 640 126" role="img" aria-label="Air content in the gearbox" class="chart"><text x="292" y="27" text-anchor="end" class="cl">Before calibration</text><rect x="300" y="13" width="61.1" height="19" rx="4" fill="#c01f24"/><text x="367.1" y="28" class="cv">0.12 %</text><text x="292" y="57" text-anchor="end" class="cl">After calibration</text><rect x="300" y="43" width="229.1" height="19" rx="4" fill="#25a361"/><text x="535.1" y="58" class="cv">0.45 %</text><text x="292" y="87" text-anchor="end" class="cl">Measured</text><rect x="300" y="73" width="218.9" height="19" rx="4" fill="#1a1a2e"/><text x="524.9" y="88" class="cv">0.43 %</text></svg></div><div class="chart-card"><div class="chart-t">Average bubble diameter</div><div class="chart-s">Micrometres.</div><svg viewBox="0 0 640 126" role="img" aria-label="Average bubble diameter" class="chart"><text x="292" y="27" text-anchor="end" class="cl">Before calibration</text><rect x="300" y="13" width="248.9" height="19" rx="4" fill="#c01f24"/><text x="554.9" y="28" class="cv">800 µm</text><text x="292" y="57" text-anchor="end" class="cl">After calibration</text><rect x="300" y="43" width="57.9" height="19" rx="4" fill="#25a361"/><text x="363.9" y="58" class="cv">186 µm</text><text x="292" y="87" text-anchor="end" class="cl">Measured</text><rect x="300" y="73" width="56.0" height="19" rx="4" fill="#1a1a2e"/><text x="362.0" y="88" class="cv">180 µm</text></svg></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>How far does a calibration travel?</h4><p>Geometry: no problem. Speed: coefficients scale with the velocity ratio from a calibrated reference. Additive package: no, because Particleworks does not solve chemistry; a new additive or anti-foam means a new calibration. Temperature: an open point, and the trend can even change sign from oil to oil.</p></div></div>
            <blockquote class="pq"><p>“For one and the same base oil with different additive packages, you can have an increase in air content with an increase in temperature. But with the other one, you get a decrease in air content with an increase in temperature.”</p><div class="pqf">Dr. Lukas Hafner <a href="../experience/proceedings2026.php?talk=07&amp;t=1462#talk-07"><i class="bi bi-play-fill"></i> 24:22 Watch the moment</a></div></blockquote>
            <figure class="slide"><img src="images/pwe2026/s07-19.jpg" alt="Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems — slide" loading="lazy"><figcaption><b>Slide.</b> Quantitative comparison: air content and bubble-size distribution against the measurement, before and after calibration (deepfluid).</figcaption></figure>
            <div class="keypoints"><h5>In short</h5><ul><li>Calibrate two things: total air generated and bubble-size distribution.</li><li>Scale with speed from a reference; recalibrate for a new additive package; temperature scaling is open.</li><li>The sensor complements the simulation: local truth against a global view.</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=07&amp;t=325#talk-07"><i class="bi bi-play-fill"></i> 5:25 Same air, different bubbles</a><a href="../experience/proceedings2026.php?talk=07&amp;t=732#talk-07"><i class="bi bi-play-fill"></i> 12:12 Calibrating the model</a><a href="../experience/proceedings2026.php?talk=07&amp;t=858#talk-07"><i class="bi bi-play-fill"></i> 14:18 The differential gear</a><a href="../experience/proceedings2026.php?talk=07&amp;t=1138#talk-07"><i class="bi bi-play-fill"></i> 18:58 Before vs after calibration</a><a href="../experience/proceedings2026.php?talk=07&amp;t=1316#talk-07"><i class="bi bi-play-fill"></i> 21:56 Q&A: new additive, new calibration</a><a href="../experience/proceedings2026.php?talk=07&amp;t=1462#talk-07"><i class="bi bi-play-fill"></i> 24:22 Additives and temperature</a></div>


            <hr class="section-rule">

            <div class="sec-eyebrow">03 · Wear</div>
            <h2>Simulating what breaks</h2>
            <p class="sec-lead">Two very different machines, one question: can a particle simulation say where, and how fast, the hardware will wear?</p>
            <div class="talk-intro" id="talk-05"><img src="../experience/speakers/jean-decaix.jpg" alt="Jean Decaix"><div><div class="t-time">Wear · 12:15–12:45</div><h3>Moving Particle Simulation of Eroded Pelton Runners</h3><div class="t-who">Jean Decaix — HES-SO Valais/Wallis (CH)</div></div></div>
            <p class="standfirst">Europe’s hydropower is ageing and silting up. HES-SO uses Particleworks to put a number on what <mark class="hl">sediment erosion costs a Pelton runner in torque</mark>.</p>
            <div class="blk-label">The context</div>
            <p>ReHydro is a Horizon Europe project of 18 partners, coordinated by SINTEF, to refurbish and modernise European hydropower. The fleet is about 50 to 55 years old and now has to balance solar and wind, and as glaciers retreat more sediment reaches the turbines. In the worst plants, after a year of operation a Pelton runner can “lose maybe half a bucket”.</p>
            <p>A Pelton turbine is an impulse turbine: a water jet hits the buckets and the torque on the shaft is the power. The physics is simple and the machines are huge, so they cannot be tested in a laboratory. Measuring the efficiency of a real runner means stopping production for two or three days, which is why a prediction of the efficiency lost to erosion is worth having.</p>
            <figure class="slide"><img src="images/pwe2026/s05-04.jpg" alt="Moving Particle Simulation of Eroded Pelton Runners — slide" loading="lazy"><figcaption><b>Slide.</b> Sediment and cavitation erosion in hydraulic turbines: from Francis runners to Pelton buckets (HES-SO).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>Whole revolutions, not fragments</h4><p>With Particleworks HES-SO can simulate <mark class="hl">more than one revolution</mark> of the runner on a single GPU, where a finite-volume code takes “more than one week”. After four years of use that changed what is feasible: several simulations, not one.</p></div></div>
            <blockquote class="pq"><p>“One of the power plants on which we are working in this project, you have the equivalent of a cargo train every year full of sediment that goes through the turbines.”</p><div class="pqf">Jean Decaix <a href="../experience/proceedings2026.php?talk=05&amp;t=278#talk-05"><i class="bi bi-play-fill"></i> 4:38 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">2</span><div><h4>Torque converges, and can be extrapolated</h4><p>For a healthy runner the dimensionless torque rises toward the target as the particles shrink, and a linear extrapolation to zero particle size lands close to it. That means a fast, coarse run can be used to estimate what a very fine one would give.</p></div></div>
            <div class="finding"><span class="fn">3</span><div><h4>Artificial erosion follows the known trends</h4><p>Flat, rounded and cut-out erosion reproduce the analytical and published efficiency drops, more closely with finer particles. A rounded erosion collapses onto a laboratory experiment on <mark class="hl">another turbine at another scale</mark>, which hints that the effect may not depend on runner size. The worn splitter tip is the exception: the particles are as large as the eroded layer.</p></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>Real erosion: the loss comes early</h4><p>Three real runners were computed: new, after three years, after five (when the owner refurbished). The torque decrease is predicted accurately, and <mark class="hl">mid-life is already close to end-of-life</mark>: torque drops of 6 % and 6.6 % for the mid-life and end-of-life runners, “we have already lost the main part of efficiency even at stage T2”.</p></div></div>
            <blockquote class="pq"><p>“It could be one flood event that can make this high level of erosion. So after one flood event, we lost 2%. It’s not a progressive phenomenon.”</p><div class="pqf">Jean Decaix <a href="../experience/proceedings2026.php?talk=05&amp;t=1339#talk-05"><i class="bi bi-play-fill"></i> 22:19 Watch the moment</a></div></blockquote>
            <figure class="slide"><img src="images/pwe2026/s05-15.jpg" alt="Moving Particle Simulation of Eroded Pelton Runners — slide" loading="lazy"><figcaption><b>Slide.</b> Dimensionless torque of the three physically eroded runners, T-3 new to T-1 after five years, with the extrapolation to zero particle size (HES-SO).</figcaption></figure>
            <div class="keypoints"><h5>In short</h5><ul><li>Torque loss is predicted, which lets an owner decide whether to refurbish in February or November.</li><li>Next: partial load, where the drop should be larger, then a runner whose speed responds to load rejection.</li><li>A brick of a digital twin: what does 2 % of efficiency lost to one flood cost over a year?</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=05&amp;t=70#talk-05"><i class="bi bi-play-fill"></i> 1:10 ReHydro: why erosion matters</a><a href="../experience/proceedings2026.php?talk=05&amp;t=252#talk-05"><i class="bi bi-play-fill"></i> 4:12 Half a bucket in a year</a><a href="../experience/proceedings2026.php?talk=05&amp;t=278#talk-05"><i class="bi bi-play-fill"></i> 4:38 A cargo train of sediment</a><a href="../experience/proceedings2026.php?talk=05&amp;t=417#talk-05"><i class="bi bi-play-fill"></i> 6:57 Revolutions in days, not weeks</a><a href="../experience/proceedings2026.php?talk=05&amp;t=549#talk-05"><i class="bi bi-play-fill"></i> 9:09 Extrapolating to zero size</a><a href="../experience/proceedings2026.php?talk=05&amp;t=689#talk-05"><i class="bi bi-play-fill"></i> 11:29 New, 3 years, 5 years</a><a href="../experience/proceedings2026.php?talk=05&amp;t=1012#talk-05"><i class="bi bi-play-fill"></i> 16:52 Mid-life is already end-of-life</a><a href="../experience/proceedings2026.php?talk=05&amp;t=1196#talk-05"><i class="bi bi-play-fill"></i> 19:56 Q&A: load rejection, digital twin</a></div>

            <div class="talk-intro" id="talk-11"><img src="../experience/speakers/bernd-valtwies.jpg" alt="Bernd Valtwies"><div><div class="t-time">Wear · 17:00–17:30</div><h3>Simulation of Sand Separation and Wear in the Börger FlowSep</h3><div class="t-who">Bernd Valtwies — Börger GmbH (DE) &amp; Riccardo Sala — EnginSoft (IT)</div></div></div>
            <p class="standfirst">A sand separator for biogas plants, simulated before its second prototype: the model showed where the sand escapes, why <mark class="hl">more flow is worse</mark>, and where the housing wears.</p>
            <div class="blk-label">The context</div>
            <p>Biogas plants used to be fed with energy crops, a clean medium. Today they run on manure, and with it come sand, stones and soil. In the example shown, 1.9 m of sand settled in 36 months in a 16 m tank: about 1,000 tons. It blocks pipes, defeats the mixers, shrinks the usable volume, blocks the slurry tankers, and is expensive special waste to dig out.</p>
            <p>Börger’s BioSelect separator already removes fibres larger than 0.5 mm. The new FlowSep adds centrifugal forces to remove the sand below that size before the final tank. The first mock-up worked immediately; the open questions for the prototype were the geometry, the throughput that still gives an acceptable result, and where the machine wears. EnginSoft built a Particleworks and Granuleworks model, with Börger measuring flows, densities, ash content (burnt at 800 °C) and particle fractions.</p>
            <figure class="slide"><img src="images/pwe2026/s11-05.jpg" alt="Simulation of Sand Separation and Wear in the Börger FlowSep — slide" loading="lazy"><figcaption><b>Slide.</b> The problem: sand in the final storage tank of a biogas plant, 1.9 m after 36 months (Börger).</figcaption></figure>
            <div class="blk-label">What they found</div>
            <div class="finding"><span class="fn">1</span><div><h4>Where the sand escapes</h4><p>About 10 % of the sand leaves through the clean outlet, close to what the tests showed, and <mark class="hl">only the small particles</mark>: large ones are centrifuged outward, as intended. The model shows the path: particles pushed onto the back plate recirculate, and where two opposed fluxes meet a particle that drifts slightly is sucked out with the water. That points straight at a geometry change.</p></div></div>
            <blockquote class="pq"><p>“In a timeline of 36 months, they have had an average of 1.9 meters height of sand. [...] In a container with a diameter of 16 meters, we are talking about 1,000 tons of sand.”</p><div class="pqf">Bernd Valtwies <a href="../experience/proceedings2026.php?talk=11&amp;t=353#talk-11"><i class="bi bi-play-fill"></i> 5:53 Watch the moment</a></div></blockquote>
            <div class="finding"><span class="fn">2</span><div><h4>More flow, less separation</h4><p>Börger’s first idea was to raise the flow rate. At twice the flow the sand not separated grows from about <mark class="hl">10 % to about 25 %</mark>, with more of the coarse fraction reaching the clean phase. “It’s better to go slower and separate better”, or change the geometry: radius, length, motor size.</p></div></div>
            <blockquote class="pq"><p>“At the beginning, the idea of Börger was: let’s just increase the flow rate, we will be faster, everything will be good. But then, with this simulation, we realized that it’s not possible. It’s better to go slower and separate better.”</p><div class="pqf">Riccardo Sala <a href="../experience/proceedings2026.php?talk=11&amp;t=1544#talk-11"><i class="bi bi-play-fill"></i> 25:44 Watch the moment</a></div></blockquote>
            <div class="chart-card"><div class="chart-t">Sand that leaves through the clean outlet</div><div class="chart-s">Percent of the sand fed, from the simulation (Börger / EnginSoft).</div><svg viewBox="0 0 640 96" role="img" aria-label="Sand that leaves through the clean outlet" class="chart"><text x="292" y="27" text-anchor="end" class="cl">Low flow rate</text><rect x="300" y="13" width="93.3" height="19" rx="4" fill="#25a361"/><text x="399.3" y="28" class="cv">10 %</text><text x="292" y="57" text-anchor="end" class="cl">High flow rate (×2)</text><rect x="300" y="43" width="233.3" height="19" rx="4" fill="#c01f24"/><text x="539.3" y="58" class="cv">25 %</text></svg></div>
            <div class="finding"><span class="fn">3</span><div><h4>Where the housing wears</h4><p>Wall interaction was read from the particle number density within 1 mm of the wall together with velocity. It flags the area near the blades and the back plate, and the prototype, after about half a year of round-the-clock operation, showed strong erosion exactly there. With version 9 the force on the wall is the more direct indicator.</p></div></div>
            <div class="finding"><span class="fn">4</span><div><h4>Fewer prototypes</h4><p>Each prototype costs a lot, and the simulation says early which change makes sense, widening the radius or lengthening the unit, before steel is cut.</p></div></div>
            <div class="pair"><figure class="slide"><img src="images/pwe2026/s11-27.jpg" alt="Simulation of Sand Separation and Wear in the Börger FlowSep — slide" loading="lazy"><figcaption>Simulation: high sand interaction at the housing near the blades and at the back plate (Börger, EnginSoft).</figcaption></figure><figure class="slide"><img src="images/pwe2026/s11-30.jpg" alt="Simulation of Sand Separation and Wear in the Börger FlowSep — slide" loading="lazy"><figcaption>The prototype housing: “the wear pattern corresponds to simulation” (Börger).</figcaption></figure></div>
            <div class="keypoints"><h5>In short</h5><ul><li>Of the sand that escapes, the small particles are the problem; the geometry can be changed to catch them.</li><li>Higher flow rate: bad separation 10 % → 25 %.</li><li>Simulated wear zones match the prototype: blades and back plate.</li></ul></div>
            <div class="moments-blog"><span class="lbl">Watch the moment</span><a href="../experience/proceedings2026.php?talk=11&amp;t=330#talk-11"><i class="bi bi-play-fill"></i> 5:30 The sand problem</a><a href="../experience/proceedings2026.php?talk=11&amp;t=353#talk-11"><i class="bi bi-play-fill"></i> 5:53 1.9 m of sand</a><a href="../experience/proceedings2026.php?talk=11&amp;t=619#talk-11"><i class="bi bi-play-fill"></i> 10:19 How the FlowSep works</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1364#talk-11"><i class="bi bi-play-fill"></i> 22:44 Who leaks</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1495#talk-11"><i class="bi bi-play-fill"></i> 24:55 Higher flow rate</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1544#talk-11"><i class="bi bi-play-fill"></i> 25:44 Faster is not better</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1601#talk-11"><i class="bi bi-play-fill"></i> 26:41 The wear map</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1661#talk-11"><i class="bi bi-play-fill"></i> 27:41 Prototype wear</a><a href="../experience/proceedings2026.php?talk=11&amp;t=1811#talk-11"><i class="bi bi-play-fill"></i> 30:11 With 9.0: wall force</a></div>

            <hr class="section-rule">

            <div class="sec-eyebrow">From the floor</div>
            <h2>The questions that mattered</h2>
            <div class="qa"><b>How many manual iterations does the pump model take?</b><span>Three to five, and a steady CHT converges in minutes on a GPU. “Sometimes the setup is longer than the simulation itself.” (R&amp;D CFD)</span></div><div class="qa"><b>Does an aeration calibration transfer?</b><span>Across geometry yes, across speed by scaling, across additives no: the same base oil with another additive package needs a new one, and the temperature trend can flip sign. (deepfluid)</span></div><div class="qa"><b>Why start from such basic verification cases?</b><span>Because once a bearing rotates there is no good reference model; complexity is added step by step. (SKF)</span></div><div class="qa"><b>What do owners want from a Pelton simulation?</b><span>Not newtons: what 2&nbsp;% of efficiency lost to one flood costs over a year, and when to refurbish. (HES-SO)</span></div>

            <hr class="section-rule">

            <div class="sec-eyebrow">Take-home</div>
            <h2>What we take home</h2>

            <div class="keypoints"><h5>Four things the day showed</h5><ul>
              <li><strong>Heat became a deliverable.</strong> Three talks closed thermal models with a fast steady CHT: minutes to a day per case, and every gap against the bench stated (about 5–6 °C worst on the pump, up to about 12 % on the roller oil).</li><li><strong>Where you read the number matters.</strong> On one sphere the same code returned an HTC of 66 or 169 W/m²K depending on where it was sampled; one air content (0.65 %) hid bubbles of 132 µm or 68 µm.</li><li><strong>Calibrate on what is measured.</strong> Optical bubble data took a gearbox aeration model from 0.12 % to 0.45 % air against a measured 0.43 %, and from 800 to 186 µm bubbles against 180 µm.</li><li><strong>Simulation says where it wears — and what not to do.</strong> Pelton torque loss and the wear zones of a separator housing were predicted; doubling the separator flow rate, the obvious fix, lifted the sand lost from 10 % to 25 %.</li>
            </ul></div>

            <p>Meshless CFD in Modena looked less like a promise and more like a tool with a known price, and with speakers who were exact about it.</p>

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