ENV_FERRY = "LU PU VILLAGE ferry landing under the enormous old camphor tree, the stone steps, the FERRY BOAT, the thatched tea pavilion, the slow green river"

EPS = {}

EPS["13"] = dict(cn="十三", jq="立秋", title="摇篮",
summary="立秋,啃秋瓜。午后一场暴雨,石生在檐下赶做摇篮,用的是去年老樟树断下的一根枝。桑娘的肚子已经显了。阿禾帮着磨木头,磨得满头大汗。雨停的时候,摇篮做好了,空着,在风里自己轻轻晃。",
info=[("物候", "凉风至,白露降,寒蝉鸣"), ("人物", "石生、桑娘、阿禾、周老篙"),
      ("风俗", "立秋“啃秋”:在树荫下吃西瓜,意为咬住夏天、迎接秋天。"),
      ("细节", "摇篮的木头来自渡口老樟树断下的枝,这棵树看着全村人长大。")],
curve="甜(啃秋瓜)→ 骤(暴雨)→ 专(做摇篮)→ 柔(空摇篮自己晃)。",
scenes=[
dict(head="外景 老樟树下 午", short="老樟树下 午", era="秋", env=ENV_FERRY + ", early autumn, a few yellow leaves, watermelons split on a stone",
     tone="sweet end of summer", crowd="a few villagers eating watermelon in the shade",
script="""
字幕:立秋。凉风至,白露降,寒蝉鸣。
老樟树下,周老篙一刀劈开一只西瓜。阿禾抱着一大块,啃得满脸都是。
桑娘坐在树荫里,肚子已经显了,手搭在上面。
桑娘:啃了秋,夏天就咬住了,跑不掉。
天边忽然黑了一片。
""",
shots=[
 S("1", "大远景,固定", "初秋的渡口,老樟树下几片黄叶", "寒蝉;字幕“立秋”与三候", 8,
   "extreme long shot of the ferry landing at the start of autumn, the old camphor tree with a few yellow leaves, VILLAGERS in its shade, the river bright", "static camera, a leaf falls", key=True),
 S("2", "特写", "一刀劈开西瓜,红瓤", "“咔嚓”", 4,
   "close-up, a knife splitting a big green watermelon on a flat stone, bright red flesh", "static camera, the melon splits open"),
 S("3", "中景", "阿禾抱一大块瓜啃得满脸都是;桑娘坐在树荫里,肚子已显", "桑娘:“啃了秋,夏天就咬住了,跑不掉。”", 7,
   "medium shot in the camphor shade, A HE, AGE 8: [锚点], biting into a huge slice of watermelon, juice on her face, SANG NIANG, AGE 19: [锚点], visibly pregnant, resting a hand on her belly and laughing", "static camera, the girl eats, the woman laughs"),
 S("4", "大远景,固定", "天边忽然黑了一片,风起", "风骤起", 5,
   "extreme long shot, a wall of dark storm cloud sweeping over the blue hills toward the village, the river surface roughening", "static camera, the storm advances"),
]),
dict(head="外景 石生家屋檐下 暴雨", short="屋檐下 暴雨", era="秋", env="the deep tiled eaves of the carpenter's house during a summer downpour, a workbench, wood shavings, a half-built cradle of pale camphor wood",
     tone="focused hands in loud rain",
script="""
暴雨。石生在屋檐下的木工凳前刨木头,刨花一卷卷落下。
石生:这是老樟树去年断下来的那根枝。樟木,不生虫,孩子睡着香。
阿禾坐在小板凳上,用砂石磨摇篮的边,磨得满头大汗。
阿禾:它摇起来会唱歌吗?
石生:你摇摇看。
""",
shots=[
 S("5", "全景", "暴雨,石生在檐下刨木头,刨花一卷卷落下", "暴雨声、刨木声", 7,
   "wide shot under the deep eaves of the carpenter's house in a downpour, SHI SHENG, AGE 22: [锚点], planing pale wood at a workbench, curls of shavings falling, a half-built cradle beside him", "static camera, rain pours off the eaves"),
 S("6", "近景", "石生", "石生:“这是老樟树去年断下来的那根枝。樟木,不生虫,孩子睡着香。”", 8,
   "close shot, SHI SHENG, AGE 22: [锚点], running his palm along a planed board, smelling it", "static camera, he speaks shyly"),
 S("7", "中景", "阿禾坐在小板凳上用砂石磨摇篮边,满头大汗", "—", 5,
   "medium shot, A HE, AGE 8: [锚点], on a low stool rubbing the edge of the cradle with a sanding stone, sweating, tongue out in concentration", "static camera, she sands"),
 S("8", "双人", "阿禾问", "阿禾:“它摇起来会唱歌吗?”石生:“你摇摇看。”", 6,
   "two-shot, A HE, AGE 8: [锚点], looking up from the cradle at SHI SHENG, AGE 22: [锚点]", "static camera, she asks, he grins"),
]),
dict(head="外景 石生家屋檐下 雨后", short="屋檐下 雨后", era="秋", env="the carpenter's eaves after the storm, dripping, clear cool light, the finished cradle hanging from a beam",
     tone="quiet expectation",
script="""
雨停了。檐下滴着水。
摇篮做好了,用绳子吊在梁上。桑娘伸手推了一下。摇篮轻轻晃起来,吱呀,吱呀。
大家都不说话,看着它晃。
风从河上吹过来,摇篮停了一下,又自己晃了起来。
阿禾(旁白):立秋。小人有床了。还有九个节气。
""",
shots=[
 S("9", "全景", "雨停,檐下滴水,摇篮吊在梁上", "滴水声", 6,
   "wide shot after the storm, water dripping from the eaves, a finished pale camphor-wood cradle hanging from a beam on ropes, SHI SHENG, AGE 22: [锚点], SANG NIANG, AGE 19: [锚点], and A HE, AGE 8: [锚点], around it", "static camera, drops fall"),
 S("10", "特写", "桑娘伸手推了一下,摇篮轻轻晃起来", "吱呀,吱呀", 6,
   "close-up, a woman's hand giving the empty cradle a gentle push, the cradle swinging, the ropes creaking", "static camera, it swings", key=True),
 S("11", "中景", "大家都不说话,看着它晃", "—", 5,
   "medium shot, three people standing silent, watching the empty cradle swing in the cool light", "static camera, they watch"),
 S("12", "大远景,固定", "风从河上吹来,空摇篮停了一下,又自己晃起来", "阿禾(旁白):“立秋。小人有床了。还有九个节气。”", 9,
   "extreme long shot of the carpenter's house by the river after rain, under the eaves an empty cradle swaying by itself in the wind", "static camera, the cradle sways on its own", key=True,
   out="hold on the swaying cradle; end of episode."),
]),
])

