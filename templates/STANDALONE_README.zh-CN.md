# 🏛️ Project Vault

> 项目操作系统 —— 人类可视化 + Agent 可执行。为每个项目创建结构化知识库，让任何 Agent（或人类）都能安全地理解、维护和扩展项目。

[English](README.md) | 中文

## 这是什么？

AI Agent 做项目时经常缺上下文——不知道什么能碰、什么命令能跑、架构怎么搭。**Project Vault** 通过在 `docs/vault/` 下创建结构化知识库来解决这个问题，Agent 每次动手前先读 vault。

不是"初始化就完事"——它是一套**完整生命周期系统**，包含初始化、同步、审计。

## 快速开始

### 第一步：把模板拿到你的项目里

**方式 A：直接下载**

1. 点击 GitHub 页面右上角 **Code → Download ZIP**
2. 解压，把 `templates/INIT_PROMPT.md` 复制到你的项目根目录

**方式 B：Git Clone**

```bash
git clone https://github.com/gunqiuwang/project-vault.git /tmp/project-vault
cp /tmp/project-vault/templates/INIT_PROMPT.md /你的项目路径/
```

**方式 C：Hermes Agent 用户**（无需下载，内置 Skill）

```markdown
Run project-vault with action: init
```

### 第二步：让 AI 读取 Prompt 并初始化 Vault

把 `INIT_PROMPT.md` 的内容粘贴给你正在用的 AI Agent。

适用于：ChatGPT、Claude、Gemini、通义千问、豆包、Kimi、DeepSeek……任何能对话的 AI。

AI 会自动：
1. 检查你的项目结构（只读，不改代码）
2. 在项目里创建 `docs/vault/` 目录
3. 填入 13 个结构化知识文件
4. 提交到 Git

**平台专属快捷方式**（存成项目文件后一条命令触发）：

<details>
<summary>Claude Code</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .claude/commands/init-project-vault.md
# 然后：/init-project-vault
```
</details>

<details>
<summary>Cursor</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .cursor/rules/init-project-vault.md
# 然后：@init-project-vault
```
</details>

<details>
<summary>GitHub Copilot</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .github/copilot-init-vault.md
# 然后：@workspace read .github/copilot-init-vault.md and execute it
```
</details>

<details>
<summary>Aider</summary>

```bash
cp /tmp/project-vault/templates/INIT_PROMPT.md .aider-init-vault.md
# 然后：aider --read .aider-init-vault.md
```
</details>

<details>
<summary>Windsurf / Codeium</summary>

```bash
mkdir -p .windsurf/rules
cp /tmp/project-vault/templates/INIT_PROMPT.md .windsurf/rules/init-project-vault.md
```
</details>

### 第三步：连接 Obsidian（可选但推荐）

Obsidian 是免费的笔记软件，可以可视化 vault 的知识图谱。

1. **下载 Obsidian**：[obsidian.md](https://obsidian.md)（免费，全平台）
2. **安装后运行连接脚本**：

```bash
# 自动检测你的系统（macOS / Linux / Windows / WSL）
bash /tmp/project-vault/templates/setup-obsidian-link.sh /你的项目路径/docs/vault "项目名"
```

3. **打开 Obsidian**，选择你的 Vault 目录
4. **左侧栏** 会显示所有 vault 文件，**Graph View**（Ctrl+G）展示知识图谱

### 第四步：日常使用

以后每次让 AI 做任务时，只加一句：

```
先读 docs/vault/00_HOME.md，再开始工作。
```

换模型、换 Agent、换平台——这一句就够了。

**AI 读完 00_HOME 就知道：**
- 项目是什么
- 代码在哪
- 什么不能碰
- 已知问题是什么
- 上次做到哪了
- 设计规范是什么

## 完整流程图

```
用户下载 Project Vault 模板
        ↓
粘贴 INIT_PROMPT.md 给 AI Agent
        ↓
AI 自动创建 docs/vault/（13 个文件）
        ↓
用户连接 Obsidian（可选）
        ↓
┌───────────────────────────────────────┐
│         日常开发循环                    │
│                                       │
│  AI 读 00_HOME → 理解项目 → 执行任务   │
│       ↓                               │
│  任务完成 → 更新 vault → Git commit    │
│       ↓                               │
│  Obsidian 自动刷新 → 用户审查/确认     │
│       ↓                               │
│  下次 AI 再读 00_HOME → 循环           │
└───────────────────────────────────────┘
```

## 6 个生命周期命令

| 命令 | 时机 | 作用 |
|------|------|------|
| `vault init` | 新项目 / 接手旧项目 | 从零创建 vault |
| `vault init --greenfield` | 空项目（只有想法） | 最小化初始化 |
| `vault sync` | 代码大改后 | 更新受影响的 vault 文件 |
| `vault audit` | 每月 / 交接前 | 健康检查，检测过期知识 |
| `vault upgrade` | 版本升级 / 阶段变更 | 迁移 vault 结构 |
| `vault score` | 任何时候 | 计算 vault 健康评分（0-100） |

## Vault 结构

```
docs/vault/
├── 00_HOME.md                    # Agent 入口页（唯一入口）
├── 01_CURRENT_BASELINE.md        # 当前真相：分支、提交、状态
├── 02_DECISION_LOG.md            # 为什么做了这些选择
├── 03_DO_NOT_TOUCH.md            # 🚫 危险区 + 安全规则
├── 04_ARCHITECTURE.md            # 技术栈、数据流
├── 05_COMMANDS_AND_FILES.md      # 能跑什么、能碰什么
├── 06_DEPLOYMENT.md              # 怎么部署
├── 07_TESTING_AND_VERIFICATION.md # 怎么验证
├── 08_INCIDENTS_AND_FIXES.md     # 出过什么问题
├── 09_AGENT_PROMPTS.md           # 可复用的 Agent prompt
├── 10_REPORT_INDEX.md            # 报告索引
├── VAULT_SCHEMA.md               # 项目规则 + 阈值
├── VAULT_CHANGELOG.md            # 操作日志
└── templates/                    # 模板文件

