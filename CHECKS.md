# Cumulative check log — pw-website

Append-only, **newest block on top**. Every diagnostic gets a block: what was run, the numbers,
the verdict, the date. A check that exists only in terminal scrollback did not happen.

---

## 2026-09-10 · claude · Oct 6 — full timetable, chronological order, Saigo on multi-resolution

Client grid (as given): 15:00–15:25 Structures/Federica · 15:25–15:50 Air/Gianluca ·
15:50–16:30 break · 16:30–16:55 MPS+DEM/Riccardo · 16:55–17:20 Multi-resolution/Federica + Iori
(restart) · 17:20–17:45 CHT/Riccardo. Michele's segment closes at 15:00 by subtraction.

| check | expected | got | verdict |
|---|---|---|---|
| card times | 6 `.talk-time` | 14:10—15:00 · 15:00—15:25 · 15:25—15:50 · 16:30—16:55 · 16:55—17:20 · 17:20—17:45 | ✅ |
| break rows | 1 | 15:50 — 16:30 | ✅ |
| contiguity | no gap, no overlap 14:10 → 17:45 (segments + break included) | contiguous | ✅ |
| card order | chronological | talk-ai · talk-fsi · talk-multiphase · **break** · talk-cfd-dem · talk-refinement · talk-cht | ✅ |
| labels | TOPIC 01…06 once each, matching the new order | idem | ✅ |
| Saigo | headshot + speaker row + Restart chip on Topic 05 | `iori-saigo.jpg` referenced & on disk, 1 Restart chip, `Speakers:` line with both | ✅ |
| tag balance | balanced | div 120/120 · a 29/29 · span 56/56 · article 6/6 · section 4/4 · p 24/24 · h3 8/8 · h4 2/2 | ✅ |
| twins | `diff -q` silent | silent, 50 448 B each | ✅ |
| render | Edge headless 1280 px | `scratchpad/oct6-times.png` — badges, break row and both speaker rows on Topic 05 all render | ✅ |

CSS lifted verbatim from `program.php`: `.talk-time` (+ its 767 px rule) and the four `.break-row`
rules. Anchors (`#talk-cht` …) were **not** renamed, so any external link still lands on the right
card; nothing else in the repo links to them (`grep -rn 'workshop.php#'` → no hits).

**Unverified:** the 14:00 — 18:00 in the hero and in `index.php` is unchanged — the talks now run
14:10 → 17:45 and the 1:1 meetings fill the rest; nobody confirmed the 14:00–14:10 opening or the
17:45–18:00 tail. The restart sentence added to Topic 05's abstract is my wording, not the
speaker's — "iori restart" was all the brief said.

---

## 2026-09-10 · claude · Oct 6 — Univance guest contribution in the AI session

Change: `experience/workshop.php` + `.html` — Topic 01 (AI-driven Particleworks) split into two
timed segments, Naohiro Fujita (Univance Corporation, JP) **before** Michele Merelli.

| check | command | expected | got | verdict |
|---|---|---|---|---|
| talk articles | `grep -c '<article class="talk'` | 6 | 6 | ✅ |
| topic labels | `grep -o 'talk-no">[^<]*'` | TOPIC 01…06, once each | idem | ✅ |
| segments | `grep -c 'class="kn-seg"'` | 2 | 2 | ✅ |
| segment times | `grep -o 'kn-seg-title">[^<]*'` | 14:10 — 14:25 · Guest contribution / From 14:25 · Particleworks Europe | idem | ✅ |
| headshot | `images/experience2026/naohiro-fujita.jpg` | referenced + on disk | both true | ✅ |
| tag balance (SVG + head excluded) | python count | balanced | div 114/114 · a 29/29 · span 46/46 · article 6/6 · section 4/4 · p 23/23 · h3 8/8 · h4 2/2 | ✅ |
| twins | `diff -q workshop.php workshop.html` | no output | no output | ✅ |
| encoding | `head -c3` / `cat -v` | no BOM, UTF-8 em-dash `M-bM-^@M-^T` | idem, CRLF preserved | ✅ |
| diff size | `git diff --stat` | localised | 30 lines changed per twin (48+/12-) | ✅ |

Rendered check — Edge headless (`--headless=new`, `#talk-ai` so the abstract is open):
`scratchpad/oct6.png` at 1280 px and `scratchpad/oct6-mobile.png` at 390 px. Topic 01 shows the
two segments with a dashed separator, both headshots load, tags/abstract/`Speakers:` line intact.
**Note:** at 390 px the card overflows the right edge in the capture — the *untouched* Topic 02
overflows identically, so it is a headless-without-mobile-emulation artifact, not a regression.

Copy also touched: section intro now "Six focused topics … opening with a guest contribution from
Univance Corporation"; hero still reads "6 technical topics" (still true — Univance sits inside
Topic 01, no renumbering). `index.php` "Explore the six topics" left unchanged, still correct.

**Unverified:** Michele's end time — the client gave only 14:10 — 14:25, so segment 2 reads
"From 14:25" rather than an invented closing time. The other five topics remain untimed.

---

## 2026-08-27 · claude · Experience 2026 — programma definitivo (orari + break)

### A. Struttura di `experience/program.php` dopo la riscrittura

| controllo | comando | atteso | ottenuto | esito |
|---|---|---|---|---|
| articoli talk | `grep -c '<article class="talk'` | 11 | 11 | ✅ |
| chiusure | `grep -c '</article>'` | 11 | 11 | ✅ |
| orari per card | `grep -c 'class="talk-time"'` | 11 | 11 | ✅ |
| righe pausa | `grep -c 'class="break-row'` | 4 | 4 | ✅ |
| righe tabella | `grep -c 'class="tt-row'` | 15 | 15 | ✅ |
| etichette | `grep -o 'talk-no">[^<]*'` | KEYNOTE + TALK 01…10, una volta ciascuna | idem | ✅ |