EPS["14"] = dict(cn="十四", jq="处暑", title="河灯",
summary="七月半,放河灯。周老篙扎了两盏荷花灯,一盏给阿禾的奶奶,一盏给阿禾的娘。阿禾这一年跟陈先生学会了几个字,在自己那盏灯上歪歪扭扭写了一个“娘”。全村的河灯顺水漂下来,经过渡口。爷爷撑着船,陪着两盏灯走了很远。",
info=[("物候", "鹰乃祭鸟,天地始肃,禾乃登"), ("人物", "周老篙、阿禾、陈先生、村民"),
      ("风俗", "中元节(七月十五)放河灯,为逝去的亲人照路;时在处暑前后。"),
      ("回收", "阿禾跟陈先生学字(第 10 集)。")],
curve="静(扎灯)→ 认真(写一个字)→ 满(一河的灯)→ 送(陪灯走一程)。",
scenes=[
dict(head="内景 周家 黄昏", short="周家 黄昏", era="秋", env="the ferryman's small house at dusk, a low table with paper, bamboo strips, glue and a candle, an open door to the river",
     tone="careful, private",
script="""
字幕:处暑。鹰乃祭鸟,天地始肃,禾乃登。
黄昏。周老篙用竹篾和红纸扎荷花灯,手很慢,很稳。两盏。
阿禾拿着毛笔,趴在桌上,在一盏灯的纸瓣上写字。写坏了一张,又换一张。
周老篙:写的什么?
阿禾举起来:一个歪歪扭扭的“娘”字。
阿禾:先生教的。笔画对吗?
周老篙看了很久。
周老篙:对。
""",
shots=[
 S("1", "大远景,固定", "处暑黄昏,稻子开始黄了,河上有凉意", "秋虫;字幕“处暑”与三候", 8,
   "extreme long shot at dusk, rice fields beginning to turn gold around LU PU VILLAGE, a cool mist on the river", "static camera, mist gathers", key=True),
 S("2", "特写", "竹篾和红纸,一朵荷花灯慢慢成形", "—", 6,
   "close-up, old hands bending thin bamboo strips and pasting red paper petals into a lotus-shaped lantern", "static camera, the hands work slowly and steadily"),
 S("3", "中景", "阿禾趴在桌上,在灯瓣上写字,写坏一张又换一张", "—", 6,
   "medium shot, A HE, AGE 8: [锚点], lying across a low table with a brush, writing on a paper petal, crumpling one and starting again, ZHOU THE FERRYMAN, AGE 68: [锚点], beside her", "static camera, she writes carefully"),
 S("4", "特写", "纸瓣上一个歪歪扭扭的字(文字后期合成)", "周老篙:“写的什么?”", 4,
   "close-up, one large clumsy brush character on a red paper petal held up by small hands", "static camera, she holds it up"),
 S("5", "近景", "阿禾", "阿禾:“先生教的。笔画对吗?”", 4,
   "close shot, A HE, AGE 8: [锚点], anxious, holding the petal up to her grandfather", "static camera, she asks"),
 S("6", "近景,极缓推", "周老篙看了很久", "周老篙:“对。”", 6,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], looking at the character for a long time in the candlelight", "extremely slow push in, he looks, then nods", key=True),
]),
dict(head="外景 河上 夜", short="河上 夜", era="秋", env="the river at night with hundreds of small lotus lanterns drifting downstream, the stone bridge, the camphor tree, the ferry",
     tone="luminous and tender", crowd="villagers setting lanterns on the water from the steps",
script="""
夜。全村的人在石阶上把河灯放进水里。灯一盏接一盏,顺水往下漂,把整条河照亮了。
阿禾蹲在渡口最下一级台阶上,把两盏灯轻轻放进水里。
灯漂开了。阿禾站起来,看着它们混进别的灯里。
周老篙解开渡船。
周老篙:上船。送一送。
渡船跟着那两盏灯,慢慢往下游去。
阿禾(旁白):处暑。我给娘写了一个字。还有八个节气。
""",
shots=[
 S("7", "大远景,固定", "满河的荷花灯顺水漂,照亮了石桥和老樟树", "流水声、低声的念祷", 10,
   "extreme long shot of the river at night filled with hundreds of small glowing lotus lanterns drifting downstream past the stone bridge and the camphor tree", "static camera, the lanterns drift", key=True),
 S("8", "中景", "村民在石阶上把河灯放进水里", "—", 5,
   "medium shot, VILLAGERS kneeling on the stone steps setting lanterns onto the dark water", "static camera, lanterns are set down"),
 S("9", "特写", "两盏灯被小手轻轻放进水里", "水声", 5,
   "close-up, small hands lowering two red paper lotus lanterns onto the water, one with a large clumsy character on a petal", "static camera, the lanterns float free"),
 S("10", "近景", "阿禾站起来,看着它们混进别的灯里", "—", 5,
   "close shot, A HE, AGE 8: [锚点], standing on the lowest step, lantern light on her face, watching", "static camera, she watches"),
 S("11", "双人", "周老篙解开渡船", "周老篙:“上船。送一送。”", 4,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], untying the FERRY BOAT, A HE, AGE 8: [锚点], turning to him", "static camera, he unties the rope"),
 S("12", "大远景,固定", "渡船跟着两盏灯,在满河灯火里慢慢往下游去", "阿禾(旁白):“处暑。我给娘写了一个字。还有八个节气。”羌笛", 10,
   "extreme long shot, the small ferry boat moving slowly downstream among the drifting lanterns, an old man poling, a child in the bow, two red lanterns just ahead of them", "static camera, the boat follows the lights away", key=True,
   out="hold as the lights move away; end of episode."),
]),
])

