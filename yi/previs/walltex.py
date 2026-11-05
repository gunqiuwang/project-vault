# 题诗壁贴图: 787(满墙、褪色)与 736(三分之一、墨新)
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, os
W, H = 1980, 1020            # 6.6m x 3.4m, 300px/m; 面向墙时左=北(最老), 右=南(门)
FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
POOL = "天地风沙月客行人马山河关塞西东归故乡春秋夜灯酒别离愁云雪长路远声寒烟草水泉驿城柳青白黄日暮孤舟去来不见问君何处可知千里万年一身无家明朝相送泪满衣花落空江南北今昔"
POEM = ["苦泉犹可饮", "离恨不堪尝", "明日西行客", "回头望故乡"]

def col(d, x, y, n, size, alpha, font):
    for i in range(n):
        d.text((x, y + i * size * 1.08), random.choice(POOL), font=font, fill=(20, 18, 16, alpha))

def make(era):
    random.seed(3 if era == 787 else 5)
    base = (214, 206, 190) if era == 787 else (238, 233, 222)
    im = Image.new("RGBA", (W, H), base + (255,))
    # 墙面斑驳
    d0 = ImageDraw.Draw(im)
    for _ in range(900 if era == 787 else 250):
        x, y, r = random.randint(0, W), random.randint(0, H), random.randint(6, 60)
        g = random.randint(-22, 10)
        d0.ellipse((x - r, y - r, x + r, y + r), fill=tuple(max(0, c + g) for c in base) + (255,))
    im = im.filter(ImageFilter.GaussianBlur(6))
    txt = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(txt)
    # 最老的一首: 左上角, 竖排, 从右往左
    ps = 66
    f = ImageFont.truetype(FONT, ps)
    x0 = 360
    for li, line in enumerate(POEM):
        for ci, ch in enumerate(line):
            if era == 787:
                a = 175 if (li == 0) else 28
            else:
                a = 235
            d.text((x0 - li * ps * 1.35, 60 + ci * ps * 1.1), ch, font=f, fill=(15, 13, 12, a))
    # 其余题诗: 一块块竖排
    right_limit = W - 30 if era == 787 else int(W * 0.36)
    x = 440
    while x < right_limit:
        size = random.randint(34, 80)
        ff = ImageFont.truetype(FONT, size)
        ncol = random.randint(3, 8)
        y0 = random.randint(30, 200)
        nrow = random.randint(5, int((H - 160 - y0) / (size * 1.08)))
        alpha = random.randint(55, 150) if era == 787 else random.randint(190, 245)
        for k in range(ncol):
            col(d, x + k * size * 1.3, y0, nrow, size, alpha, ff)
        # 下方再塞一块
        wtop = ncol * size * 1.3; wlow = 0
        if random.random() < (0.85 if era == 787 else 0.6):
            s2 = random.randint(30, 60); f2 = ImageFont.truetype(FONT, s2)
            yb = y0 + nrow * size * 1.08 + 40
            nb = int((H - 70 - yb) / (s2 * 1.08))
            if nb > 2:
                nk = random.randint(2, 6); wlow = nk * s2 * 1.3
                a2 = random.randint(40, 120) if era == 787 else random.randint(180, 240)
                for k in range(nk):
                    col(d, x + k * s2 * 1.3, yb, nb, s2, a2, f2)
        x += max(wtop, wlow) + random.randint(25, 70)
    if era == 787:
        # 墙脚炭画小马: 稚拙线条, 周围擦得干净
        hx, hy = 1050, 900
        d.ellipse((hx - 190, hy - 190, hx + 210, hy + 160), fill=(0, 0, 0, 0))
        d.ellipse((hx - 70, hy - 30, hx + 70, hy + 30), outline=(25, 25, 25, 230), width=6)
        for lx in (-50, -20, 25, 55):
            d.line((hx + lx, hy + 22, hx + lx + random.randint(-8, 8), hy + 95), fill=(25, 25, 25, 230), width=6)
        d.line((hx + 60, hy - 15, hx + 100, hy - 85), fill=(25, 25, 25, 230), width=6)
        d.ellipse((hx + 85, hy - 115, hx + 135, hy - 75), outline=(25, 25, 25, 230), width=6)
        d.line((hx - 70, hy - 5, hx - 115, hy + 30), fill=(25, 25, 25, 230), width=6)
        d.ellipse((hx + 115, hy - 100, hx + 121, hy - 94), fill=(25, 25, 25, 230))
        txt = txt.filter(ImageFilter.GaussianBlur(0.8))
    im = Image.alpha_composite(im, txt).convert("RGB")
    if era == 787:
        # 墙脚一带: 积灰更重, 唯小马周围擦净
        sh = Image.new("L", (W, H), 0); ds = ImageDraw.Draw(sh)
        ds.rectangle((0, H - 200, W, H), fill=70); ds.ellipse((900, 760, 1220, 1020), fill=0)
        sh = sh.filter(ImageFilter.GaussianBlur(30))
        im = Image.composite(Image.new("RGB", (W, H), (150, 140, 125)), im, sh)
    im.save(f"tex/wall{era}.png")

make(787); make(736); print("ok")
