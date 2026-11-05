# 《驿》第一集 第3-6场 白模预演 (沿用 previs.py 的基础函数)
# 用法: python previs2.py -- stills [镜号...] / shot 镜号...
import os, sys, math, random
ROOT = os.path.dirname(os.path.abspath(__file__))
_src = open(os.path.join(ROOT, "previs.py"), encoding="utf-8").read()
_src = _src.split("# ---------------------------------------------------------------- 各镜头")[0]
exec(_src)          # 带入 bpy, Vector, mat/prim/box/rod/hip_roof/person/horse/... 及 build_world
import bpy
from mathutils import Vector

# 镜号: (秒, 静止, 场次)
SHOTS = {
    "18": (10, True, 3), "19": (6, False, 3), "20a": (6, False, 3), "20b": (10, False, 3), "21": (5, False, 3),
    "22": (4, True, 3), "23": (9, False, 3), "24": (10, False, 3), "25": (4, True, 3), "26": (7, True, 3),
    "27": (5, False, 3), "28": (4, False, 3), "29": (5, True, 3), "30": (6, False, 3),
    "31": (10, True, 4), "32": (7, False, 4), "33": (5, True, 4), "34": (4, True, 4), "35": (4, True, 4),
    "36": (8, False, 4), "37": (5, False, 4), "38a": (6, True, 4), "39": (4, True, 4), "38b": (6, False, 4),
    "40": (6, False, 4), "41": (5, False, 4), "42": (6, False, 4), "43": (8, False, 4),
    "44": (10, True, 5), "45": (6, False, 5), "46": (7, False, 5), "47": (5, False, 5), "48": (8, True, 5),
    "49": (5, False, 5), "50": (4, True, 5), "51a": (7, False, 5), "51b": (7, False, 5), "52": (4, True, 5),
    "53": (5, True, 5), "54": (4, True, 5), "55": (7, False, 5), "56": (7, False, 5), "57": (6, False, 5),
    "58": (6, False, 6), "59": (8, False, 6), "60": (8, False, 6), "61": (5, True, 6), "62": (10, False, 6),
    "63": (6, False, 6), "64": (7, True, 6), "65": (5, False, 6), "66": (5, False, 6), "67": (5, False, 6),
}
ERA = {3: 787, 4: 736, 5: 736, 6: 787}

_M0 = M
def M(name):
    extra = {"young": (0.86, 0.86, 0.86), "father": (0.52, 0.53, 0.50), "kang": (0.40, 0.36, 0.34),
             "scholar": (0.92, 0.92, 0.90), "crowd": (0.45, 0.45, 0.45), "camel": (0.62, 0.58, 0.52),
             "paper": (0.85, 0.82, 0.72), "floor": (0.36, 0.34, 0.31), "ember": (0.9, 0.35, 0.08)}
    return extra[name] if name in extra else _M0(name)

STATE = {"era": 787, "interior": False}

# ---------------------------------------------------------------- 题诗壁
def poem_wall(era):
    img = bpy.data.images.load(os.path.join(ROOT, "tex", f"wall{era}.png"))
    m = bpy.data.materials.new(f"wall{era}")
    m.use_nodes = True
    nt = m.node_tree
    bsdf = nt.nodes["Principled BSDF"]
    bsdf.inputs["Roughness"].default_value = 0.95
    t = nt.nodes.new("ShaderNodeTexImage"); t.image = img
    nt.links.new(t.outputs["Color"], bsdf.inputs["Base Color"])
    bpy.ops.mesh.primitive_plane_add(size=1)
    o = bpy.context.object
    # 平面 UV: u 沿局部 X, v 沿局部 Y。转到墙上: 法线朝 -X, 局部 X -> 世界 -Y(左北右南), 局部 Y -> 世界 +Z
    o.scale = (6.6, 3.4, 1)
    o.rotation_euler = (math.pi / 2, 0, -math.pi / 2)
    o.location = (7.74, 35.5, 1.8)
    o.data.materials.append(m)
    return o

