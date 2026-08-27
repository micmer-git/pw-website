# Agent handoff log

Append-only, **newest block on top**. One block whenever an agent stops, hands over, or gets
blocked. Format and rules: `AGENTS.md` §5.

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
