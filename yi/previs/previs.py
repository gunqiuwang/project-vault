# 《驿》第一集 第1-2场 白模预演 (Blender / Cycles CPU)
# 用法: python previs.py -- stills            每镜渲一帧(中间帧)检查构图
#       python previs.py -- shot 10 [11 ...]   渲染指定镜头的动画帧
import bpy, math, sys, os, random
from mathutils import Vector

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "out")
FPS = 24
W, H = 1280, 640

args = sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else ["stills"]

# 镜号: (秒数, 是否静止镜头)
SHOTS = {
    1: (10, True), 2: (8, False), 3: (6, False), 4: (10, False), 5: (6, True),
    6: (6, False), 7: (5, False), 8: (6, True), 9: (4, False), 10: (10, False),
    11: (4, True), 12: (5, False), 13: (4, False), 14: (5, True), 15: (4, True),
    16: (7, False), 17: (6, True),
}

# ---------------------------------------------------------------- 基础
MATS = {}
def mat(name, rgb):
    if name in MATS:
        return MATS[name]
    m = bpy.data.materials.new(name)
    m.use_nodes = True
    bsdf = m.node_tree.nodes["Principled BSDF"]
    bsdf.inputs["Base Color"].default_value = (*rgb, 1)
    bsdf.inputs["Roughness"].default_value = 0.95
    MATS[name] = m
    return m

def M(name):
    return {
        "set": (0.60, 0.59, 0.57), "ground": (0.50, 0.49, 0.47), "road": (0.42, 0.40, 0.38),
        "dark": (0.03, 0.03, 0.03), "water": (0.06, 0.07, 0.08), "wood": (0.46, 0.44, 0.41), "eyes": (0.03, 0.03, 0.03),
        "lu": (0.80, 0.80, 0.80), "zhang": (0.30, 0.32, 0.36), "tibet": (0.22, 0.20, 0.19),
        "horse": (0.28, 0.26, 0.24), "hui": (0.72, 0.72, 0.72), "red": (0.55, 0.04, 0.03),
        "mount": (0.55, 0.57, 0.62), "bowl": (0.50, 0.45, 0.40),
    }[name]

def link(o, m):
    if m:
        o.data.materials.clear()
        o.data.materials.append(mat(m, M(m)))
    return o

def prim(kind, loc=(0, 0, 0), scale=(1, 1, 1), rot=(0, 0, 0), m="set", parent=None, **kw):
    f = {"cube": bpy.ops.mesh.primitive_cube_add, "cyl": bpy.ops.mesh.primitive_cylinder_add,
         "cone": bpy.ops.mesh.primitive_cone_add, "sphere": bpy.ops.mesh.primitive_uv_sphere_add,
         "plane": bpy.ops.mesh.primitive_plane_add}[kind]
    f(location=(0, 0, 0), **kw)
    o = bpy.context.object
    if parent:
        o.parent = parent
    o.location = loc
    o.rotation_euler = rot
    o.scale = scale
    return link(o, m)

def box(loc, size, m="set", parent=None, rot=(0, 0, 0)):
    return prim("cube", loc, (size[0] / 2, size[1] / 2, size[2] / 2), rot, m, parent, size=2)

def empty(name, loc=(0, 0, 0), parent=None, rot=(0, 0, 0)):
    o = bpy.data.objects.new(name, None)
    bpy.context.scene.collection.objects.link(o)
    if parent:
        o.parent = parent
    o.location = loc
    o.rotation_euler = rot
    return o

def rod(p1, p2, r, m="set", verts=8):
    p1, p2 = Vector(p1), Vector(p2)
    d = p2 - p1
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts, radius=r, depth=d.length, location=(p1 + p2) / 2)
    o = bpy.context.object
    o.rotation_mode = "QUATERNION"
    o.rotation_quaternion = d.to_track_quat("Z", "Y")
    return link(o, m)

