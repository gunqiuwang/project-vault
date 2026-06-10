# Walkthrough: 世界杯信息站 (MatchLens AI)

## Project Profile

- **Type:** React SPA (世界杯信息站)
- **Phase:** mvp (功能完整，待部署)
- **Path:** D:\C1\worldcup2026 (WSL: /mnt/d/C1/worldcup2026)
- **Repo:** gunqiuwang/worldcup-2026 (SSH: git@github.com:gunqiuwang/worldcup-2026.git)
- **Domain:** 404969.xyz (Cloudflare, not yet deployed)
- **Stack:** React 18 + Vite + TypeScript + Tailwind CSS + Framer Motion
- **Obsidian Vault:** C:\Users\guoku\Documents\Obsidian Vault\Projects\世界杯

## Init (2026-06-02) — Prototype Phase

| Metric | Value |
|--------|-------|
| Vault files created | 13 |
| Source files | 项目构想.md (detailed planning) + index.html (1219-line demo) |
| Vault score | 75/100 (Good) |

**Lesson:** If a project has a detailed planning document, read it FIRST. It contains 80% of what the vault needs.

## Major Sync (2026-06-07) — Prototype → MVP

Project migrated from vanilla HTML to React+Vite+TS+Tailwind SPA. Vault was 5 days stale.

### What Changed

| Area | Old (prototype) | New (mvp) |
|------|-----------------|-----------|
| Architecture | vanilla HTML + Cloudflare Workers | React 18 + Vite + TS + Tailwind + Framer Motion |
| Data | 3 sources (Elo/Form/ensemble) + 7 Python scripts | predictions.ts 唯一数据源 |
| Tabs | 5Tab | 4Tab (赛程/排名/分析/资讯) |
| News | None | fetch_news.py (ESPN+BBC RSS) via GitHub Action |
| Git | HTTPS (timeout in WSL) | SSH (git@github.com:gunqiuwang/xxx.git) |
| Bundle | N/A | JS 377KB / CSS 27KB |
| Dev server | Open index.html | `npm run dev` → port 4173 |

### Sync Approach (Reusable Pattern)

1. Read all 13 vault files to understand current state
2. Compare with actual project state (`git log`, file structure, `npm run build`)
3. Batch update all files via `execute_code` with `write_file` (faster than individual calls)
4. `git add docs/vault/ && git commit -m "docs: vault 全面同步"`
5. Calculate vault score

### Post-Sync Score

| Dimension | Before | After |
|-----------|--------|-------|
| Confidence | 61% | 92% |
| Freshness | stale | 100% |
| Completeness | 100% | 100% |
| Review | 30% | 0% (all agent-written) |
| **Total** | 75 | **82** |

## Analysis Page Refactor (2026-06-07)

**Problem:** Analysis page had 6 modules, 2 with fake/random data.

| Module | Issue | Action |
|--------|-------|--------|
| 赔率异动排行 | 异动方向用伪随机 `matchId % 3` 模拟 | 🔴 Deleted |
| 预测总览 | 势均力敌/碾压局计数，看完即弃 | 🔴 Deleted |
| 今日焦点 | 标题"今日"但没按日期过滤 | 🟡 Renamed to "焦点比赛" |
| 全场赔率一览 | 核心功能但排太低 | 🟢 Moved to top + 分组折叠 |

**New info hierarchy (user preference: most important on top):**
1. 🥇 全场赔率一览 (核心卖点)
2. 🥈 焦点比赛 (赔率最接近5场)
3. 🥉 爆冷预警 (扩展到10条 + 解释文案)
4. 4️⃣ 热门球队 (静态tier信息)

**Lesson:** When user says "把最关心的放上面", reorder components by user value, not by complexity or alphabetical order.

## News Pipeline v3 (2026-06-07)

**Problem:** news.json had 376 articles with no expiry, many not World Cup related.

**Fix:**
- Strict WC filter: must contain "世界杯"/"2026"/"FIFA" core words (team name alone not enough)
- 48h rolling window: auto-expire old articles
- Max 30 articles cap
- Merge old + new data (don't replace entirely)

**Pattern:** Data pipelines with rolling windows need: `load_existing() → merge_and_prune(old, new, max_age, max_count) → write`.

## Pitfalls Encountered

1. **D: drive path** — Project on D: not C:. Symlink script handled it correctly via `wslpath`.

2. **Staleness threshold** — Set to 7 days (not 30) because World Cup is fast-moving.

3. **Proactive vault loading** — User corrected: agent should read `docs/vault/00_HOME.md` at session START for any project with an existing vault, instead of asking "what do you want to do?" without context. The vault exists to survive context compression.

4. **HTTPS push timeout** — WSL environment: `git push` via HTTPS frequently times out. Switched to SSH (`git@github.com:gunqiuwang/xxx.git`). This is a durable WSL pattern.

5. **Continuous vault sync** — User corrected: agent must update vault DURING work, not batch at end. This became the "Continuous Sync Rule" in the main SKILL.md. Agent should write vault file changes incrementally as code is committed, then do a single "docs:" commit at the end to bundle them.

6. **Fake data in components** — Analysis page used `matchId` pseudo-random for "odds movement direction". User spotted it. Rule: any data shown to users must come from a real source or be clearly labeled as static/estimated. Never use Math.random to simulate live data.

## Key Decisions (Historical)

| Date | Decision | Why |
|------|----------|-----|
| 2026-06-01 | 深色科技感 + 金色 | 世界杯氛围 + 科技感 |
| 2026-06-01 | 移动端优先 | 用户主要在手机看比赛 |
| 2026-06-03 | React SPA 重写 | vanilla JS 不可维护 |
| 2026-06-05 | predictions.ts 唯一数据源 | 三套数据互相矛盾 |
| 2026-06-05 | 5Tab → 4Tab | 信息碎片化 |
| 2026-06-06 | GitHub Action 新闻管道 | 免费可靠 |
| 2026-06-04 | SSH 替代 HTTPS | WSL 超时 |