Sequenza oraria letta dal file, in ordine di apparizione — **contigua, nessun buco, nessuna
sovrapposizione**: 08:45→09:00 · 09:00→10:00 · 10:00→10:30 · 10:30→11:00 · **11:00→11:45 break** ·
11:45→12:15 · 12:15→12:45 · 12:45→13:15 · **13:15→14:30 lunch** · 14:30→15:00 · 15:00→15:30 ·
15:30→16:00 · **16:00→16:30 break** · 16:30→17:00 · 17:00→17:30.

Ordine degli `<article id=…>`: keynote, shot-peening, stator, pump, pelton, skf-htc, air-in-oil,
bubble-dynamics, gear-airflow, carrier-roller, flowsep — **corrisponde alla griglia del cliente**
(IAV prima di Univance, Track One dopo).

### B. Bilanciamento tag (SVG esclusi, `<head>` escluso)

```
index         div  97/97 | a 42/42 | span  12/12 | article  0/0 | section 5/5 | p 11/11
program       div 168/168| a 39/39 | span 128/128| article 11/11| section 3/3 | p 31/31
workshop      div 105/105| a 29/29 | span  45/45 | article  6/6 | section 4/4 | p 22/22
registration  div  28/28 | a 26/26 | span  10/10 | article  0/0 | section 2/2 | p  6/6
```
Nessuno sbilanciamento. ✅

### C. Conservazione del contenuto — `program.php` HEAD vs working tree

Diff per multiinsieme di righe normalizzate: **13 righe perse, tutte intenzionali**
(la regola `.talk-art`, l'`<h1>` "is taking shape", il sottotitolo "Preliminary line-up",
i 9 commenti `<!-- TALK n: … -->` rinumerati, la nota "More talks to be announced").
Nessun abstract, nessuno speaker, nessun SVG perso. ✅

### D. Ancore

- 11 `href="program.php#…"` in `index.php` → 11 `id=` corrispondenti in `program.php` ✅
- 11 `href="#…"` nella tabella at-a-glance → 11 `id=` corrispondenti ✅
- Il JS `openHashTalk()` è selector-based e filtra su `classList.contains('talk')`:
  le `.break-row` non hanno id e non lo intercettano. Cliccare una riga della tabella
  apre l'abstract del talk giusto. ✅

### E. Parità gemelli `.php` / `.html`

`diff -q` su index, program, workshop, registration → **nessun output**, i quattro gemelli sono
byte-identici. ✅

### F. Stato produzione — `particleworks-europe.com` (misurato, non assunto)

| pagina | live | repo | delta |
|---|---:|---:|---|
| index | 27.521 B | 28.372 B | **stale** — nessuna occorrenza di FlowSep/Valtwies/Börger |
| program | 78.500 B | 85.874 B | stale |
| workshop | 46.214 B | 46.268 B | stale |
| registration | 17.590 B | 17.823 B | stale |

- Cache-buster + `Cache-Control: no-cache` → stessa risposta: **è il file sul server a essere vecchio**,
  non una cache. Server `Apache`, `X-Powered-By: PHP/8.4`, IP 51.255.117.202 (OVH).
- **`/images/experience2026/` NON esiste in produzione: 404 su tutti e 15 i file testati.**
  Il sito live usa ancora `experience/speakers/` (200) e `experience/img/`.
  → caricare le pagine nuove *senza* prima caricare la cartella immagini romperebbe ogni ritratto.
- GitHub Pages (`micmer-git.github.io/pw-website`) è invece **allineato**: `index.html` 28.372 B,
  identico al locale, Börger presente. Le due superfici sono host diversi.

**Verdetto:** il "manca Borger su index.php" segnalato dal cliente **non è un bug di codice** —
il commit `f203ea7` (08/07/2026) lo aveva già aggiunto. È un buco di deploy sul solo host di
produzione, aperto da almeno sette settimane.

### H. Deploy GitHub Pages — verificato dopo il push `c387369`

`micmer-git.github.io/pw-website` ricostruito e servito:

- `program.html` — griglia oraria completa e contigua letta dalla pagina pubblicata:
  `08:45—09:00 · 09:00—10:00 · 10:00—10:30 · 10:30—11:00 · 11:00—11:45 · 11:45—12:15 ·
  12:15—12:45 · 12:45—13:15 · 13:15—14:30 · 14:30—15:00 · 15:00—15:30 · 15:30—16:00 ·
  16:00—16:30 · 16:30—17:00 · 17:00—17:30` ✅
- `registration.html` — "11 talks · 5 countries" ✅
- Differenza di byte fra Pages e working tree (es. program 85.874 vs 86.852) = **CRLF**:
  `core.autocrlf=true`, i blob in git sono LF, il checkout Linux di Actions serve LF.
  Non è un disallineamento di contenuto.

Bundle `deploy-prod/` riallineato al checkout corrente dopo la conversione CRLF —
i 4 `.php` del bundle sono `diff`-identici a quelli del repo. ✅

**Resta aperto:** l'host di produzione. Vedi §F.

### G. Non verificato

- **Resa grafica reale**: nessuno screenshot. L'estensione Chrome non è installata in questa
  sessione, quindi le pagine **non sono state aperte in un browser**. Restano da guardare a occhio:
  (a) l'orario bianco nel pannello `.talk-art` — il rischio di collisione con l'SVG è stato tolto
  portando il `padding-top` del pannello da `1.4rem` a `3.4rem`, ma non è stato osservato;
  (b) la tabella at-a-glance sotto i 575 px, dove passa a una colonna sola.
- Nessun controllo su come la pagina appare a un lettore di schermo.