def hip_roof(cx, cy, z0, w, d, h, m="set"):
    """唐式庑殿顶: 出檐深远、屋角平缓。"""
    import bmesh
    me = bpy.data.meshes.new("roof")
    bm = bmesh.new()
    rl = max(w - d, 0.2) / 2
    v = [bm.verts.new(p) for p in [(-w/2, -d/2, 0), (w/2, -d/2, 0), (w/2, d/2, 0), (-w/2, d/2, 0),
                                   (-rl, 0, h), (rl, 0, h)]]
    for f in [(0, 1, 5, 4), (1, 2, 5), (2, 3, 4, 5), (3, 0, 4), (0, 3, 2, 1)]:
        bm.faces.new([v[i] for i in f])
    bm.to_mesh(me)
    o = bpy.data.objects.new("roof", me)
    bpy.context.scene.collection.objects.link(o)
    o.location = (cx, cy, z0)
    link(o, m)
    # 屋脊两端鸱尾
    for sx in (-1, 1):
        box((cx + sx * rl, cy, z0 + h + 0.18), (0.18, 0.25, 0.42), m)
    return o

def key(o, f, loc=None, rot=None):
    if loc is not None:
        o.location = loc
        o.keyframe_insert("location", frame=f)
    if rot is not None:
        o.rotation_euler = rot
        o.keyframe_insert("rotation_euler", frame=f)

def linear(o):
    if o.animation_data and o.animation_data.action:
        act = o.animation_data.action
        curves = []
        try:
            curves = list(act.fcurves)
        except Exception:
            for layer in act.layers:
                for strip in layer.strips:
                    for bag in strip.channelbags:
                        curves += list(bag.fcurves)
        for fc in curves:
            for k in fc.keyframe_points:
                k.interpolation = "LINEAR"

# ---------------------------------------------------------------- 世界
def build_world():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    MATS.clear()
    random.seed(7)
    sc = bpy.context.scene
    sc.render.resolution_x, sc.render.resolution_y = W, H
    sc.render.fps = FPS
    sc.render.engine = "CYCLES"
    sc.cycles.device = "CPU"
    sc.cycles.samples = 8
    sc.cycles.use_denoising = True
    sc.cycles.max_bounces = 3
    sc.cycles.diffuse_bounces = 2
    sc.cycles.glossy_bounces = 0
    sc.cycles.transmission_bounces = 0
    sc.cycles.caustics_reflective = sc.cycles.caustics_refractive = False
    sc.render.use_persistent_data = True
    sc.render.image_settings.file_format = "PNG"
    sc.view_settings.view_transform = "AgX"
    try:
        sc.view_settings.look = "AgX - Medium High Contrast"
    except Exception:
        pass

    # 天空: 黄昏冷蓝灰
    w = bpy.data.worlds.new("sky")
    sc.world = w
    w.use_nodes = True
    w.node_tree.nodes["Background"].inputs[0].default_value = (0.42, 0.50, 0.62, 1)
    w.node_tree.nodes["Background"].inputs[1].default_value = 0.55
    # 低角度夕阳, 从西(+X)偏南来
    e = math.radians(13)
    s = Vector((math.cos(e) * 0.93, -math.cos(e) * 0.37, math.sin(e))).normalized()
    bpy.ops.object.light_add(type="SUN")
    sun = bpy.context.object
    sun.rotation_mode = "QUATERNION"
    sun.rotation_quaternion = (-s).to_track_quat("-Z", "Y")
    sun.data.energy = 4.2
    sun.data.angle = math.radians(1.5)
    sun.data.color = (1.0, 0.93, 0.85)

    # 地面、驿道(沿 X 轴, +X 为西)
    prim("plane", (0, 0, 0), (1, 1, 1), m="ground", size=16000)
    prim("plane", (0, 0, 0.02), (3000, 3.2, 1), m="road", size=1)
    # 进门的小路
    prim("plane", (0, 6, 0.021), (2.0, 6, 1), m="road", size=1)

    # 远山一圈(北面祈连山更高)
    for i in range(70):
        a = random.uniform(0, 2 * math.pi)
        dist = random.uniform(3800, 6500)
        x, y = math.cos(a) * dist, math.sin(a) * dist
        hgt = random.uniform(40, 110) * (2.0 if y > 0 else 1.0)
        prim("cone", (x, y, hgt / 2), (random.uniform(600, 1300), random.uniform(600, 1300), 1),
             (0, 0, random.uniform(0, 6)), m="mount", vertices=6, radius1=1, radius2=0.05, depth=hgt)

    # 汉代废烽燧
    prim("cone", (140, 210, 4.5), (1, 1, 1), (0, 0, 0.3), m="set", vertices=4, radius1=5, radius2=3.2, depth=9)

    build_station()

