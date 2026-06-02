# Agent Vault — Audit Methodology

## 12-Issue Systematic Audit (v4.1)

After agent-vault reached v4.0, a critical review found 12 gaps. This reference captures the methodology so it can be reused for any skill.

### How to Run the Audit

1. **Read the entire SKILL.md** as a new agent encountering it for the first time
2. **Cross-reference check** — every field name in one section vs every other section
3. **Directory check** — every path referenced but never created
4. **Rule contradiction check** — every "never"/"always" for internal contradictions
5. **Edge case check** — empty project, single file, no git, no package.json
6. **Multi-agent check** — what if two agents write the same file?
7. **Evolution check** — phase changes, version upgrades, project splits/merges

### Issue Categories

| Category | Example | Fix Pattern |
|----------|---------|-------------|
| Logic contradiction | "Reports not in vault" but setup report in vault | Remove contradiction |
| Missing creation | `assets/intake/reports/` never mkdir'd | Add to init flow |
| Inconsistent naming | `last_verified` vs `last_updated` | Global rename |
| Missing edge case | Empty project can't init | Add `--greenfield` mode |
| Missing lifecycle | No upgrade path | Add `vault upgrade` command |
| Missing governance | No write conflict protocol | Add file ownership table |
| Hardcoded values | 90-day staleness | Move to schema config |
| Security blind spot | Secrets could leak | Add security rules + scan |
| Missing concept | No project phase awareness | Add phase model |
| Missing accountability | No "who confirmed" | Add `reviewed_by` field |
| Missing operation | No split/merge | Document procedures |
| Missing metrics | No health score | Add weighted formula |

### Severity Levels

- **🔴 Logic defect** — contradictory rules, missing creation steps, inconsistent naming
- **🟡 Process gap** — missing lifecycle, governance, hardcoded values, security
- **🟢 Enhancement** — new concepts, accountability, operations, metrics

Fix 🔴 first (small effort, high impact), then 🟡, then 🟢.

### Lesson

After any skill reaches v2+, run this audit. The pattern: read as newbie → cross-references → edge cases → governance → evolution.
