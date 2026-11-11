P = "[风格前缀], "
EP = dict(
cn="一", title="题壁", keep_ids=True,
summary="第一集只做三件事:立住老人和墙,埋下“十天”的倒计时,让观众听见第一声驿铃。不交代卢七的身世,不让他说太多话。张归带两名吐蕃兵到驿宣读撤驿令,限十日;老人不争,只问“能等我把墙擦完吗?”诺桑碰响了驿厅门口的铜铃,铃声把画面带回开元二十四年:十四岁的卢七扶着梯子,看父亲把崭新的铜铃挂上门楼,学到了驿站的规矩。夜里,张归提着灯笼看墙,在墙脚发现一匹稚拙的炭画马。",
info=[("场次", "6 场:现实 3 场,回忆 2 场(736),现实收尾 1 场"),
      ("现实线人物", "卢七(65)、张归(18)、吐蕃兵甘布与诺桑、老马“灰”"),
      ("回忆线人物", "少年卢七(14)、卢老驿长(约 50)、康萨保(约 30)、一位无名书生"),
      ("钥匙物件", "铜驿铃"),
      ("本页与文档的关系", "分镜表与文档第一集标签一致(镜 20、38、51 已拆成 a/b)。关键帧提示词照抄文档;其余镜头的提示词是本页补齐的。"),
      ("连续性修订", "787 年铜铃挂在驿厅门内(第 8 集交代卢七何时把它从门楼移进来),所以第 2 场门楼下只剩一截空铃绳,镜 6 改为“门楼下空着的铃绳”;诺桑在驿厅门框碰响的就是它。")],
text_block="""**墙上最老的一首诗(原创拟作,无名氏《题苦泉驿》):**

苦泉犹可饮,离恨不堪尝。明日西行客,回头望故乡。""",
curve="冷(吐蕃人到来)→ 疑(一个老人为什么只在乎一面墙)→ 暖(少年时代的驿站有多热闹)→ 想知道(墙脚那匹炭画马是谁画的)。",
anchors="""
FATHER LU, AGE 50: stocky Han Chinese man, square weathered face, greying short beard, black futou cap, dark green round-collar post-station official robe, a slight limp from an old leg wound, stern but warm eyes

KANG SABAO, AGE 30: young Sogdian merchant, curly reddish-brown beard, pointed white felt hat, red turned-down-collar kaftan with brocade trim, leather boots, booming laugh, gold ring on one hand

SCHOLAR: thin Han Chinese scholar in his twenties, white hemp round-collar robe slightly loosened, black soft cap, flushed from wine, gentle melancholy face

TIBETAN SOLDIERS (GAMPO, NORSANG): two Tibetan Empire soldiers, braided hair, thick sheepskin robes with one sleeve off the shoulder, red ochre on cheeks, leather belts with short swords, ordinary tired men, not villains

HUI (THE HORSE): old grey horse, thin, white muzzle, gentle eyes, worn bridle

POST STATION 787: small rammed-earth courtyard post station, weathered gate tower with a blank faded wooden plaque, cracked walls, empty stables, a stone-lined spring outside the gate beside a huge old willow tree hung with dozens of faded red cords

POST STATION 736: the same post station brand new, fresh plaster and timber, freshly painted blank plaque, stables full of horses, busy post soldiers, a stone-lined spring outside the gate with no tree beside it

POEM WALL 787: interior west wall of a low earthen hall, whitewashed plaster covered floor to ceiling with Chinese calligraphy in many different hands and ink tones, oldest lines faded to ghost marks, a child's charcoal drawing of a horse near the floor

POEM WALL 736: the same wall only one third covered with fresh black ink calligraphy, the rest bare white plaster
""",
scenes=[
dict(head="外景 驿道 黄昏(787)", short="驿道 黄昏(787)", era="787",
     env="the endless Gobi at dusk, a straight ancient caravan road crossing it, distant Qilian mountains, later POST STATION 787 alone with its old willow",
     tone="vast, silent, austere; the land is bigger than the people",
script="""
戈壁一望无际,驿道横贯画面。风声。字幕:贞元三年 河西。
西边地平线的热浪里,出现三个骑马的小点。张归骑在最前面,辫发,吐蕃羊皮袍,腰间露出一角叠好的旧布。身后是两名吐蕃兵,甘布与诺桑。
远处,一座孤零零的土院。门外一棵老柳树,枝上系满红绳,在风里飘。
张归(旁白):那年秋天,我奉命去拆一座驿站。
""",
shots=[
 S("1", "大远景,固定", "戈壁黄昏,驿道横贯画面,空无一人", "风声;字幕“贞元三年 河西”", 10,
   P + "extreme wide shot, endless Gobi desert at dusk, a straight ancient caravan road crossing the frame from horizon to horizon, distant snow-capped Qilian mountains, no people, [现实线 787]",
   "static camera, wind moving low dust across the road, faint heat shimmer on the horizon", key=True),
 S("2", "远景,固定", "右侧地平线热浪中出现三个骑马小点,缓慢向左", "远处马蹄", 8,
   "long shot, the empty ancient caravan road crossing the Gobi at dusk, three tiny horse riders appearing on the far right horizon inside rippling heat haze, distant Qilian mountains low on the skyline, sun low behind them on the right",
   "static camera, the three tiny riders move very slowly from right to left along the road, heat shimmer, low dust drifting"),
 S("3", "中景,侧跟", "张归侧脸,辫发、吐蕃袍,腰间露出一角旧布", "旁白:“那年秋天,我奉命去拆一座驿站。”", 6,
   "medium tracking side shot, ZHANG GUI, AGE 18: [锚点], riding from right to left in profile, a corner of an old faded cloth bundle showing at his waist, TIBETAN SOLDIERS (GAMPO, NORSANG) riding just behind him slightly out of focus, low sun from behind the riders on the right",
   "camera tracks alongside at the riders' speed, horses walk steadily, the young man looks ahead without expression, robe edges flutter in the wind"),
 S("4", "远景,缓推", "孤立的土院驿站,门外老柳系满红绳", "风声加大", 10,
   P + "long shot, POST STATION 787 standing alone in the desert, the huge old willow by the gate, three tiny horse riders approaching from the right, [现实线 787]",
   "very slow push in, willow branches and red cords swaying in strong wind", key=True),
 S("5", "特写,固定", "柳枝上的红绳在风中摇曳", "羌笛主题第一次进入", 6,
   "telephoto close-up, long hanging willow branches of the huge old willow by the gate, dozens of faded red cords tied along them, the earthen wall of POST STATION 787 soft and out of focus behind, the red cords are the only saturated color in frame",
   "static camera, the willow strands and red cords sway and twist in gusting wind"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the old willow with red cords, the stone-lined spring, the empty courtyard and the hall beyond",
     tone="cold arrival met with a bowl of water",
script="""
门楼上的匾额字迹褪色:“苦泉驿”。门楼下垂着一截空铃绳,在风里一动不动。
甘布下马。张归朝院里喊。
张归:有人吗?
无人应答,只有风卷着沙。马厩暗处,一匹老灰马抬起头,低低嘶了一声。
院子深处,卢七端着一只陶碗走出来。他看了看三人的吐蕃装束,脸上没有任何反应,把碗递到张归面前。
卢七:先喝口水。
张归喝了一口,眉头一皱。
张归:苦的。
卢七:苦泉。往西就没有水了。
张归:我们从西边来。
卢七顿了一下,望向东边空荡荡的驿道。
卢七:……那就是往东没有了。
""",
shots=[
 S("6", "中景,缓摇上", "门楼,褪色匾额“苦泉驿”,门楼下一截空铃绳", "风声", 6,
   "medium shot from just outside the gate looking up, the weathered rammed-earth gate tower of POST STATION 787, deep Tang dynasty eaves with gentle upturned ridge ends, a short frayed bell cord hanging empty from the lintel, blank faded wooden plaque under the eaves",
   "slow tilt up from the empty bell cord to the blank plaque, faint dust blowing across the gate"),
 S("7", "中景,固定", "甘布下马,张归朝院内喊", "张归:“有人吗?”", 5,
   "medium shot at the gate of POST STATION 787, GAMPO of the TIBETAN SOLDIERS (GAMPO, NORSANG) swinging down from his horse, ZHANG GUI, AGE 18: [锚点], standing by his horse facing the open gate and calling inside, three tired horses, the huge old willow with red cords on the right edge of frame",
   "static camera, the soldier dismounts heavily, the young man takes one step toward the gate and calls out, horses shift their weight"),
 S("8", "全景,固定", "空荡的院子,风卷着沙", "风声", 6,
   "wide shot looking through the open gate into the empty courtyard of POST STATION 787, the low earthen hall at the far end with a dark doorway, open stables along the left wall, kitchen and side rooms along the right wall, long shadows from the low sun, no people",
   "static camera, wind sweeps thin streams of sand across the bare courtyard floor"),
 S("9", "近景,固定", "马厩暗处,老灰马抬头", "一声低嘶", 4,
   "close shot inside the dim open stable, HUI (THE HORSE) standing at an old wooden manger with its head lowered, a slanting band of dusk light falling across its white muzzle",
   "static camera, the old horse slowly lifts its head and turns one ear toward the gate, a soft low whinny"),
 S("10", "全景,门框构图,固定", "从门外望进院内,卢七端着陶碗从深处走来,由小变大", "脚步声", 10,
   P + "wide shot framed by the dark gate opening, looking into the empty courtyard, LU QI, AGE 65: [锚点], small in the far depth, carrying a clay bowl of water, [现实线 787]",
   "static camera, the old man walks slowly toward camera, careful not to spill the bowl", key=True),
 S("11", "近景,固定", "卢七看着三人的吐蕃装束,面无表情", "—", 4,
   "close shot over the shoulder, LU QI, AGE 65: [锚点], standing just inside the gate facing camera holding a clay bowl, slightly stooped, the out-of-focus sheepskin-robed shoulder of ZHANG GUI in the left foreground, the empty courtyard behind him",
   "static camera, the old man's eyes move slowly over the strangers' Tibetan clothes, his face stays expressionless"),
 S("12", "近景,双人", "卢七把碗递到张归面前", "卢七:“先喝口水。”", 5,
   "close two-shot in profile, LU QI, AGE 65: [锚点], on the right holding out a clay bowl of water with both hands, ZHANG GUI, AGE 18: [锚点], on the left, the bowl in the center of frame between them, the station's earthen outer wall and open desert behind",
   "static camera, the old man extends the bowl, the young man hesitates a beat then takes it with both hands"),
 S("13", "特写", "张归喝水,皱眉", "张归:“苦的。”", 4,
   "close-up over the shoulder, ZHANG GUI, AGE 18: [锚点], drinking from a rough clay bowl, LU QI's out-of-focus white-haired head in the left foreground, the empty desert road behind the young man, low warm side light from the left",
   "static camera, he drinks, swallows, lowers the bowl slightly and frowns at the bitter taste"),
 S("14", "近景", "卢七", "卢七:“苦泉。往西就没有水了。”", 5,
   "close shot over the shoulder, LU QI, AGE 65: [锚点], facing camera, the out-of-focus shoulder of ZHANG GUI in the left foreground, the courtyard behind him",
   "static camera, the old man speaks a short sentence calmly, barely moving"),
 S("15", "近景", "张归", "张归:“我们从西边来。”", 4,
   "close shot over the shoulder, ZHANG GUI, AGE 18: [锚点], facing camera holding the clay bowl, LU QI's out-of-focus shoulder in the left foreground, the desert road behind him, low warm side light from the left",
   "static camera, the young man answers quietly, eyes steady"),
 S("16", "特写,极缓推", "卢七停顿,目光移向画外东方", "卢七:“……那就是往东没有了。”", 7,
   P + "close-up, LU QI, AGE 65: [锚点], eyes turning slowly to look off-frame left toward the east, cold dusk light on one side of his face, [现实线 787]",
   "extremely slow push in, only his eyes move, a strand of white hair stirs in the wind", key=True),
 S("17", "远景,固定", "向东的驿道,空无一人,延伸到天边", "风声", 6,
   "long shot, the ancient caravan road running away from camera toward the east, straight to the horizon, completely empty, long shadows stretching ahead along the road from the low sun behind camera, the sky darkening toward the east",
   "static camera, low dust drifts along the road, nothing else moves"),
]),
dict(head="内景 驿厅 黄昏转夜(787)", short="驿厅 黄昏转夜(787)", era="787",
     env="the low earthen hall of POST STATION 787 at dusk turning to night, POEM WALL 787 on the west side, the hall door with the bronze bell hanging just inside it, a fire pit",
     tone="an order read aloud to a man who does not turn around",
script="""
低矮的土屋,西墙写满了字,不同的笔迹,不同的墨色,层层叠叠。卢七回到墙前,接着刚才的地方,用一块软布一寸一寸地擦。
张归展开一卷令书,上半幅是吐蕃文,下半幅是汉文。他用汉话读。
张归:奉节儿令:苦泉驿,唐之旧驿,即日撤废。限十日内,驿中器物登簿,房舍拆毁,改设新驿。
卢七没有回头,继续擦。
张归:老人家,你听到了吗?
卢七的手停下来。
卢七:十天。
(停顿)
卢七:能等我把墙擦完吗?
张归抬头,第一次好好看这面墙:从屋梁下一直写到墙脚。
张归:一面墙,要擦十天?
卢七:一天擦一遍。擦了五十年了。
诺桑靠在门框上大笑,用吐蕃话说了一句。
诺桑(吐蕃语):老疯子。
他一抬手,手肘碰到了门框上挂着的铜铃。
“叮——”
卢七的手停在墙上。铃声在屋里长长地荡开,风声渐渐低下去。镜头推向墙上的墨迹,墨色慢慢晕开、变暖。
""",
shots=[
 S("18", "全景,固定", "昏暗土屋,西墙占画面右侧三分之二,卢七背影擦墙", "布擦墙壁的沙沙声", 10,
   P + "wide interior shot, dim earthen hall, POEM WALL 787 fills the right two thirds of the frame, LU QI, AGE 65: [锚点], seen from behind wiping the wall with a soft cloth, one shaft of low sunlight from a small window, [现实线 787]",
   "static camera, his arm moves slowly left to right, dust floats in the light shaft", key=True),
 S("19", "特写,缓横移", "软布擦过墨迹,灰尘在斜光里飘", "同上", 6,
   "close-up, a soft grey cloth in an old hand sliding across dense faded calligraphy on cracked plaster, dust motes rising in a slanting shaft of light",
   "slow lateral move following the cloth from right to left, the cloth wipes steadily"),
 S("20a", "特写,固定", "张归的手展开令书,上半吐蕃文、下半汉文(文字后期合成)", "读令声起:“奉节儿令:苦泉驿,唐之旧驿,即日撤废。”", 6,
   P + "close-up insert, a young man's ink-stained hands unrolling an aged blank paper order scroll with faint vertical ruled columns, the sleeve of a sheepskin robe at the edge of frame, dim earthen hall behind, [现实线 787]",
   "static camera, the hands slowly unroll the scroll from top to bottom, then hold it still", key=True),
 S("20b", "中景,固定", "张归双手持令书读令,前景虚焦处是卢七擦墙的背影", "读令声接续:“限十日内,驿中器物登簿,房舍拆毁,改设新驿。”", 10,
   P + "medium shot, ZHANG GUI, AGE 18: [锚点], standing in the dim hall holding the unrolled blank paper scroll at chest height and reading aloud, LU QI, AGE 65: [锚点], out of focus in the foreground with his back to camera wiping the poem wall, [现实线 787]",
   "static camera, the young man reads steadily with lips moving, the old man's arm keeps wiping slowly in the foreground", key=True),
 S("21", "近景", "卢七继续擦,不回头", "擦墙声", 5,
   "close shot from behind and to the side, LU QI, AGE 65: [锚点], wiping the wall without turning his head, the order still being read somewhere behind him",
   "static camera, the cloth keeps moving at the same pace"),
 S("22", "中景", "张归", "张归:“老人家,你听到了吗?”", 4,
   "medium shot over the old man's shoulder, ZHANG GUI, AGE 18: [锚点], lowering the order scroll and looking at the old man's back",
   "static camera, he lowers the scroll and asks"),
 S("23", "近景", "卢七的手停下", "卢七:“十天。”(停顿)“能等我把墙擦完吗?”", 9,
   "close shot, LU QI, AGE 65: [锚点], his hand with the cloth stopping on the wall, head turning only slightly toward the voice",
   "static camera, the hand stops; a pause; he speaks twice"),
 S("24", "主观,缓摇下", "张归抬头,整面墙从屋梁写到墙脚", "风声隐去", 10,
   P + "point-of-view shot looking up at POEM WALL 787 from rafters to floor, layers of calligraphy in dozens of hands, [现实线 787]",
   "slow tilt down from the rafters to the floor, ending on the bottom corner", key=True),
 S("25", "近景", "张归", "张归:“一面墙,要擦十天?”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking up at the wall, the order scroll hanging from his hand",
   "static camera, he asks without looking down"),
 S("26", "近景,侧脸", "卢七", "卢七:“一天擦一遍。擦了五十年了。”", 7,
   "close shot in profile, LU QI, AGE 65: [锚点], facing the wall, the cloth resting on the plaster, dusk light on his face",
   "static camera, he speaks plainly to the wall"),
 S("27", "中景", "诺桑倒靠门框大笑,手肘碰到铜铃", "诺桑(吐蕃语):“老疯子。”", 5,
   "medium shot, NORSANG of the TIBETAN SOLDIERS (GAMPO, NORSANG) leaning back against the hall door frame laughing, his elbow knocking a fist-sized bronze bell hanging just inside the door",
   "static camera, he laughs, lifts his arm, the elbow hits the bell and it swings"),
 S("28", "特写", "铜铃摇晃", "“叮——”", 4,
   "close-up, the fist-sized bronze bell swinging inside the hall door, its clapper tied with a faded red cord, dusk light",
   "static camera, the bell swings and rings, the swing slowly dies"),
 S("29", "大特写,固定", "卢七的眼睛", "铃声延长,风声渐弱", 5,
   "extreme close-up, the eyes of LU QI, AGE 65: [锚点], wide and still, the ringing reaching him",
   "static camera, he does not blink"),
 S("30", "特写,缓推", "墙上墨迹,墨色晕开变暖(转场)", "铃声尾音接入驼铃", 6,
   "close-up of old ink calligraphy on the wall, the ink starting to bleed and warm",
   "slow push in, the ink spreads and turns warm gold",
   out="the ink bleeds into warm golden morning light; the next segment opens on the new station of 736."),
]),
dict(head="外景 驿门 清晨(回忆,736)", short="驿门 清晨(736)", era="开元",
     env="POST STATION 736 at morning, brand new, busy courtyard, the stone-lined spring with no tree beside it, the road west",
     tone="young, bright, ordered",
     crowd="post soldiers grooming horses, a Sogdian camel caravan arriving",
script="""
字幕:开元二十四年。
同一座驿站,却是新的。匾额字迹鲜亮,院里人声马嘶,驿卒在喂马、刷马。门外苦泉边没有柳树。
卢老驿长站在梯子上,把一只崭新的铜铃挂上门楼。十四岁的少年卢七在下面扶着梯子。
卢父:记住,铃响了,就是有客。
少年卢七:那要是半夜响呢?
卢父:半夜也起来。
远处传来驼铃。西边驿道的热浪里,一队骆驼慢慢浮现。卢父从梯子上下来,摇响铜铃,三声。
卢父:来的都是客,走的都是人。驿站不问来处,不问去处,只管一碗水、一匹马、一夜灯。
少年卢七嘴唇动着,默默跟着念。
康萨保从骆驼上跳下来,大笑着走过来,汉话带着粟特口音。
康萨保:卢驿长!今年的水还苦吗?
卢父:比去年还苦。
两人大笑。康萨保看见少年,往他手里塞了一把葡萄干。
康萨保:你儿子?长得比骆驼还快。
少年卢七牵着骆驼到苦泉边,用木勺舀水。骆驼低头喝水。
""",
shots=[
 S("31", "远景,与镜 4 同机位", "同一座驿站,整洁、热闹,暖金色晨光;苦泉边没有柳树", "马嘶人声;字幕“开元二十四年”", 10,
   P + "long shot from exactly the same angle as shot 4, POST STATION 736, busy courtyard, post soldiers feeding horses, no tree by the spring, [开元]",
   "static camera, people and horses moving in the courtyard, morning smoke rising from the kitchen", key=True),
 S("32", "中景,仰拍", "卢父在梯上挂崭新的铜铃,少年卢七扶梯", "—", 7,
   "low-angle medium shot, FATHER LU, AGE 50: [锚点], on a wooden ladder hanging a new bright bronze bell from the gate tower lintel on a long cord, LU QI, AGE 14: [锚点], holding the ladder steady below, morning sun",
   "static camera, the father ties the cord, the bell swings once"),
 S("33", "近景", "卢父", "卢父:“记住,铃响了,就是有客。”", 5,
   "close shot from below, FATHER LU, AGE 50: [锚点], on the ladder looking down at his son",
   "static camera, he speaks down to the boy"),
 S("34", "近景,仰拍", "少年卢七", "少年卢七:“那要是半夜响呢?”", 4,
   "low-angle close shot, LU QI, AGE 14: [锚点], holding the ladder and looking up, squinting into the sun",
   "static camera, he asks looking up"),
 S("35", "近景", "卢父", "卢父:“半夜也起来。”", 4,
   "close shot, FATHER LU, AGE 50: [锚点], answering without hesitation",
   "static camera, he answers and turns back to the bell"),
 S("36", "远景,固定", "西边驿道热浪中,驼队浮现", "驼铃由远而近", 8,
   P + "long shot down the western road, a Sogdian camel caravan emerging from the heat haze, banners and bales, [开元]",
   "static camera, the caravan slowly grows larger, camels swaying, heat shimmer", key=True),
 S("37", "特写", "卢父的手摇铃,三声", "铃声清亮(与镜 28 对比)", 5,
   "close-up, a strong weathered hand ringing the new bronze bell hanging at the gate three times, bright morning light",
   "static camera, three clear swings and rings"),
 S("38a", "中景,双人", "卢父侧身对少年说规矩(前半句)", "卢父:“来的都是客,走的都是人。”", 6,
   "medium two-shot under the gate, FATHER LU, AGE 50: [锚点], turned sideways speaking to LU QI, AGE 14: [锚点], the bell above them",
   "static camera, the father speaks, the boy listens"),
 S("39", "特写", "少年的嘴唇默念", "—", 4,
   "close-up, the lips of LU QI, AGE 14: [锚点], moving silently, repeating words",
   "static camera, only the lips move"),
 S("38b", "近景,极缓推", "卢父说完后半句,微微点头", "卢父:“驿站不问来处,不问去处,只管一碗水、一匹马、一夜灯。”", 6,
   P + "close shot, FATHER LU, AGE 50: [锚点], looking down and speaking to someone just below frame, the new bronze bell on the gate post behind him, morning sunlight, [开元]",
   "extremely slow push in, he speaks calmly, gives one small nod at the end, then holds still", key=True),
 S("40", "中景", "康萨保跳下骆驼,大笑走来", "康萨保:“卢驿长!今年的水还苦吗?”", 6,
   "medium shot, KANG SABAO, AGE 30: [锚点], jumping down from a camel and striding toward the gate laughing, the caravan behind",
   "static camera, he jumps down and walks in laughing"),
 S("41", "中景", "卢父与康萨保大笑、抱拳", "卢父:“比去年还苦。”", 5,
   "medium shot, FATHER LU, AGE 50: [锚点], and KANG SABAO, AGE 30: [锚点], laughing and clasping fists in greeting at the gate",
   "static camera, they laugh and salute"),
 S("42", "近景", "康萨保往少年手里塞葡萄干", "康萨保:“你儿子?长得比骆驼还快。”", 6,
   "close shot, KANG SABAO, AGE 30: [锚点], pouring a handful of raisins into the hands of LU QI, AGE 14: [锚点]",
   "static camera, he pours and grins"),
 S("43", "中景,固定", "少年在苦泉边用木勺舀水,骆驼低头饮水", "水声、驼铃", 8,
   P + "medium shot, LU QI, AGE 14: [锚点], scooping water with a wooden ladle from the stone-lined spring, a Bactrian camel lowering its head to drink beside him, bare ground where the willow will later grow, [开元]",
   "static camera, water pours from the ladle, the camel drinks, the boy laughs", key=True),
]),
dict(head="内景 驿厅 夜(回忆,736)", short="驿厅 夜(736)", era="开元",
     env="the hall of POST STATION 736 at night, crowded and warm, a roaring fire, POEM WALL 736 only one third covered, oil lamps, a table near the west wall",
     tone="warm abundance; the first time the boy hears the poem",
     crowd="merchants and post soldiers eating and drinking, a pipa player",
script="""
炉火旺盛,屋里挤满了客商和驿卒,康萨保的伙计在弹琵琶。西墙只写了三分之一,墨色尚新。
少年卢七端着一盘胡饼穿过人群,在西墙前停下,仰头看着那些他不认得的字。
康萨保:你认得?
少年摇头。
康萨保:我也不认得汉字。我们粟特人说,字是走过的人留下的脚印。
灯下,一个微醺的书生向少年招手。
书生:小子,想知道写的什么?
他抬手指向墙上最左上角、最老的一首,慢慢念。
书生:苦泉犹可饮,离恨不堪尝。明日西行客,回头望故乡。
少年的嘴唇跟着动,无声地念:苦泉犹可饮。
书生:这是说,你们家的水苦,离别更苦。
少年卢七:离别是苦的吗?
书生笑了笑,没有回答,转头望向门外西边的夜色。
卢父(画外):七郎!马!
少年应了一声,跑向门口,到门边又回头看了一眼那面墙。镜头推向那首诗,墨色由暖转冷,慢慢褪去。
""",
shots=[
 S("44", "全景,与镜 18 同机位", "炉火、满屋客商;西墙只写了三分之一", "琵琶、人声", 10,
   P + "wide interior shot from exactly the same angle as shot 18, the hall crowded with merchants and post soldiers around a roaring fire, a musician playing a pipa held horizontally, POEM WALL 736, [开元], night interior lit by fire",
   "static camera, firelight flickering, people laughing and passing food", key=True),
 S("45", "中景", "少年端胡饼穿过人群,停在墙前", "—", 6,
   "medium shot, LU QI, AGE 14: [锚点], carrying a tray of round flatbreads through the crowded hall and stopping in front of POEM WALL 736",
   "camera holds as he weaves through the crowd and stops at the wall"),
 S("46", "主观,缓摇上", "少年仰望满墙不认识的字", "人声渐远", 7,
   "point-of-view shot from a boy's height looking up at fresh black calligraphy on the white plaster of POEM WALL 736, firelight",
   "slow tilt up across the writing"),
 S("47", "双人", "康萨保走到少年身边", "康萨保:“你认得?”少年摇头", 5,
   "two-shot, KANG SABAO, AGE 30: [锚点], stepping up beside LU QI, AGE 14: [锚点], at the wall, both looking up",
   "static camera, the merchant asks, the boy shakes his head"),
 S("48", "近景", "康萨保", "康萨保:“我也不认得汉字。我们粟特人说,字是走过的人留下的脚印。”", 8,
   "close shot, KANG SABAO, AGE 30: [锚点], looking at the wall with a fond smile, firelight in his red beard",
   "static camera, he speaks warmly"),
 S("49", "中景", "灯下的书生招手", "书生:“小子,想知道写的什么?”", 5,
   "medium shot, SCHOLAR: [锚点], sitting at a small table under an oil lamp near the wall, beckoning with one hand",
   "static camera, he beckons and smiles"),
 S("50", "特写", "书生的手指指向左上最老的一首", "—", 4,
   "close-up, a thin scholar's finger pointing up toward the upper left corner of the wall, the oldest poem out of focus beyond it, lamp light",
   "static camera, the finger lifts and points"),
 S("51a", "近景,极缓推", "书生慢慢念前两句,灯火映在脸上", "书生:“苦泉犹可饮,离恨不堪尝。”羌笛轻入", 7,
   P + "close shot, SCHOLAR: [锚点], reading aloud from the wall with one hand raised, oil lamplight warm on his face, blurred crowd behind, [开元], night interior lit by lamps",
   "extremely slow push in, his lips move slowly, lamplight flickers", key=True),
 S("51b", "特写,缓横移", "墙上这首诗的字迹,灯火摇曳(书法后期合成)", "书生(画外):“明日西行客,回头望故乡。”", 7,
   P + "close-up of the upper left corner of POEM WALL 736, a clean rectangular area of white plaster with faint brush marks reserved for one short poem, other fresh calligraphy around it, warm flickering oil lamp light, [开元], night interior lit by lamps",
   "slow lateral move from right to left across the reserved area, lamplight flickers on the plaster", key=True),
 S("52", "特写", "少年嘴唇跟读", "少年卢七:“苦泉犹可饮……”", 4,
   "close-up, the lips of LU QI, AGE 14: [锚点], silently shaping the words, firelight",
   "static camera, the lips move slowly"),
 S("53", "近景", "书生", "书生:“这是说,你们家的水苦,离别更苦。”", 5,
   "close shot, SCHOLAR: [锚点], turning from the wall to the boy, gentle",
   "static camera, he explains softly"),
 S("54", "近景", "少年", "少年卢七:“离别是苦的吗?”", 4,
   "close shot, LU QI, AGE 14: [锚点], looking up at the scholar, innocent",
   "static camera, he asks"),
 S("55", "近景", "书生笑而不答,望向门外西边夜色", "风声从门外渗入", 7,
   "close shot, SCHOLAR: [锚点], smiling without answering and turning his head toward the dark open door",
   "static camera, he smiles and turns to look out"),
 S("56", "中景", "少年跑向门口,回头看墙一眼", "卢父(画外):“七郎!马!”", 7,
   "medium shot, LU QI, AGE 14: [锚点], running through the crowd to the door, stopping at the threshold to look back at the wall",
   "static camera, he runs, stops, looks back"),
 S("57", "特写,缓推", "那首诗,墨色由暖转冷、褪去(转场)", "人声消失,只余风声", 6,
   "close-up of the oldest short poem at the upper left of the wall in lamplight",
   "slow push in, the ink cools from warm black to faded grey",
   out="the ink fades and cools; the next segment opens on the same poem in 787, almost gone."),
]),
dict(head="内景 驿厅 夜(787)", short="驿厅 夜(787)", era="787",
     env="the hall of POST STATION 787 at night, POEM WALL 787, a dying fire with two Tibetan soldiers asleep beside it, the bronze bell inside the door, the dark stable across the courtyard",
     tone="night, discovery, a question left open",
script="""
同一首诗,如今只剩下前五个字还看得清,后面的已经褪成一片淡痕。卢七的手带着软布,从这几个字旁边轻轻擦过。
入夜。甘布和诺桑裹着袍子睡在火堆边。卢七点亮桌上的油灯,拿起布,走进院里。马厩的黑暗里传来他的声音。
卢七(画外,轻声):来客人了。
张归独自提着灯笼,站在西墙前。灯光从层层叠叠的字迹上扫过。
张归(旁白):西墙,从左往右,从上往下。最老的那一首,只剩下五个字。
灯光沿着墙一点点往下移,直到墙脚。那里有一匹用炭画的马,线条稚拙,是小孩的手笔。周围的灰尘都擦得干干净净,唯独这匹马,从来没有被擦过。
张归蹲下来,手指悬在那匹马上方,没有碰。他回头,望向马厩那片黑暗。
门口,铜铃在夜风里轻轻晃着,没有响。
黑场。字幕:第一日。
""",
shots=[
 S("58", "特写,与镜 57 匹配剪辑", "同一首诗,只剩前五字可辨;卢七的手擦过", "擦墙声", 6,
   "close-up, the same oldest poem on POEM WALL 787, only the first five characters still legible, the rest faded to pale ghost marks, an old hand with a soft cloth wiping gently beside them",
   "static camera, the cloth passes beside the characters without touching them"),
 S("59", "全景", "吐蕃兵睡在火堆边,卢七点亮油灯,拿布出门", "火声", 8,
   "wide shot of the hall at night, TIBETAN SOLDIERS (GAMPO, NORSANG) asleep wrapped in their robes by a low fire, LU QI, AGE 65: [锚点], lighting an oil lamp on the table, picking up a cloth and walking to the door",
   "static camera, the lamp flares, he walks out"),
 S("60", "远景,门框构图", "卢七走进马厩的黑暗", "卢七(画外):“来客人了。”", 8,
   "long shot framed by the hall doorway, across the dark courtyard LU QI, AGE 65: [锚点], walking with a lamp into the black opening of the stable",
   "static camera, the small lamp disappears into the stable"),
 S("61", "中景", "张归独自提灯笼站在墙前", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], standing alone before POEM WALL 787 holding a paper lantern, the rest of the hall dark",
   "static camera, he lifts the lantern"),
 S("62", "特写,缓横移", "灯光扫过层层字迹", "旁白前半:“西墙,从左往右,从上往下。”", 10,
   P + "close-up, warm lantern light falling across POEM WALL 787 in darkness, overlapping calligraphy and cracks in plaster, [现实线 787]",
   "slow lateral move right to left, the pool of lantern light sliding over the characters", key=True),
 S("63", "特写,缓摇下", "灯光沿墙下移到墙脚", "旁白后半:“最老的那一首,只剩下五个字。”", 6,
   "close-up, the pool of lantern light sliding down the wall over layers of writing toward the floor",
   "slow tilt down following the light to the foot of the wall"),
 S("64", "特写,固定", "墙脚炭画的稚拙小马,周围擦得干净,唯独它未被擦过", "羌笛一个长音", 7,
   P + "close-up at floor level, a small clumsy child's charcoal drawing of a horse on the bottom of POEM WALL 787, the plaster around it wiped clean but the drawing itself untouched, lantern light, [现实线 787]",
   "static camera, lantern light trembles slightly, nothing else moves", key=True),
 S("65", "近景", "张归蹲下,手指悬在马上方,没有碰", "—", 5,
   "close shot, ZHANG GUI, AGE 18: [锚点], crouching at the foot of the wall, one finger hovering just above the charcoal horse without touching it",
   "static camera, the finger hovers and stays"),
 S("66", "中景", "张归回头望向马厩的黑暗", "远处马的鼻息", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], still crouching, turning his head to look through the dark doorway toward the stable",
   "static camera, he turns his head and holds"),
 S("67", "特写", "门口铜铃在夜风中轻晃,不响", "风声", 5,
   "close-up, the bronze bell hanging inside the hall door swaying very slightly in the night wind, moonlight beyond the door",
   "static camera, the bell sways without ringing",
   out="the bell sways; cut to black; title card."),
 S("68", "黑场", "字幕“第一日”", "风声渐止", 5, "", ""),
]),
])