def build_station():
    # 夯土围墙: 南墙 y=12(门在中间), 北墙 y=40, 东墙 x=-17, 西墙 x=17; 分段高度略有起伏, 显得残旧
    def wall(x0, y0, x1, y1):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / 4))
        for i in range(n):
            ax, ay = x0 + (x1 - x0) * i / n, y0 + (y1 - y0) * i / n
            bx, by = x0 + (x1 - x0) * (i + 1) / n, y0 + (y1 - y0) * (i + 1) / n
            h = random.uniform(3.0, 3.5)
            box(((ax + bx) / 2, (ay + by) / 2, h / 2),
                (abs(bx - ax) + 1.0, abs(by - ay) + 1.0, h))
    wall(-17, 12, -3.5, 12); wall(3.5, 12, 17, 12)
    wall(-17, 40, 17, 40); wall(-17, 12, -17, 40); wall(17, 12, 17, 40)

    # 门楼: 两个门墩 + 额枋 + 庑殿顶; 门洞宽 4m
    for sx in (-1, 1):
        box((sx * 2.75, 12, 2.3), (1.5, 1.8, 4.6))
    box((0, 12, 4.9), (7.0, 1.8, 0.6), "wood")
    hip_roof(0, 12, 5.2, 8.6, 3.6, 1.5)
    box((0, 11.05, 4.85), (1.8, 0.1, 0.7), "wood")              # 空白匾额
    # 铜铃: 挂在门洞内右侧, 额枋下
    rod((1.75, 12.4, 4.6), (1.75, 12.4, 3.45), 0.008, "dark")
    prim("cone", (1.75, 12.4, 3.32), m="bowl", vertices=16, radius1=0.12, radius2=0.05, depth=0.24)

    # 驿厅(北), 门洞做暗
    box((0, 35.5, 1.9), (16, 7, 3.8))
    hip_roof(0, 35.5, 3.8, 18.4, 9.0, 2.0)
    box((0, 31.95, 1.25), (2.2, 0.12, 2.5), "dark")
    for sx in (-5, 5):
        box((sx, 31.95, 2.0), (1.4, 0.12, 1.0), "dark")
    # 马厩(东侧, 朝院内敞开)
    box((-14, 25, 3.0), (6.5, 14.5, 0.25), "wood", rot=(0, math.radians(-9), 0))
    for y in (18.2, 21.7, 25.2, 28.7, 32.2):
        rod((-10.9, y, 0), (-10.9, y, 2.55), 0.12, "wood")
    for y in (18, 32):
        box((-14, y, 1.0), (6, 0.4, 2.0))
    box((-15.6, 25, 0.5), (0.8, 12, 1.0), "wood")            # 马槽
    # 西侧灶房、厢房
    box((12.5, 33, 1.5), (6, 5, 3)); hip_roof(12.5, 33, 3, 7.2, 6.2, 1.3)
    box((13.5, 21, 1.5), (5, 10, 3)); hip_roof(13.5, 21, 3, 6.2, 11.2, 1.3)
    rod((11, 33.5, 3.5), (11, 33.5, 5.2), 0.25)                # 烟囱

    # 苦泉: 石砌井口
    prim("cyl", (6.5, 8.2, 0.3), m="set", vertices=24, radius=1.0, depth=0.6)
    prim("cyl", (6.5, 8.2, 0.605), m="water", vertices=24, radius=0.72, depth=0.02)

    build_willow(9.6, 9.6)

