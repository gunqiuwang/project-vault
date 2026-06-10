# GitHub Actions Debugging via API

## Problem

`gh` CLI isn't authenticated, or browser isn't available. Need to check workflow run status.

## Solution: GitHub REST API (public, no auth needed for public repos)

### List recent workflow runs

```bash
curl -s "https://api.github.com/repos/OWNER/REPO/actions/runs?per_page=5" | python3 -c "
import json,sys
d=json.load(sys.stdin)
if 'message' in d:
    print(f'Error: {d[\"message\"]}')
else:
    for r in d.get('workflow_runs',[]):
        conclusion = r['conclusion'] or ''
        print(f'{r[\"status\"]:12} {conclusion:12} {r[\"created_at\"]:25} {r[\"name\"]}')"
```

### Check specific run's jobs

```bash
RUN_ID=27164935946
curl -s "https://api.github.com/repos/OWNER/REPO/actions/runs/$RUN_ID/jobs" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for j in d.get('jobs',[]):
    print(f'{j[\"name\"]:30} {j[\"conclusion\"]}')
    for s in j.get('steps',[]):
        c = s.get('conclusion','') or ''
        print(f'  → {s[\"name\"]:25} {c}')"
```

### Common conclusions

| Conclusion | Meaning |
|-----------|---------|
| `success` | All steps passed |
| `failure` | A step failed |
| `skipped` | `if:` condition not met (often intentional) |
| `cancelled` | Workflow was cancelled |
| `action_required` | Needs manual approval |

### Private repos

For private repos, the public API returns 404. Options:
1. `gh auth login` first, then use `gh run list`
2. Use a Personal Access Token: `curl -H "Authorization: token ghp_xxx" ...`

## Real-World Example: worldcup-2026

```bash
# Check automation status
curl -s "https://api.github.com/repos/gunqiuwang/worldcup-2026/actions/runs?per_page=5" | python3 -c "
import json,sys
d=json.load(sys.stdin)
for r in d.get('workflow_runs',[]):
    conclusion = r['conclusion'] or ''
    print(f'{r[\"status\"]:12} {conclusion:12} {r[\"created_at\"]:25} {r[\"name\"]}')"

# Output:
# completed    skipped      2026-06-08T22:12:22Z      Update Live Scores & Simulate
# completed    failure      2026-06-08T20:27:59Z      Update World Cup News
```

Interpretation:
- **Live Scores = skipped** → Normal. Tournament hasn't started (June 11). The `if:` condition correctly skips.
- **News = failure** → Script bug. `fetch_news.py` hit an error in GitHub's environment.

## Pitfalls

1. **Private repos need auth.** Public API returns 404 for private repos.
2. **`skipped` ≠ failure.** Check the workflow's `if:` conditions — `skipped` is often intentional.
3. **Rate limit.** Unauthenticated: 60 req/hour. Authenticated: 5000 req/hour.
4. **Conclusion is null while running.** A `status: "in_progress"` with `conclusion: null` means it's still going.
5. **Check both `status` and `conclusion`.** `status` = lifecycle (queued/in_progress/completed), `conclusion` = outcome (success/failure/skipped).

## Fixing Common Workflow Failures

### Exit code 128 on `git push`

**Symptom:** Workflow runs but `git push` step fails with exit code 128.

**Root cause:** Default `GITHUB_TOKEN` doesn't have write permission.

**Fix:** Add `permissions: contents: write` to the job:
```yaml
jobs:
  update-news:
    runs-on: ubuntu-latest
    permissions:
      contents: write    # ← required for git push
```

### Schedule stops triggering

**Symptom:** Cron workflow stops running after a few days. No new runs appear.

**Root cause:** GitHub pauses scheduled workflows on low-activity repos (known behavior).

**Fix:** Add a `push` trigger alongside `schedule`. Pushing code re-activates the schedule:
```yaml
on:
  schedule:
    - cron: '0 */2 * * *'
  workflow_dispatch:
  push:
    branches: [master]
    paths:
      - 'scripts/fetch_news.py'        # only re-trigger on relevant changes
      - '.github/workflows/update-news.yml'
```

### Script runs but no commit produced

**Symptom:** Workflow completes with `success` but no new commit appears.

**Root cause:** Script fetched data but `git diff --cached --quiet` found no changes (all data was duplicate or filtered out). Common when:
- RSS source is unreachable from GitHub runners (timeout)
- Keyword filter is too strict
- Single source dominates all slots, pushing others out

**Diagnosis:** Check the run logs for the step output. If `📥 本次抓取: 0 条` or sources show `❌`, that's the issue.

### Multi-source RSS with interleaved sorting

When a Python script fetches from multiple RSS/web sources, one source with many articles can crowd out all others (e.g., zhibo8 has 100+ articles, ESPN has 15, but all 30 slots go to zhibo8).

**Fix: Source round-robin with per-source cap:**
```python
from collections import defaultdict

# Group articles by source
by_source = defaultdict(list)
for a in unique:
    by_source[a.get("source", "")].append(a)

# Interleave: max 60% from any single source
max_per_source = max(3, int(max_count * 0.6))
interleaved = []
source_keys = list(by_source.keys())
idx = 0
while len(interleaved) < max_count:
    added = False
    for src in source_keys:
        if idx < len(by_source[src]) and len(interleaved) < max_count:
            article = by_source[src][idx]
            count_so_far = sum(1 for a in interleaved if a.get("source") == src)
            if count_so_far < max_per_source:
                interleaved.append(article)
                added = True
    idx += 1
    if not added:
        break
```
