# 生成各集 md、总览,并转成网页片段
import os, glob, markdown
import gen
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
EPDIR = os.path.join(HERE, "..", "episodes")
os.makedirs(EPDIR, exist_ok=True)
rows = []
for i in range(1, 25):
    no = f"{i:02d}"
    gen.build(no)
    ep = gen.load(no)
    t = sum(s["secs"] for sc in ep["scenes"] for s in sc["shots"])
    n = sum(len(sc["shots"]) for sc in ep["scenes"])
    sg = sum(len(gen.segments(sc)) for sc in ep["scenes"])
    txt = open(os.path.join(HERE, "out", f"ep{no}.md"), encoding="utf-8").read()
    open(os.path.join(EPDIR, f"ep{no}.md"), "w", encoding="utf-8").write(txt)
    open(os.path.join(SITE, f"ep{no}.html"), "w", encoding="utf-8").write(markdown.markdown(txt, extensions=["tables", "fenced_code"]))
    rows.append(f"| [第{ep['cn']}集《{ep['title']}》](#ep{no}) | {ep['jq']} | {gen.fmt_secs(t)} | {n} | {sg} | {ep['summary'][:50]}… |")
md = open(os.path.join(HERE, "overview_static.md"), encoding="utf-8").read().replace("{{EP_TABLE}}", "\n".join(rows))
open(os.path.join(EPDIR, "00-overview.md"), "w", encoding="utf-8").write(md)
open(os.path.join(SITE, "overview.html"), "w", encoding="utf-8").write(markdown.markdown(md, extensions=["tables", "fenced_code"]))
print("ok")
