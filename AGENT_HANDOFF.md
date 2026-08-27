# Agent handoff log

Append-only, **newest block on top**. One block whenever an agent stops, hands over, or gets
blocked. Format and rules: `AGENTS.md` §5.

## 2026-08-27 · claude · shared agent manual added
- **Did:** added `AGENTS.md` (shared core, canonical copy in `~/.claude/skills/AGENTS.md`) and
  this log to every Particleworks repo; wired PI's skills and global context file.
- **Evidence:** `python ~/.claude/skills/sync_agents.py` reports every repo in sync.
- **Unverified:** nothing here is enforced by a hook — the rules hold only if agents read them.
- **Next:** when a rule turns out to be wrong or missing, fix the canonical copy and re-run
  `sync_agents.py --write`; never patch one repo's core in place.