# ---------------------------------------------------------------- 驿站(两个年代)
def build_station():
    era, interior = STATE["era"], STATE["interior"]
    def wall(x0, y0, x1, y1):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / 4))
        for i in range(n):
            ax, ay = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            bx, by = x0 + (x1 - x0) * (i + 1) / n, y0 + (y1 - y0) * (i + 1) / n
            h = random.uniform(3.0, 3.5) if era == 787 else 3.6
            box(((ax + bx) / 2, (ay + by) / 2, h / 2), (abs(bx - ax) + 1.0, abs(by - ay) + 1.0, h))
    wall(-17, 12, -3.5, 12); wall(3.5, 12, 17, 12)
    wall(-17, 40, 17, 40); wall(-17, 12, -17, 40); wall(17, 12, 17, 40)
    for sx in (-1, 1):
        box((sx * 2.75, 12, 2.3), (1.5, 1.8, 4.6))
    box((0, 12, 4.9), (7.0, 1.8, 0.6), "wood")
    hip_roof(0, 12, 5.2, 8.6, 3.6, 1.5)
    box((0, 11.05, 4.85), (1.8, 0.1, 0.7), "wood")
    if era == 736:
        # 736: 门楼外侧新挂的铜铃(绳长, 站在地上伸手够得到)
        rod((1.9, 11.0, 4.6), (1.9, 11.0, 2.75), 0.01, "dark")
        bell = prim("cone", (1.9, 11.0, 2.62), m="bowl", vertices=16, radius1=0.13, radius2=0.05, depth=0.26)
        STATE["bell"] = bell
    else:
        # 787: 门楼上只剩铃绳的旧钩(铜铃已被卢七移到驿厅门内)
        rod((1.9, 11.0, 4.6), (1.9, 11.0, 4.3), 0.012, "dark")
    # 驿厅: 内景镜头做成空心, 有门窗
    if interior:
        build_hall_interior(era)
    else:
        box((0, 35.5, 1.9), (16, 7, 3.8))
        box((0, 31.95, 1.25), (2.2, 0.12, 2.5), "dark")
        for sx in (-5, 5):
            box((sx, 31.95, 2.0), (1.4, 0.12, 1.0), "dark")
    hip_roof(0, 35.5, 3.8, 18.4, 9.0, 2.0)
    # 马厩
    box((-14, 25, 3.0), (6.5, 14.5, 0.25), "wood", rot=(0, math.radians(-9), 0))
    for y in (18.2, 21.7, 25.2, 28.7, 32.2):
        rod((-10.9, y, 0), (-10.9, y, 2.55), 0.12, "wood")
    for y in (18, 32):
        box((-14, y, 1.0), (6, 0.4, 2.0))
    box((-15.6, 25, 0.5), (0.8, 12, 1.0), "wood")
    box((12.5, 33, 1.5), (6, 5, 3)); hip_roof(12.5, 33, 3, 7.2, 6.2, 1.3)
    box((13.5, 21, 1.5), (5, 10, 3)); hip_roof(13.5, 21, 3, 6.2, 11.2, 1.3)
    rod((11, 33.5, 3.5), (11, 33.5, 5.2), 0.25)
    prim("cyl", (6.5, 8.2, 0.3), m="set", vertices=24, radius=1.0, depth=0.6)
    prim("cyl", (6.5, 8.2, 0.605), m="water", vertices=24, radius=0.72, depth=0.02)
    if era == 787:
        build_willow(9.6, 9.6)
    else:
        # 736: 马厩里满是马, 院里有驿卒
        for i, y in enumerate((19.5, 23, 26.5, 30)):
            horse(f"sh{i}", (-14.2, y, 0), -90)
        if not interior:
            for i, (x, y, h) in enumerate(((-6, 24, 70), (-8.5, 21, -40), (4, 27, 160), (8, 18, 200))):
                person(f"soldier{i}", (x, y, 0), h, "crowd", topknot=True)

def build_hall_interior(era):
    # 驿厅内: x -8..8, y 32..39, 高 3.8; 门在南墙正中, 两扇窗
    T = 0.25
    box((0, 39.0, 1.9), (16.5, T, 3.8))                          # 北墙
    box((-8.0, 35.5, 1.9), (T, 7.25, 3.8))                       # 东墙
    box((8.0, 35.5, 1.9), (T, 7.25, 3.8))                        # 西墙(题诗壁)
    # 南墙: 门洞 x±1.1(高 2.5), 窗 x=±5(z 1.5-2.5, 宽 1.4)
    for (x0, x1) in ((-8.1, -5.7), (-4.3, -1.1), (1.1, 4.3), (5.7, 8.1)):
        box(((x0 + x1) / 2, 32.0, 1.9), (x1 - x0, T, 3.8))
    for x in (-5, 5):
        box((x, 32.0, 0.75), (1.4, T, 1.5)); box((x, 32.0, 3.15), (1.4, T, 1.3))
    box((0, 32.0, 3.15), (2.2, T, 1.3))
    box((0, 35.5, 3.85), (16.5, 7.25, 0.1), "wood")             # 顶棚
    for x in (-4, 0, 4):
        box((x, 35.5, 3.6), (0.25, 7.0, 0.3), "wood")            # 梁
    prim("plane", (0, 35.5, 0.01), (8, 3.5, 1), m="floor", size=2)
    poem_wall(era)
    # 火塘
    prim("cyl", (-2.0, 35.6, 0.1), m="set", vertices=16, radius=0.8, depth=0.2)
    for i in range(5):
        a = i / 5 * 6.28
        rod((-2.0 + math.cos(a) * 0.35, 35.6 + math.sin(a) * 0.35, 0.2), (-2.0, 35.6, 0.55), 0.05, "wood")
    # 桌、凳、油灯
    for (tx, ty) in ((-4.8, 37.6), (4.6, 37.9)):
        box((tx, ty, 0.7), (1.4, 0.8, 0.08), "wood")
        for dx in (-0.6, 0.6):
            for dy in (-0.3, 0.3):
                box((tx + dx, ty + dy, 0.35), (0.06, 0.06, 0.7), "wood")
        prim("cyl", (tx + 0.3, ty, 0.78), m="bowl", vertices=12, radius=0.07, depth=0.08)
    # 驿厅门内铜铃(787 由卢七移来; 736 时门内无铃)
    if era == 787:
        rod((1.3, 32.3, 2.55), (1.3, 32.3, 2.32), 0.008, "dark")
        STATE["bell"] = prim("cone", (1.3, 32.3, 2.2), m="bowl", vertices=16, radius1=0.12, radius2=0.05, depth=0.24)