def build_willow(x, y):
    # 主干 + 6 根主枝 + 下垂枝条 + 几十根红绳
    top = Vector((x - 0.3, y + 0.2, 3.3))
    rod((x, y, 0), top, 0.42, "wood", 10)
    limbs = []
    for i in range(6):
        a = i / 6 * 2 * math.pi + 0.4
        end = top + Vector((math.cos(a) * 2.6, math.sin(a) * 2.6, random.uniform(1.6, 2.6)))
        rod(top, end, 0.16, "wood", 8)
        limbs.append((top, end))
    # 朝南(朝镜头)的一根矮枝, 专门挂红绳给镜 5 用
    low_end = top + Vector((-0.2, -2.4, 0.9))
    rod(top, low_end, 0.13, "wood", 8)
    limbs.append((top, low_end))
    for (a, b) in limbs:
        for k in range(28):
            t = random.uniform(0.25, 1.0)
            p = a.lerp(b, t) + Vector((random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5), 0))
            length = random.uniform(1.6, 3.4)
            q = p + Vector((random.uniform(-0.2, 0.2), random.uniform(-0.2, 0.2), -length))
            rod(p, q, 0.016, "wood", 5)
    cords = 0
    for (a, b) in limbs:
        n = 14 if b == low_end else 6
        for k in range(n):
            p = a.lerp(b, random.uniform(0.35, 1.0))
            q = p + Vector((random.uniform(-0.05, 0.05), random.uniform(-0.05, 0.05), -random.uniform(0.4, 0.9)))
            rod(p, q, 0.022, "red", 5)
            cords += 1

# ---------------------------------------------------------------- 人物与马
def person(name, loc, heading=0, m="lu", stoop=0.0, braid=False, topknot=False,
           spear=False, hat=False, parent=None, height=1.0):
    root = empty(name, loc, parent, (0, 0, math.radians(heading)))
    root.scale = (height, height, height)
    waist = empty(name + "_waist", (0, 0, 0.95), root, (-stoop, 0, 0))
    prim("cyl", (0, 0, 0.3), (0.19, 0.13, 0.3), m=m, parent=waist, vertices=12, radius=1, depth=2)
    prim("cone", (0, 0, -0.37), m=m, parent=waist, vertices=14, radius1=0.33, radius2=0.19, depth=0.75)
    neck = empty(name + "_neck", (0, 0, 0.62), waist)
    head = prim("sphere", (0, 0, 0.13), (0.1, 0.11, 0.12), m=m, parent=neck, segments=16, ring_count=10)
    box((0, 0.11, 0.12), (0.035, 0.05, 0.05), m, parent=neck)          # 鼻子, 标示朝向
    box((0, 0.10, 0.16), (0.15, 0.05, 0.035), "eyes", parent=neck)   # 眼带, 一眼看出脸朝哪
    if topknot:
        prim("sphere", (0, -0.02, 0.27), (0.045, 0.045, 0.045), m=m, parent=neck, segments=10, ring_count=6)
    if braid:
        prim("cyl", (0, -0.1, -0.12), m=m, parent=neck, rot=(0.15, 0, 0), vertices=6, radius=0.03, depth=0.55)
    if hat:
        prim("cyl", (0, 0, 0.24), m=m, parent=neck, vertices=12, radius=0.12, depth=0.1)
    arms = []
    for sx in (-1, 1):
        sh = empty(f"{name}_sh{sx}", (sx * 0.23, 0, 0.55), waist)
        prim("cyl", (0, 0, -0.28), m=m, parent=sh, vertices=8, radius=0.05, depth=0.56)
        arms.append(sh)
    legs = []
    for sx in (-1, 1):
        hp = empty(f"{name}_hip{sx}", (sx * 0.1, 0, 0.92), root)
        prim("cyl", (0, 0, -0.45), m=m, parent=hp, vertices=8, radius=0.065, depth=0.9)
        legs.append(hp)
    if spear:
        prim("cyl", (0.32, 0.12, 1.3), m="wood", parent=root, vertices=6, radius=0.02, depth=2.6)
    return {"root": root, "waist": waist, "neck": neck, "arms": arms, "legs": legs}

