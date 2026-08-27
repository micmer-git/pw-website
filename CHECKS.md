# Cumulative check log — pw-website

Append-only, **newest block on top**. Every diagnostic gets a block: what was run, the numbers,
the verdict, the date. A check that exists only in terminal scrollback did not happen.

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

### G. Non verificato

- **Resa grafica reale**: nessuno screenshot. L'estensione Chrome non è installata in questa
  sessione, quindi le pagine **non sono state aperte in un browser**. Restano da guardare a occhio:
  (a) l'orario bianco nel pannello `.talk-art` — il rischio di collisione con l'SVG è stato tolto
  portando il `padding-top` del pannello da `1.4rem` a `3.4rem`, ma non è stato osservato;
  (b) la tabella at-a-glance sotto i 575 px, dove passa a una colonna sola.
- Nessun controllo su come la pagina appare a un lettore di schermo.
