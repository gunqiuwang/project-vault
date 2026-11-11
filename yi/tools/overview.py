# 生成 site/overview.md, 并把各集 md 复制到 site/
import os, glob, shutil, re, importlib
import gen
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
EPDIR = os.path.join(HERE, "..", "episodes")
eps = []
for p in sorted(glob.glob(os.path.join(HERE, "eps", "ep*.py"))):
    no = os.path.basename(p)[2:4]
    gen.build(no)
    ep = gen.load(no)
    total = sum(s["secs"] for sc in ep["scenes"] for s in sc["shots"])
    n = sum(len(sc["shots"]) for sc in ep["scenes"])
    segs = sum(len(gen.segments(sc)) for sc in ep["scenes"])
    eps.append((no, ep, total, n, segs))
    shutil.copy(os.path.join(HERE, "out", f"ep{no}.md"), os.path.join(SITE, f"ep{no}.md"))
    shutil.copy(os.path.join(HERE, "out", f"ep{no}.md"), os.path.join(EPDIR, f"ep{no}.md"))

STATIC = open(os.path.join(HERE, "overview_static.md"), encoding="utf-8").read()
rows = "\n".join(f"| [第{ep['cn']}集《{ep['title']}》](#ep{no}) | {gen.fmt_secs(t)} | {n} | {sg} | {ep['summary'][:60]}… |" for no, ep, t, n, sg in eps)
anchors = "\n\n".join(f"**第{ep['cn']}集新增**\n\n```\n{ep['anchors'].strip()}\n```" for no, ep, *_ in eps if ep.get("anchors"))
md = STATIC.replace("{{EP_TABLE}}", rows).replace("{{ANCHORS}}", anchors)
open(os.path.join(SITE, "overview.md"), "w", encoding="utf-8").write(md)
open(os.path.join(EPDIR, "00-overview.md"), "w", encoding="utf-8").write(md)
print("overview ok,", len(eps), "episodes")

import markdown
for p in glob.glob(os.path.join(SITE, "*.md")):
    h = markdown.markdown(open(p, encoding="utf-8").read(), extensions=["tables", "fenced_code"])
    open(p[:-3] + ".html", "w", encoding="utf-8").write(h)
    os.remove(p)
print("html ok")
