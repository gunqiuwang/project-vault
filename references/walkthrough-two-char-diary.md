# Agent Vault — First Real-World Walkthrough: 二字日记

## Project Profile

- **Type:** WeChat mini-program (native WXML/WXSS/JS)
- **Phase:** mvp
- **Repo:** https://github.com/gunqiuwang/two-char-diary
- **Path:** C:\Users\guoku\Desktop\two-char-diary (WSL: /mnt/c/Users/guoku/Desktop/two-char-diary)
- **Obsidian Vault:** C:\Users\guoku\Documents\Obsidian Vault

## Init Results

| Metric | Value |
|--------|-------|
| Vault files created | 13 |
| Templates | 4 |
| Reports | 1 (setup report) |
| Wikilinks | 21 |
| Metadata compliance | 100% (all files have type/confidence/last_updated/reviewed_by) |
| Vault score | 81/100 (Good) |

### Score Breakdown

| Dimension | Score | Weight | Notes |
|-----------|-------|--------|-------|
| Confidence | 76% | 35% | 10/13 files at high confidence |
| Freshness | 100% | 30% | All files created today |
| Completeness | 100% | 20% | All mvp-phase files present |
| Review | 38% | 15% | Only 5/13 files reviewed by human |

**To reach 93:** User reviews the 8 unreviewed files.

## Obsidian Setup

### Symlink Failed

Initial attempt with WSL symlink:
```bash
ln -sf "/mnt/c/Users/guoku/Desktop/two-char-diary/docs/vault" \
  "/mnt/c/Users/guoku/Documents/Obsidian Vault/Projects/二字日记"
```

**Result:** Obsidian reported `EACCES: permission denied, lstat 'C:\Users\guoku\Documents\Obsidian Vault\Projects\二字日记'`

**Root cause:** WSL `ln -sf` creates Linux symlinks that Windows processes cannot follow. The symlink exists in WSL filesystem but Windows sees it as an inaccessible file.

### Junction Fixed It

```powershell
powershell.exe -Command "cmd /c mklink /J 'C:\Users\guoku\Documents\Obsidian Vault\Projects\二字日记' 'C:\Users\guoku\Desktop\two-char-diary\docs\vault'"
```

**Result:** `Junction created for ... <<===>> ...`

After clicking "重新加载" in Obsidian, all 13 vault files appeared in the sidebar and Graph View showed `00_HOME` as the central hub with 21 links.

**Key lesson:** `mklink /J` (directory junction) does NOT require admin privileges, unlike `mklink /D` (symlink). Always use `/J` for WSL→Windows vault linking.

### Obsidian Default Files

Obsidian auto-created `未命名.base` and `欢迎.md` in the vault root. These are safe to delete — they are Obsidian defaults, not vault content.

## Pitfalls Encountered

1. **WSL symlink invisible to Windows Obsidian** — `ln -sf` creates Linux symlinks. Must use `mklink /J` (junction) from PowerShell.

2. **cmd.exe UNC path warning** — When WSL CWD is a UNC path (`\\wsl.localhost\...`), `cmd.exe` warns "UNC paths are not supported" but still executes the command. Safe to ignore.

3. **Obsidian deep link with space in vault name** — `obsidian://open?vault=Obsidian%20Vault` may fail. Manual open via Obsidian UI is more reliable.

4. **Project had no `docs/` directory** — Must create both `docs/vault/` AND `assets/intake/reports/` during init.

5. **PowerShell .NET screenshot** — Need `Add-Type -AssemblyName System.Windows.Forms` AND `System.Drawing` before `CopyFromScreen`.

## Data Sources Used

| Source | What It Provided |
|--------|-----------------|
| `git log --oneline -10` | Commit history, current HEAD |
| `git status --short` | Modified files, untracked files |
| `README.md` | Project description, design specs, color palette |
| `PROJECT-REVIEW.md` | Complete feature inventory, known issues, architecture decisions |
| `miniprogram/app.json` | Page routes (5 pages) |
| `miniprogram/project.config.json` | Build settings, platform config |
| `.gitignore` | What to exclude (used for security rules) |

**Lesson:** `PROJECT-REVIEW.md` was a goldmine — it had everything needed for vault init. If a project has a review/assessment document, read it FIRST.