# ---------------------------------------------------------------- 光
def lights(scene_no):
    sc = bpy.context.scene
    sun = [o for o in sc.objects if o.type == "LIGHT" and o.data.type == "SUN"][0]
    bg = sc.world.node_tree.nodes["Background"]
    def point(loc, energy, color, radius=0.1):
        bpy.ops.object.light_add(type="POINT", location=loc)
        l = bpy.context.object; l.data.energy = energy; l.data.color = color; l.data.shadow_soft_size = radius
        return l
    def area(loc, target, energy, color, size=2.0):
        bpy.ops.object.light_add(type="AREA", location=loc)
        l = bpy.context.object; l.data.energy = energy; l.data.color = color; l.data.size = size
        l.rotation_mode = "QUATERNION"
        l.rotation_quaternion = (Vector(target) - Vector(loc)).to_track_quat("-Z", "Y")
        return l
    if scene_no == 3:       # 黄昏转夜, 室内: 门窗进来的冷光 + 一束斜光
        bg.inputs[1].default_value = 0.35
        area((0, 30.5, 2.6), (6, 36, 1.0), 260, (0.85, 0.9, 1.0), 2.2)
        area((5, 30.6, 2.2), (7.6, 35.5, 1.6), 380, (1.0, 0.85, 0.7), 1.0)
        point((-2, 35.6, 0.6), 60, (1.0, 0.5, 0.2), 0.3)
    elif scene_no == 4:     # 736 清晨, 东边(-X)低角度暖光
        e = math.radians(14)
        s = Vector((-math.cos(e) * 0.9, -math.cos(e) * 0.43, math.sin(e))).normalized()
        sun.rotation_quaternion = (-s).to_track_quat("-Z", "Y")
        sun.data.color = (1.0, 0.86, 0.68); sun.data.energy = 4.6
        bg.inputs[0].default_value = (0.62, 0.58, 0.55, 1); bg.inputs[1].default_value = 0.7
    elif scene_no == 5:     # 736 夜, 炉火旺, 满屋灯
        sun.data.energy = 0.0
        bg.inputs[0].default_value = (0.05, 0.06, 0.1, 1); bg.inputs[1].default_value = 0.3
        point((-2, 35.6, 0.9), 700, (1.0, 0.55, 0.25), 0.5)
        for p in ((-4.5, 37.6, 0.95), (4.9, 37.9, 0.95), (6.6, 34.0, 2.6), (-6.5, 34.0, 2.6)):
            point(p, 120, (1.0, 0.7, 0.4), 0.1)
    elif scene_no == 6:     # 787 夜, 月光冷蓝, 余烬; 灯笼另加
        sun.data.energy = 0.5; sun.data.color = (0.6, 0.7, 1.0)
        bg.inputs[0].default_value = (0.05, 0.07, 0.12, 1); bg.inputs[1].default_value = 0.35
        area((0, 30.5, 2.6), (6, 36, 1.0), 90, (0.6, 0.7, 1.0), 2.2)
        point((-2, 35.6, 0.5), 70, (1.0, 0.4, 0.15), 0.4)
    return point

# ---------------------------------------------------------------- 人物
def lu(loc, h, **kw):    return person("lu", loc, h, "lu", stoop=0.22, topknot=True, **kw)
def zhang(loc, h, **kw): return person("zhang", loc, h, "zhang", braid=True, **kw)
def young(loc, h):       return person("young", loc, h, "young", topknot=True, height=0.82)
def father(loc, h):      return person("father", loc, h, "father", hat=True, height=1.02)
def kang(loc, h):
    p = person("kang", loc, h, "kang", height=1.04)
    prim("cone", (0, 0, 0.32), m="kang", parent=p["neck"], vertices=10, radius1=0.12, radius2=0.01, depth=0.34)
    return p
def scholar(loc, h, seated=False):
    p = person("scholar", loc, h, "scholar", hat=True)
    if seated:
        p["root"].location.z -= 0.45
        for hp in p["legs"]:
            hp.rotation_euler = (1.5, 0, 0)
    return p