EPS["15"] = dict(cn="十五", jq="白露", title="露",
summary="王婆的眼睛越来越看不清了。老人说,白露这天早上的露水洗眼睛最灵。天没亮,阿禾就端着碗下了地,一片叶子一片叶子地扫露水,扫了小半碗。王婆用露水洗了眼,眯着看她:“看清楚了。”阿禾知道她说的不全是真话。王婆说:等你爹回来,我还要看看他胖了瘦了。",
info=[("物候", "鸿雁来,玄鸟归,群鸟养羞"), ("人物", "阿禾、王婆"),
      ("风俗", "白露收清露:民间以为白露晨露可明目。"),
      ("铺垫", "王婆霜降去世(第 18 集)。")],
curve="冷(黎明的露)→ 执(一片片扫)→ 暖(洗眼)→ 知(不全是真话)→ 盼(等你爹回来)。",
scenes=[
dict(head="外景 桑园 黎明", short="桑园 黎明", era="秋", env="a mulberry field at grey dawn, every leaf and grass blade heavy with white dew, mist low on the ground",
     tone="cold, patient, devoted",
script="""
字幕:白露。鸿雁来,玄鸟归,群鸟养羞。
天还没亮。桑园里,每片叶子上都挂着白白的露珠。
阿禾端着一只粗瓷碗,用一根鸡毛,一片叶子一片叶子地把露水扫进碗里。
手冻红了。碗底才盖住。
天上一行大雁往南飞。阿禾抬头看了一眼,低头接着扫。
""",
shots=[
 S("1", "大远景,固定", "灰蓝的黎明,桑园里每片叶子挂着露,天上一行大雁南飞", "雁鸣;字幕“白露”与三候", 9,
   "extreme long shot at grey-blue dawn over a mulberry field heavy with white dew, low mist, a line of wild geese flying south across the pale sky", "static camera, the geese cross", key=True),
 S("2", "特写", "鸡毛扫过叶片,露珠滚进碗里", "—", 6,
   "close-up, a chicken feather brushing dew drops from a mulberry leaf into a rough porcelain bowl", "static camera, drops roll into the bowl", key=True),
 S("3", "中景", "阿禾一片叶子一片叶子地扫,手冻红了", "—", 6,
   "medium shot, A HE, AGE 8: [锚点], crouching among the wet mulberry bushes, brushing leaf after leaf, her hands red with cold", "static camera, she works along the row"),
 S("4", "特写,俯拍", "碗底才盖住", "—", 4,
   "top-down close-up of a rough bowl with a thin layer of clear dew at the bottom", "static camera, a drop falls in"),
 S("5", "近景", "阿禾抬头看了一眼大雁,低头接着扫", "雁鸣", 5,
   "close shot, A HE, AGE 8: [锚点], looking up briefly at the geese, then back down to the leaves", "static camera, she looks up and back"),
]),
dict(head="外景 茶亭 晨", short="茶亭 晨", era="秋", env="the tea pavilion by the ferry in early morning, the kettle not yet lit, the old woman sitting with a blanket on her knees",
     tone="a kind lie and a wish",
script="""
茶亭里,王婆裹着毯子坐着。阿禾小心地端着碗走进来,一滴也没洒。
阿禾:婆婆,白露的露水。洗眼睛。
王婆用手指蘸了露水,轻轻抹在眼皮上。抹了三遍。
她眯着眼睛,看着阿禾。
王婆:看清楚了。脸上还有泥。
阿禾去擦脸。脸上没有泥。她知道婆婆是看不清的。
王婆拉过她冻红的手,揣进自己怀里焐着。
王婆:等你爹回来,我还要看看他,胖了还是瘦了。
阿禾(旁白):白露。婆婆说她看清楚了。还有七个节气。
""",
shots=[
 S("6", "中景", "王婆裹着毯子坐在茶亭里;阿禾端着碗小心走进来", "阿禾:“婆婆,白露的露水。洗眼睛。”", 7,
   "medium shot of the tea pavilion in early light, GRANNY WANG, AGE 80: [锚点], wrapped in a blanket, A HE, AGE 8: [锚点], stepping in carefully with the bowl held in both hands", "static camera, she walks in without spilling"),
 S("7", "特写", "王婆用手指蘸露水,轻轻抹在眼皮上,抹三遍", "—", 7,
   "close-up, an old wrinkled finger dipping into the dew and gently stroking it across closed eyelids, three times", "static camera, the finger strokes three times", key=True),
 S("8", "近景", "王婆眯着眼看阿禾", "王婆:“看清楚了。脸上还有泥。”", 5,
   "close shot, GRANNY WANG, AGE 80: [锚点], squinting at the girl with clouded eyes and a sly smile", "static camera, she squints and smiles"),
 S("9", "近景", "阿禾去擦脸,脸上没有泥", "—", 4,
   "close shot, A HE, AGE 8: [锚点], rubbing her clean cheek, then pausing, understanding", "static camera, she rubs, then stops"),
 S("10", "特写", "王婆把她冻红的手揣进自己怀里焐着", "—", 5,
   "close-up, two thin old hands pulling a child's red cold hands inside the front of a dark jacket", "static camera, the hands are tucked in"),
 S("11", "近景,极缓推", "王婆", "王婆:“等你爹回来,我还要看看他,胖了还是瘦了。”", 7,
   "close shot, GRANNY WANG, AGE 80: [锚点], holding the child's hands against her chest, looking toward the river", "extremely slow push in, she speaks", key=True),
 S("12", "大远景,固定", "清晨的茶亭,一老一小挨着坐", "阿禾(旁白):“白露。婆婆说她看清楚了。还有七个节气。”", 8,
   "extreme long shot at morning of the tea pavilion and camphor tree by the misty river, an old woman and a child sitting close together inside", "static camera, mist lifts", key=True,
   out="hold; end of episode."),
]),
])

