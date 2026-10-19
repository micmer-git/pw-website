<?php
// Proceedings 2026 — form-gated.  No secrets / no talk content in this file (public repo):
// everything private lives in proceedings2026-private.php, uploaded by FTP only (see the .sample.php).
// Gate: the MachForm "redirect after submit" URL is  proceedings2026.php?access=<access_token>.
$cfg = is_file(__DIR__ . '/proceedings2026-private.php') ? require __DIR__ . '/proceedings2026-private.php' : null;
function e($s) { return htmlspecialchars((string)$s, ENT_QUOTES, 'UTF-8'); }
$COOKIE = 'pwe26_proc';
$authed = false;
if ($cfg) {
    $good = hash_hmac('sha256', 'pwe26-proceedings', $cfg['secret']);
    $secure = !empty($_SERVER['HTTPS']);
    if (isset($_GET['access']) && hash_equals($cfg['access_token'], (string)$_GET['access'])) {
        if (!isset($_GET['go'])) {                       // we may be inside the MachForm iframe: bounce the TOP window to us
            header('Cache-Control: no-store'); header('X-Robots-Tag: noindex, nofollow');
            $u = 'proceedings2026.php?access=' . rawurlencode($_GET['access']) . '&go=1';
            echo '<!doctype html><meta charset="utf-8"><title>Thank you</title><script>try{top.location.replace(' . json_encode($u) . ')}catch(x){location.replace(' . json_encode($u) . ')}</script><p style="font-family:sans-serif">Thank you! <a href="' . e($u) . '" target="_top">Open the proceedings</a></p>';
            exit;
        }
        setcookie($COOKIE, $good, ['expires' => time() + 60 * 60 * 24 * 90, 'path' => '/', 'secure' => $secure, 'httponly' => true, 'samesite' => 'Lax']);
        header('Location: proceedings2026.php'); exit;
    }
    $authed = isset($_COOKIE[$COOKIE]) && hash_equals($good, (string)$_COOKIE[$COOKIE]);
    if ($authed && isset($_GET['dl'])) {                 // authenticated PDF download — files sit in a Deny-all folder
        foreach ($cfg['talks'] as $t) {
            if ((empty($t['publish_from']) || date('Y-m-d') >= $t['publish_from']) && $t['id'] === $_GET['dl'] && !empty($t['pdf'])) {
                $f = __DIR__ . '/proceedings2026-files/' . basename($t['pdf']);
                if (is_file($f)) {
                    header('Content-Type: application/pdf'); header('Content-Length: ' . filesize($f));
                    header('Content-Disposition: attachment; filename="' . basename($f) . '"'); header('X-Robots-Tag: noindex, nofollow');
                    readfile($f); exit;
                }
            }
        }
        http_response_code(404); exit('File not found.');
    }
}
header('X-Robots-Tag: noindex, nofollow'); header('Cache-Control: private, no-cache');
// talks with a publish_from date stay hidden until that day (server date)
$talks = [];
if ($cfg) foreach ($cfg['talks'] as $t) { if (empty($t['publish_from']) || date('Y-m-d') >= $t['publish_from']) $talks[] = $t; }
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta name="robots" content="noindex,nofollow">
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="icon" type="image/png" href="../favicon.ico">
  <title>Proceedings — Particleworks Experience 2026 | Modena, October 7</title>
  <meta name="description" content="Presentations and key findings from Particleworks Experience 2026, Modena. Free access after a short form.">
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
    .reg-hero { position:relative; padding:8.5rem 0 4rem; background:linear-gradient(135deg, rgba(217,80,63,0.85), rgba(143,22,27,0.93)), url('../images/experience2026/theme-bg.jpg') center/cover no-repeat; overflow:hidden; }
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
  
    /* ---- proceedings 2026 ---- */
    .pr-hero { position:relative; padding:8.5rem 0 4rem; background:linear-gradient(135deg, rgba(217,80,63,0.85), rgba(143,22,27,0.93)), url('img/theme-bg.jpg') center/cover no-repeat; overflow:hidden; }
    .pr-hero .container { position:relative; z-index:3; }
    .pr-hero h1 { font-size:clamp(2.2rem,5.2vw,3.6rem); font-weight:900; color:#fff; letter-spacing:-1px; line-height:1.08; }
    .pr-hero h1 .accent { background:linear-gradient(120deg,#fff,#ffd9c2); -webkit-background-clip:text; background-clip:text; -webkit-text-fill-color:transparent; }
    .pr-hero .lead { font-size:1.15rem; color:rgba(255,255,255,0.85); max-width:640px; line-height:1.7; margin-top:1.2rem; }
    .pr-eyebrow { display:inline-flex; align-items:center; gap:0.5rem; background:rgba(255,255,255,0.14); border:1px solid rgba(255,255,255,0.32); color:#ffe6dd; padding:0.4rem 1rem; border-radius:50px; font-size:0.78rem; font-weight:700; letter-spacing:1.5px; text-transform:uppercase; margin-bottom:1.2rem; }
    .pr-facts { display:flex; flex-wrap:wrap; gap:0.7rem; margin-top:2rem; }
    .pr-fact { display:inline-flex; align-items:center; gap:0.5rem; background:rgba(255,255,255,0.10); border:1px solid rgba(255,255,255,0.20); color:#fff5f1; padding:0.55rem 1.05rem; border-radius:50px; font-size:0.9rem; font-weight:500; }
    .pr-fact i { color:#ffd9c2; }
    .pr-section { padding:3.5rem 0 4.5rem; background:linear-gradient(180deg,#fff,#f6fafd); }
    .pr-h2 { font-size:1.7rem; font-weight:800; letter-spacing:-0.5px; margin-bottom:0.4rem; }
    .pr-sub { color:var(--pw-gray); margin-bottom:2rem; max-width:720px; }
    .take-grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(250px,1fr)); gap:1rem; margin-bottom:3rem; }
    .take { background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:18px; padding:1.3rem 1.4rem; }
    .take .n { width:34px; height:34px; border-radius:10px; background:var(--ev-accent); color:#fff; display:flex; align-items:center; justify-content:center; font-weight:800; margin-bottom:0.8rem; }
    .take b { display:block; margin-bottom:0.3rem; }
    .take p { margin:0; font-size:0.9rem; color:#445; line-height:1.55; }
    .talk { background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:22px; box-shadow:0 14px 40px rgba(7,40,70,0.06); margin-bottom:1.6rem; overflow:hidden; }
    .talk-top { display:flex; gap:1.1rem; align-items:center; padding:1.4rem 1.6rem; background:linear-gradient(135deg,#fff6f3,#fdeeec); border-bottom:1px solid rgba(0,0,0,0.06); }
    .talk-top img { width:72px; height:72px; border-radius:50%; object-fit:cover; border:3px solid #fff; box-shadow:0 4px 14px rgba(143,22,27,0.18); flex-shrink:0; }
    .talk-time { font-size:0.78rem; font-weight:700; letter-spacing:1.2px; text-transform:uppercase; color:var(--ev-crimson); }
    .talk-top h3 { font-size:1.12rem; font-weight:800; letter-spacing:-0.2px; margin:0.15rem 0; line-height:1.3; }
    .talk-who { font-size:0.88rem; color:var(--pw-gray); }
    .talk-body { display:grid; grid-template-columns:minmax(0,1fr) minmax(0,1.15fr); gap:0; }
    @media(max-width:860px){ .talk-body { grid-template-columns:1fr; } }
    .talk-find { padding:1.4rem 1.6rem; }
    .talk-find h4 { font-size:0.78rem; font-weight:800; letter-spacing:1.3px; text-transform:uppercase; color:var(--pw-gray); margin-bottom:0.7rem; }
    .talk-find ul { padding-left:1.1rem; margin:0; }
    .talk-find li { font-size:0.93rem; line-height:1.55; color:#334; margin-bottom:0.5rem; }
    .talk-find li::marker { color:var(--ev-crimson); }
    .talk-media { padding:1.4rem 1.6rem; border-left:1px solid rgba(0,0,0,0.06); display:flex; flex-direction:column; gap:0.9rem; }
    @media(max-width:860px){ .talk-media { border-left:0; border-top:1px solid rgba(0,0,0,0.06); } }
    .vid { position:relative; aspect-ratio:16/9; border-radius:14px; overflow:hidden; background:#11111e; }
    .vid iframe, .vid button, .vid video { position:absolute; inset:0; width:100%; height:100%; border:0; }
    .vid video { object-fit:contain; background:#000; }
    .vid button { background-size:cover; background-position:center; cursor:pointer; padding:0; }
    .vid button::after { content:'\25B6'; position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:62px; height:62px; line-height:62px; border-radius:50%; background:var(--ev-accent); color:#fff; font-size:1.4rem; padding-left:4px; box-shadow:0 8px 24px rgba(0,0,0,0.35); }
    .vid.soon { display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.6); font-size:0.9rem; gap:0.5rem; }
    .moments { display:flex; flex-wrap:wrap; gap:0.4rem; align-items:center; }
    .moments span { font-size:0.72rem; font-weight:800; letter-spacing:1.2px; text-transform:uppercase; color:var(--pw-gray); margin-right:0.2rem; }
    .moments button { border:1px solid rgba(192,31,36,0.3); background:#fff; color:var(--ev-crimson); border-radius:50px; padding:0.25rem 0.7rem 0.25rem 0.45rem; font-size:0.78rem; font-weight:600; cursor:pointer; }
    .moments button:hover { background:var(--ev-crimson); color:#fff; }
    .moments button i { font-size:0.9rem; vertical-align:-1px; }
    .btn-red { background:var(--ev-accent); color:#fff; border:0; padding:0.6rem 1.3rem; border-radius:50px; font-weight:600; font-size:0.9rem; display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; box-shadow:0 6px 18px rgba(181,30,35,0.25); }
    .btn-red:hover { color:#fff; filter:brightness(1.08); }
    .btn-soft { color:var(--pw-gray); font-size:0.88rem; }
    .blog-card { display:flex; gap:1.2rem; align-items:center; background:var(--ev-gradient); color:#fff; border-radius:22px; padding:1.6rem 1.9rem; margin-top:2.4rem; text-decoration:none; }
    .blog-card:hover { color:#fff; filter:brightness(1.06); }
    .blog-card i { font-size:2rem; }
    .blog-card b { font-size:1.15rem; display:block; }
    .blog-card span { opacity:.85; font-size:0.92rem; }

    .open-talk { display:flex; gap:1.2rem; background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:18px; padding:1.3rem 1.5rem; margin-bottom:1rem; }
    .open-talk img { width:84px; height:84px; border-radius:50%; object-fit:cover; flex-shrink:0; border:3px solid #fff; box-shadow:0 4px 14px rgba(143,22,27,0.18); }
    .ot-who { font-size:0.8rem; font-weight:700; letter-spacing:0.4px; text-transform:uppercase; color:var(--pw-gray); }
    .open-talk h3 { font-size:1.08rem; font-weight:800; color:var(--ev-crimson); margin:0.2rem 0 0.5rem; line-height:1.3; }
    .open-talk p { font-size:0.9rem; line-height:1.6; margin:0 0 0.45rem; color:#334; }
    .open-talk .ot-hook { background:#f3faf6; border-left:3px solid #25a361; padding:0.5rem 0.8rem; border-radius:0 8px 8px 0; }
    .open-talk .ot-hook i { color:#25a361; }
    @media(max-width:600px){ .open-talk { flex-direction:column; } }
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
          <li class="nav-item"><a class="nav-link" href="index.php">Experience 2026</a></li>
          <li class="nav-item"><a class="nav-link" href="workshop.php">Oct 6 · Technical Session</a></li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Past editions</a>
            <ul class="dropdown-menu dropdown-menu-end">
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2025.php"><i class="bi bi-calendar3"></i> Proceedings 2025</a></li>
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2024.php"><i class="bi bi-calendar3"></i> Proceedings 2024</a></li>
              <li><a class="dropdown-item" href="https://particleworks-europe.com/experience/proceedings2023.php"><i class="bi bi-calendar3"></i> Proceedings 2023</a></li>
            </ul>
          </li>
          <li class="nav-item"><a class="nav-link" href="https://particleworks-europe.com/experience/contact.php">Contact</a></li>
          <li class="nav-item ms-lg-2"><a class="nav-link nav-register active" href="proceedings2026.php">Proceedings 2026</a></li>
        </ul>
      </div>
    </div>
  </nav>

  

  <?php if (!$authed): ?>
  <section class="pr-hero">
    <div class="container">
      <div class="pr-eyebrow"><i class="bi bi-lock"></i> Proceedings 2026</div>
      <h1>Take the <span class="accent">Modena</span> talks home.</h1>
      <p class="lead">Slides and key findings of Particleworks Experience 2026 — every talk the speakers released for sharing. Leave your details once and the whole collection opens.</p>
      <div class="pr-facts">
        <span class="pr-fact"><i class="bi bi-calendar-event"></i> October 7, 2026</span>
        <span class="pr-fact"><i class="bi bi-geo-alt"></i> BPER FORUM Monzani, Modena (IT)</span>
        <span class="pr-fact"><i class="bi bi-gift"></i> Free access</span>
      </div>
    </div>
  </section>
  <section class="reg-section" id="form">
    <div class="container">
      <div class="row g-4 justify-content-center">
        <div class="col-lg-8">
          <div class="reg-card">
            <div class="reg-card-head">
              <div class="ic"><i class="bi bi-unlock"></i></div>
              <div><h2>Unlock the proceedings</h2><p>Fill in your details — you'll land on the proceedings straight after.</p></div>
            </div>
            <?php if ($cfg && !empty($cfg['machform_url'])): ?>
            <div class="reg-embed-wrap">
              <iframe id="reg-form" class="reg-embed" style="min-height:760px" src="<?= e($cfg['machform_url']) ?>" title="Proceedings 2026 access form" loading="lazy" scrolling="yes"></iframe>
            </div>
            <div class="reg-fallback">Trouble loading the form? <a href="<?= e($cfg['machform_url']) ?>" target="_blank" rel="noopener">Open it in a new tab <i class="bi bi-box-arrow-up-right"></i></a></div>
            <?php else: ?>
            <div class="reg-fallback" style="border:0;padding:2.5rem 1.5rem">The proceedings are being prepared. Write to <a href="mailto:info@particleworks-europe.com">info@particleworks-europe.com</a> and we will send them to you.</div>
            <?php endif; ?>
          </div>
        </div>
        <div class="col-lg-4">
          <div class="aside-card">
            <h3>What you get</h3>
            <ul class="aside-list">
              <li><i class="bi bi-file-earmark-pdf"></i><span><b>The slides</b>PDF of each talk released by its speaker.</span></li>
              <li><i class="bi bi-lightbulb"></i><span><b>Key findings</b>A short summary of what each talk showed.</span></li>
              <li><i class="bi bi-shield-check"></i><span><b>Your data</b>Processed in line with GDPR, solely to share the proceedings and follow up on them.</span></li>
            </ul>
            <div class="d-flex flex-wrap gap-2 mt-3"><a href="../blog/pw-experience-2026.php" class="btn-ghost-red"><i class="bi bi-journal-text"></i> Read the story of the day</a></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="pr-section pr-open" id="talks">
    <div class="container">
      <h2 class="pr-h2">The talks</h2>
      <p class="pr-sub">What was presented in Modena on October 7, 2026. Slides, recordings and the key findings of every released talk open with the form above.</p>
      <div class="open-talk"><img src="speakers/leonardo-lanciotti.jpg" alt="Leonardo Lanciotti"><div><div class="ot-who">R&D CFD S.R.L. – Comet S.p.A. | Leonardo Lanciotti</div><h3>CHT Analysis of a Reciprocating Pump</h3><p>Thermal analysis of a reciprocating pump operating at a fixed working point. The objective is to identify potential hot spots within the system and to verify that the resulting thermal levels remain within acceptable limits for the piston seals.</p><p>The first phase consists of an isothermal sloshing analysis of the oil inside the pump housing, used to compute the heat transfer coefficient (HTC) distribution on the internal walls — subsequently applied as a boundary condition in the second phase. The second phase is a steady-state conjugate heat transfer (CHT) analysis: frictional losses from the dynamic analysis of the crank mechanism are applied to the relevant contact regions as heat sources, and heat transfer is evaluated between the solid components, the external environment, and the prescribed HTC and temperature boundary conditions. CFD results are compared and validated against experimental thermocouple measurements.</p></div></div><div class="open-talk"><img src="speakers/jean-decaix.jpg" alt="Jean Decaix"><div><div class="ot-who">HES-SO Valais/Wallis | Jean Decaix</div><h3>Moving Particle Simulation of Eroded Pelton Runners</h3><p>Hydropower is essential for grid stability but faces growing challenges from increased sediment transport driven by climate change, which induces erosion affecting turbine efficiency, wear, and maintenance costs. Pelton turbines are particularly vulnerable, with nozzle tips and runner buckets suffering erosion-related efficiency losses. Predicting such losses with traditional CFD is difficult due to complex free-surface, high-velocity flows and rotating components.</p><p>Meshless methods, especially Moving Particle Simulation (MPS), offer promising alternatives enhanced by GPU computing. This study uses scans of real erosion geometries from runners at different life stages (new, mid-life, end-of-life). Simulations at best efficiency conditions with a single jet configuration show torque drops of <strong>6%</strong> and <strong>6.6%</strong> for mid-life and end-of-life runners. The findings confirm the capability of MPS to accurately capture performance losses due to realistic erosion patterns. Future work will focus on experimental validation and scaling the methodology to larger Pelton turbines.</p></div></div><div class="open-talk"><img src="speakers/lijun-cao.jpg" alt="Lijun Cao"><div><div class="ot-who">SKF | Lijun Cao & Fabrizio Mandrile</div><h3>Integrating Particleworks into SKF Engineering Tools: Part I</h3><p>The calculation of the heat transfer coefficient (HTC) in Particleworks provides a new way of quickly estimating convective HTCs on bearing components. These HTCs are coupled with SKF internal tools such as <strong>BEAST</strong> to calculate bearing temperatures, enhancing the accuracy and robustness of bearing thermal analysis.</p><p>This work presents a detailed evaluation of Particleworks' capability to predict HTCs under flow conditions relevant to rolling-element bearings. Simplified benchmark cases were considered, including heat transfer on a sphere in a uniform flow and between rotating concentric cylinders (Taylor vortices). Particleworks results are compared with well-established HTC correlations from the literature as well as solutions from ANSYS Fluent. The findings contribute to SKF's ongoing efforts to improve the thermal modelling capabilities of rolling bearings.</p></div></div><div class="open-talk"><img src="speakers/lukas-hafner.jpg" alt="Lukas Hafner"><div><div class="ot-who">deepfluid | Dr. Lukas Hafner & Gianluca Parma</div><h3>Direct Optical Air-in-Oil Measurement as an Enabler for Accurate Simulation of Gearings and Hydraulic Systems</h3><p>Air entrainment in oils is a critical factor influencing the efficiency, reliability and lifetime of gearings and hydraulic systems. This contribution presents a direct air-in-oil measurement approach based on optical machine vision, enabling the direct detection and quantification of air bubbles in lubricants and hydraulic fluids. A central objective is to generate reliable measurement data that can be transferred from laboratory investigations to field applications — providing the physical input needed to describe real air-in-oil behavior in simulations more accurately.</p><p>By connecting direct optical measurements with simulation models, uncertainties in assumptions and boundary conditions can be reduced, improving the prediction of system behavior under aerated oil conditions. The availability of validated measurement data can also reduce the number of required simulation and design-iteration steps, making development faster while supporting optimized efficiency and reliability. Overall, the approach highlights how direct air-in-oil measurement can serve as an enabler for accurate simulation, condition monitoring and system optimization.</p></div></div><div class="open-talk"><img src="speakers/leonardo-tiberi.jpg" alt="Leonardo Tiberi"><div><div class="ot-who">TrackOne SRL – Unimore | Leonardo Tiberi</div><h3>Study of the Lubrication on Carrier Roller using a CFD 3D-MPS Method</h3><p>In the context of undercarriage systems engineering, the continuous increase in operational speeds and applied loads requires increasingly advanced design strategies to ensure maximum component reliability and operator safety. One of the most critical components is the track/carrier roller, which is subjected not only to severe mechanical wear but also to overheating induced by internal friction and interaction with adjacent components.</p><p>This study presents an analysis model to evaluate the lubrication of a carrier roller, investigating both fluid-dynamic and thermal aspects. Field operating conditions were considered and replicated within the model to analyze the lubricant's behavior inside the roller layout. The model was validated through bench testing, where roller temperatures were monitored up to thermal convergence; a comparison between these experimental measurements and the proposed CFD model results showed good correlation.</p></div></div><div class="open-talk"><img src="speakers/bernd-valtwies.jpg" alt="Bernd Valtwies"><div><div class="ot-who">Börger GmbH | Bernd Valtwies & Riccardo Sala</div><h3>Simulation of Sand Separation and Wear in the Börger FlowSep</h3><p>The Börger FlowSep is a compact separation unit that removes abrasive sand and grit from process fluids using centrifugal force, protecting downstream pumps and equipment from premature wear. This study applies Particleworks to simulate the separation process — resolving how sand particles are driven out of the fluid stream inside the unit.</p><p>Beyond separation efficiency, the simulation is used to anticipate where abrasive wear is likely to concentrate on the wetted surfaces, so that geometry and material choices can be optimised for a longer service life. Coupling the particle-laden flow with the expected wear patterns gives Börger's engineers a predictive view of both performance and durability ahead of physical prototyping.</p></div></div>
      <a class="blog-card" href="../blog/pw-experience-2026.php"><i class="bi bi-journal-text"></i><div><b>Read the story of the day</b><span>What Modena taught us about heat, air and wear: quotes, slides and the moments to watch.</span></div></a>
      <p class="pr-sub mt-4 mb-0"><i class="bi bi-clock-history"></i> Earlier editions: <a href="proceedings2025.php">Proceedings 2025</a> · <a href="proceedings2024.php">Proceedings 2024</a></p>
    </div>
  </section>
  <?php else: ?>

  <section class="pr-hero">
    <div class="container">
      <div class="pr-eyebrow"><i class="bi bi-unlock"></i> Proceedings 2026</div>
      <h1>The <span class="accent">Modena</span> proceedings.</h1>
      <p class="lead"><?= e($cfg['intro']) ?></p>
      <div class="pr-facts">
        <span class="pr-fact"><i class="bi bi-calendar-event"></i> October 7, 2026</span>
        <span class="pr-fact"><i class="bi bi-geo-alt"></i> BPER FORUM Monzani, Modena (IT)</span>
        <span class="pr-fact"><i class="bi bi-mic"></i> <?= count($talks) ?> talks</span>
      </div>
    </div>
  </section>

  <section class="pr-section">
    <div class="container">
      <?php if (!empty($cfg['takeaways'])): ?>
      <h2 class="pr-h2">What the day showed</h2>
      <p class="pr-sub">Threads that ran through the talks.</p>
      <div class="take-grid">
        <?php foreach ($cfg['takeaways'] as $i => $t): ?>
        <div class="take"><div class="n"><?= $i + 1 ?></div><b><?= e($t[0]) ?></b><p><?= e($t[1]) ?></p></div>
        <?php endforeach; ?>
      </div>
      <?php endif; ?>

      <h2 class="pr-h2">Talks</h2>
      <p class="pr-sub">Slides of the presentations released by their speakers.</p>
      <?php foreach ($talks as $t): ?>
      <article class="talk" id="talk-<?= e($t['id']) ?>">
        <div class="talk-top">
          <?php if (!empty($t['photo'])): ?><img src="speakers/<?= e($t['photo']) ?>" alt="<?= e($t['speaker']) ?>"><?php endif; ?>
          <div>
            <div class="talk-time"><?= e($t['time']) ?></div>
            <h3><?= e($t['title']) ?></h3>
            <div class="talk-who"><?= e($t['speaker']) ?> · <?= e($t['org']) ?></div>
          </div>
        </div>
        <div class="talk-body">
          <div class="talk-find">
            <h4>Key findings</h4>
            <ul><?php foreach ($t['findings'] as $f): ?><li><?= e($f) ?></li><?php endforeach; ?></ul>
          </div>
          <div class="talk-media">
            <?php $pdfok = !empty($t['pdf']) && is_file(__DIR__ . '/proceedings2026-files/' . basename($t['pdf'])); ?>
            <?php if (!empty($t['video_file'])): ?>
            <div class="vid"><video controls preload="metadata" src="<?= e($t['video_file']) ?>" data-vid="<?= e($t['id']) ?>"></video></div>
            <?php elseif (!empty($t['youtube'])): ?>
            <div class="vid"><button type="button" aria-label="Play the recording" style="background-image:url(https://i.ytimg.com/vi/<?= e($t['youtube']) ?>/hqdefault.jpg)" data-yt="<?= e($t['youtube']) ?>" data-vid="<?= e($t['id']) ?>"></button></div>
            <?php else: ?>
            <div class="vid soon"><i class="bi bi-camera-video"></i> Recording coming soon</div>
            <?php endif; ?>
            <?php if (!empty($t['moments']) && (!empty($t['youtube']) || !empty($t['video_file']))): ?>
            <div class="moments"><span>Jump to</span>
              <?php foreach ($t['moments'] as $m): ?><button type="button" data-seek="<?= e($t['id']) ?>" data-t="<?= (int)$m[0] ?>"><i class="bi bi-play-fill"></i><?= sprintf('%d:%02d', intdiv($m[0], 60), $m[0] % 60) ?> <?= e($m[1]) ?></button><?php endforeach; ?>
            </div>
            <?php endif; ?>
            <div class="d-flex flex-wrap align-items-center gap-3">
              <?php if ($pdfok): ?>
              <a class="btn-red" href="proceedings2026.php?dl=<?= e($t['id']) ?>"><i class="bi bi-download"></i> Slides (PDF)</a>
              <?php else: ?>
              <span class="btn-soft"><i class="bi bi-envelope"></i> Slides on request: <a href="mailto:info@particleworks-europe.com?subject=Proceedings%202026%20-%20<?= rawurlencode($t['org']) ?>">info@particleworks-europe.com</a></span>
              <?php endif; ?>
            </div>
          </div>
        </div>
      </article>
      <?php endforeach; ?>

      <?php if (!empty($cfg['blog_url'])): ?>
      <a class="blog-card" href="<?= e($cfg['blog_url']) ?>"><i class="bi bi-journal-text"></i><div><b>Read the story of the day</b><span>Quotes, slides and the moments to watch: what Modena taught us about heat, air and wear.</span></div></a>
      <?php endif; ?>
    </div>
  </section>
  <?php endif; ?>

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
            <li class="mb-2"><a href="index.php">Conference overview</a></li>
            <li class="mb-2"><a href="workshop.php">Technical Session (Oct 6)</a></li>
            <li class="mb-2"><a href="proceedings2026.php">Proceedings 2026</a></li>
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
      <div class="d-flex flex-wrap gap-3 small mb-3" style="opacity:.85;">
        <span class="text-white-50">Past editions:</span>
        <a href="https://particleworks-europe.com/experience/proceedings2025.php">Proceedings 2025</a>
        <a href="https://particleworks-europe.com/experience/proceedings2024.php">Proceedings 2024</a>
        <a href="https://particleworks-europe.com/experience/gallery2024.php">Gallery 2024</a>
        <a href="https://particleworks-europe.com/experience/proceedings2023.php">Proceedings 2023</a>
        <a href="https://particleworks-europe.com/experience/speakers2023.php">Speakers 2023</a>
        <a href="https://particleworks-europe.com/experience/gallery2023.php">Gallery 2023</a>
      </div>
      <div class="d-flex flex-wrap justify-content-between align-items-center">
        <p class="small mb-0">&copy; 2026 Particleworks Europe. All rights reserved.</p>
        <p class="small mb-0"><a href="../privacy.php" class="me-3">Privacy</a>Meshfree CFD simulation technology</p>
      </div>
    </div>
  </footer>

  
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    window.addEventListener('scroll', function(){ document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30); });
    // ---- video: click-to-play, jump to a moment, deep links from the blog (?talk=04&t=370) ----
    function playAt(id, t) {
      var v = document.querySelector('video[data-vid="' + id + '"]');
      if (v) { v.currentTime = t; v.play(); v.scrollIntoView({behavior:'smooth', block:'center'}); return; }
      var f = document.querySelector('iframe[data-vid="' + id + '"]');
      if (f) { f.contentWindow.postMessage(JSON.stringify({event:'command', func:'seekTo', args:[t, true]}), '*'); f.contentWindow.postMessage(JSON.stringify({event:'command', func:'playVideo', args:[]}), '*'); f.scrollIntoView({behavior:'smooth', block:'center'}); return; }
      var b = document.querySelector('button[data-yt][data-vid="' + id + '"]');
      if (b) { var fr = document.createElement('iframe'); fr.dataset.vid = id;
        fr.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0&enablejsapi=1&start=' + t;
        fr.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; fr.allowFullscreen = true; fr.title = 'Recording'; b.replaceWith(fr); fr.scrollIntoView({behavior:'smooth', block:'center'}); }
    }
    document.querySelectorAll('button[data-yt]').forEach(function(b){ b.addEventListener('click', function(){ playAt(b.dataset.vid, 0); }); });
    document.querySelectorAll('button[data-seek]').forEach(function(b){ b.addEventListener('click', function(){ playAt(b.dataset.seek, parseInt(b.dataset.t, 10)); }); });
    (function(){
      var q = new URLSearchParams(location.search), tgt = q.get('talk') ? {talk:q.get('talk'), t:q.get('t')||'0'} : null;
      try {
        if (tgt && !document.querySelector('.talk')) { sessionStorage.setItem('pwe26_target', JSON.stringify(tgt)); return; }   // gate view: remember where the visitor was going
        if (!tgt && document.querySelector('.talk')) { var k = sessionStorage.getItem('pwe26_target'); if (k) { tgt = JSON.parse(k); sessionStorage.removeItem('pwe26_target'); } }
      } catch (e) {}
      if (tgt && document.querySelector('.talk')) { var el = document.getElementById('talk-' + tgt.talk); if (el) setTimeout(function(){ playAt(tgt.talk, parseInt(tgt.t, 10) || 0); }, 400); }
    })();
    // the form iframe posts its height: fit it
    window.addEventListener('message', function(e){
      if (typeof e.origin !== 'string' || e.origin.indexOf('forms-eu.com') === -1) return;
      var h = null, d = e.data;
      if (typeof d === 'number') h = d; else if (d && typeof d === 'object') h = d.height || d.frameHeight || (d.iframe && d.iframe.height);
      else if (typeof d === 'string') { var m = d.match(/(\d{3,5})/); if (m) h = parseInt(m[1], 10); }
      if (h && h > 300 && h < 20000) { var f = document.getElementById('reg-form'); if (f) f.style.height = h + 'px'; }
    }, false);
  </script>
</body>
</html>
