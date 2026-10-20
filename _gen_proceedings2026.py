#!/usr/bin/env python3
"""Build experience/proceedings2026.php — the form-gated Proceedings page of Particleworks Experience 2026.

Reuses <head>/navbar/footer of experience/registration.html so the page matches the Modena microsite.
The page itself holds NO secrets and NO content of the talks: both live in experience/proceedings2026-private.php
(gitignored — the repo is public — and uploaded by FTP).  See experience/proceedings2026-private.sample.php.
Run:  python _gen_proceedings2026.py
"""
import re, pathlib
root = pathlib.Path(__file__).parent
import sys as _s; _s.path.insert(0, str(root))
from _experience_chrome import fix_nav, fix_footer
reg = (root / '_templates' / 'experience-registration.html').read_text(encoding='utf8')

head = reg[:reg.index('</style>')]
head = re.sub(r'<title>.*?</title>', '<title>Proceedings — Particleworks Experience 2026 | Modena, October 7</title>', head, flags=re.S)
head = re.sub(r'<meta name="description" content=".*?">',
              '<meta name="description" content="Presentations and key findings from Particleworks Experience 2026, Modena. Free access after a short form.">', head, flags=re.S)
head = head.replace('<head>', '<head>\n  <meta name="robots" content="noindex,nofollow">', 1)

nav = reg[reg.index('<!-- Navbar -->'):reg.index('<!-- Hero -->')]
nav = fix_nav(nav).replace('nav-register" href="proceedings2026.php"', 'nav-register active" href="proceedings2026.php"')

