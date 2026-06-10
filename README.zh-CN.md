# 🏛️ Project Vault

> 项目的知识库。AI 开工前先读它——不用再重复解释。

[English](README.md) | [中文](#快速开始)

## 这是什么

换 AI、换模型、换平台——都没关系。项目知识存在 `docs/vault/` 里，任何 AI 读 `00_HOME.md` 就能理解一切。

## 快速开始

```bash
# 1. 下载
git clone https://github.com/guqiuwang/project-vault.git /tmp/project-vault

# 2. 初始化（一条命令，自动检测）
bash /tmp/project-vault/templates/init-vault.sh /你的/项目 "项目名"

# 3. 告诉你的 AI
# "修改前先读 docs/vault/00_HOME.md。"
```

完事。

## 你会得到

```
your-project/
├── docs/vault/
│   ├── 00_HOME.md              ← AI 入口 + vault 过期检查
│   ├── 01_CURRENT_BASELINE.md  ← 当前状态
│   ├── 03_DO_NOT_TOUCH.md      ← 危险区域
│   └── ... (共 13 个文件)
└── assets/intake/reports/      ← 报告
```

支持 ChatGPT、Claude、Cursor、Copilot 等任何 AI。

## 更新内容 (v5.6.0)

### 🔴 Vault 启动同步 — vault 再也不会过期

最大痛点：agent 做完活忘了更新 vault。3 天后 vault 变成废纸。

**解决方案：** 每个 `00_HOME.md` 顶部加了过期检查。agent 第一眼就看到：

```
1. 读 00_HOME.md 的 last_updated
2. git log --oneline --since=<last_updated>
3. 有未同步的 commit → 先跑 vault sync，再开始干活
```

不需要 cron job，不需要额外 token。只是一条 `git log` 命令。

**之前：**
```
agent 进项目 → 干了 3 天 → 37 个 commit → vault 一个字没更新 → 💀
```

**之后：**
```
agent 进项目 → 读 00_HOME.md → git log 发现 37 个未同步 commit
→ 先跑 vault sync → vault 保持最新 → ✅
```

### Karpathy 编码原则 (v5.5.0)

来自 [Andrej Karpathy 的观察](https://x.com/karpathy/status/2015883857489522876)，四条规则写进每个 agent prompt：

| 原则 | 规则 |
|------|------|
| **先想后写** | 不要假设。列出前提。不确定就问。 |
| **简单优先** | 最少代码。200 行能缩到 50 行吗？ |
| **精准改动** | 只碰需要碰的。每一行都对得上需求。 |
| **目标驱动** | 定义验收标准。循环直到验证通过。 |

## 4 个脚本

| 脚本 | 用途 | 什么时候用 |
|------|------|-----------|
| `init-vault.sh` | 创建 vault | 新项目 |
| `sync-vault.sh` | 同步变更 | 代码改动后 |
| `audit-vault.sh` | 健康检查 | 每月 / 交接前 |
| `setup-obsidian-link.sh` | 连接 Obsidian | 可视化知识图谱 |

## Obsidian（可选）

```bash
bash /tmp/project-vault/templates/setup-obsidian-link.sh /你的/项目/docs/vault "项目名"
```

打开 Obsidian → 侧边栏看到项目 → `Ctrl+G` 看知识图谱。多个项目不同颜色。

<img src="assets/graph-view-demo.png" width="500" alt="Obsidian 知识图谱 — 4 个项目带颜色编码">

详见 [QUICKSTART.md](QUICKSTART.md)。

## 许可证

MIT