EPS["16"] = dict(cn="十六", jq="秋分", title="信",
summary="秋分,稻子熟了,全村割稻。阿禾在金黄的田里找自己芒种插的那一行歪的,怎么也找不到了。傍晚,一个跑船的捎来一封信,是爹托人写的。陈先生在月亮底下念给她听:“冬至前必回。”",
info=[("物候", "雷始收声,蛰虫坯户,水始涸"), ("人物", "阿禾、周老篙、陈先生、桑娘、石生、跑船人、村民"),
      ("回收", "芒种那一行歪秧(第 9 集):“秋天你再来看,分不出哪行是歪的。”"),
      ("时令", "淳熙十二年中秋在秋分前后,剧中合在一夜。")],
curve="丰(割稻)→ 找(歪的那行)→ 悟(分不出了)→ 喜(来信)→ 圆(月)。",
scenes=[
dict(head="外景 稻田 午", short="稻田 午", era="秋", env="golden ripe rice fields outside LU PU VILLAGE under a high clear sky, sheaves standing, sickles flashing",
     tone="abundant and warm", crowd="villagers harvesting with sickles",
script="""
字幕:秋分。雷始收声,蛰虫坯户,水始涸。
稻田一片金黄。全村人弯腰割稻,稻捆一排排立在田里。
阿禾在田埂上来回走,一行一行地数。
阿禾:爷爷,我那行歪的呢?
周老篙直起腰,也看了看。满田的稻子一样高,一样黄。
周老篙:你说呢?
阿禾找了很久,找不到。她笑了。
""",
shots=[
 S("1", "大远景,固定", "高天下一片金黄的稻田,稻捆一排排立着", "镰刀声、鸟鸣;字幕“秋分”与三候", 9,
   "extreme long shot of golden ripe rice fields under a high clear sky, VILLAGERS bent harvesting, sheaves standing in rows, the village beyond", "static camera, the rice ripples in the wind", key=True),
 S("2", "特写", "镰刀割下一把稻子", "“嚓”", 4,
   "close-up, a sickle cutting through a handful of heavy golden rice stalks", "static camera, the sickle cuts"),
 S("3", "中景", "阿禾在田埂上来回走,一行一行地数", "阿禾:“爷爷,我那行歪的呢?”", 6,
   "medium shot, A HE, AGE 8: [锚点], walking along the earth bank, counting the rows with her finger", "camera follows her slowly"),
 S("4", "主观,俯拍", "满田的稻子一样高,一样黄", "—", 5,
   "high-angle point-of-view shot over the field, every row of ripe rice the same height and the same gold, no crooked line anywhere", "slow pan across the field", key=True),
 S("5", "双人", "周老篙直起腰", "周老篙:“你说呢?”", 4,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], straightening up with a sickle, A HE, AGE 8: [锚点], on the bank", "static camera, he straightens and grins"),
 S("6", "近景", "阿禾找了很久,找不到,笑了", "—", 5,
   "close shot, A HE, AGE 8: [锚点], searching the field, giving up, starting to laugh", "static camera, she laughs"),
]),
dict(head="外景 渡口 夜", short="渡口 夜", era="秋", env=ENV_FERRY + ", a huge round mid-autumn moon over the river, moon cakes and pomelos on a low table",
     tone="joy held quietly",
script="""
傍晚,一条跑船停在渡口,船上的人扬着一封信。
跑船人:周老篙!临安捎来的!
夜里,月亮又大又圆。渡口的矮桌上摆着月饼和柚子。陈先生就着月光拆信。
阿禾跪在凳子上,脖子伸得老长。
陈先生:“爹在临安好。漕船上管饭,胖了。冬至前,必回。”
阿禾:必回是什么?
陈先生:就是一定回来。
阿禾不说话了,抬头看月亮。
阿禾(旁白):秋分。爹说他胖了,冬至一定回来。还有六个节气。
""",
shots=[
 S("7", "中景", "一条跑船停在渡口,船上的人扬着一封信", "跑船人:“周老篙!临安捎来的!”", 6,
   "medium shot at dusk, a passing cargo boat at the ferry steps, a boatman waving a folded letter, ZHOU THE FERRYMAN, AGE 68: [锚点], reaching for it", "static camera, the letter is handed over"),
 S("8", "大远景,固定", "又大又圆的月亮升在河上", "秋虫", 7,
   "extreme long shot of a huge round mid-autumn moon rising over the river and the camphor tree, a small table on the ferry landing", "static camera, the moon rises", key=True),
 S("9", "中景", "矮桌摆着月饼柚子,陈先生就着月光拆信,阿禾跪在凳子上伸长脖子", "—", 6,
   "medium shot by moonlight, MR CHEN, AGE 46: [锚点], unfolding a letter at a low table with moon cakes and pomelos, A HE, AGE 8: [锚点], kneeling on a stool craning her neck, ZHOU THE FERRYMAN, AGE 68: [锚点], beside them", "static camera, he unfolds the letter"),
 S("10", "近景", "陈先生念信", "陈先生:“爹在临安好。漕船上管饭,胖了。冬至前,必回。”", 8,
   "close shot, MR CHEN, AGE 46: [锚点], reading aloud by moonlight", "static camera, he reads"),
 S("11", "双人", "阿禾问", "阿禾:“必回是什么?”陈先生:“就是一定回来。”", 5,
   "two-shot, A HE, AGE 8: [锚点], looking up at MR CHEN, AGE 46: [锚点]", "static camera, she asks, he answers"),
 S("12", "近景", "阿禾不说话,抬头看月亮", "—", 5,
   "close shot, A HE, AGE 8: [锚点], silent, looking up at the moon, moonlight on her face", "static camera, she looks up", key=True),
 S("13", "大远景,固定", "月亮底下的渡口,三个人一张桌", "阿禾(旁白):“秋分。爹说他胖了,冬至一定回来。还有六个节气。”", 8,
   "extreme long shot of the ferry landing under the full moon, three small figures around a table, the moon's path on the water", "static camera, still", key=True,
   out="hold; end of episode."),
]),
])

