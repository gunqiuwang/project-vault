# Skill Lifecycle Management

`hermes skills disable` does NOT exist. The CLI has: browse, search, install, inspect, list, check, update, audit, uninstall, reset, publish, snapshot, tap, config.

## Disable a Skill

Move the skill directory to `.disabled/`:

```bash
mkdir -p ~/.hermes/skills/.disabled
mv ~/.hermes/skills/SKILL_NAME ~/.hermes/skills/.disabled/
```

Skills in `.disabled/` are invisible to the loader but recoverable.

## Disable by Name (when directory name ≠ skill name)

Some skills have directory names different from their `name:` field in SKILL.md (e.g., `mlops/training/trl-fine-tuning` contains `name: fine-tuning-with-trl`). Find by content:

```bash
# Find the directory containing a skill name
dir=$(find ~/.hermes/skills -name "SKILL.md" -exec grep -l "name: SKILL_NAME" {} \; | head -1)
skill_dir=$(dirname "$dir")
mv "$skill_dir" ~/.hermes/skills/.disabled/
```

## Re-enable

```bash
mv ~/.hermes/skills/.disabled/SKILL_NAME ~/.hermes/skills/
```

## Bulk Disable Pattern

```bash
for skill in skill1 skill2 skill3; do
  for dir in $(find ~/.hermes/skills -maxdepth 3 -name "SKILL.md" -exec grep -l "name: $skill" {} \;); do
    mv "$(dirname "$dir")" ~/.hermes/skills/.disabled/ 2>/dev/null && echo "✅ $skill"
  done
done
```

## Curator

The curator auto-archives stale agent-created skills. Manual archive:

```bash
hermes curator archive SKILL_NAME
```

Curator only touches `created_by: "agent"` skills. Bundled and hub-installed are off-limits.