def camel(name, loc, heading=0, drink=False):
    root = empty(name, loc, None, (0, 0, math.radians(heading)))
    prim("cyl", (0, 0, 1.6), (1, 1, 1), (math.pi / 2, 0, 0), m="camel", parent=root, vertices=14, radius=0.42, depth=1.7)
    for y in (0.35, -0.35):
        prim("sphere", (0, y, 2.05), (0.28, 0.32, 0.35), m="camel", parent=root, segments=12, ring_count=8)
    neck = empty(name + "_neck", (0, 0.8, 1.75), root, (0.0 if not drink else -1.2, 0, 0))
    prim("cyl", (0, 0.35, 0.35), m="camel", parent=neck, rot=(-0.8, 0, 0), vertices=10, radius=0.13, depth=1.0)
    box((0, 0.75, 0.75), (0.2, 0.5, 0.2), "camel", parent=neck)
    for (sx, sy) in ((-1, 1), (1, 1), (-1, -1), (1, -1)):
        hp = empty(f"{name}_leg{sx}{sy}", (sx * 0.22, sy * 0.6, 1.35), root)
        prim("cyl", (0, 0, -0.67), m="camel", parent=hp, vertices=8, radius=0.07, depth=1.35)
    return {"root": root, "neck": neck}

def caravan(x0, y=0.0, n=6, heading=90, f0=1, f1=None, dx=0):
    cs = []
    for i in range(n):
        c = camel(f"camel{i}", (x0 + i * 3.4, y + (0.5 if i % 2 else -0.4), 0), heading)
        if f1:
            p0 = tuple(c["root"].location)
            key(c["root"], f0, loc=p0); key(c["root"], f1, loc=(p0[0] + dx, p0[1], 0)); linear(c["root"])
        cs.append(c)
    return cs

def wipe(p, f0, f1, period=28, stop=None):
    """右臂抬起擦墙: 前后左右小幅摆动; stop 之后停住"""
    sh = p["arms"][1]
    f = f0
    end = stop if stop else f1
    while f <= end:
        ph = 2 * math.pi * (f - f0) / period
        key(sh, f, rot=(1.55 + 0.18 * math.sin(ph), 0.25 * math.cos(ph), 0))
        f += period / 4
    if stop:
        key(sh, f1, rot=list(sh.rotation_euler))
    cloth = prim("cube", (0, 0.62, 0), (0.08, 0.04, 0.08), m="paper", parent=sh, size=1)
    cloth.location = (0, 0, -0.6)

def fades(o, f0, f1, a0, a1):
    pass

