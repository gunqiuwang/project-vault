import markdown, glob, os, re
m = {"00-design.md": "design", "01-prologue.md": "prologue", "40-shots.md": "shots", "41-shots2.md": "shots2"}
for p in glob.glob("md/*.md"):
    b = os.path.basename(p)
    mm = re.match(r"\d+-ch(\d+)\.md", b)
    if mm: m[b] = f"ch{mm.group(1)}"
    if b == "99-epilogue.md": m[b] = "epilogue"
    me = re.match(r"\d+-ep(\d+)\.md", b)
    if me: m[b] = f"ep{me.group(1)}"
out = []
for src, name in m.items():
    if os.path.exists("md/" + src):
        open(f"site/{name}.html", "w").write(markdown.markdown(open("md/" + src).read(), extensions=["tables", "fenced_code"]))
        out.append(name)
print(" ".join(sorted(out)))
