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

See [QUICKSTART.md](QUICKSTART.md) for more.

## License

MIT
