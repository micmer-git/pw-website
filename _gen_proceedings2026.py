#!/usr/bin/env python3
"""Build experience/proceedings2026.php — the form-gated Proceedings page of Particleworks Experience 2026.

Reuses <head>/navbar/footer of experience/registration.html so the page matches the Modena microsite.
The page itself holds NO secrets and NO content of the talks: both live in experience/proceedings2026-private.php
(gitignored — the repo is public — and uploaded by FTP).  See experience/proceedings2026-private.sample.php.
Run:  python _gen_proceedings2026.py
"""
import re, pathlib
root = pathlib.Path(__file__).parent
reg = (root / 'experience' / 'registration.html').read_text(encoding='utf8')

head = reg[:reg.index('</style>')]
head = re.sub(r'<title>.*?</title>', '<title>Proceedings — Particleworks Experience 2026 | Modena, October 7</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Presentations, recordings and key findings from Particleworks Experience 2026, Modena. Free access after a short form.">', head, flags=re.S)
head = head.replace('<head>', '<head>\n  <meta name="robots" content="noindex,nofollow">', 1)

nav = reg[reg.index('<!-- Navbar -->'):reg.index('<!-- Hero -->')]
nav = nav.replace('<li class="nav-item"><a class="nav-link" href="program.php">Oct 7 · Program</a></li>',
                  '<li class="nav-item"><a class="nav-link" href="program.php">Oct 7 · Program</a></li>\n          <li class="nav-item"><a class="nav-link active" href="proceedings2026.php">Proceedings 2026</a></li>')

footer = reg[reg.index('<!-- Footer -->'):reg.index('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3')]
footer = footer.replace('<li class="mb-2"><a href="registration.php">Registration</a></li>',
                        '<li class="mb-2"><a href="proceedings2026.php">Proceedings 2026</a></li>\n            <li class="mb-2"><a href="registration.php">Registration</a></li>')

css = r'''
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
    .talk-body { display:grid; grid-template-columns:1.1fr 1fr; gap:0; }
    @media(max-width:860px){ .talk-body { grid-template-columns:1fr; } }
    .talk-find { padding:1.4rem 1.6rem; }
    .talk-find h4 { font-size:0.78rem; font-weight:800; letter-spacing:1.3px; text-transform:uppercase; color:var(--pw-gray); margin-bottom:0.7rem; }
    .talk-find ul { padding-left:1.1rem; margin:0; }
    .talk-find li { font-size:0.93rem; line-height:1.55; color:#334; margin-bottom:0.5rem; }
    .talk-find li::marker { color:var(--ev-crimson); }
    .talk-media { padding:1.4rem 1.6rem; border-left:1px solid rgba(0,0,0,0.06); display:flex; flex-direction:column; gap:0.9rem; }
    @media(max-width:860px){ .talk-media { border-left:0; border-top:1px solid rgba(0,0,0,0.06); } }
    .vid { position:relative; aspect-ratio:16/9; border-radius:14px; overflow:hidden; background:#11111e; }
    .vid iframe, .vid button { position:absolute; inset:0; width:100%; height:100%; border:0; }
    .vid button { background-size:cover; background-position:center; cursor:pointer; padding:0; }
    .vid button::after { content:'\25B6'; position:absolute; left:50%; top:50%; transform:translate(-50%,-50%); width:62px; height:62px; line-height:62px; border-radius:50%; background:var(--ev-accent); color:#fff; font-size:1.4rem; padding-left:4px; box-shadow:0 8px 24px rgba(0,0,0,0.35); }
    .vid.soon { display:flex; align-items:center; justify-content:center; color:rgba(255,255,255,0.6); font-size:0.9rem; gap:0.5rem; }
    .btn-red { background:var(--ev-accent); color:#fff; border:0; padding:0.6rem 1.3rem; border-radius:50px; font-weight:600; font-size:0.9rem; display:inline-flex; align-items:center; gap:0.5rem; text-decoration:none; box-shadow:0 6px 18px rgba(181,30,35,0.25); }
    .btn-red:hover { color:#fff; filter:brightness(1.08); }
    .btn-soft { color:var(--pw-gray); font-size:0.88rem; }
    .blog-card { display:flex; gap:1.2rem; align-items:center; background:var(--ev-gradient); color:#fff; border-radius:22px; padding:1.6rem 1.9rem; margin-top:2.4rem; text-decoration:none; }
    .blog-card:hover { color:#fff; filter:brightness(1.06); }
    .blog-card i { font-size:2rem; }
    .blog-card b { font-size:1.15rem; display:block; }
    .blog-card span { opacity:.85; font-size:0.92rem; }
'''

