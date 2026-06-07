# README Style Guide

User has strong preferences for how project READMEs should look. These override any default templates.

## Rules

1. **~50 lines max.** README is a quick intro, not a manual. If it scrolls more than one screen, it's too long.
2. **No professional tone.** This is a small helper tool, not an enterprise product. Don't use corporate language, badges, shields, or feature matrices.
3. **Screenshots > text.** One good screenshot explains more than 5 paragraphs. Use `<img src="..." width="500">` to control size.
4. **Chinese and English separate.** Two files: `README.md` (English) and `README.zh-CN.md` (Chinese). Link them at the top. Don't mix languages in one file.
5. **Image at bottom, 500px wide.** Not at the top. Not full-width. Bottom of the Chinese README.
6. **3-step quickstart.** Download → run command → tell AI. Nothing more.
7. **No feature tables.** A simple bullet list or one sentence is enough.
8. **Collapsible sections for platform-specific setup.** Use `<details><summary>` for Claude Code, Cursor, Copilot, Aider, etc.

## Bad Example (too long, too professional)

```markdown
# 🏛️ Project Vault
> A comprehensive knowledge management system for AI-agent-maintained projects...

## Features
| Feature | Description |
|---------|-------------|
| ... | ... |

## Architecture
## Configuration
## API Reference
## Contributing
## Changelog
```

## Good Example (~50 lines, simple)

```markdown
# 🏛️ Project Vault
> 给你的项目建一个「知识保险箱」，AI 开工前读一遍，就不会乱搞。

## 一句话说明
每次换 AI 都要重新解释项目？不用了。存进 docs/vault/，AI 读一遍就全懂。

## 30 秒上手
git clone ...
bash init-vault.sh /你的项目 "项目名"
告诉 AI：先读 00_HOME

## 你会得到什么
13 个文件，记录架构/命令/危险区/决策历史

## 4 个脚本
init / sync / audit / setup-obsidian

## 截图
<img src="assets/graph-view-demo.png" width="500" alt="...">
```
