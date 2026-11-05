# 《二十四节气》设定数据:季节色调、画风块、全剧角色锚点(生成器与总览页共用)

ERA_TONE = {"春": "[春]", "夏": "[夏]", "秋": "[秋]", "冬": "[冬]"}
ERA_STYLE = {"春": "STYLE 绢本 · 春", "夏": "STYLE 绢本 · 夏", "秋": "STYLE 绢本 · 秋", "冬": "STYLE 绢本 · 冬"}

STYLE_PREFIX = ("cinematic film still, Southern Song dynasty China, 12th century, a small silk-farming water village south of Lake Tai, "
                "natural light, soft film grain, historically accurate Song costumes and architecture, quiet and poetic everyday life, generous negative space")

TONES = {
    "春": "[春] pale celadon green and peach-blossom pink, soft misty light, fine rain, wet stone, young and tender",
    "夏": "[夏] deep lush green, white light and dark shade, lotus pink, heavy humid air, cicadas, bright and drowsy",
    "秋": "[秋] warm ochre, rice-gold and persimmon orange, clear high sky, long slanting afternoon light, ripe and calm",
    "冬": "[冬] ink grey and snow white, a single warm lamp or red accent, low pale sun, breath visible in the cold, quiet and close",
}

ANIM_STYLES = {
    "STYLE 绢本 · 春": "hand-painted 2D animated film in the manner of Southern Song academy painting on silk, fine ink line, light washes of mineral green and indigo, warm silk ground showing through, misty spring air rendered as blank silk, delicate and airy, gentle limited animation",
    "STYLE 绢本 · 夏": "hand-painted 2D animated film in the manner of Southern Song academy painting on silk, fine ink line, saturated malachite green and lotus pink washes, deep ink shadows under trees, white silk highlights for sunlight, lush and still, gentle limited animation",
    "STYLE 绢本 · 秋": "hand-painted 2D animated film in the manner of Southern Song academy painting on silk, fine ink line, ochre, rice-gold and persimmon washes on warm silk, long soft shadows, clear sky left as pale silk, ripe and calm, gentle limited animation",
    "STYLE 绢本 · 冬": "hand-painted 2D animated film in the manner of Southern Song ink-wash winter landscapes, sparse ink line and grey washes, snow left as bare white silk, one small warm accent of lamp light or red cloth per frame, quiet and close, gentle limited animation",
}

# 全剧固定角色与场景(每次原样复制,不改词)
ANCHORS = """
ZHOU THE FERRYMAN, AGE 68: lean old Han Chinese man of the Southern Song, sun-browned lined face, short white beard, hair in a topknot under a black cloth band, sleeveless hemp jacket over a faded indigo tunic, rolled trousers, bare feet or straw sandals, a long bamboo punting pole, few words, kind narrow eyes

A HE, AGE 8: small Han Chinese girl, round face, hair in two little buns tied with faded red string, patched indigo jacket and short trousers, straw sandals, a cloth bag across her body, watchful dark eyes, the ferryman's granddaughter

ZHOU DA, AGE 34: A HE's father, broad-shouldered grain-boat hauler, sunburnt square face, short beard, brown hemp short jacket, rope over one shoulder, quiet and awkward with tenderness

SANG NIANG, AGE 19: young Han Chinese silkworm-raising woman, oval face, hair in a single bun with a wooden pin, pale green jacket with sleeves rolled, a mulberry-leaf basket on her hip, steady capable hands, a quick laugh

SHI SHENG, AGE 22: young village carpenter and boatwright, tall and lean, short hair tied up with a cloth strip, plain grey-brown short jacket, wood shavings on his sleeves, shy smile, big careful hands

MR CHEN, AGE 46: village schoolteacher who failed the imperial exams three times, thin and slightly stooped, neat short beard, black soft cap, a washed-pale blue scholar's robe with ink on the cuffs, gentle self-mocking eyes

XU XIUCAI, AGE 20: young scholar of the village preparing for the imperial exams, slender, clean-shaven earnest face, black scholar's cap, a new pale grey robe, a book box on his back when travelling

GRANNY WANG, AGE 80: the oldest woman in the village, tiny and bent, white hair in a small bun with a silver pin, dark brown jacket, keeps the tea pavilion by the ferry, sharp humorous eyes, a bamboo fan

VILLAGERS: Southern Song villagers of a silk-farming water village, men in short hemp jackets and rolled trousers, women in plain jackets and long skirts with head cloths, children with tufted hair, all ordinary and unidealised

LU PU VILLAGE: a small Southern Song water village south of Lake Tai, whitewashed walls and dark tiled roofs along a slow green river, a hump-backed stone bridge, a wooden ferry landing under an enormous old camphor tree, a thatched tea pavilion beside it, mulberry fields and rice paddies beyond, low blue hills on the horizon

FERRY BOAT: a small flat-bottomed wooden ferry boat with a woven bamboo awning at the stern, worn smooth, moored at the stone steps of the landing

SILKWORM ROOM: a dim tiled-roof room lined with tiers of round bamboo trays full of silkworms on mulberry leaves, a charcoal brazier, paper windows
"""

def anchor_names():
    names = []
    for ln in ANCHORS.strip().splitlines():
        if ":" in ln and ln[:1].isupper():
            names.append(ln.split(":")[0].strip())
    return names
