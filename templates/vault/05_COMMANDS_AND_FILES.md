---

type: commands-files
status: active
confidence: medium
last_updated: YYYY-MM-DD
owner: both
reviewed_by: unreviewed
---# ⚡ Commands & Files Inventory

> Know what you can run and what you can touch. Classify everything by risk.

## Command Classification

### 🟢 Safe Local Commands

| Command | Purpose | Side Effects | Expected Output |
|---------|---------|-------------|-----------------|
| `{CMD}` | {PURPOSE} | None | {OUTPUT} |

### 🟡 Test / Build Commands

| Command | Purpose | Writes to DB | Deploys |
|---------|---------|-------------|---------|
| `{CMD}` | {PURPOSE} | No | No |

### 🟡 Content / Data Generation

| Command | Purpose | Writes to DB | Deploys |
|---------|---------|-------------|---------|
| `{CMD}` | {PURPOSE} | {Yes/No} | No |

### 🟠 Database Commands

| Command | Purpose | Risk | Approval Required |
|---------|---------|------|-------------------|
| `{CMD}` | {PURPOSE} | High | Yes |

### 🔴 Deploy Commands

| Command | Purpose | Environment | Approval Required |
|---------|---------|------------|-------------------|
| `{CMD}` | {PURPOSE} | {Prod/Staging} | Always |

### ⛔ Dangerous Commands

| Command | What It Does | Why It's Dangerous |
|---------|-------------|-------------------|
| `{CMD}` | {EFFECT} | {REASON} |

## File Inventory

### Core Files

| File | Purpose | Read When | Update When | Risk |
|------|---------|-----------|-------------|------|
| `{FILE}` | {PURPOSE} | {WHEN} | {WHEN} | 🟢/🟡/🟠/🔴 |

### Configuration Files

| File | Purpose | Read When | Update When | Risk |
|------|---------|-----------|-------------|------|
| `{FILE}` | {PURPOSE} | {WHEN} | {WHEN} | 🟢/🟡/🟠/🔴 |

### Source Files

| File | Purpose | Read When | Update When | Risk |
|------|---------|-----------|-------------|------|
| `{FILE}` | {PURPOSE} | {WHEN} | {WHEN} | 🟢/🟡/🟠/🔴 |

## Package Scripts

> Extracted from `package.json`, `Makefile`, `pyproject.toml`, etc.

| Script | Command | Purpose |
|--------|---------|---------|
| `{SCRIPT_NAME}` | `{FULL_COMMAND}` | {PURPOSE} |
