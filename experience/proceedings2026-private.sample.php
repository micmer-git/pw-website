<?php
// Copy to proceedings2026-private.php (same folder, NOT committed — the repo is public) and fill in.
// MachForm: create the form, set "Redirect to website after submission" to
//   https://particleworks-europe.com/experience/proceedings2026.php?access=<access_token>
// PDFs go in experience/proceedings2026-files/ (that folder carries a Deny-all .htaccess).
return [
  'secret'       => 'long-random-string',      // signs the session cookie
  'access_token' => 'another-long-random-string',
  'machform_url' => 'https://particleworks-europe.forms-eu.com/embed.php?id=XXXXX',
  'blog_url'     => '../blog/pw-experience-2026.php',
  'intro'        => 'One paragraph under the hero.',
  'takeaways'    => [ ['Headline', 'One or two sentences.'] ],
  'talks'        => [[
      'id' => '01', 'time' => '09:00–10:00', 'title' => 'Talk title', 'speaker' => 'Name', 'org' => 'Company',
      'photo' => 'name.jpg',                   // file in experience/speakers/
      'findings' => ['Finding one.', 'Finding two.'],
      'pdf' => 'file.pdf',                     // file in proceedings2026-files/, '' = "on request"
  ]],
];