def horse(name, loc, heading=0, m="horse"):
    root = empty(name, loc, None, (0, 0, math.radians(heading)))
    prim("cyl", (0, 0, 1.25), (1, 1, 1), (math.pi / 2, 0, 0), m=m, parent=root, vertices=14, radius=0.32, depth=1.5)
    neck = empty(name + "_neck", (0, 0.65, 1.42), root)
    prim("cyl", (0, 0.22, 0.35), m=m, parent=neck, rot=(-0.55, 0, 0), vertices=10, radius=0.14, depth=0.85)
    box((0, 0.52, 0.62), (0.2, 0.56, 0.22), m, parent=neck, rot=(-0.95, 0, 0))
    for sx in (-1, 1):
        prim("cone", (sx * 0.06, 0.38, 0.86), m=m, parent=neck, vertices=6, radius1=0.04, radius2=0.0, depth=0.14)
    legs = []
    for (sx, sy) in ((-1, 1), (1, 1), (-1, -1), (1, -1)):
        hp = empty(f"{name}_leg{sx}{sy}", (sx * 0.18, sy * 0.58, 1.05), root)
        prim("cyl", (0, 0, -0.52), m=m, parent=hp, vertices=8, radius=0.065, depth=1.05)
        legs.append(hp)
    prim("cyl", (0, -0.85, 1.05), m=m, parent=root, rot=(0.35, 0, 0), vertices=6, radius=0.05, depth=0.7)
    return {"root": root, "neck": neck, "legs": legs}

def ride(rider_kw, h):
    p = person(**rider_kw, parent=h["root"], loc=(0, -0.05, 0.66))
    for sx, hp in zip((-1, 1), p["legs"]):
        hp.rotation_euler = (0.5, sx * 0.45, 0)
    return p

def walk_cycle(limbs_pairs, f0, f1, period=24, amp=0.4):
    """limbs_pairs: [(obj, phase)], 在 f0..f1 摆动"""
    f = f0
    while f <= f1:
        ph = 2 * math.pi * (f - f0) / period
        for o, p in limbs_pairs:
            r = list(o.rotation_euler)
            base = o.get("base_x", r[0])
            o["base_x"] = base
            r[0] = base + amp * math.sin(ph + p)
            key(o, f, rot=r)
        f += period / 4

def walk_person(p, f0, f1, p0, p1, period=26):
    key(p["root"], f0, loc=p0); key(p["root"], f1, loc=p1); linear(p["root"])
    walk_cycle([(p["legs"][0], 0), (p["legs"][1], math.pi)], f0, f1, period, 0.35)
    walk_cycle([(p["arms"][0], math.pi), (p["arms"][1], 0)], f0, f1, period, 0.15)

def walk_horse(h, f0, f1, p0, p1, period=30):
    key(h["root"], f0, loc=p0); key(h["root"], f1, loc=p1); linear(h["root"])
    walk_cycle([(h["legs"][0], 0), (h["legs"][3], 0), (h["legs"][1], math.pi), (h["legs"][2], math.pi)],
               f0, f1, period, 0.35)

# ---------------------------------------------------------------- 摄影机
def camera():
    bpy.ops.object.camera_add()
    c = bpy.context.object
    bpy.context.scene.camera = c
    c.data.sensor_fit = "HORIZONTAL"
    c.data.sensor_width = 36
    c.data.clip_end = 10000
    return c

def aim(c, f, loc, target, lens):
    loc, target = Vector(loc), Vector(target)
    c.location = loc
    c.rotation_euler = (target - loc).to_track_quat("-Z", "Y").to_euler()
    c.data.lens = lens
    c.keyframe_insert("location", frame=f)
    c.keyframe_insert("rotation_euler", frame=f)
    c.data.keyframe_insert("lens", frame=f)

# ---------------------------------------------------------------- 各镜头
def riders_on_road(x, y=0.0, heading=90):
    """三骑: 张归在前, 甘布、诺桑在后。heading 90 = 朝东(-X)走。"""
    hz = horse("h_zhang", (x, y, 0), heading)
    hg = horse("h_gampo", (x + 3.2, y + 1.6, 0), heading)
    hn = horse("h_norsang", (x + 6.0, y + 0.4, 0), heading)
    pz = ride(dict(name="zhang", m="zhang", braid=True), hz)
    ride(dict(name="gampo", m="tibet", braid=True, spear=True, hat=True), hg)
    ride(dict(name="norsang", m="tibet", braid=True), hn)
    return [hz, hg, hn], pz

def ride_along(hs, f0, f1, dx):
    for h in hs:
        p0 = tuple(h["root"].location)
        walk_horse(h, f0, f1, p0, (p0[0] + dx, p0[1], p0[2]))

