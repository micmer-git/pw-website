# AGENTS.md — pw-website

**Repo:** `micmer-git/pw-website` — the Particleworks Europe case-study site: ~120 paired
`.html` / `.php` pages plus `cases/`, `applications/`, `blog/`, `experience/`, `images/`.

The `_*.py` scripts at the root are the generators — `_unify_site.py`, `_seo_sync.py`,
`_gen_evergreen.py`, `_fix_absolute_paths.py`, `_apply_hero_refresh*.py`. **Edit the generator,
not 120 pages by hand**, and keep each `.html`/`.php` twin in step. Re-run `_seo_sync.py` after
adding a page so `sitemap.xml` and the meta tags stay true.

Public, client-facing surface: publishing needs an explicit ask.

<!-- SHARED-CORE:BEGIN — canonical copy lives in ~/.claude/skills/AGENTS.md.
     Edit it THERE and re-run sync_agents.sh. Anything above this marker is repo-specific. -->

# Agent operating manual — Particleworks Europe

Three agents work on these repos and they share one set of rules:

| agent | what it is | reads |
|---|---|---|
| **Claude Code** | Anthropic CLI, large context, MCP connectors (Drive, Gmail, Notion, Canva) | `CLAUDE.md` + `~/.claude/skills/` |
| **Codex** | OpenAI CLI | `AGENTS.md` + `~/.codex/AGENTS.md` |
| **PI** | `pi` CLI on a **local Qwen3.5-9B, 64k context** — cheap, offline, small | `AGENTS.md` (cwd + parents + `~/.pi/agent/AGENTS.md`) + `~/.pi/agent/skills/` |

Delegating to PI from another agent: `cd <the repo> && pi -p '<task>'`. **The prompt must be a
single line** — `-p` truncates at the first newline, and PI then answers the fragment it got,
politely and uselessly. Front-load the imperative, cite **line numbers** rather than quoting
code (the shell mangles nested quotes), and say explicitly what *not* to do — it will otherwise
finish a small edit by proposing to launch the run. Verify what comes back: diff it against a
backup you took first, since the study folders are not under version control.

Small context is not a smaller version of the job — it changes *how* the job is done.
See §2. Nobody is exempt from §1.

---

## 1. The five inviolable rules

1. **NEVER kill a Particleworks process.** No `Stop-Process`, no `taskkill`, on any `PW*`,
   viewer, solver or preprocessor — a solve someone is watching is not yours to end. Stop only
   the launcher *you* started. A dead run leaves `result/out_*.lock`; delete the stale lock, not
   the process.
2. **Ship every surface in the same session.** A change is not done when the code works — it is
   done when **git**, the **published site**, the **index doc** and the **skill/memory** all say
   the same thing. Name each surface and its state before you claim done. A tool that changed in
   git but is documented with its old flags on the site is worse than no documentation.
3. **Every check appends to a cumulative report.** A diagnostic that exists only in terminal
   scrollback did not happen. Append: what you ran, the numbers, the verdict, the date.
4. **When deliverables land, open the folder** — `explorer.exe "<output dir>"`. Every project,
   every time.
5. **Nothing leaves the machine without approval.** Never push to `main`/`master`, never send
   mail or outreach, never publish or share a file, never touch a client-facing surface unless
   the user asked in this session. Local work — read, analyse, branch, commit — is free.

## 2. Context discipline — how agents actually get stuck

The failure is never a hard error. The window fills with directory listings and the agent
starts guessing. Non-negotiable:

- **Never list or search from a home directory.** `ls -la ~`, `find . -name "*.py"` from
  `C:\Users\...`, `git log` with no `-n` — thousands of lines, context gone, task lost.
  `cd` into the repo *first*, then look.
- **Cap every command.** `| head -50` on anything you have not seen before. `rg -n pattern | head -30`.
  Never `cat` a file over ~300 lines, a `.pptx`, a `.csv` of results, or anything binary.
- **Read slices, not files** — `sed -n '120,180p' file`. Grep for the line number first.
- **`rg` and `fd` beat `grep` and `find`** (PI ships them at `~/.pi/agent/bin/`).
- **Ask the repo, not the disk.** `git ls-files | head`, `README.md`, `AGENT_HANDOFF.md` —
  three cheap reads that answer most "where is X" questions.
- **Write state down before you run low.** The moment a task looks long, put the plan and the
  numbers in `AGENT_HANDOFF.md` (§5). The file survives a context reset; your reasoning does not.
- **Blocked twice on the same thing? Stop, write the handoff block, hand it over.** Grinding
  costs more than a handoff.
- **Never run a solve in the foreground.** A `pwpy` solve is hours to days; a blocking tool call
  turns your session into a paperweight and hides what the run is costing. Launch it detached,
  have it write a status file, and poll that.
- **Price the run in the first five minutes.** Every solve writes `result/trace-*.csv` with a
  `remaining time` column. It is meaningless for the first ~100 steps and honest by ~1000:
  read it, and if it says *days*, stop and re-scope rather than finding out on day three.
  Measured 2026-08-27: a KOSTAL v6 run sat at **26.8 days remaining** after one hour, 0.16 %
  done, while its own `status.json` still read `fail` from the previous attempt.

## 3. Skills — load one, not all

