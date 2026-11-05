EP = dict(
cn="二", title="柳",
summary="第二集讲柳树的来历。现实线里,吐蕃兵要砍老柳当柴,卢七一声不吭站到树下;张归用“拆驿须先登记”拦下了斧子。回忆线回到天宝三载:十七岁的和义公主西嫁途中在驿里住了一夜,把母亲在灞桥折给她的柳枝插在苦泉边。同年秋天,老驿长病逝,柳枝发了第一片芽。",
info=[("场次", "8 场:现实 3 场(开场、后房、收尾),回忆 5 场(744)"),
      ("现实线人物", "卢七(65)、张归、甘布、诺桑"),
      ("回忆线人物", "卢七(22)、卢老驿长(58,病中)、和义公主(17)、两名宫女、护送的唐军骑兵"),
      ("钥匙物件", "孤柳、空脂粉盒、红绳"),
      ("要立住的东西", "红绳的来历:第一根是公主系的,此后每年她离开的那天,卢七系一根")],
curve="紧(斧子举起来)→ 静(空脂粉盒)→ 亮(公主的车驾)→ 柔(泉边夜话)→ 痛(父亲去世)→ 暖(第一片芽)→ 定(第四十三根)。",
anchors="""
LU QI, AGE 22: lean young Han Chinese man, sun-darkened face, faint first beard, black futou cap, plain dark green round-collar robe of a post-station clerk, leather belt, earnest guarded eyes

FATHER LU, AGE 58: the same stocky man grown gaunt and grey, sunken cheeks, grey beard, black futou cap, dark green robe hanging loose, leans on a wooden staff, a dry cough, still upright and stern

PALACE MAID: young Tang palace maid in a plain travelling hu-style coat over a long skirt, hair in a double bun, carrying a lacquer box

TANG ESCORT: Tang cavalry soldiers in cloth-covered lamellar armour, red tassels on spears, dusty riding boots

WILLOW 744: a single bare willow twig about one metre tall, pushed into wet sand beside the stone-lined spring, one faded red cord tied around it
""",
scenes=[
dict(head="外景 驿门 清晨(787)", short="驿门 清晨(787)", era="787",
     env="POST STATION 787 at dawn, the huge old willow hung with red cords beside the stone-lined spring, the gate tower, the empty road",
     tone="tense and quiet; nobody raises a voice",
script="""
字幕:第二日。
张归(旁白):第二日。柳一株,在泉边。登记的时候,他说这不是驿站的树。
天刚亮。卢七从苦泉打上一桶水,提进门去。
甘布拎着一把斧子走到柳树下,用斧背敲了敲树干,听声音。诺桑在后面抱起一捆干枝。
甘布(吐蕃语,字幕):够烧一个冬天。
卢七从门里出来。他没有说话,走到柳树下,背靠着树干站定。
甘布看了他一眼,举起斧子。诺桑笑出声。
张归抱着一本簿子从院里跑出来。
张归:等一下!
张归(吐蕃语,字幕):拆驿要先登记。树也是驿里的东西,少一样,我交不了差。
甘布骂了一句,把斧子扛回肩上,转身去拆马厩的旧栏杆。
张归翻开簿子,看着卢七。
张归:这树,怎么登?
卢七:不是驿里的。
张归:那是谁的?
卢七:一个公主的。
""",
shots=[
 S("1", "大远景,固定", "黎明,驿站和老柳的剪影,天边一线青白", "风声;字幕“第二日”;旁白:“第二日。柳一株,在泉边。”", 8,
   "extreme long shot at first light, POST STATION 787 and the huge old willow as dark shapes against a thin pale blue-white band on the horizon, the empty road", "static camera, locked-off tripod shot, the willow strands stir slowly, the sky brightens a little", key=True),
 S("2", "中景,固定", "卢七在苦泉边打水,提桶进门", "井绳声;旁白:“登记的时候,他说这不是驿站的树。”", 7,
   "medium shot, LU QI, AGE 65: [锚点], lifting a wooden bucket of water out of the stone-lined spring under the old willow, the gate behind him", "static camera, the old man lifts the bucket with both hands, turns and walks toward the gate"),
 S("3", "近景,固定", "斧背敲树干,树皮开裂处系着红绳", "咚、咚两声", 4,
   "close shot, the back of an iron axe tapping the cracked bark of the old willow trunk, faded red cords tied around the trunk, a sheepskin sleeve at frame edge", "static camera, the axe taps the trunk twice, then rests"),
 S("4", "中景", "甘布扛斧子打量柳树,诺桑抱着干枝在后面", "甘布(吐蕃语):“够烧一个冬天。”", 5,
   "medium shot, GAMPO, one of TIBETAN SOLDIERS (GAMPO, NORSANG), looking up at the old willow with an axe on his shoulder, NORSANG behind him holding a bundle of dry branches", "static camera, the soldier looks up at the branches and nods to himself"),
 S("5", "全景,门框构图", "卢七从门洞里走出,走到树下,背靠树干站定", "脚步声", 8,
   "wide shot framed by the dark gate opening, LU QI, AGE 65: [锚点], walking out of the gate toward the old willow, the two Tibetan soldiers at the tree", "static camera, the old man walks slowly to the tree and stands with his back against the trunk"),
 S("6", "近景", "卢七背靠树,不看任何人", "风声", 4,
   "close shot, LU QI, AGE 65: [锚点], standing with his back pressed against the willow trunk, red cords hanging around his head, eyes looking at the road", "static camera, he stands still, only his white beard moves in the wind"),
 S("7", "中景,侧面", "甘布举起斧子,诺桑笑出声", "诺桑的笑声", 4,
   "medium side shot, GAMPO raising the axe high beside the willow, LU QI at the trunk, NORSANG laughing behind, TIBETAN SOLDIERS (GAMPO, NORSANG)", "static camera, the soldier raises the axe over his shoulder and holds it there"),
 S("8", "中景,跟拍", "张归抱着簿子从院里跑出门洞", "张归:“等一下!”", 4,
   "medium tracking shot, ZHANG GUI, AGE 18: [锚点], running out through the gate holding a bound register book", "camera tracks with him for a few steps as he runs out and stops"),
 S("9", "双人", "张归挡在斧子前,用吐蕃话对甘布说", "张归(吐蕃语):“拆驿要先登记。树也是驿里的东西,少一样,我交不了差。”", 8,
   "two-shot, ZHANG GUI, AGE 18: [锚点], stepping between the raised axe and the tree, speaking firmly to GAMPO, the register book held up", "static camera, the young man speaks, the soldier slowly lowers the axe"),
 S("10", "中景", "甘布骂一句,扛斧转身去拆马厩栏杆", "吐蕃语的咒骂", 4,
   "medium shot, GAMPO shouldering the axe and turning away toward the gate, muttering, NORSANG dropping the dry branches", "static camera, the soldier turns and walks out of frame"),
 S("11", "近景,过肩", "张归翻开簿子问卢七", "张归:“这树,怎么登?”", 4,
   "close shot over the shoulder of LU QI, ZHANG GUI, AGE 18: [锚点], opening the register book and looking at the old man", "static camera, he opens the book and asks"),
 S("12", "近景,过肩", "卢七", "卢七:“不是驿里的。”", 3,
   "close shot over the shoulder of ZHANG GUI, LU QI, AGE 65: [锚点], still leaning on the trunk", "static camera, the old man answers without moving"),
 S("13", "近景", "张归", "张归:“那是谁的?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], brush in hand above the open register", "static camera, he looks up from the book"),
 S("14", "特写,极缓推", "卢七抬头看柳枝", "卢七:“一个公主的。”羌笛入", 6,
   "close-up, LU QI, AGE 65: [锚点], lifting his eyes to the willow branches and red cords above, soft dawn light", "extremely slow push in, he looks up, then holds still", key=True),
]),
dict(head="内景 后房 晨(787)", short="后房 晨(787)", era="787",
     env="LU QI's small back room, earthen walls, a narrow bed, an old poplar-wood chest with many red cords tied to the objects inside, a small high window",
     tone="hushed and private",
script="""
卢七的后房,窄床,墙角一只胡杨木旧箱。张归跟在后面,抱着簿子。
卢七打开木箱。箱里的东西每件都拴着一根红绳。他取出一只小小的圆盒,漆已经斑驳。
他打开盒盖。里面是空的。
张归:空的?
卢七:她说,用完了,就留个盒子。
盒盖内侧有一面磨得发乌的铜镜。卢七看着镜子,镜子里映出一点晨光。
镜头推进镜面,光变暖、变亮。
""",
shots=[
 S("15", "全景,固定", "窄小的后房,卢七蹲在木箱前,张归在门口", "木箱合页吱呀", 6,
   "wide shot of LU QI's small back room, LU QI, AGE 65: [锚点], kneeling before an old poplar-wood chest, ZHANG GUI, AGE 18: [锚点], standing in the doorway with the register", "static camera, the old man lifts the chest lid"),
 S("16", "特写,俯拍", "箱内物件各拴红绳:布鞋、信、酒囊、金币……", "—", 6,
   "top-down close-up into the open chest, small objects each tied with a faded red cord: a pair of cloth shoes, a folded letter, a felt wine skin, a small coin, a half-embroidered pouch", "very slow push in, a hand moves aside the shoes", key=True),
 S("17", "特写", "卢七取出一只斑驳的漆盒", "—", 5,
   "close-up, an old man's hands lifting out a small round lacquer powder box with flaking paint, a red cord tied around it", "static camera, the hands lift the box and hold it"),
 S("18", "特写", "盒盖打开,里面是空的", "张归:“空的?”", 4,
   "close-up, the lacquer box opening, empty inside, a dull bronze mirror on the inner lid", "static camera, the lid opens slowly and stops"),
 S("19", "近景", "卢七看着镜子", "卢七:“她说,用完了,就留个盒子。”", 6,
   "close shot, LU QI, AGE 65: [锚点], looking down into the open box, a little light reflected from the mirror onto his face", "static camera, he speaks quietly, eyes on the box"),
 S("20", "大特写,缓推", "发乌的铜镜里,晨光变暖、变亮(转场)", "羌笛,渐入驼铃与车轮声", 6,
   "extreme close-up of the dull bronze mirror in the lid, a small point of light in it", "slow push in, the light in the mirror grows warm and bright until it fills the frame"),
]),
dict(head="外景 驿门 黄昏(回忆,744)", short="驿门 黄昏(744)", era="天宝",
     env="POST STATION 736 eight years later, still busy and well kept, the stone-lined spring with no tree beside it, warm dusk, the road from the east",
     tone="splendid and solemn; a girl inside a ceremony",
     crowd="four palace maids, a dozen Tang escort riders and post soldiers in the background",
script="""
字幕:天宝三载。
驿道东头,一队车驾在黄昏里驶来。护送的骑兵举着红缨长枪,车帷是青色的。
卢老驿长站在门前,拄着木杖,咳了两声。二十二岁的卢七站在他身后。
卢父:马牵进去,喂豆子。车不进门,停在泉边。
卢七:是。
车停下。两个宫女掀开车帷。一个戴着帷帽的少女下车,手里握着一根用湿布裹着的柳枝。
她没有看驿站,先转身看向西边。西边是一望无际的碛。
卢父躬身行礼。
卢父:苦泉驿驿长卢某,恭迎公主。
公主轻轻点了点头,声音很轻。
和义公主:水是苦的吗?
卢父:是。
和义公主:那也好。
""",
shots=[
 S("21", "大远景,固定", "黄昏驿道,一队车驾从东边(画左)驶来", "车轮声、马蹄;字幕“天宝三载”", 9,
   "extreme long shot at golden dusk, a Tang royal carriage train with blue-green curtains and red-tasselled escort riders coming along the road from frame left toward the post station, long shadows", "static camera, the procession moves slowly from left to right toward the station", key=True),
 S("22", "中景", "卢父拄杖站在门前咳嗽,卢七在身后", "咳嗽声", 5,
   "medium shot, FATHER LU, AGE 58: [锚点], standing before the gate leaning on a staff, LU QI, AGE 22: [锚点], one step behind him, POST STATION 736 gate", "static camera, the old man coughs twice and straightens"),
 S("23", "近景", "卢父交代儿子", "卢父:“马牵进去,喂豆子。车不进门,停在泉边。”卢七:“是。”", 6,
   "close shot, FATHER LU, AGE 58: [锚点], turning his head to speak to his son, LU QI, AGE 22: [锚点], soft focus beside him", "static camera, he speaks briefly, the son nods once"),
 S("24", "中景", "车驾停在泉边,宫女掀开车帷", "马喷鼻", 6,
   "medium shot, the carriage stopping beside the stone-lined spring, two PALACE MAID lifting the blue-green curtain, escorts dismounting", "static camera, the maids lift the curtain"),
 S("25", "近景,缓推", "帷帽少女下车,手握湿布裹着的柳枝", "—", 7,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], stepping down from the carriage, holding a willow branch wrapped in damp cloth, veil moving in the wind", "slow push in, she steps down and stands, holding the branch to her chest", key=True),
 S("26", "全景,背面", "公主不看驿站,转身望向西边的碛", "风声加大", 7,
   "wide shot from behind, PRINCESS HEYI, AGE 17: [锚点], a small figure turning away from the station to face the endless desert to the west, frame right, golden dusk", "static camera, she turns slowly toward the west and stands still"),
 S("26a", "中景", "卢七把护送骑兵的马一匹匹牵到泉边饮水", "马饮水声", 6,
   "medium shot, LU QI, AGE 22: [锚点], leading two Tang cavalry horses to the stone-lined spring to drink, TANG ESCORT soldiers unloading behind him", "static camera, the horses lower their heads to the water"),
 S("27", "中景", "卢父躬身行礼", "卢父:“苦泉驿驿长卢某,恭迎公主。”", 5,
   "medium shot, FATHER LU, AGE 58: [锚点], bowing deeply with the staff in one hand, LU QI, AGE 22: [锚点], bowing behind him, PRINCESS HEYI's back in the foreground", "static camera, the two men bow and hold"),
 S("28", "近景", "公主隔着帷纱", "和义公主:“水是苦的吗?”卢父:“是。”", 5,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], speaking softly through the thin veil", "static camera, she asks quietly without lifting the veil"),
 S("29", "近景", "公主轻声", "和义公主:“那也好。”", 4,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], looking down at the willow branch in her hands", "static camera, she looks down at the branch and answers"),
]),
dict(head="外景 苦泉边 夜(回忆,744)", short="苦泉边 夜(744)", era="天宝",
     env="the stone-lined spring outside the gate at night, bare wet sand beside it, the gate tower behind with one lantern, a sky full of stars",
     tone="tender and restrained; two young people who will never meet again",
script="""
夜深。驿里的灯都熄了,只有门楼下一盏灯笼。
公主一个人坐在苦泉边的石沿上,柳枝搁在膝上。
卢七提着一盏油灯出门巡夜,看见她,停住,想退回去。
和义公主:你别走。
卢七站在灯下,不知道该站在哪里。
和义公主:从这里往西,还有柳树吗?
卢七:没见过。往西是碛,碛那边……我没去过。
公主低头看柳枝。
和义公主:这是灞桥的柳。长安送人,折一枝柳。我阿娘折给我的。
和义公主:我一路带着,浇了一路的水。再往西,它就活不成了。
她抬头看他。
和义公主:让它留在这儿吧。到了这儿,它就不用再往西走了。
卢七:这里的水是苦的,它活不了。
和义公主:苦水也是水。
卢七放下油灯,跪在泉边,用手在湿沙里挖了一个坑。公主把柳枝插进去,用手把沙按实。
她从袖口解下一根红绳,系在柳枝上。
和义公主:红绳是平安。
两人在泉边坐着,谁也没有再说话。
""",
shots=[
 S("30", "大远景,固定", "星空下的驿站,门楼下一盏灯笼,泉边一个小小的人影", "夜风、虫声", 8,
   "extreme long shot of the post station under a sky full of stars, one lantern under the gate tower, a tiny seated figure beside the spring", "static camera, the stars and the lantern flicker faintly", key=True),
 S("31", "中景", "公主独坐泉边石沿,柳枝在膝上", "—", 6,
   "medium shot, PRINCESS HEYI, AGE 17: [锚点], sitting alone on the stone rim of the spring at night, veil lifted back, the wrapped willow branch across her knees, lantern light from behind", "static camera, she sits still, looking at the water"),
 S("32", "中景", "卢七提灯出门,看见她,想退回", "脚步停住", 5,
   "medium shot, LU QI, AGE 22: [锚点], stepping out of the gate with an oil lamp, stopping when he sees someone at the spring", "static camera, he stops and takes half a step back"),
 S("33", "近景", "公主没回头", "和义公主:“你别走。”", 3,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], not turning around, lamp light on her cheek", "static camera, she speaks without turning"),
 S("34", "近景", "公主看着西边的黑暗", "和义公主:“从这里往西,还有柳树吗?”", 5,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], her face turned toward the dark west, starlight", "static camera, she asks, eyes on the darkness"),
 S("35", "近景", "卢七站在灯下", "卢七:“没见过。往西是碛,碛那边……我没去过。”", 6,
   "close shot, LU QI, AGE 22: [锚点], standing awkwardly with the oil lamp, the light from below", "static camera, he answers slowly and lowers his eyes"),
 S("36", "特写", "公主的手解开湿布,露出柳枝", "和义公主:“这是灞桥的柳。长安送人,折一枝柳。我阿娘折给我的。”", 9,
   "close-up, a girl's hands unwrapping damp cloth from a single willow twig with a few dry leaves, on her knees, lamp light", "static camera, the hands unwrap the cloth and hold the twig still", key=True),
 S("37", "近景", "公主抬头看卢七", "和义公主:“我一路带着,浇了一路的水。再往西,它就活不成了。”", 7,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], looking up at the young man, eyes wet but steady", "static camera, she speaks and looks up"),
 S("38", "近景", "公主", "和义公主:“让它留在这儿吧。到了这儿,它就不用再往西走了。”", 7,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], a faint smile, the lamp flame reflected in her eyes", "extremely slow push in, she speaks, then smiles a little"),
 S("39", "双人", "卢七犹豫", "卢七:“这里的水是苦的,它活不了。”和义公主:“苦水也是水。”", 7,
   "two-shot by the spring, LU QI, AGE 22: [锚点], standing with the lamp, PRINCESS HEYI, AGE 17: [锚点], seated on the stone rim, the dark spring between them", "static camera, he speaks, she answers without hesitation"),
 S("40", "特写", "卢七跪下,用手在湿沙里挖坑", "沙声", 6,
   "close-up, a young man's hands digging a hole in wet sand beside the stone rim of the spring, an oil lamp set down beside them", "static camera, the hands dig quickly, then stop"),
 S("41", "特写", "公主把柳枝插进去,按实沙土", "—", 6,
   "close-up, a girl's hands pushing the willow twig into the wet sand and pressing the sand firm around it", "static camera, the hands plant the twig and press the sand"),
 S("42", "特写", "她解下袖口的红绳,系在柳枝上", "和义公主:“红绳是平安。”", 7,
   "close-up, a girl's fingers tying a thin red cord around the planted willow twig, lamp light, wet sand", "static camera, she ties a small knot and lets go", key=True),
 S("43", "远景,固定", "两个人坐在泉边,一盏灯,一根枝", "羌笛主题", 8,
   "long shot, two small figures sitting apart on the stone rim of the spring, one oil lamp between them, a single twig in the sand, the gate lantern behind, stars", "static camera, they sit still, the lamp flickers"),
 S("43a", "近景", "灯下,公主看着那根枝,卢七看着公主,又移开目光", "—", 5,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], gazing at the planted twig in the lamp light, LU QI, AGE 22: [锚点], soft focus behind her, looking at her then away", "static camera, she keeps looking at the twig; he looks away"),
]),
dict(head="外景 驿门 清晨(回忆,744)", short="驿门 清晨(744)", era="天宝",
     env="POST STATION 736 at sunrise, the stone-lined spring with a single willow twig tied with a red cord beside it, the road running west",
     tone="quiet, polite, final",
     crowd="palace maids and Tang escort riders preparing to leave",
script="""
天亮。车驾已经整好,骑兵上马。
公主走到卢七面前,把那只小小的漆盒放在他手里。
和义公主:里面的用完了。盒子留给你,装点什么。
卢七:装什么?
和义公主:你想装的。
卢父拄杖站在门口,对着车驾说了一句。
卢父:前头有水。
车驾向西驶去。卢七捧着盒子站在柳枝旁边,看着帷帽越来越小。
""",
shots=[
 S("44", "全景", "车驾整装,骑兵上马", "马嘶、甲叶声", 6,
   "wide shot at sunrise, the royal carriages ready on the road, Tang escort riders mounting, the single willow twig by the spring in the foreground", "static camera, riders mount and settle"),
 S("45", "双人", "公主把漆盒放到卢七手里", "和义公主:“里面的用完了。盒子留给你,装点什么。”", 7,
   "two-shot, PRINCESS HEYI, AGE 17: [锚点], placing a small round lacquer powder box into the hands of LU QI, AGE 22: [锚点], morning light", "static camera, she puts the box in his hands and steps back"),
 S("46", "近景", "卢七", "卢七:“装什么?”", 3,
   "close shot, LU QI, AGE 22: [锚点], holding the small box, looking at her", "static camera, he asks"),
 S("47", "近景", "公主放下帷纱前一刻", "和义公主:“你想装的。”", 5,
   "close shot, PRINCESS HEYI, AGE 17: [锚点], about to lower her veil, a small smile", "static camera, she answers and lowers the veil"),
 S("48", "中景", "卢父拄杖在门口", "卢父:“前头有水。”", 4,
   "medium shot, FATHER LU, AGE 58: [锚点], standing in the gate leaning on his staff, facing the departing carriages", "static camera, he speaks the farewell line once"),
 S("49", "大远景,固定", "车驾向西(画右)驶入碛中,越来越小;前景是柳枝和捧着盒子的卢七", "车轮声渐远", 10,
   "extreme long shot, the carriage train moving away to the west toward frame right into the desert, growing small, in the foreground LU QI, AGE 22: [锚点], holding the box beside the single willow twig", "static camera, the procession recedes slowly to the right", key=True),
]),
dict(head="内景 后房 夏夜(回忆,744)", short="后房 夏夜(744)", era="天宝",
     env="the back room in 744, a narrow bed, an oil lamp on a stool, the bronze post bell lying on a folded cloth, a small high window with summer night",
     tone="plain and heavy; a father who will not let his son cry",
script="""
字幕:同年夏。
后房。卢老驿长躺在窄床上,脸瘦得只剩骨头。油灯放在凳子上。
卢七跪在床边。床头的布上放着门楼上的那只铜铃。
卢父:铃,你拿去。
卢七没有动。
卢父:有客,就响。没客……也擦一擦。
卢七:爹……
卢父:不许哭。
卢七低下头,把铃捧起来。铃舌碰了一下,轻轻一响。
卢父闭上眼睛,嘴角动了一下。
""",
shots=[
 S("49a", "全景,固定", "油灯下的后房,卢父躺在窄床上,卢七跪在床边", "夏虫;字幕“同年夏”", 7,
   "wide shot of the small back room at night, FATHER LU, AGE 58: [锚点], lying on a narrow bed, LU QI, AGE 22: [锚点], kneeling beside it, one oil lamp on a stool", "static camera, the lamp flame trembles"),
 S("49b", "特写", "床头布上的铜铃", "—", 4,
   "close-up, a fist-sized bronze post bell lying on a folded cloth at the head of the bed, its clapper tied with a red cord, lamp light", "static camera, the lamp light flickers on the bronze"),
 S("49c", "近景", "卢父侧过脸", "卢父:“铃,你拿去。”", 4,
   "close shot, FATHER LU, AGE 58: [锚点], gaunt face on the pillow, turning toward his son", "static camera, he turns his head slowly and speaks"),
 S("49d", "近景", "卢父", "卢父:“有客,就响。没客……也擦一擦。”", 7,
   "close shot, FATHER LU, AGE 58: [锚点], eyes half closed, speaking with effort", "static camera, he speaks slowly with a pause in the middle"),
 S("49e", "近景", "卢七", "卢七:“爹……”卢父:“不许哭。”", 5,
   "close shot, LU QI, AGE 22: [锚点], kneeling, his jaw tight, holding back tears", "static camera, he starts to speak and stops himself"),
 S("49f", "特写", "卢七捧起铜铃,铃舌轻轻一响", "“叮”(极轻)", 5,
   "close-up, a young man's hands lifting the bronze bell from the cloth, the clapper swinging once", "static camera, the hands lift the bell, it rings once very softly", key=True),
 S("49g", "近景,极缓推", "卢父闭上眼睛,嘴角动了一下", "风声", 6,
   "close shot, FATHER LU, AGE 58: [锚点], closing his eyes, the corner of his mouth moving into the ghost of a smile", "extremely slow push in, he closes his eyes and stays still"),
]),
dict(head="外景 苦泉边 秋(回忆,744)", short="苦泉边 秋(744)", era="天宝",
     env="the stone-lined spring in late autumn, the single willow twig with a red cord, a new low grave mound beyond the station wall, grey sky",
     tone="grief held in; then a small green surprise",
script="""
秋天。驿站后面多了一座新坟。
卢七穿着白麻孝服,手里握着父亲的木杖,从坟前走回来。他没有哭。
他在泉边停下。那根柳枝在风里立着,半年了,还是光的。
他蹲下来。枝上,冒出了一点绿。
卢七看了很久。
卢七:你活了。
他低下头,眼泪掉进沙里。
""",
shots=[
 S("50", "大远景,固定", "灰天下,驿站后面一座新坟", "西风", 7,
   "extreme long shot under a grey autumn sky, a small new grave mound behind the post station wall, a white mourning banner on a pole", "static camera, the banner flaps in the wind"),
 S("51", "中景,跟", "卢七穿白麻孝服,握着父亲的木杖走回来", "脚步声", 6,
   "medium shot, LU QI, AGE 22: [锚点], wearing white hemp mourning clothes, holding his father's wooden staff, walking back from the grave", "camera tracks slowly beside him, his face is dry"),
 S("52", "近景", "他在泉边停下,看那根光秃秃的柳枝", "—", 5,
   "close shot, LU QI, AGE 22: [锚点], stopping beside the spring and looking down at the bare twig", "static camera, he stops and looks down"),
 S("53", "大特写,缓推", "光秃的枝上,冒出一点新绿", "风声忽然停了", 6,
   "extreme close-up, a bare willow twig with a faded red cord, a single tiny green bud opening near the top", "very slow push in on the green bud", key=True),
 S("54", "近景", "卢七蹲下,看了很久", "卢七:“你活了。”", 6,
   "close shot, LU QI, AGE 22: [锚点], crouching beside the twig, staring at the bud", "static camera, he speaks very softly"),
 S("55", "特写", "眼泪掉进沙里", "羌笛一个长音", 5,
   "close-up, a tear falling onto the wet sand beside the twig, a hand gripping a wooden staff", "static camera, a single tear falls; the hand tightens on the staff"),
 S("56", "特写,叠化", "嫩芽叠化为老柳的满枝红绳(转场回现实)", "风声回来", 6,
   "close-up dissolve, the single green bud dissolving into dense old willow branches hung with dozens of faded red cords", "slow dissolve, colors cool down to blue-grey",
   out="the green bud dissolves into the dense old willow branches with red cords of 787; colors cool to blue-grey."),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="POST STATION 787 at dusk, the huge old willow hung with dozens of faded red cords beside the stone-lined spring",
     tone="calm; a small act of protection",
script="""
黄昏。卢七站在老柳下,把一根新的红绳系在一根低枝上。
张归抱着簿子站在一旁。
张归:这是第几根?
卢七:第四十三根。
张归:一年一根?
卢七点头。
张归蹲下来,把簿子摊在膝上,写下一行。
张归(旁白):柳一株,公主所植,不在拆列。这是我写的第一行,不是吐蕃人要的。
""",
shots=[
 S("57", "中景", "卢七在低枝上系新红绳", "风声", 7,
   "medium shot, LU QI, AGE 65: [锚点], tying a new bright red cord onto a low branch of the old willow among dozens of faded ones, dusk", "static camera, his old hands tie the knot slowly"),
 S("58", "近景", "张归", "张归:“这是第几根?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], holding the register, watching", "static camera, he asks"),
 S("59", "近景", "卢七没有回头", "卢七:“第四十三根。”", 4,
   "close shot, LU QI, AGE 65: [锚点], hands still on the cord, not turning", "static camera, he answers, eyes on the knot"),
 S("60", "近景", "张归;卢七点头", "张归:“一年一根?”", 4,
   "close shot over the shoulder of ZHANG GUI, LU QI, AGE 65: [锚点], nodding once", "static camera, the old man nods once"),
 S("61", "特写", "簿子上的毛笔落下(文字后期合成)", "旁白:“柳一株,公主所植,不在拆列。”", 7,
   "close-up, a brush writing on a blank page of a register book resting on a knee, sheepskin sleeve, dusk light", "static camera, the brush writes one vertical line"),
 S("62", "大远景,固定", "黄昏,一新一旧的红绳在风里飘,驿道空无一人", "旁白:“这是我写的第一行,不是吐蕃人要的。”羌笛收", 9,
   "extreme long shot at dusk, the old willow and the gate, one new bright red cord among the faded ones, an old man and a young man small beneath the tree, the empty road", "static camera, the cords sway, light fades", key=True,
   out="hold the final image; the light slowly fades to dusk blue; end of episode."),
]),
])
