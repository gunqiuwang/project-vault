# 🏛️ Project Vault

> 给你的项目建一个「知识保险箱」，任何 AI 开工前先读它，就不会乱搞。

English | [中文](#中文版)

## 一句话说明

每次换 AI、换模型、换平台，都要重新解释项目？**不用了。** 把项目知识存进 `docs/vault/`，AI 开工前读一遍就全懂。

## 30 秒上手

```bash
# 1. 下载
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault

# 2. 在你的项目里跑一行命令
bash /tmp/project-vault/templates/init-vault.sh /你的项目 "项目名"

# 3. 告诉你的 AI
# "先读 docs/vault/00_HOME.md，再开始工作。"
```

完事。

## 你会得到什么

```
你的项目/
├── docs/vault/
│   ├── 00_HOME.md           ← AI 入口（项目是什么、不能碰什么）
│   ├── 01_CURRENT_BASELINE.md ← 当前状态
│   ├── 03_DO_NOT_TOUCH.md   ← 危险区
│   └── ... (共 13 个文件)
└── assets/intake/reports/   ← 报告
```

换 ChatGPT、Claude、Cursor、Copilot、豆包、Kimi……加一句 `先读 00_HOME` 就行。

## 4 个脚本

| 脚本 | 干什么 | 什么时候用 |
|------|--------|----------|
| `init-vault.sh` | 创建 vault | 新项目开局 |
| `sync-vault.sh` | 同步变更 | 代码改了之后 |
| `audit-vault.sh` | 健康检查 | 每月 / 交接前 |
| `setup-obsidian-link.sh` | 连接 Obsidian | 想可视化看图谱 |

## 连接 Obsidian（可选）

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /你的项目/docs/vault "项目名"
```

打开 Obsidian → 左侧看到项目 → `Ctrl+G` 看知识图谱。多个项目各有不同颜色，一眼分清。

## 适用平台

Claude Code、Cursor、Copilot、Aider、ChatGPT、Gemini、豆包、Kimi……任何能读 prompt 的 AI。

详见 → [QUICKSTART.md](QUICKSTART.md)

## 许可证

MIT

---

# 中文版

## 一句话说明

给项目建个知识库，AI 开工前读一遍，不会乱改乱删。

## 30 秒上手

```bash
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault
bash /tmp/project-vault/templates/init-vault.sh /你的项目 "项目名"
# 然后告诉 AI：先读 docs/vault/00_HOME.md
```

## 你会得到什么

13 个 markdown 文件，记录了项目的架构、命令、危险区、决策历史。AI 换了、模型换了，读一遍就懂。

## 4 个脚本

- `init-vault.sh` — 建 vault
- `sync-vault.sh` — 同步变更
- `audit-vault.sh` — 健康检查
- `setup-obsidian-link.sh` — 连 Obsidian 看图谱

## 截图

<img src="assets/graph-view-demo.png" width="500" alt="Obsidian 里的知识图谱 — 4 个项目，颜色区分">

## 许可证

MIT
