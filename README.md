# 🏛️ Project Vault

> A knowledge vault for your projects. AI reads it before working — no more re-explaining.

[English](#quick-start) | [中文](README.zh-CN.md)

## What Is This

Switch AI, switch model, switch platform — doesn't matter. Store project knowledge in `docs/vault/`, any AI reads `00_HOME.md` and understands everything.

## Quick Start

```bash
# 1. Download
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault

# 2. Init your project (one command, auto-detects everything)
bash /tmp/project-vault/templates/init-vault.sh /your/project "Project Name"

# 3. Tell your AI
# "Read docs/vault/00_HOME.md before making changes."
```

Done.

## What You Get

```
your-project/
├── docs/vault/
│   ├── 00_HOME.md              ← AI entry (what's this project, what not to touch)
│   ├── 01_CURRENT_BASELINE.md  ← current state
│   ├── 03_DO_NOT_TOUCH.md      ← danger zones
│   └── ... (13 files total)
└── assets/intake/reports/      ← reports
```

Works with ChatGPT, Claude, Cursor, Copilot, or any AI.

## What's New (v5.5.0)

### Karpathy Coding Principles

Four rules from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls, integrated into every agent prompt:

| Principle | Rule |
|-----------|------|
| **Think Before Coding** | Don't assume. State assumptions. Ask when confused. |
| **Simplicity First** | Minimum code. 200 lines → 50 if possible. |
| **Surgical Changes** | Touch only what's needed. Every line traces to the request. |
| **Goal-Driven Execution** | Define success criteria. Loop until verified. |

### Vault Sync Workflow

Agent updates the vault **during** work, not after. Every code change syncs to the corresponding vault file immediately. No more "update vault later" — later never comes.

## 4 Scripts

| Script | What | When |
|--------|------|------|
| `init-vault.sh` | Create vault | New project |
| `sync-vault.sh` | Sync changes | After code changes |
| `audit-vault.sh` | Health check | Monthly / handoff |
| `setup-obsidian-link.sh` | Connect Obsidian | Visualize knowledge graph |

## Obsidian (Optional)

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /your/project/docs/vault "Project Name"
```

Open Obsidian → see project in sidebar → `Ctrl+G` for knowledge graph. Multiple projects show in different colors.

<img src="assets/graph-view-demo.png" width="500" alt="Obsidian knowledge graph — 4 projects with color coding">

See [QUICKSTART.md](QUICKSTART.md) for more.

## License

MIT