footer = reg[reg.index('<!-- Footer -->'):reg.index('<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3')]
footer = fix_footer(footer)

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
'''


# ---- the OPEN part (as proceedings2024/2025): public abstracts of the released talks, copied from program.php ----
import sys, html as _html
sys.path.insert(0, str(root))
from _pwexp26_content import TALKS as _T, ORDER as _O
import json as _json
_AB = _json.loads((root / '_pwexp26_abstracts.json').read_text(encoding='utf8'))
def _abstract(key):
    return _AB.get(key, '')
from _pwexp26_programme import PROGRAMME, STATUS
_cards = ''
for _id, _photo, _title, _spk, _org, _st, _when in PROGRAMME:
    if _photo is None:
        d = _T[_id]; _photo = 'speakers/' + d['photo'][0]; _title = d['title']; _spk = d['speaker']; _org = d['org'].split(' (')[0]
    _label = STATUS[_st] + _when
    _cards += (f'<div class="open-talk"><img src="{_photo}" alt="{_spk}">'
               f'<div><div class="ot-who">{_org} | {_spk}</div><h3>{_title}</h3>{_abstract(_id)}'
               f'<span class="ot-st ot-{_st}">{_label}</span></div></div>')
open_section = ('''
  <section class="pr-section pr-open" id="talks">
    <div class="container">
      <h2 class="pr-h2">The talks</h2>
      <p class="pr-sub">The eleven talks of October 7, 2026. Slides, recordings and key findings of the released talks open after the form above.</p>
      ''' + _cards + '''
      <a class="blog-card" href="../blog/pw-experience-2026.php"><i class="bi bi-journal-text"></i><div><b>Read the story of the day</b><span>What Modena taught us about heat, air and wear: quotes, slides and the moments to watch.</span></div></a>
      <p class="pr-sub mt-4 mb-0"><i class="bi bi-clock-history"></i> Earlier editions: <a href="proceedings2025.php">Proceedings 2025</a> · <a href="proceedings2024.php">Proceedings 2024</a></p>
    </div>
  </section>''')
css += '''
    .open-talk { display:flex; gap:1.2rem; background:#fff; border:1px solid rgba(0,0,0,0.07); border-radius:18px; padding:1.3rem 1.5rem; margin-bottom:1rem; }
    .open-talk img { width:84px; height:84px; border-radius:50%; object-fit:cover; flex-shrink:0; border:3px solid #fff; box-shadow:0 4px 14px rgba(143,22,27,0.18); }
    .ot-who { font-size:0.8rem; font-weight:700; letter-spacing:0.4px; text-transform:uppercase; color:var(--pw-gray); }
    .open-talk h3 { font-size:1.08rem; font-weight:800; color:var(--ev-crimson); margin:0.2rem 0 0.5rem; line-height:1.3; }
    .open-talk p { font-size:0.9rem; line-height:1.6; margin:0 0 0.45rem; color:#334; }
    .ot-st { display:inline-block; font-size:0.72rem; font-weight:800; letter-spacing:0.8px; text-transform:uppercase; padding:0.25rem 0.7rem; border-radius:50px; margin-top:0.2rem; background:#fdeeec; color:var(--ev-crimson); }
    .ot-none { background:#eee; color:#666; }
    .ot-later { background:#fff2dc; color:#a3600b; }
    .open-talk .ot-hook { background:#f3faf6; border-left:3px solid #25a361; padding:0.5rem 0.8rem; border-radius:0 8px 8px 0; }
    .open-talk .ot-hook i { color:#25a361; }
    @media(max-width:600px){ .open-talk { flex-direction:column; } }
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
        setcookie($COOKIE, $good, ['expires' => time() + 60 * 60 * 24 * 7, 'path' => '/', 'secure' => $secure, 'httponly' => true, 'samesite' => 'Lax']);
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
'''

hero_gate = r'''
  <?php if (!$authed): ?>
  <section class="pr-hero">
    <div class="container">
      <div class="pr-eyebrow"><i class="bi bi-lock"></i> Proceedings 2026</div>
      <h1>Take the <span class="accent">Modena</span> talks home.</h1>
      <p class="lead">Slides and key findings of Particleworks Experience 2026 — every talk the speakers released for sharing. Fill in the form once; this browser keeps your access for 7 days.</p>
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
              <div><h2>Get the proceedings</h2><p>Fill in your details — you'll land on the proceedings straight after.</p></div>
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
''' + open_section + r'''
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
            <?php if (!empty($t['findings'])): ?>
            <h4>Key findings</h4>
            <ul><?php foreach ($t['findings'] as $f): ?><li><?= e($f) ?></li><?php endforeach; ?></ul>
            <?php else: ?>
            <h4>About the talk</h4>
            <?php foreach ((array)($t['abstract'] ?? []) as $p): ?><p style="font-size:0.93rem;line-height:1.6;color:#334"><?= e($p) ?></p><?php endforeach; ?>
            <?php endif; ?>
          </div>
          <div class="talk-media">
            <?php $pdfok = !empty($t['pdf']) && is_file(__DIR__ . '/proceedings2026-files/' . basename($t['pdf'])); ?>
            <?php if (!empty($t['no_video'])): ?>
            <?php elseif (!empty($t['video_file'])): ?>
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

      <p class="pr-sub mt-2"><i class="bi bi-info-circle"></i> The speaker of the shot-peening talk did not release the slides. The keynote, the Univance and the IAV talks are slides only, without a recording. Michelangelo Raimondo's talk follows in January 2027. Your access stays active in this browser for 7 days.</p>
      <?php if (!empty($cfg['blog_url'])): ?>
      <a class="blog-card" href="<?= e($cfg['blog_url']) ?>"><i class="bi bi-journal-text"></i><div><b>Read the story of the day</b><span>Quotes, slides and the moments to watch: what Modena taught us about heat, air and wear.</span></div></a>
      <?php endif; ?>
    </div>
  </section>
  <?php endif; ?>
'''

js = r'''
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
'''

out = php_top + head + css + '  </style>\n</head>\n<body>\n\n  ' + nav + '\n' + hero_gate + content + '\n  ' + footer + js
(root / 'experience' / 'proceedings2026.php').write_text(out, encoding='utf8')
print('written', len(out), 'bytes')