php_top = r'''<?php
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
            if ($t['id'] === $_GET['dl'] && !empty($t['pdf'])) {
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
?>
'''

hero_gate = r'''
  <?php if (!$authed): ?>
  <section class="pr-hero">
    <div class="container">
      <div class="pr-eyebrow"><i class="bi bi-lock"></i> Proceedings 2026</div>
      <h1>Take the <span class="accent">Modena</span> talks home.</h1>
      <p class="lead">Slides, recordings and the key findings of Particleworks Experience 2026 — every talk the speakers released for sharing. Leave your details once and the whole collection opens.</p>
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
              <li><i class="bi bi-play-circle"></i><span><b>The recordings</b>Each talk as its own video.</span></li>
              <li><i class="bi bi-lightbulb"></i><span><b>Key findings</b>A short summary of what each talk showed.</span></li>
              <li><i class="bi bi-shield-check"></i><span><b>Your data</b>Processed in line with GDPR, solely to share the proceedings and follow up on them.</span></li>
            </ul>
            <div class="d-flex flex-wrap gap-2 mt-3"><a href="program.php" class="btn-ghost-red"><i class="bi bi-calendar3"></i> View the program</a></div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <?php else: ?>
'''

content = r'''
  <section class="pr-hero">
    <div class="container">
      <div class="pr-eyebrow"><i class="bi bi-unlock"></i> Proceedings 2026</div>
      <h1>The <span class="accent">Modena</span> proceedings.</h1>
      <p class="lead"><?= e($cfg['intro']) ?></p>
      <div class="pr-facts">
        <span class="pr-fact"><i class="bi bi-calendar-event"></i> October 7, 2026</span>
        <span class="pr-fact"><i class="bi bi-geo-alt"></i> BPER FORUM Monzani, Modena (IT)</span>
        <span class="pr-fact"><i class="bi bi-mic"></i> <?= count($cfg['talks']) ?> talks</span>
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
      <p class="pr-sub">Slides and recordings of the presentations released by their speakers.</p>
      <?php foreach ($cfg['talks'] as $t): ?>
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
            <?php if (!empty($t['youtube'])): ?>
            <div class="vid"><button type="button" aria-label="Play the recording" style="background-image:url(https://i.ytimg.com/vi/<?= e($t['youtube']) ?>/hqdefault.jpg)" data-yt="<?= e($t['youtube']) ?>"></button></div>
            <?php else: ?>
            <div class="vid soon"><i class="bi bi-camera-video"></i> Recording coming soon</div>
            <?php endif; ?>
            <div class="d-flex flex-wrap align-items-center gap-3">
              <?php if (!empty($t['pdf'])): ?>
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
      <a class="blog-card" href="<?= e($cfg['blog_url']) ?>"><i class="bi bi-journal-text"></i><div><b>Read the story of the day</b><span>A 1,000-word look at what Modena taught us about lubrication, air-in-oil and thermal simulation.</span></div></a>
      <?php endif; ?>
    </div>
  </section>
  <?php endif; ?>
'''

js = r'''
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
  <script>
    window.addEventListener('scroll', function(){ document.querySelector('.navbar').classList.toggle('scrolled', window.scrollY > 30); });
    // click-to-play: the YouTube player (and its cookies) only loads when asked
    document.querySelectorAll('button[data-yt]').forEach(function(b){
      b.addEventListener('click', function(){
        var f = document.createElement('iframe');
        f.src = 'https://www.youtube-nocookie.com/embed/' + b.dataset.yt + '?autoplay=1&rel=0';
        f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen'; f.allowFullscreen = true; f.title = 'Recording';
        b.replaceWith(f);
      });
    });
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
'''

out = php_top + head + css + '  </style>\n</head>\n<body>\n\n  ' + nav + '\n' + hero_gate + content + '\n  ' + footer + js
(root / 'experience' / 'proceedings2026.php').write_text(out, encoding='utf8')
print('written', len(out), 'bytes')
