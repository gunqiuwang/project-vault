# 《驿》分集生成器: 每集一份结构化数据 -> 文档标签页 markdown
# 用法: python3 gen.py 02        生成 out/ep02.md
import re, sys, importlib.util, os, json

HERE = os.path.dirname(os.path.abspath(__file__))

import bible
ERA_TONE = bible.ERA_TONE
ERA_STYLE = bible.ERA_STYLE
SIZE_EN = [("大特写", "extreme close-up"), ("特写", "close-up"), ("近景", "close shot"), ("中景", "medium shot"),
           ("全景", "wide shot"), ("大远景", "extreme long shot"), ("远景", "long shot"), ("主观", "point-of-view shot"),
           ("双人", "two-shot"), ("黑场", "black frame")]
NAME_RE = None
PLACES = {"LU PU VILLAGE", "FERRY BOAT", "SILKWORM ROOM"}

def set_names(ep):
    global NAME_RE
    names = bible.anchor_names()
    for ln in (ep.get("anchors") or "").strip().splitlines():
        if ":" in ln and ln[:1].isupper():
            names.append(ln.split(":")[0].strip())
    names = sorted({n for n in names if n not in PLACES}, key=len, reverse=True)
    NAME_RE = re.compile("(" + "|".join(re.escape(n) for n in names) + ")")
LINE_RE = re.compile(r"([一-龥]{1,6})(?:[((]([^))]*)[))])?[::]“([^”]+)”")


def S(id, sm, pic, snd, secs, en, mv, key=False, out=None, era=None):
    return dict(id=str(id), sm=sm, pic=pic, snd=snd, secs=secs, en=en, mv=mv, key=key, out=out, era=era)