def setup_shot(n, c, frames):
    F = frames
    if n == 1:      # 大远景: 戈壁黄昏, 驿道横贯, 空无一人
        aim(c, 1, (420, -12, 3), (420, 400, -4), 24)
    elif n == 2:    # 远景: 三个骑马小点从右侧入画, 缓慢向左
        hs, _ = riders_on_road(520)
        ride_along(hs, 1, F, -30)
        aim(c, 1, (470, -70, 2.5), (490, 300, 3), 40)
    elif n == 3:    # 中景侧跟: 张归侧脸
        hs, _ = riders_on_road(420)
        ride_along(hs, 1, F, -9.6)
        aim(c, 1, (420.3, -5.6, 2.35), (420.3, 0, 2.25), 65)
        aim(c, F, (410.7, -5.6, 2.35), (410.7, 0, 2.25), 65)
    elif n == 4:    # 远景缓推: 孤立的驿站, 老柳; 三骑从右侧远处接近
        hs, _ = riders_on_road(44)
        ride_along(hs, 1, F, -14)
        aim(c, 1, (12, -78, 3), (4, 15, 4), 35)
        aim(c, F, (11, -60, 3), (4, 15, 4), 35)
    elif n == 5:    # 特写: 柳枝上的红绳
        aim(c, 1, (4.6, 7.5, 4.0), (9.1, 7.9, 3.75), 100)
    elif n == 6:    # 中景缓摇上: 门楼、空白匾额、门内铜铃
        aim(c, 1, (0.8, 3.2, 1.6), (0.2, 12, 1.9), 35)
        aim(c, F, (0.8, 3.2, 1.6), (0.2, 12, 5.0), 35)
    elif n == 7:    # 中景: 甘布下马, 张归朝院内喊
        hz = horse("h_zhang", (0.4, 6.8, 0), 0); ride(dict(name="zhang", m="zhang", braid=True), hz)
        hn = horse("h_norsang", (3.2, 6.0, 0), 10); ride(dict(name="norsang", m="tibet", braid=True), hn)
        horse("h_gampo", (-2.0, 6.2, 0), -8)
        g = person("gampo", (-2.9, 6.2, 1.3), 90, "tibet", braid=True, hat=True, spear=True)
        key(g["root"], 1, loc=(-2.9, 6.2, 1.3)); key(g["root"], 30, loc=(-2.9, 6.2, 0)); linear(g["root"])
        aim(c, 1, (-7.5, 2.6, 1.7), (0, 8.6, 2.0), 35)
    elif n == 8:    # 全景: 空荡的院子
        aim(c, 1, (0, 12.6, 1.6), (0, 36, 1.9), 28)
    elif n == 9:    # 近景: 马厩暗处, 老灰马抬头
        h = horse("hui", (-13.4, 24.6, 0), -90, "hui")
        key(h["neck"], 1, rot=(-0.75, 0, 0)); key(h["neck"], 18, rot=(-0.75, 0, 0)); key(h["neck"], 60, rot=(0.05, 0, 0))
        aim(c, 1, (-8.2, 23.0, 1.5), (-12.6, 24.6, 1.55), 50)
    elif n == 10:   # 全景 门框构图: 卢七端碗从院子深处走来
        lu = person("lu", (0.4, 27, 0), 180, "lu", stoop=0.22, topknot=True)
        for sh in lu["arms"]:
            sh.rotation_euler = (1.05, 0, 0)
        walk_person(lu, 1, F, (0.4, 27, 0), (0.2, 14.3, 0), 32)
        for sh in lu["arms"]:
            sh.animation_data_clear()
            sh.rotation_euler = (1.05, 0, 0)
        bowl = prim("cyl", (0, 0.42, 0.98), m="bowl", parent=lu["root"], vertices=16, radius=0.09, depth=0.06)
        aim(c, 1, (0.3, 0.8, 1.6), (0, 30, 2.6), 32)
    elif n in (11, 12, 13, 14, 15, 16):   # 门外对话区
        lu = person("lu", (0, 9.7, 0), 180, "lu", stoop=0.22, topknot=True)
        zg = person("zhang", (0, 8.2, 0), 0, "zhang", braid=True)
        person("gampo", (-1.7, 7.4, 0), 15, "tibet", braid=True, hat=True, spear=True)
        person("norsang", (1.7, 7.3, 0), -20, "tibet", braid=True)
        horse("h_zhang", (-3.5, 4.5, 0), 70); horse("h_gampo", (-5.2, 5.6, 0), 80); horse("h_norsang", (4.2, 4.8, 0), -80)
        if n == 11:     # 近景: 卢七看着三人的吐蕃装束
            aim(c, 1, (1.15, 6.9, 1.63), (0, 9.52, 1.62), 85)
        elif n == 12:   # 近景双人: 卢七把碗递给张归
            for sh in lu["arms"]:
                key(sh, 1, rot=(0.9, 0, 0)); key(sh, 30, rot=(0.9, 0, 0)); key(sh, 70, rot=(1.25, 0, 0))
            for sh in zg["arms"]:
                key(sh, 1, rot=(0.1, 0, 0)); key(sh, 40, rot=(0.1, 0, 0)); key(sh, 70, rot=(1.2, 0, 0))
            bowl = prim("cyl", (0, 9.32, 1.05), m="bowl", vertices=16, radius=0.09, depth=0.06)
            key(bowl, 1, loc=(0, 9.32, 1.05)); key(bowl, 30, loc=(0, 9.32, 1.05)); key(bowl, 75, loc=(0, 8.95, 1.12))
            aim(c, 1, (3.4, 8.95, 1.45), (0, 8.95, 1.35), 50)
        elif n == 13:   # 特写: 张归喝水, 皱眉
            for sh in zg["arms"]:
                key(sh, 1, rot=(1.2, 0, 0)); key(sh, 36, rot=(1.65, 0, 0))
            bowl = prim("cyl", (0, 8.55, 1.12), m="bowl", vertices=16, radius=0.09, depth=0.06)
            key(bowl, 1, loc=(0, 8.55, 1.12)); key(bowl, 36, loc=(0, 8.36, 1.66))
            key(zg["neck"], 36, rot=(0, 0, 0)); key(zg["neck"], 60, rot=(-0.25, 0, 0))
            aim(c, 1, (-1.1, 10.7, 1.7), (0, 8.2, 1.68), 85)
        elif n == 14:   # 近景: 卢七 "苦泉。往西就没有水了。"
            aim(c, 1, (1.05, 7.0, 1.63), (0, 9.52, 1.62), 85)
        elif n == 15:   # 近景: 张归 "我们从西边来。"
            aim(c, 1, (-1.1, 10.8, 1.7), (0, 8.2, 1.7), 85)
        elif n == 16:   # 特写极缓推: 卢七停顿, 目光移向东方
            key(lu["neck"], 1, rot=(0, 0, 0)); key(lu["neck"], 50, rot=(0, 0, 0)); key(lu["neck"], 120, rot=(0.05, 0, -0.6))
            aim(c, 1, (1.0, 7.1, 1.63), (0, 9.52, 1.64), 85)
            aim(c, F, (0.75, 7.75, 1.63), (0, 9.52, 1.64), 85)
    elif n == 17:   # 远景: 向东的驿道, 空无一人, 延伸到天边
        aim(c, 1, (-26, -2.5, 1.7), (-700, 0, 1.0), 35)