EPS["17"] = dict(cn="十七", jq="寒露", title="登高",
summary="重阳登高。王婆走不动了,石生和许秀才用一把竹椅把她抬上了村后的小山。山上菊花开了,大家喝菊花酒。王婆坐在山顶,眯着眼看底下的村子、河、渡口和老樟树。“看了八十年,看不够。”她把头上的银簪拔下来,插在阿禾的小髻上。",
info=[("物候", "鸿雁来宾,雀入大水为蛤,菊有黄华"), ("人物", "王婆、阿禾、石生、许秀才、桑娘、陈先生、周老篙、村民"),
      ("风俗", "重阳(九月初九)登高、赏菊、饮菊花酒、敬老;时在寒露前后。"),
      ("铺垫", "银簪。王婆霜降去世(第 18 集)。")],
curve="热闹(抬椅上山)→ 开阔(山顶)→ 恋(看不够)→ 传(银簪)。",
scenes=[
dict(head="外景 村后小山 午", short="小山 午", era="秋", env="a low hill behind LU PU VILLAGE in mid autumn, yellow chrysanthemums among the grass, the whole village, river and ferry visible below, clear sky",
     tone="cheerful procession, wide view", crowd="villagers climbing with baskets and wine jars",
script="""
字幕:寒露。鸿雁来宾,雀入大水为蛤,菊有黄华。
重阳。石生和许秀才一前一后,抬着一把绑了竹竿的椅子往山上走。椅子上坐着王婆,手里摇着扇子,像坐轿子。
王婆:慢点!我这把骨头,摔了可没处配!
后面跟着全村的人,提着酒坛、食盒。阿禾一路采菊花,插满了王婆的椅背。
""",
shots=[
 S("1", "大远景,固定", "秋天的小山,黄菊遍地,一队人沿山路往上走", "笑声;字幕“寒露”与三候", 9,
   "extreme long shot of a low autumn hill dotted with yellow chrysanthemums, a line of VILLAGERS climbing a winding path, two men carrying a chair on bamboo poles at the front", "static camera, the procession climbs", key=True),
 S("2", "中景", "石生和许秀才抬着竹椅,王婆坐在上面摇扇", "王婆:“慢点!我这把骨头,摔了可没处配!”", 7,
   "medium shot, SHI SHENG, AGE 22: [锚点], and XU XIUCAI, AGE 20: [锚点], carrying a bamboo chair on poles up the slope, GRANNY WANG, AGE 80: [锚点], riding in it fanning herself like an empress", "camera moves up the path with them"),
 S("3", "近景", "阿禾一路采菊花,插满了椅背", "—", 5,
   "close shot, A HE, AGE 8: [锚点], running alongside the chair tucking yellow chrysanthemums into its back and the old woman's hair", "static camera, she tucks flowers in"),
]),
dict(head="外景 小山顶 午后", short="山顶 午后", era="秋", env="the top of the hill in afternoon light, a wide view of the village, the river, the ferry and the camphor tree, wine cups with chrysanthemum petals",
     tone="a long last look",
script="""
山顶。大家铺开席子,喝菊花酒。陈先生摇头晃脑地吟诗,没人听。
王婆坐在椅子上,眯着眼睛往下看。底下是村子,河,石拱桥,渡口,老樟树。
王婆:那是我家。那是你家。那是渡口,我在那烧了五十年茶。
王婆:看了八十年,看不够。
她伸手把头上的银簪拔下来,摸索着插在阿禾的小髻上。
王婆:替我戴着。
阿禾摸了摸头上的簪子,凉凉的。
阿禾(旁白):寒露。婆婆把簪子给了我。还有五个节气。
""",
shots=[
 S("4", "全景", "山顶铺开席子喝菊花酒,陈先生摇头晃脑吟诗,没人听", "说笑", 6,
   "wide shot on the hilltop, VILLAGERS on mats drinking from cups with chrysanthemum petals, MR CHEN, AGE 46: [锚点], reciting a poem with his eyes closed while nobody listens", "static camera, they drink and chat"),
 S("5", "主观,大远景", "山下:村子、河、石拱桥、渡口、老樟树", "风声", 8,
   "point-of-view extreme long shot from the hilltop down onto LU PU VILLAGE, the river, the stone bridge, the ferry landing and the tiny camphor tree in clear autumn light", "very slow pan across the village", key=True),
 S("6", "近景", "王婆眯着眼往下看,一处处指", "王婆:“那是我家。那是你家。那是渡口,我在那烧了五十年茶。”", 9,
   "close shot, GRANNY WANG, AGE 80: [锚点], with chrysanthemums in her hair, squinting down and pointing with her fan", "static camera, she points and talks"),
 S("7", "近景,极缓推", "王婆", "王婆:“看了八十年,看不够。”", 6,
   "close shot, GRANNY WANG, AGE 80: [锚点], lowering the fan, gazing down, wind in her white hair", "extremely slow push in, she speaks softly", key=True),
 S("8", "特写", "她把银簪拔下来,摸索着插在阿禾的小髻上", "王婆:“替我戴着。”", 7,
   "close-up, wrinkled hands drawing a silver hairpin from a white bun and fumbling to push it into a child's small hair bun", "static camera, the pin goes in"),
 S("9", "近景", "阿禾摸了摸头上的簪子", "—", 4,
   "close shot, A HE, AGE 8: [锚点], touching the silver pin in her hair, solemn", "static camera, she touches it"),
 S("10", "大远景,固定", "山顶上的人和菊花,底下是整个村子", "阿禾(旁白):“寒露。婆婆把簪子给了我。还有五个节气。”", 9,
   "extreme long shot from behind, the villagers small on the hilltop among yellow flowers, an old woman in a chair and a child beside her, the whole valley below", "static camera, wind moves the flowers", key=True,
   out="hold; end of episode."),
]),
])

