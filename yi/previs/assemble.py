# 把各镜头帧合成 1280x640 / 24fps 的预演片, 加镜号、台词字幕和风声
import os, subprocess, glob, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out")
SEG = os.path.join(OUT, "seg")
FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
os.makedirs(SEG, exist_ok=True)

# 镜号: (秒, 静止, 标签, 字幕)
SHOTS = {
    1: (10, True, "镜1 大远景 固定", "贞元三年  河西"),
    2: (8, False, "镜2 远景 固定", ""),
    3: (6, False, "镜3 中景 侧跟", "张归(旁白): 那年秋天, 我奉命去拆一座驿站。"),
    4: (10, False, "镜4 远景 缓推 [关键帧]", ""),
    5: (6, True, "镜5 特写 固定", ""),
    6: (6, False, "镜6 中景 缓摇上", ""),
    7: (5, False, "镜7 中景 固定", "张归: 有人吗?"),
    8: (6, True, "镜8 全景 固定", ""),
    9: (4, False, "镜9 近景 固定", ""),
    10: (10, False, "镜10 全景 门框构图 [关键帧]", ""),
    11: (4, True, "镜11 近景", ""),
    12: (5, False, "镜12 近景 双人", "卢七: 先喝口水。"),
    13: (4, False, "镜13 特写", "张归: 苦的。"),
    14: (5, True, "镜14 近景", "卢七: 苦泉。往西就没有水了。"),
    15: (4, True, "镜15 近景", "张归: 我们从西边来。"),
    16: (7, False, "镜16 特写 极缓推 [关键帧]", "卢七: ……那就是往东没有了。"),
    17: (6, True, "镜17 远景 固定", ""),
}

def txt(name, s):
    p = os.path.join(SEG, name)
    open(p, "w", encoding="utf-8").write(s)
    return p

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)

parts = []
for n, (secs, static, label, sub) in SHOTS.items():
    d = os.path.join(OUT, f"shot{n:02d}")
    frames = sorted(glob.glob(os.path.join(d, "*.png")))
    if not frames:
        print("missing shot", n); continue
    lab = txt(f"l{n}.txt", label)
    vf = [f"drawtext=fontfile={FONT}:textfile={lab}:x=16:y=14:fontsize=20:fontcolor=white@0.85:box=1:boxcolor=black@0.45:boxborderw=6",
          f"drawtext=fontfile={FONT}:text='《驿》第一集 白模预演 v1':x=w-tw-16:y=14:fontsize=18:fontcolor=white@0.6"]
    if sub:
        st = txt(f"s{n}.txt", sub)
        vf.append(f"drawtext=fontfile={FONT}:textfile={st}:x=(w-tw)/2:y=h-62:fontsize=30:fontcolor=white:borderw=2:bordercolor=black@0.8")
    out = os.path.join(SEG, f"{n:02d}.mp4")
    if static:
        src = ["-loop", "1", "-framerate", "24", "-t", str(secs), "-i", frames[0]]
    else:
        lst = txt(f"f{n}.txt", "".join(f"file '{f}'\nduration {1/12:.6f}\n" for f in frames) + f"file '{frames[-1]}'\n")
        src = ["-f", "concat", "-safe", "0", "-i", lst]
    run(["ffmpeg", "-v", "error", "-y", *src, "-vf", ",".join(vf) + f",fps=24,trim=duration={secs},setpts=PTS-STARTPTS",
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "20", "-r", "24", out])
    parts.append(out)

lst = txt("all.txt", "".join(f"file '{p}'\n" for p in parts))
total = sum(v[0] for k, v in SHOTS.items() if os.path.join(SEG, f"{k:02d}.mp4") in parts)
final = os.path.join(OUT, "yi_ep01_sc01-02_previs_v1.mp4")
# 风声: 低通的棕噪声, 轻微起伏
run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst,
     "-f", "lavfi", "-i", f"anoisesrc=color=brown:amplitude=0.25:duration={total},lowpass=f=500,volume=0.6,tremolo=f=0.15:d=0.5",
     "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-shortest", final])
print("OK", final, total, "s")