def load(no):
    import glob
    for p in sorted(glob.glob(os.path.join(HERE, "eps", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3], p)
        m = importlib.util.module_from_spec(spec)
        m.S = S
        spec.loader.exec_module(m)
        if no in getattr(m, "EPS", {}):
            return m.EPS[no]
    raise KeyError(no)


def mmss(t):
    return f"{int(t // 60):02d}:{t % 60:06.3f}"


def fmt_secs(t):
    return f"{int(t // 60)} 分 {int(t % 60):02d} 秒" if t >= 60 else f"{int(t)} 秒"


def size_en(sm):
    for cn, en in SIZE_EN:
        if cn in sm:
            return en
    return "shot"


def script_md(text):
    out = []
    for ln in text.strip().splitlines():
        ln = ln.strip()
        if not ln:
            continue
        m = re.match(r"^([一-龥]{1,6}(?:[((][^))]*[))])?)[::]\s*(.+)$", ln)
        if m and not ln.startswith("字幕") and len(m.group(1)) <= 14:
            out.append(f"**{m.group(1)}:** {m.group(2)}")
        elif ln.startswith("(") or ln.startswith("("):
            out.append(f"*{ln}*")
        else:
            out.append(ln)
    return "\n\n".join(out)


def segments(scene):
    """同一场内按 10-13 秒分段; 单镜超过 13 秒自成一段"""
    segs, cur, t = [], [], 0
    shots = [s for s in scene["shots"] if "黑场" not in s["sm"]]
    for s in shots:
        if cur and t + s["secs"] > 13:
            segs.append(cur); cur, t = [], 0
        cur.append(s); t += s["secs"]
    if cur:
        if segs and t < 6 and sum(x["secs"] for x in segs[-1]) + t <= 16:
            segs[-1] += cur
        else:
            segs.append(cur)
    return segs


def strip_ph(en):
    en = en.replace("[风格前缀], ", "")
    en = re.sub(r",?\s*\[(春|夏|秋|冬)\]", "", en)
    return en


def seg_prompt(ep, sc, seg, idx, nxt):
    T = sum(s["secs"] for s in seg)
    t = 0.0
    lines, timeline, cast = [], [], []
    for s in seg:
        a, b = t, t + s["secs"]
        for n in NAME_RE.findall(s["en"]):
            if n not in cast:
                cast.append(n)
        said = LINE_RE.findall(s["snd"])
        lt = a + 0.4
        say_txt = []
        for who, how, txt in said:
            dur = min(max(1.2, len(txt) * 0.27), b - lt - 0.2)
            if who == "旁白" or (how and ("旁白" in how or "画外" in how)):
                kind = "voice-over, off-screen, no lips move"
            elif how and "吐蕃" in how:
                kind = "on-screen line spoken in Tibetan, subtitled in post"
            else:
                kind = "on-screen line"
            if who == "旁白":
                who = "张归"
            lines.append(f"{mmss(lt)}–{mmss(lt + dur)} {who}({kind}): \"{txt}\"")
            say_txt.append(f'{who} says "{txt}" at {mmss(lt)}')
            lt += dur + 0.3
        body = strip_ph(s["en"])
        timeline.append(f"[{mmss(a)}–{mmss(b)} | SHOT {s['id']} — {size_en(s['sm'])}] {body}. Motion: {s['mv']}"
                        + (f". {'; '.join(say_txt)}." if say_txt else ""))
        t = b
    cuts = [mmss(sum(x["secs"] for x in seg[:i + 1])) for i in range(len(seg) - 1)]
    style = ERA_STYLE[sc["era"]]
    PRI = ["LU QI", "ZHANG GUI", "PRINCESS", "ZHAO", "WEI", "KANG", "A HENG", "LIU", "WANG", "LI CHENGZHI", "FATHER", "THE JIER"]
    ranked = list(cast)
    main = ranked[0] if ranked else None
    others = [c for c in cast if c != main]
    if nxt is None:
        endf = sc.get("out") or "hold the final image still for the last 0.5 s, wind keeps moving dust and cloth; it is the scene's last frame."
    else:
        endf = ("from the last 0.4 s, keep the subject moving in the same direction and speed so the next segment can continue the action; "
                "no new action starts in the last 0.4 s.")
    cast_rule = ((f"Only these characters may appear: {', '.join(cast)}" if cast else
                  "Only the unnamed hands, riders or figures written in the timeline below may appear, exactly as many as written")
                 + (f"; plus {sc['crowd']}" if sc.get("crowd") else "") + ". No other people, no silhouettes, no reflections, no extra animals.")
    p = [f"For this segment, generate exactly {T:g} s of cinematic animated video, 2:1 widescreen. <Audio {idx}> is this segment's audio, already cut; the local clock starts at 00:00."]
    if lines:
        p.append("Dialogue timing:\n" + "\n".join(lines))
    p.append(f"STYLE: [{style}]. Keep this painted look in every frame; never drift toward photorealism or 3D.")
    pic1 = ((f"Picture 1 ONLY defines {main}'s identity and appearance" + (f"; the character sheets of {', '.join(others)} are used the same way when supplied" if others else "") + ".\n")
            if main else "Picture 1 is not used in this segment (no named character).\n")
    p.append("REFERENCES:\n" + pic1 +
             "Picture 2 ONLY defines composition and camera position of the labelled shots. Ignore its materials and lighting.\n"
             f"Picture 3 ONLY defines the environment: {sc['env']}. Ignore any figure in it.")
    p.append("CAST RULE: " + cast_rule)
    p.append("ENVIRONMENT LOCK, CAMERA LAW, PERFORMANCE LAW: [通用法则].")
    p.append(f"TONE: {sc['tone']}.")
    p.append("CAMERA PLAN AND ACTION TIMELINE (local time):\n" + "\n".join(timeline))
    p.append("END FRAME / OUTGOING MATCH: " + endf)
    p.append(f"EDITING: {len(seg)} shot{'s' if len(seg) > 1 else ''}" + (f", hard cuts exactly at {', '.join(cuts)}" if cuts else "") + "; slow, held rhythm; no random quick cuts.")
    p.append("AVOID: [通用禁止项]")
    return "\n\n".join(p), T, lines


def build(no):
    ep = load(no)
    set_names(ep)
    if not ep.get("keep_ids"):
        n = 0
        for sc in ep["scenes"]:
            for s in sc["shots"]:
                n += 1
                s["id"] = str(n)
    total = sum(s["secs"] for sc in ep["scenes"] for s in sc["shots"])
    nshots = sum(len(sc["shots"]) for sc in ep["scenes"])
    md = [f"# 第{ep['cn']}集 · {ep['jq']}《{ep['title']}》", "## 本集概要", ep["summary"]]
    rows = [("目标时长", f"镜头合计 {fmt_secs(total)}({nshots} 个镜头),另加片头片尾")] + ep["info"]
    md.append("| 项目 | 内容 |\n|---|---|\n" + "\n".join(f"| {a} | {b} |" for a, b in rows))
    if ep.get("text_block"):
        md.append(ep["text_block"])
    md.append(f"**本集的情绪曲线:** {ep['curve']}")
    if ep.get("anchors"):
        md.append("### 本集新增锚点")
        md.append("```\n" + ep["anchors"].strip() + "\n```")
    md.append("## 分场剧本")
    for k, sc in enumerate(ep["scenes"], 1):
        md.append(f"### 第 {k} 场 {sc['head']}")
        md.append(script_md(sc["script"]))
    md.append("## 分镜表")
    md.append("分镜表里的“秒”是剪辑后的时长。视频工具每条固定 10 秒:10 秒以下的镜头生成后截取前段,动作写在前半段完成。标“关键帧”的镜头先出,其余以关键帧为参考图生成。")
    for k, sc in enumerate(ep["scenes"], 1):
        st = sum(s["secs"] for s in sc["shots"])
        md.append(f"### 第 {k} 场 {sc['short']} · {st} 秒")
        md.append("| 镜号 | 景别 / 运镜 | 画面 | 声音 / 台词 | 秒 |\n|---|---|---|---|---|\n" +
                  "\n".join(f"| {s['id']}{' 关键帧' if s['key'] else ''} | {s['sm']} | {s['pic']} | {s['snd']} | {s['secs']} |" for s in sc["shots"]))
    md.append("## 生成提示词")
    md.append("每个镜头两行:“图”是首帧提示词,“动”是图生视频的动态提示词。`[风格前缀]`、年代色调后缀和人物大写名后的 `[锚点]`,按总览页的通用块和锚点原样替换(季节色调四选一)。反向提示词统一用总览页的那一段。")
    for k, sc in enumerate(ep["scenes"], 1):
        md.append(f"### 第 {k} 场 {sc['short']}")
        for s in sc["shots"]:
            if "黑场" in s["sm"]:
                md.append(f"**镜 {s['id']} · 黑场**\n\n不生成,剪辑时加黑场与字幕。")
                continue
            tone = ERA_TONE[s.get("era") or sc["era"]]
            img = s["en"] if s["en"].startswith("[风格前缀]") else f"[风格前缀], {s['en']}, {tone}"
            md.append(f"**镜 {s['id']} · {s['pic'][:18]}{'…' if len(s['pic']) > 18 else ''}{'(关键帧)' if s['key'] else ''}**")
            md.append(f"```\n图:{img}\n动:{s['mv']}\n```")
    # 动画版
    md.append("## 动画版分段提示词")
    md.append("按 MiniMax H3 工作流:每段 10–13 秒一次生成,段内按时间轴排镜头。`[STYLE …]`、`[通用法则]`、`[通用禁止项]` 见总览页。Picture 2 用该段镜头已定稿的首帧拼成一张带镜号的构图图。")
    allsegs = []
    for k, sc in enumerate(ep["scenes"], 1):
        for sg in segments(sc):
            allsegs.append((k, sc, sg))
    trs = []
    blocks = []
    for i, (k, sc, sg) in enumerate(allsegs, 1):
        nxt = allsegs[i][2] if i < len(allsegs) and allsegs[i][0] == k else None
        prompt, T, lines = seg_prompt(ep, sc, sg, i, nxt)
        ids = f"{sg[0]['id']}–{sg[-1]['id']}" if len(sg) > 1 else sg[0]["id"]
        said = ";".join(f"{w}:“{x}”" for s in sg for w, h, x in LINE_RE.findall(s["snd"]))
        trs.append(f"| {i} | {k} | 镜 {ids} | {T:g} 秒 | {said or '—'} |")
        blocks.append(f"**第 {i} 段 · 第 {k} 场 · 镜 {ids} · {T:g} 秒**")
        blocks.append("```\n" + prompt + "\n```")
    md.append("| 段 | 场 | 镜头 | 时长 | 台词 |\n|---|---|---|---|---|\n" + "\n".join(trs))
    md += blocks
    text = "\n\n".join(md) + "\n"
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    open(os.path.join(HERE, "out", f"ep{no}.md"), "w", encoding="utf-8").write(text)
    print(f"ep{no}: {nshots} shots, {fmt_secs(total)}, {len(allsegs)} segments, {len(text)} chars")


if __name__ == "__main__":
    for no in sys.argv[1:]:
        build(no)