EPS["18"] = dict(cn="十八", jq="霜降", title="柿",
summary="霜降。第一场霜。清晨阿禾来茶亭,王婆坐在她的竹椅上,扇子搁在膝上,像睡着了。炉子是凉的。窗台上摆着一排柿子,下面压着一张纸条,是王婆请陈先生写的:给阿禾。第二天早上,阿禾自己生起了茶亭的炉子。",
info=[("物候", "豺乃祭兽,草木黄落,蛰虫咸俯"), ("人物", "阿禾、王婆、周老篙、陈先生、村民"),
      ("风俗", "霜降吃柿子,江南俗谓“霜降吃柿,不会流鼻涕”。"),
      ("这一集", "全剧的低点。不哭天抢地,只有凉了的炉子和一排柿子。")],
curve="白(霜)→ 静(像睡着了)→ 凉(炉子)→ 痛(给阿禾)→ 续(自己生火)。",
scenes=[
dict(head="外景 渡口 黎明", short="渡口 黎明", era="秋", env=ENV_FERRY + ", white frost on the steps, the boat and the thatch, the camphor tree, persimmon trees bare except for orange fruit",
     tone="hushed, white",
script="""
字幕:霜降。豺乃祭兽,草木黄落,蛰虫咸俯。
清晨。台阶、船篷、茅草亭顶都白了。第一场霜。
阿禾呵着白气跑来茶亭,头上插着那根银簪。
阿禾:婆婆,下霜了!
王婆坐在她的竹椅上,扇子搁在膝上,头微微歪着,像睡着了。
阿禾走近。炉子是凉的。
""",
shots=[
 S("1", "大远景,固定", "第一场霜:台阶、船篷、茶亭顶都白了", "极静;字幕“霜降”与三候", 9,
   "extreme long shot at dawn of the ferry landing white with the first frost, the steps, the boat's bamboo awning and the thatched tea pavilion all frosted, orange persimmons on a bare tree", "static camera, breath of mist on the river", key=True),
 S("2", "中景,跟", "阿禾呵着白气跑向茶亭,头上插着银簪", "阿禾:“婆婆,下霜了!”", 5,
   "medium tracking shot, A HE, AGE 8: [锚点], running along the frosted path toward the tea pavilion, breath steaming, a silver pin in her hair", "camera tracks with her"),
 S("3", "全景,门框构图", "王婆坐在竹椅上,扇子搁在膝上,头微微歪着,像睡着了", "—", 7,
   "wide shot framed by the tea pavilion entrance, GRANNY WANG, AGE 80: [锚点], sitting in her bamboo chair, the fan resting on her knees, head tilted slightly, as if asleep, pale light", "static camera, nothing moves", key=True),
 S("4", "近景", "阿禾走近", "—", 4,
   "close shot, A HE, AGE 8: [锚点], stepping closer, the smile leaving her face", "static camera, she steps in"),
 S("5", "特写", "炉子是凉的,茶壶上结了一层霜", "—", 5,
   "close-up, a small clay stove with cold grey ash, a kettle on top with a thin skin of frost", "static camera, still"),
]),
dict(head="内景 茶亭 晨", short="茶亭 晨", era="秋", env="the tea pavilion in pale morning light, a row of orange persimmons on the window ledge with frost on them, a folded paper under one",
     tone="grief without noise",
script="""
窗台上摆着一排柿子,一共七个,皮上挂着霜。最边上那个下面压着一张折好的纸。
阿禾拿起来,看不懂上面的字。
陈先生站在门口,声音很轻。
陈先生:前天她叫我写的。三个字:给阿禾。
阿禾拿着纸,站了很久。她没哭。她把柿子一个个抱在怀里。
周老篙进来,把一件旧袄披在王婆身上。
""",
shots=[
 S("6", "特写,缓横移", "窗台上一排七个柿子,挂着霜,最边上一个下面压着纸", "—", 7,
   "close-up slow lateral move along a window ledge, seven ripe orange persimmons dusted with frost, a folded paper tucked under the last one", "slow lateral move along the fruit", key=True),
 S("7", "特写", "阿禾拿起纸,看不懂上面的字(文字后期合成)", "—", 4,
   "close-up, small hands unfolding a paper with three brush characters", "static camera, she unfolds it"),
 S("8", "中景,门框构图", "陈先生站在门口", "陈先生:“前天她叫我写的。三个字:给阿禾。”", 6,
   "medium shot, MR CHEN, AGE 46: [锚点], standing in the frosted doorway of the pavilion, speaking very softly", "static camera, he speaks"),
 S("9", "近景,极缓推", "阿禾拿着纸,站了很久,没哭", "—", 7,
   "close shot, A HE, AGE 8: [锚点], holding the paper, standing very still, dry-eyed, the silver pin in her hair", "extremely slow push in, she does not move", key=True),
 S("10", "中景", "她把柿子一个个抱在怀里", "—", 6,
   "medium shot, A HE, AGE 8: [锚点], gathering the seven frosted persimmons one by one into her arms", "static camera, she gathers them"),
 S("11", "中景", "周老篙进来,把一件旧袄披在王婆身上", "—", 6,
   "medium shot, ZHOU THE FERRYMAN, AGE 68: [锚点], entering quietly and laying an old padded jacket over the still woman in the chair", "static camera, he covers her gently"),
]),
dict(head="外景 茶亭 第二天黎明", short="茶亭 次日黎明", era="秋", env="the tea pavilion at the next frosty dawn, the empty bamboo chair, the clay stove",
     tone="a child continuing",
script="""
第二天黎明。又下了霜。
茶亭里,竹椅空着。
阿禾蹲在炉子前,学着婆婆的样子,往里塞干草,一下一下吹。烟呛得她直咳嗽。火着了。
第一个过河的人走进茶亭,搓着手。阿禾给他倒了一碗热茶。
阿禾(旁白):霜降。婆婆走了。茶亭我来烧。还有四个节气。
""",
shots=[
 S("12", "全景", "第二天黎明,竹椅空着", "—", 5,
   "wide shot of the tea pavilion at the next frosty dawn, the empty bamboo chair with the fan on its seat", "static camera, still"),
 S("13", "近景", "阿禾蹲在炉前塞干草,一下一下吹,呛得咳嗽,火着了", "吹气、咳嗽、火苗声", 8,
   "close shot, A HE, AGE 8: [锚点], crouching at the clay stove stuffing in dry straw and blowing, coughing in the smoke, then a flame catching and lighting her face", "static camera, she blows, coughs, the fire catches", key=True),
 S("14", "中景", "第一个过河的人进来搓手,阿禾给他倒热茶", "倒茶声", 6,
   "medium shot, a VILLAGERS traveller in a padded jacket stepping in rubbing his hands, A HE, AGE 8: [锚点], pouring him a steaming bowl of tea", "static camera, she pours"),
 S("15", "大远景,固定", "霜白的渡口,茶亭顶冒出一缕炊烟", "阿禾(旁白):“霜降。婆婆走了。茶亭我来烧。还有四个节气。”羌笛", 9,
   "extreme long shot of the frosted ferry landing at dawn, a thin thread of smoke rising from the tea pavilion roof beside the camphor tree", "static camera, the smoke rises", key=True,
   out="hold on the rising smoke; end of episode."),
]),
])