| skill | use it when |
|---|---|
| `pwpy-particleworks` | driving Particleworks/MPS headless from `pwpy`: scenes, preprocess, GPU solve, mapping, parametric sweeps, resuming a batch |
| `pwpy-cht` | thermal: churning run → HTC map → steady conjugate-heat-transfer, ISO/TR 14179-2 heat sources |

Both live in `~/.claude/skills/` and are exposed to PI at `~/.pi/agent/skills/`
(`/skill:pwpy-particleworks`).

**Read the `## Lessons learned` table, weight 5 then 4, for the area you are touching — and
nothing else.** That ranking *is* the onboarding path. Pulling a whole SKILL.md into a 64k
window to answer one question is exactly the mistake §2 is about.

### The traps that cost the most, if you read nothing else

| id | trap |
|---|---|
| `pwpy/L-015` | **every result is gated behind `scene.activate()`** — un-activated, a fully solved scene reports `frame_count = 0` and looks like it never ran |
| `pwpy-cht/L-001` | `pwpy` re-serialises its **cached** scene over your on-disk `sub.json` patch — patch the JSON, run each solver step in a **fresh process**, and re-read the file before spending GPU |
| `pwpy/L-001` | `set_animation("transform.rotation")` silently flips `rotationMode` axis→normal and spins the body about **X** — patch `sub.json`, gate on `angular_velocity` |
| `pwpy/L-011` | on a scene built from scratch `pre.coarseInitialDistance` defaults to **1.0 — one metre**; pin it to `pre.initialDistance` |
| `pwpy/L-002` | re-running the orchestrator to "continue" a batch **wipes completed runs** — use `resume_run.py` |
| `pwpy/L-018` | attribute particles to a cell by `group_index`, never by current position |
| `pwpy/L-005` | runs ≤0.5 s are **not** statistical steady state (σ ≥ mean) — average over the developed window |
| `pwpy-cht/L-002` | an adiabatic run contains **no** HTC (0 non-zero over 670,920 triangles) — phase A must be a real re-run |

Scripts must run on **Particleworks 8.2 *and* 9.0**: resolve the install at run time, never pin a
folder, compare versions numerically. `PW.FileReader`/`FileWriter` and `MATERIAL_elastic` are 9.0-only.

## 4. Lessons learned — the weighted standard

Full standard: `~/.claude/skills/CONVENTIONS.md`. In short:

- Every skill carries `## Lessons learned`, highest weight first:
  `### L-004 · weight 5 · reinforced 2 · verified 2026-07-29 · cost 2.5 h GPU`, then
  **Symptom / Cause / Fix / Evidence**.
- **Weights** — 5 inviolable · 4 strong rule *or a trap that silently produces plausible garbage*
  · 3 area context · 2 project fact · 1 background.
- **Evidence, not assertion.** "0 non-zero HTC over 670,920 triangles" beats "HTC mapping doesn't
  work". Mark unverified things unverified; reconstructed-from-binaries is not observed-working.
- **Prune as hard as you add.** Superseded lessons are rewritten, never stacked. Two contradictory
  lessons are worse than none — the reader cannot tell which is current.
- **Capture in the repo, point from memory.** Memory is per-user and dies with the machine; the
  repo is shared and versioned. Never the other way round.
- Cite the id in the commit (`pwpy-cht: L-004 …`) so `git log --grep=L-004` tells the whole story.
- Ids are never renumbered or reused. Across repos, namespace them: `pwpy/L-011`.

## 5. Talking to each other — `AGENT_HANDOFF.md`

One append-only file at the root of every repo, **newest block on top**. Write a block whenever
you stop, hand over, or get blocked — not only when you finish:

```markdown
## 2026-08-27 · pi · KOSTAL v6 plan
- **Did:** read v5 cells.csv (6 configs, g06/g10/g14 x v1/v2); g06 fails packing_ok.
- **Evidence:** D:\...\2026.KOSTAL\03.Solving\v5\cells.csv — continuity 0.20-0.52, t_min 1.0-1.16 um
- **Unverified:** whether v6 needs a finer particle size; nothing re-run.
- **Next:** one concrete step, small enough for the next agent to start cold.
```

Rules: never edit another agent's block, append your own. Trailer every commit with
`Agent: claude|codex|pi`. When two sources disagree, **the repo beats memory and evidence beats
assertion** — and the disagreement itself goes in a block.

**One working tree, several agents.** Before you touch git, `git status` *and* `git reflog -5`:
a repo that was clean a minute ago may now be mid-rebase under someone else. Then:

- **Never `git add` while another agent may be mid-commit** — the index is shared, and your
  files get swept into their commit (or theirs into yours). Build your commit with a private
  index instead, which touches neither HEAD nor the working tree:
  `GIT_INDEX_FILE=.git/tmp-idx git read-tree origin/main && … && git commit-tree` → `git branch -f`.
- **Never `checkout`, `reset`, `stash` or `rebase` a tree you do not have to yourself.** A hard
  reset deletes another agent's tracked work with no warning; untracked files survive it.
- Branch names are shared too. Prefix yours or make it unmistakable.
- Lost a commit to someone else's reset? It is still in `git reflog` — recover it onto a fresh
  branch, don't redo the work.

## 6. Working style

Report in this order: **Outcome → Evidence (paths, numbers, commands) → Risks/open items →
one Next step.** Batch related edits into one pass. Don't narrate what you are about to do.
Never mark a task done without showing it works. Italian in, Italian out.
**Never commit credentials, customer data or PII** — these repos name real clients.

<!-- SHARED-CORE:END -->