def render_shot(n, mode):
    secs, static = SHOTS[n]
    F = secs * FPS
    build_world()
    c = camera()
    setup_shot(n, c, F)
    sc = bpy.context.scene
    sc.frame_start, sc.frame_end = 1, F
    if mode == "still":
        frames = [1 if static else F // 2]
        outdir = os.path.join(OUT, "stills")
    else:
        # 静止镜头只渲一帧; 运动镜头按"一拍二"(每两帧渲一帧)
        frames = [1] if static else list(range(1, F + 1, 2))
        outdir = os.path.join(OUT, f"shot{n:02d}")
    os.makedirs(outdir, exist_ok=True)
    for f in frames:
        sc.frame_set(f)
        sc.render.filepath = os.path.join(outdir, f"s{n:02d}_{f:04d}.png" if mode == "still" else f"{f:04d}.png")
        if mode != "still" and os.path.exists(sc.render.filepath):
            continue
        bpy.ops.render.render(write_still=True)
    print(f"DONE shot {n} frames {len(frames)}", flush=True)

if args[0] == "stills":
    for n in (map(int, args[1:]) if len(args) > 1 else SHOTS):
        render_shot(n, "still")
elif args[0] == "shot":
    for n in map(int, args[1:]):
        render_shot(n, "anim")
