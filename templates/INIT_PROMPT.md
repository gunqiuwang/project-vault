# Project Vault — Init Prompt

> Copy this entire prompt and paste it to your AI agent.

---

Create a project vault for this project. 

**Do NOT:** implement features, change code, deploy, or run destructive commands.
**Only:** inspect the project and create knowledge documentation.

## Steps

1. Run `git status` and `git log --oneline -10` to understand the project
2. Read key files: README.md, package.json/requirements.txt/pyproject.toml, .gitignore, any planning docs
3. Create `docs/vault/` directory
4. Create these files with real project data:

```
docs/vault/
├── 00_HOME.md              (project overview + "read this first" checklist)
├── 01_CURRENT_BASELINE.md  (current branch, commit, status)
├── 02_DECISION_LOG.md      (key decisions)
├── 03_DO_NOT_TOUCH.md      (danger zones + security rules)
├── 04_ARCHITECTURE.md      (tech stack, data flow)
├── 05_COMMANDS_AND_FILES.md (commands by risk level)
├── 06_DEPLOYMENT.md        (how to deploy)
├── 07_TESTING.md           (how to test)
├── 08_INCIDENTS.md         (incident log)
├── 09_AGENT_PROMPTS.md     (reusable prompts)
├── 10_REPORT_INDEX.md      (report index)
├── VAULT_SCHEMA.md         (vault rules)
└── VAULT_CHANGELOG.md      (operation log)
```

5. Every file must have this frontmatter:

```yaml
---
type: {file-type}
status: active
confidence: high | medium | low
last_updated: {today}
owner: agent | human | both
reviewed_by: agent | human | unreviewed
---
```

6. 00_HOME.md must include `aliases: ["项目名"]` so Obsidian Graph View can distinguish projects
7. 03_DO_NOT_TOUCH.md must include a "Security Rules" section (no API keys, no passwords in vault)
8. If .gitignore doesn't exist, create one
9. Create `assets/intake/reports/` directory
10. Run `git add docs/vault/ assets/ && git commit -m "docs: create project vault"`

**If information is unknown, write "Unknown — not verified" and set confidence: low. Never invent facts.**
