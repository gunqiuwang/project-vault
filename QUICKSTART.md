# Quickstart — 3 Steps to Project Vault

[中文版](#中文版) | English

## Step 1: Download

```bash
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault
```

## Step 2: Initialize Your Project

**One command — auto-detects everything:**

```bash
bash /tmp/project-vault/templates/init-vault.sh /your/project "Your Project Name"
```

That's it. It auto-detects:
- Tech stack (React/Vue/Python/WeChat/etc.)
- Assets (images, audio, content)
- Backend structure
- Design files
- Recent git activity

## Step 3: Tell Your AI

```
Read docs/vault/00_HOME.md before making changes.
```

Works with ChatGPT, Claude, Gemini, Cursor, Copilot, or any AI.

---

## Optional: Connect Obsidian

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /your/project/docs/vault "Project Name"
```

Then open Obsidian — you'll see your project in the sidebar and Graph View.

## Optional: Platform Shortcuts

Store the prompt as a project file for one-command access:

| Platform | Setup | Command |
|----------|-------|---------|
| Claude Code | `cp templates/INIT_PROMPT.md .claude/commands/init-vault.md` | `/init-vault` |
| Cursor | `cp templates/INIT_PROMPT.md .cursor/rules/init-vault.md` | `@init-vault` |
| Copilot | `cp templates/INIT_PROMPT.md .github/copilot-init-vault.md` | `@workspace read .github/copilot-init-vault.md` |
| Aider | `cp templates/INIT_PROMPT.md .aider-init-vault.md` | `aider --read .aider-init-vault.md` |

## What You Get

After init, your project has:

```
docs/vault/
├── 00_HOME.md              ← Agent reads this first
├── 01_CURRENT_BASELINE.md  ← Current state
├── 03_DO_NOT_TOUCH.md      ← Danger zones
├── ... (13 files total)
```

Every AI agent task starts with `00_HOME.md`. Switch models, switch agents — one line is all you need.

---

## 中文版

### 第一步：下载

```bash
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault
```

### 第二步：初始化

```bash
bash /tmp/project-vault/templates/init-vault.sh /你的项目 "项目名"
```

自动检测技术栈、资源文件、设计稿、git 历史。

### 第三步：告诉 AI

```
先读 docs/vault/00_HOME.md，再开始工作。
```

ChatGPT、Claude、Gemini、Cursor、Copilot、豆包、Kimi……任何 AI 都行。

### 可选：连接 Obsidian

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /你的项目/docs/vault "项目名"
```

打开 Obsidian 就能看到项目知识图谱。

### 看看效果

仓库里有 `example-vault/` 目录，是一个完整的 demo vault，fork 后直接看。
