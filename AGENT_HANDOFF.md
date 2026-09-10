# Agent handoff log

Append-only, **newest block on top**. One block whenever an agent stops, hands over, or gets
blocked. Format and rules: `AGENTS.md` §5.

## 2026-09-10 · claude · Oct 6 — orari su tutti i topic + ordine cronologico
- **Did:** `experience/workshop.php` + gemello — orario su tutti e 6 i topic, riga break
  15:50 — 16:30, card riordinate in sequenza cronologica e rinumerate (l'ordine degli id ora è
  ai · fsi · multiphase · break · cfd-dem · refinement · cht), segmento di Michele chiuso a 15:00,
  **Iori Saigo (Prometech, JP)** aggiunto al Topic 05 con chip "Restart" e frase di abstract.
  CSS `.talk-time` e `.break-row` presi identici da `program.php`.
- **Evidence:** `CHECKS.md`, blocco 2026-09-10 (secondo) — griglia contigua 14:10 → 17:45, tag
  bilanciati, gemelli identici (50.448 B), screenshot `scratchpad/oct6-times.png`.
- **Unverified:** l'apertura 14:00 — 14:10 e la coda 17:45 — 18:00 (hero e `index.php` dicono
  ancora 14:00 — 18:00); il contenuto reale della parte "restart" di Saigo.
- **Next:** produzione ancora ferma — `particleworks-europe.com` non ha `/images/experience2026/`
  (404 anche su `naohiro-fujita.jpg` e `iori-saigo.jpg`): caricare prima le immagini, poi le pagine.

## 2026-09-10 · claude · Oct 6 — Univance nella sessione AI
- **Did:** `experience/workshop.php` + gemello `.html` — il Topic 01 (AI-driven Particleworks) è
  ora una sessione in due segmenti: **Naohiro Fujita (Univance Corporation, JP) 14:10 — 14:25**,
  "Examples of Python Automation and Industrial Applications", **prima** di Michele Merelli
  ("From 14:25"). Aggiunte due regole CSS (`.kn-seg + .kn-seg`, `.seg-h`), un paragrafo di
  abstract sul contributo Univance, riga `Speakers:` a due nomi, intro di sezione aggiornata.
  Nessuna rinumerazione: restano 6 topic.
- **Evidence:** `CHECKS.md`, blocco 2026-09-10 — 6 articoli, 2 segmenti, tag bilanciati, gemelli
  byte-identici, screenshot Edge headless 1280 px e 390 px.
- **Unverified:** l'ora di fine di Michele (il cliente ha dato solo 14:10 — 14:25) e la
  pubblicazione in produzione: `particleworks-europe.com` è l'Apache su 51.255.117.202, non
  GitHub Pages — questa modifica è su git/Pages, **non** ancora online sul sito del cliente.
- **Next:** quando arriva l'orario completo del 6 ottobre, mettere `.talk-time` su tutti e 6 i
  topic come già fatto su `program.php`, e caricare via FTP il bundle di `deploy-prod/`.

## 2026-08-27 · claude · Experience 2026 — programma definitivo su program.php
- **Did:** riscritto `experience/program.php` come programma definitivo del 7 ottobre — tabella
  oraria at-a-glance in cima, orario su ogni card, 4 righe `.break-row` (welcome 08:45, break
  11:00, lunch 13:15, break 16:00), talk riordinati in sequenza cronologica e rinumerati
  (IAV 07 ⟷ Track One 09). Allineati `index.php` (stesso ordine, 08:45 — 17:30),
  `workshop.php` (orario giorno 2) e `registration.php` (8 → 11 talks). Gemelli `.html`
  rigenerati per tutte e 4 le pagine.
- **Evidence:** `CHECKS.md`, blocco 2026-08-27 — 11 articoli / 11 orari / 4 pause / 15 righe
  tabella, tag bilanciati, 13 righe perse tutte intenzionali, gemelli byte-identici.
- **Il punto vero:** `particleworks-europe.com` **non è** GitHub Pages. Pages è allineato
  (`index.html` 28.372 B = locale); la produzione è un Apache/PHP 8.4 su 51.255.117.202,
  ferma a prima di `f203ea7` (Börger, 08/07/2026) e **senza la cartella `/images/experience2026/`**
  (404 su tutti e 15 i file — usa ancora `experience/speakers/`). Il "manca Borger" del cliente
  è questo, non un bug.
- **Unverified:** nessuno screenshot — l'estensione Chrome non era installata. La resa
  dell'orario nel pannello `.talk-art` e la tabella sotto 575 px non sono state osservate.
- **Next:** caricare via FTP il bundle preparato in scratchpad (`deploy-prod/` + `UPLOAD.txt`):
  **prima** `images/experience2026/` (16 file), **poi** le 8 pagine. Finché non succede, online
  Börger continua a mancare. Il form iscrizioni (MachForm 24414) resta fuori scope, per scelta.

## 2026-08-27 · claude · shared agent manual added
- **Did:** added `AGENTS.md` (shared core, canonical copy in `~/.claude/skills/AGENTS.md`) and
  this log to every Particleworks repo; wired PI's skills and global context file.
- **Evidence:** `python ~/.claude/skills/sync_agents.py` reports every repo in sync.
- **Unverified:** nothing here is enforced by a hook — the rules hold only if agents read them.
- **Next:** when a rule turns out to be wrong or missing, fix the canonical copy and re-run
  `sync_agents.py --write`; never patch one repo's core in place.