# ---------------------------------------------------------------- 各镜头
def setup_shot(n, c, F):
    scene_no = SHOTS[n][2]
    STATE["era"] = ERA[scene_no]
    STATE["interior"] = scene_no in (3, 5, 6)
    build_world()
    point = lights(scene_no)
    WALL = 7.74
    if scene_no == 3:
        L = lu((7.1, 35.5, 0), -90); wipe(L, 1, F, stop=48 if n == "23" else None)
        Z = zhang((3.6, 34.2, 0), -75)
        ga = person("gampo", (0.9, 33.0, 0), -20, "tibet", braid=True, hat=True)
        no = person("norsang", (1.0, 32.4, 0), -10, "tibet", braid=True)
        scroll = None
        if n in ("20a", "20b", "22", "25"):
            for sh in Z["arms"]:
                sh.rotation_euler = (1.25, 0, 0)
            scroll = prim("cube", (0, 0.55, 0.0), (0.32, 0.01, 0.22), m="paper", parent=Z["waist"], size=1)
            scroll.location = (0, 0.52, 0.28)
            if n == "20a":
                key(scroll, 1, loc=(0, 0.52, 0.42)); scroll.scale = (0.32, 0.01, 0.02)
                scroll.keyframe_insert("scale", frame=1); scroll.scale = (0.32, 0.01, 0.24); scroll.keyframe_insert("scale", frame=60)
        if n == "18":
            aim(c, 1, (-6.8, 37.6, 1.7), (7.8, 34.4, 1.6), 22)
        elif n == "19":
            aim(c, 1, (6.3, 35.9, 1.95), (WALL, 35.9, 1.95), 55)
            aim(c, F, (6.3, 35.1, 1.95), (WALL, 35.1, 1.95), 55)
        elif n == "20a":
            aim(c, 1, (3.1, 33.4, 1.9), (3.9, 34.5, 1.2), 50)
        elif n == "20b":
            aim(c, 1, (7.35, 34.0, 1.6), (3.6, 34.2, 1.55), 40)
        elif n == "21":
            aim(c, 1, (5.9, 34.3, 1.7), (7.3, 35.5, 1.6), 45)
        elif n == "22":
            aim(c, 1, (6.6, 34.9, 1.62), (3.6, 34.2, 1.6), 50)
        elif n == "23":
            aim(c, 1, (6.4, 36.6, 1.7), (7.6, 35.4, 1.75), 50)
        elif n == "24":
            aim(c, 1, (3.8, 34.4, 1.65), (WALL, 35.5, 3.4), 22)
            aim(c, F, (3.8, 34.4, 1.65), (WALL, 35.5, 0.6), 22)
        elif n == "25":
            aim(c, 1, (5.6, 34.9, 1.62), (3.6, 34.2, 1.66), 65)
        elif n == "26":
            aim(c, 1, (7.15, 33.7, 1.6), (7.15, 35.5, 1.58), 60)
        elif n == "27":
            no["root"].rotation_euler = (0, -0.25, math.radians(-10))
            key(no["arms"][0], 1, rot=(0.1, -0.2, 0)); key(no["arms"][0], 40, rot=(0.6, -1.3, 0))
            b = STATE["bell"]
            for f, r in ((1, 0), (44, 0), (52, 0.35), (60, -0.28), (70, 0.2), (80, -0.12), (95, 0.06), (F, 0)):
                key(b, f, rot=(r, 0, 0))
            aim(c, 1, (3.6, 36.8, 1.65), (1.0, 32.6, 1.6), 32)
        elif n == "28":
            b = STATE["bell"]
            for f, r in ((1, 0.35), (10, -0.3), (20, 0.25), (32, -0.18), (46, 0.12), (62, -0.07), (80, 0.03), (F, 0)):
                key(b, f, rot=(r, 0, 0))
            aim(c, 1, (0.35, 33.3, 2.05), (1.3, 32.3, 2.25), 85)
        elif n == "29":
            aim(c, 1, (7.3, 34.75, 1.68), (7.16, 35.62, 1.68), 105)
        elif n == "30":
            aim(c, 1, (6.2, 36.2, 2.7), (WALL, 36.2, 2.7), 50)
            aim(c, F, (6.9, 36.2, 2.7), (WALL, 36.2, 2.7), 50)
    elif scene_no == 4:
        F_ = father((1.9, 10.35, 2.0), 0)                 # 在梯上
        Y = young((1.9, 9.0, 0), 0)
        for sh in Y["arms"]:
            sh.rotation_euler = (1.9, 0, 0)
        rod((1.6, 9.5, 0), (1.6, 10.95, 4.4), 0.04, "wood"); rod((2.2, 9.5, 0), (2.2, 10.95, 4.4), 0.04, "wood")
        for k in range(1, 9):
            t = k / 9
            rod((1.6, 9.5 + 1.45 * t, 4.4 * t), (2.2, 9.5 + 1.45 * t, 4.4 * t), 0.025, "wood")
        if n == "31":
            caravan(150, 0, 6)
            aim(c, 1, (12, -78, 3), (4, 15, 4), 35)
        elif n == "32":
            key(F_["arms"][1], 1, rot=(2.6, 0, 0)); key(F_["arms"][1], 60, rot=(2.9, 0, 0)); key(F_["arms"][1], F, rot=(2.7, 0, 0))
            aim(c, 1, (0.0, 7.2, 0.6), (1.8, 11.0, 3.2), 26)
        elif n in ("33", "35"):
            F_["neck"].rotation_euler = (-0.5, 0, 0)
            aim(c, 1, (1.3, 8.7, 1.45), (1.9, 10.4, 3.85), 55)
        elif n == "34":
            Y["neck"].rotation_euler = (0.6, 0, 0)
            aim(c, 1, (2.55, 9.9, 0.85), (1.9, 9.0, 1.36), 50)
        elif n == "36":
            caravan(260, 0, 7, 90, 1, F, -12)
            aim(c, 1, (9, -6, 2.0), (300, 0, 3.0), 55)
        else:
            # 卢父下梯后: 站在门洞前; 铃挂在门楼外侧
            F_["root"].location = (1.25, 10.1, 0); F_["root"].rotation_euler = (0, 0, math.radians(-30))
            Y["root"].location = (0.15, 9.9, 0); Y["root"].rotation_euler = (0, 0, math.radians(-120))
            for sh in Y["arms"]:
                sh.rotation_euler = (0, 0, 0)
            b = STATE["bell"]
            if n == "37":
                key(F_["arms"][1], 1, rot=(2.4, 0, 0))
                for f, r in ((1, 0), (12, 0.4), (24, -0.35), (36, 0.4), (48, -0.35), (60, 0.4), (72, -0.3), (90, 0.15), (F, 0.0)):
                    key(b, f, rot=(r, 0, 0))
                aim(c, 1, (1.05, 9.5, 2.55), (1.9, 11.0, 2.65), 65)
            elif n == "38a":
                F_["root"].rotation_euler = (0, 0, math.radians(90))
                Y["root"].rotation_euler = (0, 0, math.radians(-90))
                aim(c, 1, (0.7, 6.3, 1.45), (0.7, 10.0, 1.35), 40)
            elif n == "39":
                Y["root"].rotation_euler = (0, 0, math.radians(-90))
                aim(c, 1, (0.62, 9.96, 1.35), (0.15, 9.9, 1.36), 90)
            elif n == "38b":
                F_["root"].rotation_euler = (0, 0, math.radians(90))
                key(F_["neck"], 1, rot=(0, 0, 0)); key(F_["neck"], 100, rot=(0, 0, 0)); key(F_["neck"], 118, rot=(0.25, 0, 0)); key(F_["neck"], F, rot=(0, 0, 0))
                aim(c, 1, (0.2, 10.15, 1.72), (1.25, 10.1, 1.75), 60)
                aim(c, F, (0.45, 10.14, 1.72), (1.25, 10.1, 1.75), 60)
            elif n in ("40", "41", "42"):
                caravan(9, 1.2, 5, 90)
                K = kang((6.0, 3.6, 0), 135)
                if n == "40":
                    key(K["root"], 1, loc=(8.0, 2.4, 1.5)); key(K["root"], 18, loc=(7.6, 2.6, 0))
                    key(K["root"], F, loc=(3.0, 6.9, 0)); linear(K["root"])
                    aim(c, 1, (-3.5, 4.2, 1.6), (5.0, 5.0, 1.5), 30)
                elif n == "41":
                    K["root"].location = (2.4, 7.6, 0); K["root"].rotation_euler = (0, 0, math.radians(55))
                    F_["root"].rotation_euler = (0, 0, math.radians(-125))
                    for p in (K, F_):
                        key(p["arms"][0], 1, rot=(0.2, 0, 0)); key(p["arms"][0], 40, rot=(1.4, 0, 0))
                        key(p["arms"][1], 1, rot=(0.2, 0, 0)); key(p["arms"][1], 40, rot=(1.4, 0, 0))
                    aim(c, 1, (-1.8, 5.0, 1.6), (1.6, 8.6, 1.6), 38)
                elif n == "42":
                    K["root"].location = (0.9, 8.6, 0); K["root"].rotation_euler = (0, 0, math.radians(60))
                    Y["root"].location = (0.35, 9.45, 0); Y["root"].rotation_euler = (0, 0, math.radians(-120))
                    key(K["arms"][1], 1, rot=(0.3, 0, 0)); key(K["arms"][1], 50, rot=(1.2, 0, 0))
                    key(Y["arms"][0], 1, rot=(0, 0, 0)); key(Y["arms"][0], 60, rot=(1.0, 0, 0))
                    aim(c, 1, (-0.9, 7.6, 1.45), (0.65, 9.0, 1.45), 45)
            elif n == "43":
                F_["root"].location = (-30, 0, -10)
                Y["root"].location = (5.3, 8.3, 0); Y["root"].rotation_euler = (0, 0, math.radians(-90))
                key(Y["arms"][1], 1, rot=(0.6, 0, 0)); key(Y["arms"][1], 40, rot=(1.1, 0, 0)); key(Y["arms"][1], 80, rot=(0.6, 0, 0))
                cm = camel("drinker", (7.9, 6.5, 0), 120, drink=True)
                key(cm["neck"], 1, rot=(-1.0, 0, 0)); key(cm["neck"], 60, rot=(-1.25, 0, 0)); key(cm["neck"], 120, rot=(-1.05, 0, 0))
                caravan(14, 1.2, 4, 90)
                aim(c, 1, (4.2, 3.6, 1.5), (6.6, 8.2, 0.9), 32)
    elif scene_no == 5:
        # 满屋客商
        random.seed(11)
        for i in range(14):
            x, y = random.uniform(-7, 3.5), random.uniform(33, 38.5)
            if math.hypot(x + 2, y - 35.6) < 1.3:
                continue
            person(f"guest{i}", (x, y, 0), random.uniform(0, 360), "crowd", topknot=random.random() < 0.5,
                   hat=random.random() < 0.4)
        pipa = person("pipa", (-5.6, 34.2, -0.45), 20, "crowd", hat=True)
        for hp in pipa["legs"]:
            hp.rotation_euler = (1.5, 0, 0)
        S = scholar((4.6, 38.45, 0), 180, seated=True)
        Y = young((6.4, 35.9, 0), -70)
        K = kang((5.5, 34.6, 0), 30)
        tray = prim("cyl", (0, 0.35, 0.9), m="wood", parent=Y["root"], vertices=16, radius=0.2, depth=0.03)
        for sh in Y["arms"]:
            sh.rotation_euler = (1.4, 0, 0)
        if n == "44":
            Y["root"].location = (-1, 33.5, 0); K["root"].location = (-5, 36.5, 0)
            aim(c, 1, (-6.8, 37.6, 1.7), (7.8, 34.4, 1.6), 22)
        elif n == "45":
            K["root"].location = (-5, 36.5, 0)
            Y["root"].rotation_euler = (0, 0, math.radians(-75))
            walk_person(Y, 1, F - 30, (-3.5, 33.8, 0), (6.3, 35.6, 0), 24)
            for sh in Y["arms"]:
                sh.animation_data_clear(); sh.rotation_euler = (1.4, 0, 0)
            aim(c, 1, (-6.4, 37.4, 1.7), (4.0, 35.0, 1.2), 26)
        elif n == "46":
            K["root"].location = (-5, 36.5, 0)
            aim(c, 1, (6.35, 35.85, 1.3), (WALL, 36.6, 1.2), 26)
            aim(c, F, (6.35, 35.85, 1.3), (WALL, 36.6, 3.4), 26)
        elif n == "47":
            walk_person(K, 1, 50, (4.0, 34.0, 0), (5.5, 34.6, 0), 26)
            aim(c, 1, (4.0, 37.2, 1.5), (6.0, 35.3, 1.4), 38)
        elif n == "48":
            K["root"].rotation_euler = (0, 0, math.radians(60))
            aim(c, 1, (6.8, 35.95, 1.55), (5.5, 34.6, 1.75), 60)
        elif n == "49":
            key(S["arms"][1], 1, rot=(0.2, 0, 0)); key(S["arms"][1], 30, rot=(2.2, 0, 0.3)); key(S["arms"][1], 50, rot=(1.7, 0, 0.3)); key(S["arms"][1], 70, rot=(2.2, 0, 0.3))
            aim(c, 1, (6.6, 35.0, 1.4), (4.6, 38.4, 1.15), 40)
        elif n == "50":
            S["root"].rotation_euler = (0, 0, math.radians(-110))
            S["arms"][1].rotation_euler = (1.75, 0, 0)
            aim(c, 1, (4.0, 38.0, 1.3), (WALL, 38.3, 3.2), 45)
        elif n in ("51a", "53", "55"):
            if n == "55":
                key(S["neck"], 1, rot=(0, 0, 0)); key(S["neck"], 60, rot=(0, 0, 0)); key(S["neck"], 110, rot=(0, 0, 0.9))
            aim(c, 1, (4.95, 36.9, 1.32), (4.6, 38.45, 1.27), 62)
            if n == "51a":
                aim(c, F, (4.88, 37.25, 1.32), (4.6, 38.45, 1.27), 62)
        elif n == "51b":
            aim(c, 1, (6.6, 38.2, 3.0), (WALL, 38.2, 3.0), 55)
            aim(c, F, (6.6, 37.3, 3.0), (WALL, 37.3, 3.0), 55)
        elif n in ("52", "54"):
            Y["root"].location = (6.0, 37.2, 0); Y["root"].rotation_euler = (0, 0, math.radians(-160))
            Y["neck"].rotation_euler = (0.25, 0, 0)
            if n == "52":
                aim(c, 1, (5.85, 36.75, 1.38), (6.0, 37.2, 1.36), 85)
            else:
                aim(c, 1, (5.2, 37.0, 1.3), (6.0, 37.2, 1.33), 60)
        elif n == "56":
            Y["root"].location = (6.0, 37.2, 0)
            walk_person(Y, 1, 120, (6.0, 37.2, 0), (0.4, 32.8, 0), 18)
            key(Y["root"], 120, rot=(0, 0, math.radians(140))); key(Y["root"], 130, rot=(0, 0, math.radians(-30)))
            aim(c, 1, (-4.2, 37.0, 1.7), (3.0, 34.4, 1.1), 26)
        elif n == "57":
            aim(c, 1, (6.0, 37.7, 3.0), (WALL, 37.7, 3.0), 55)
            aim(c, F, (6.6, 37.7, 3.0), (WALL, 37.7, 3.0), 55)
    elif scene_no == 6:
        ga = person("gampo", (-3.6, 35.0, 0.2), 0, "tibet", braid=True, hat=True)
        ga["root"].rotation_euler = (math.pi / 2, 0, math.radians(80))
        no = person("norsang", (-0.6, 36.6, 0.2), 0, "tibet", braid=True)
        no["root"].rotation_euler = (math.pi / 2, 0, math.radians(-100))
        if n == "58":
            L = lu((7.1, 37.7, 0), -90)
            sh = L["arms"][1]
            key(sh, 1, rot=(2.6, -0.4, 0)); key(sh, 80, rot=(2.6, 0.4, 0)); key(sh, F, rot=(2.6, 0.4, 0))
            prim("cube", (0, 0, -0.6), (0.08, 0.04, 0.08), m="paper", parent=sh, size=1)
            aim(c, 1, (6.6, 37.7, 3.0), (WALL, 37.7, 3.0), 55)
        elif n == "59":
            L = lu((-4.0, 37.0, 0), 180)
            lamp = point((-4.5, 37.6, 0.95), 0, (1.0, 0.7, 0.4))
            lamp.data.energy = 0; lamp.data.keyframe_insert("energy", frame=40)
            lamp.data.energy = 140; lamp.data.keyframe_insert("energy", frame=52)
            walk_person(L, 80, F, (-4.0, 37.0, 0), (-0.2, 32.6, 0), 30)
            aim(c, 1, (6.6, 37.4, 1.8), (-2.5, 34.5, 0.9), 22)
        elif n == "60":
            L = lu((0.0, 31.4, 0), 135)
            walk_person(L, 1, F, (0.0, 31.4, 0), (-11.6, 21.2, 0), 32)
            aim(c, 1, (2.0, 35.2, 1.6), (-12.0, 20.5, 1.0), 33)
        else:
            Z = zhang((6.4, 35.3, 0), -90)
            Z["arms"][1].rotation_euler = (1.2, 0, 0)
            lan = prim("cyl", (0, 0, -0.66), m="paper", parent=Z["arms"][1], vertices=12, radius=0.12, depth=0.28)
            lamp = point((6.75, 35.0, 1.35), 90, (1.0, 0.7, 0.4), 0.08)
            if n == "61":
                aim(c, 1, (2.4, 33.4, 1.6), (6.9, 35.4, 1.6), 38)
            elif n == "62":
                key(lamp, 1, loc=(7.0, 37.9, 2.2)); key(lamp, F, loc=(7.0, 33.4, 2.2)); linear(lamp)
                aim(c, 1, (6.3, 37.6, 2.2), (WALL, 37.6, 2.2), 45)
                aim(c, F, (6.3, 33.6, 2.2), (WALL, 33.6, 2.2), 45)
            elif n == "63":
                key(lamp, 1, loc=(7.1, 35.2, 2.1)); key(lamp, F, loc=(7.1, 35.2, 0.4)); linear(lamp)
                aim(c, 1, (6.4, 35.2, 1.5), (WALL, 35.2, 2.1), 40)
                aim(c, F, (6.4, 35.2, 1.5), (WALL, 35.2, 0.3), 40)
            elif n in ("64", "65", "66"):
                Z["root"].location = (6.9, 35.85, -0.45)
                for hp in Z["legs"]:
                    hp.rotation_euler = (1.7, 0, 0)
                lamp.location = (7.2, 36.3, 0.5)
                if n == "64":
                    Z["root"].location = (5.5, 37.2, -0.45)
                    lamp.location = (7.1, 35.6, 0.6)
                    aim(c, 1, (6.75, 35.25, 0.42), (WALL, 35.25, 0.36), 45)
                elif n == "65":
                    key(Z["arms"][0], 1, rot=(0.4, 0, 0)); key(Z["arms"][0], 50, rot=(1.25, 0, 0))
                    aim(c, 1, (5.9, 34.4, 0.95), (7.5, 35.4, 0.5), 40)
                elif n == "66":
                    key(Z["neck"], 1, rot=(0, 0, 0)); key(Z["neck"], 50, rot=(0, 0, 1.2))
                    aim(c, 1, (5.0, 36.9, 1.0), (6.9, 35.85, 0.9), 40)
            elif n == "67":
                Z["root"].location = (-30, 0, -10)
                b = STATE["bell"]
                for f, r in ((1, 0.08), (30, -0.07), (60, 0.09), (90, -0.06), (F, 0.05)):
                    key(b, f, rot=(r, 0, 0))
                aim(c, 1, (0.3, 33.5, 2.05), (1.3, 32.3, 2.22), 85)