assets/intake/reports/            # 完整报告（不污染 Graph View）
```

## 项目阶段

Vault 会根据项目阶段自动调整：

| 阶段 | 说明 | 需要的文件 |
|------|------|----------|
| **idea** | 只有想法 | 00_HOME + 04_ARCHITECTURE |
| **prototype** | 有代码没部署 | + 01_BASELINE + 05_COMMANDS |
| **mvp** | 第一批用户 | + 03_DO_NOT_TOUCH + 06_DEPLOY + 07_TESTING |
| **growth** | 全部文件 | 13 个文件 |
| **maintenance** | 维护模式 | 聚焦 02_DECISIONS + 08_INCIDENTS |
| **sunset** | 下线 | 只保留 00_HOME + 03_DO_NOT_TOUCH |

## Obsidian 使用说明

### 连接方式

```bash
# 一行命令，自动检测系统
bash templates/setup-obsidian-link.sh /你的项目路径/docs/vault "项目名"
```

| 你的系统 | 脚本自动处理 |
|---------|------------|
| macOS | 创建 symlink |
| Linux | 创建 symlink |
| Windows | 创建 junction（不需要管理员） |
| WSL + Windows | 创建 junction（不需要管理员） |

### Graph View 链接纪律

为了让 Obsidian 的知识图谱保持清晰，我们定义了链接规则：

```
00_HOME（中枢，最大的节点）
├──→ 01_CURRENT_BASELINE
├──→ 03_DO_NOT_TOUCH
├──→ 05_COMMANDS_AND_FILES
├──→ 09_AGENT_PROMPTS（第二入口）
├──→ 10_REPORT_INDEX（报告入口）
└──→ 其他文件
```

- 核心文档可以互链
- 报告只进 REPORT_INDEX，不污染主图谱
- 模板不连核心逻辑
- 禁止环形链接（A→B→C→A）

### 在 Obsidian 里你能做什么

| 功能 | 用途 |
|------|------|
| **Graph View** | 看项目知识全景图，00_HOME 是中心 |
| **Backlinks** | 看哪些文件引用了当前文件 |
| **Search** | 全局搜索 vault 内容 |
| **直接编辑** | 在 Obsidian 里修改 vault 文件，AI 下次会读到 |
| **Dataview 插件** | 查询 `confidence: low` 或 `status: stale` 的文件 |

### 人机协作闭环

```
AI Agent 写 vault 文件 → Git commit
        ↓
Obsidian 自动刷新（文件监听）
        ↓
你在 Obsidian 里审查、批注、修改
        ↓
下次 AI Agent 读 00_HOME → 读到你确认的版本
```

## 标准化 Metadata

每个 vault 文件必须有：

```yaml
---
type: baseline          # 文件类型
status: active          # active / stale / archived
confidence: high        # high / medium / low
last_updated: 2026-06-02
owner: both             # agent / human / both
reviewed_by: human      # agent / human / unreviewed
---
```

在 Obsidian 里可以用 Dataview 插件查询：

```dataview
LIST FROM "docs/vault" WHERE confidence = "low"    -- 找不确定的内容
LIST FROM "docs/vault" WHERE status = "stale"      -- 找过期的文件
LIST FROM "docs/vault" WHERE reviewed_by = "unreviewed"  -- 找没人确认的
```

## 为什么需要它

| 没有 Vault | 有 Vault |
|-----------|---------|
| AI 改崩生产环境 | AI 先读 DO_NOT_TOUCH |
| AI 重写能跑的代码 | AI 知道什么不能动 |
| AI 跑危险命令 | AI 先查命令风险等级 |
| AI 编造事实 | AI 读 baseline 源头 |
| 决策没有记录 | 决策日志保留上下文 |
| 事故反复发生 | 事故日志防止重蹈覆辙 |
| 换 AI 要重新解释 | 读 00_HOME 就全明白了 |
| Vault 过期 | sync + audit 保持新鲜 |

## 包含的模板

| 文件 | 用途 |
|------|------|
| `INIT_PROMPT.md` | 完整初始化 prompt（粘贴给任何 AI） |
| `setup-obsidian-link.sh` | 跨平台 Obsidian 连接脚本 |
| `DECISION_TEMPLATE.md` | 决策记录模板 |
| `INCIDENT_TEMPLATE.md` | 事故记录模板 |
| `DEPLOY_REPORT_TEMPLATE.md` | 部署报告模板 |
| `AGENT_TASK_TEMPLATE.md` | AI Agent 任务模板 |
| `git-hook-post-commit` | Git hook（提醒同步 vault） |
| `ci-vault-check.yml` | GitHub Actions 健康检查 |

## 设计理念

1. **先读后写** — AI 必须理解后再改
2. **显式优于隐式** — 危险的东西写出来，不要假设
3. **活文档** — vault 跟着项目一起进化
4. **安全第一** — DO_NOT_TOUCH.md 防止最常见的 AI 错误
5. **定期审计** — 过期的知识比没有知识更危险
6. **人机共用** — AI 写结构化知识，人类在 Obsidian 里审查确认

## 贡献

1. Fork 这个仓库
2. 改进模板或添加新模板
3. 提交 PR

## 许可证

MIT — 自由使用，随意修改。

---

*"记录项目的最佳时间是项目开始时。第二好的时间是现在。"*
