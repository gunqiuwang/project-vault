# Walkthrough: 世界杯信息站 (Prototype Phase)

## Project Profile

- **Type:** Web 站 (static HTML + future Cloudflare Workers)
- **Phase:** prototype
- **Path:** D:\C1\worldcup2026 (WSL: /mnt/d/C1/worldcup2026)
- **Domain:** 404969.xyz (Cloudflare, not yet deployed)
- **Obsidian Vault:** C:\Users\guoku\Documents\Obsidian Vault\Projects\世界杯

## Init Results

| Metric | Value |
|--------|-------|
| Vault files created | 13 (all prototype-phase files) |
| Reports | 1 (setup report) |
| Metadata compliance | 100% |
| Vault score | 75/100 (Good) |
| Source files | 项目构想.md (detailed planning) + index.html (1219-line demo) |

### Score Breakdown

| Dimension | Score | Notes |
|-----------|-------|-------|
| Confidence | 61% (8/13) | Some files inferred (e.g., deployment) |
| Freshness | 100% | All created today |
| Completeness | 100% | All prototype files present |
| Review | 30% (4/13) | Needs human review |

## Key Observations

### 项目构想.md was a goldmine

Like 二字日记's `PROJECT-REVIEW.md`, the planning doc had everything needed:
- Feature prioritization (赔率反算胜率 as core)
- Tech stack decision (方案 B: static + Workers)
- Data source comparison (API-Football vs The Odds API)
- Architecture diagram (data flow)
- Timeline (10 days to kickoff)
- Polymarket arbitrage research

**Lesson:** If a project has a detailed planning/review document, read it FIRST. It contains 80% of what the vault needs.

### No Git repo — had to init first

Project had no `.git`. Had to run `git init && git add . && git commit` before vault init.

**Lesson:** Always check for git. If missing, init git + commit existing files first, then create vault.

### Prototype phase — different vault shape

Compared to 二字日记 (mvp phase), the worldcup prototype:
- Fewer "known issues" (no real users yet)
- More "decisions to make" (功能优先级未确认)
- Deployment info is speculative (confidence: low)
- No testing infrastructure

The phase-based file selection worked correctly.

## Obsidian Setup

```bash
bash templates/setup-obsidian-link.sh /mnt/d/C1/worldcup2026/docs/vault "世界杯"
```

Junction created: `Obsidian Vault\Projects\世界杯` → `D:\C1\worldcup2026\docs\vault`

Graph View showed 00_HOME as central hub with clean star topology.

## Data Sources Used

| Source | What It Provided |
|--------|-----------------|
| `项目构想.md` | Complete project vision, tech decisions, feature list, timeline |
| `index.html` | Design direction (dark theme, gold accents), current demo state |

## Pitfalls Encountered

1. **D: drive path** — Project on D: not C:. Symlink script handled it correctly via `wslpath`.

2. **Staleness threshold** — Set to 7 days (not 30) because World Cup is fast-moving. This should be project-specific in VAULT_SCHEMA.md.