def render_shot(n, mode):
    secs, static, _ = SHOTS[n]
    F = secs * FPS
    c = None
    # setup_shot 内部重建世界; 摄影机在建世界之后加
    global camera
    _cam = camera
    def cam_after():
        return _cam()
    STATE.pop("bell", None)
    # 先建世界, 再建相机并调用镜头逻辑
    class Dummy: pass
    setup_shot_with_cam(n, F)
    sc = bpy.context.scene
    sc.frame_start, sc.frame_end = 1, F
    sc.cycles.samples = 6
    if mode == "still":
        frames = [1 if static else F // 2]
        outdir = os.path.join(OUT, "stills2")
    else:
        frames = [1] if static else list(range(1, F + 1, 2))
        outdir = os.path.join(OUT, f"shot{n}")
    os.makedirs(outdir, exist_ok=True)
    for f in frames:
        sc.frame_set(f)
        sc.render.filepath = os.path.join(outdir, f"s{n}_{f:04d}.png" if mode == "still" else f"{f:04d}.png")
        if mode != "still" and os.path.exists(sc.render.filepath):
            continue
        bpy.ops.render.render(write_still=True)
    print(f"DONE shot {n} frames {len(frames)}", flush=True)

def setup_shot_with_cam(n, F):
    # build_world 在 setup_shot 里调用; 相机要在其后创建, 所以包一层
    orig = globals()["aim"]
    holder = {}
    def aim2(c, f, loc, target, lens):
        if "c" not in holder:
            holder["c"] = camera()
        orig(holder["c"], f, loc, target, lens)
    globals()["aim"] = aim2
    try:
        setup_shot(n, None, F)
    finally:
        globals()["aim"] = orig

if args[0] == "stills":
    for n in (args[1:] if len(args) > 1 else SHOTS):
        render_shot(n, "still")
elif args[0] == "shot":
    for n in args[1:]:
        render_shot(n, "anim")
