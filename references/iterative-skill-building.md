# Iterative Development Pattern — Lessons from Building Project Vault

## Pattern: Build → Test on Real Project → Find Gaps → Fix → Repeat

This skill was built iteratively across 4 real projects:

| Project | Phase | What It Revealed |
|---------|-------|-----------------|
| 二字日记 | mvp | Basic init works, but WSL symlink fails with Obsidian |
| 世界杯 | prototype | Script doesn't scan design/ or extract from project构想.md |
| 晚安小书房 | idea | Script doesn't scan assets/ outside `assets/` dir; WSL path issue |
| 星爻 | growth | Script misses full-stack detection, miniprogram/images, pages count |

## Key Iteration Cycles

### v1→v2: Skeleton vs Soul
- **Problem:** init-vault.sh generated generic placeholders, score was 30%
- **Fix:** Added project scanning (tech stack, assets, docs, commands from package.json)
- **Result:** Score improved to 46% auto-fill

### v2→v3: Multi-directory scanning
- **Problem:** Only scanned `assets/`, missed `miniprogram/images/`, `design/`, `backend/`
- **Fix:** Scan 5 asset directories, detect full-stack, extract pages from app.json, read backend deps
- **Result:** `WeChat Mini Program + FastAPI` instead of just `WeChat Mini Program`

### v3→v4: Obsidian integration hardening
- **Problem:** WSL symlinks invisible to Windows Obsidian (`EACCES`)
- **Fix:** `setup-obsidian-link.sh` uses `mklink /J` (junction) for WSL
- **Problem:** All `00_HOME.md` nodes identical in Graph View
- **Fix:** `aliases` in frontmatter + color groups in `graph.json`

### v4→v5: Lifecycle tooling
- **Problem:** Only init script existed, no sync or audit
- **Fix:** Added `sync-vault.sh` (git diff analysis) and `audit-vault.sh` (10-point checklist)

## Anti-Pattern: Don't Over-Engineer the README

User explicitly corrected: "比较简单易上手的小帮手不要搞得很复杂很专业的样子"

The README went from 200+ lines of professional documentation to ~50 lines with a screenshot. This is a helper tool, not a framework. Keep it approachable.

## Testing Methodology

1. Run init on a real project (not a toy example)
2. Check the score — if < 70, the script isn't filling enough
3. Open in Obsidian — check Graph View for disambiguation
4. Ask: "Would a new user understand this in 30 seconds?"
5. If not, simplify
