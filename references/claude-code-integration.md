# Claude Code + Project Vault Integration

## Problem

Claude Code (and Codex) are standalone CLI agents. They don't automatically read your vault. Without explicit integration, they'll start from scratch every session.

## Solution: CLAUDE.md at Project Root

Claude Code automatically reads `CLAUDE.md` at the project root on startup. Create one that points to the vault.

### Template

```markdown
# Project Name

## 开工纪律（Agent 必读）

开工前必读：
1. `docs/vault/00_HOME.md` — 项目入口、当前状态
2. `docs/vault/01_CURRENT_BASELINE.md` — 最新版本/部署状态
3. `docs/vault/03_DO_NOT_TOUCH.md` — 禁区

边做边更新 vault。改完代码后立即更新对应的 vault 文件。
不要把所有 vault 更新攒到最后一口气写。

## 项目结构

（简要列出关键目录和文件）
```

### Real Example: 媒体写作项目

```markdown
# 媒体写作项目

## 开工纪律（Agent 必读）

开工前必读：
1. `docs/vault/00_HOME.md` — 项目入口、当前状态
2. `docs/vault/01_CURRENT_BASELINE.md` — 最新版本/部署状态
3. `docs/vault/03_DO_NOT_TOUCH.md` — 禁区

子项目也要读 vault：
- 公众号/梦黎井 → 读 `公众号/梦黎井/docs/vault/00_HOME.md`

边做边更新 vault。改完代码后立即更新对应的 vault 文件。

## 项目结构

```
公众号/梦黎井/     # BDSM/小众心理学公众号
小红书/            # 待建
X/                 # 待建
抖音/              # 待建
```
```

### For Codex

Codex reads `.codex.md` or `AGENTS.md` at project root. Same content, different filename.

```bash
# Both at project root
CLAUDE.md          # Claude Code reads this
AGENTS.md          # Codex reads this (also Claude Code fallback)
```

If using both, keep CLAUDE.md and AGENTS.md identical, or have one reference the other.

## Multi-Level Vault Projects

For projects with nested vaults (e.g., media-writing → 梦黎井):

```
project-root/
├── CLAUDE.md                       # Points to top-level vault
├── docs/vault/00_HOME.md           # Top-level vault
└── 子项目/
    ├── docs/vault/00_HOME.md       # Sub-project vault
    └── CLAUDE.md                   # Optional: points to sub-vault
```

The top-level CLAUDE.md should list sub-projects and their vault paths.

## Pitfalls

1. **CLAUDE.md must be at project root.** Claude Code looks for it where you run `claude`, not in subdirectories.
2. **Keep it short.** CLAUDE.md is injected into every prompt. A 2000-line CLAUDE.md wastes tokens. Point to vault files instead.
3. **Don't duplicate vault content in CLAUDE.md.** Just point to it.
4. **CLAUDE.md survives git.** It should be committed, not in .gitignore.
