EP = dict(
cn="九", title="白发",
summary="第九集以现实线为主,过去和现在撞在一起。七个白发安西老兵徒步东归,要回关中。其中一人在苦泉边认出了柳树,喝了一口水,说出三十六年前卢七说过的那句话——他就是赵小满,今年五十一。卢七从木箱里取出那封没寄的信和那双没穿的鞋。张归知道往东全是吐蕃的地界,他本该上报,却连夜用吐蕃文写了一张通行文书,盖上了自己的印。黄昏,赵小满穿上那双小了的布鞋上路,卢七把铜铃拿到门口,摇了三声。",
info=[("场次", "8 场:现实 7 场,闪回 1 场(751)"),
      ("现实线人物", "卢七(65)、张归、甘布、诺桑、赵小满(51)、另外六名白发安西老兵、马“灰”"),
      ("闪回人物", "赵小满(15)"),
      ("钥匙物件", "未寄出的家书、布鞋(第 4 集)、张归写的通行文书、铜铃"),
      ("回收", "第 4 集卢七对少年说“苦泉。往西就没有水了。”本集由五十一岁的赵小满说出来;第 1 集卢七对张归说的也是这句。"),
      ("吐蕃兵的人性", "诺桑一句话不说,把自己的糌粑口袋放在老兵中间。他们不是反派。")],
curve="紧(敌我相遇)→ 认(苦泉那句话)→ 叠(十五岁与五十一岁)→ 沉(十二个人只剩七个)→ 哭(“不许哭”)→ 抉择(张归盖印)→ 送(鞋小了也穿着走)→ 响(三声铃)。",
anchors="""
ZHAO XIAOMAN, AGE 51: white-haired gaunt Tang veteran from Anxi, deeply sunburnt face, the same big ears and gap-toothed grin of the boy he was, battered lamellar armour patched with leather thongs, a cloth bundle on his back, a broken spear shaft as a walking stick, worn-out boots

VETERANS: six more white-haired Tang veterans of the Anxi garrison, gaunt and sunburnt, battered armour patched with leather, ragged red headscarves, walking sticks, one with an arm in a sling, dignified and exhausted

TIBETAN PASS: a sheet of paper written in Tibetan script with a small red square seal, folded in four
""",
scenes=[
dict(head="外景 驿门 清晨(787)", short="驿门 清晨(787)", era="787",
     env="the gate of POST STATION 787 at dawn, the old willow, the road from the west",
     tone="enemies face to face, too tired to fight",
script="""
字幕:第九日。
清晨。昨天黄昏出现在山口的人影走到了驿前。七个人,头发全白,身上的甲片残破,用皮绳一片一片补着。有人拄着断了的枪杆,有人吊着胳膊。
甘布抓起长矛,诺桑拔出了刀。
老兵们停下来。没有人去摸兵器。他们太累了。
张归从门里冲出来,挡在中间。
张归(吐蕃语,字幕):是回家的老人!
卢七提着一桶水,从门里走出来,放在地上。
""",
shots=[
 S("1", "大远景,固定", "清晨,七个白发老兵走到驿前", "脚步拖沓;字幕“第九日”", 9,
   "extreme long shot at dawn, seven white-haired VETERANS in patched armour walking slowly along the road from frame right to the gate of POST STATION 787 and the old willow", "static camera, the seven figures arrive slowly", key=True),
 S("2", "中景,缓横移", "一张张白发、晒裂的脸,补过的甲片,断枪杆,吊着的胳膊", "—", 7,
   "medium lateral shot along the line of VETERANS, white hair, cracked sunburnt faces, armour scales tied with leather thongs, a broken spear as a stick, an arm in a sling", "slow lateral move along the line of old men"),
 S("3", "中景", "甘布抓起长矛,诺桑拔刀", "拔刀声", 4,
   "medium shot, TIBETAN SOLDIERS (GAMPO, NORSANG) seizing a spear and drawing a short sword at the gate", "static camera, they raise their weapons"),
 S("4", "近景", "老兵们停下,没人去摸兵器", "—", 5,
   "close shot, the front VETERANS stopping, hands staying at their sides, too exhausted to fight, looking at the weapons without fear", "static camera, they stand still"),
 S("5", "中景", "张归冲出来挡在中间", "张归(吐蕃语):“是回家的老人!”", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], running out of the gate and stepping between the Tibetan weapons and the old men, arms spread", "static camera, he runs in and spreads his arms"),
 S("6", "中景", "卢七提一桶水出来,放在地上", "水桶落地", 5,
   "medium shot, LU QI, AGE 65: [锚点], walking out of the gate carrying a wooden bucket of water and setting it down in front of the old soldiers", "static camera, he sets the bucket down"),
]),
dict(head="外景 苦泉边 清晨(787)", short="苦泉边 清晨(787)", era="787",
     env="the stone-lined spring under the old willow hung with red cords, morning light",
     tone="recognition, slow then total",
script="""
老兵们围着苦泉喝水。一个老兵没有喝,仰头看着那棵柳树,看了很久。
赵小满:这柳树……当年才这么高。
他用手比了比自己的肩膀。然后低头,舀了一瓢水,喝了一口。
赵小满:苦的。
卢七提着空桶,站住了。
赵小满:苦泉。往西就没有水了。
卢七手里的桶掉在地上。
卢七:……小满?
老兵慢慢转过身来,咧开嘴,缺了一颗牙。
赵小满:哥?
""",
shots=[
 S("7", "中景", "老兵们围着苦泉喝水", "水声", 5,
   "medium shot, the VETERANS kneeling around the stone-lined spring drinking from their hands under the old willow", "static camera, they drink"),
 S("8", "近景,仰拍", "一个老兵仰头看柳树,看了很久", "—", 6,
   "low-angle close shot, ZHAO XIAOMAN, AGE 51: [锚点], standing apart looking up at the old willow and its red cords for a long time", "static camera, he gazes up"),
 S("9", "近景", "他用手比了比自己的肩膀", "赵小满:“这柳树……当年才这么高。”", 5,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], holding a hand flat at his own shoulder height, speaking to himself", "static camera, he measures with his hand"),
 S("10", "近景", "他舀一瓢水喝了一口", "赵小满:“苦的。”", 5,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], drinking from a ladle and screwing up his face exactly like a boy", "static camera, he drinks and grimaces"),
 S("11", "近景", "卢七提着空桶站住了", "—", 3,
   "close shot, LU QI, AGE 65: [锚点], holding an empty bucket, stopping dead", "static camera, he freezes"),
 S("12", "近景", "赵小满", "赵小满:“苦泉。往西就没有水了。”", 5,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], saying it to the water with a small smile", "static camera, he says it softly", key=True),
 S("13", "特写", "桶掉在地上", "咚", 3,
   "close-up, a wooden bucket dropping onto the sand by the spring", "static camera, the bucket falls and rolls"),
 S("14", "近景,极缓推", "卢七", "卢七:“……小满?”", 5,
   "close shot, LU QI, AGE 65: [锚点], his mouth open, eyes wet, saying a name", "extremely slow push in, he says the name"),
 S("15", "近景", "老兵慢慢转身,咧开嘴,缺一颗牙", "赵小满:“哥?”", 6,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], turning around slowly and breaking into a gap-toothed grin", "static camera, he turns and grins", key=True),
]),
dict(head="外景 驿门(闪回,751 / 787)", short="驿门 叠化(751/787)", era="天宝",
     env="the same gate from the same camera position in 751 and 787, the willow young in 751 and old in 787",
     tone="thirty-six years in one dissolve",
script="""
同一个机位。三十六年前,十五岁的少年在门前回头大喊:“哥——!”
画面叠化。同一个位置,站着五十一岁的白发老兵。两个人的手同时抬起来。
""",
shots=[
 S("16", "中景,固定", "751:十五岁的少年在门前回头挥手(与第 4 集同机位)", "少年的喊声回响:“哥——!”", 5,
   "medium shot from a fixed position at the gate in 751, ZHAO XIAOMAN, AGE 15: [锚点], turning back on the road and waving both arms, the young willow behind", "static camera, locked-off, the boy waves", key=True),
 S("17", "中景,固定,叠化", "叠化为 787:同一位置站着五十一岁的老兵,手同时抬起来", "风声", 7,
   "medium shot from the identical fixed position in 787, ZHAO XIAOMAN, AGE 51: [锚点], standing on the same spot, slowly raising one hand, the old willow with red cords behind", "slow dissolve from the boy to the old man, identical framing, the raised hands overlap", era="787"),
]),
dict(head="内景 驿厅 午(787)", short="驿厅 午(787)", era="787",
     env="the hall of POST STATION 787 at noon, the fire pit relit, the old soldiers resting on the floor, POEM WALL 787",
     tone="a long road told in few words",
script="""
驿厅。火塘重新生了火。老兵们靠墙坐着,有人已经睡着了。
诺桑一句话不说,走过来,把自己的糌粑口袋放在老兵中间,转身走了。
赵小满:怛罗斯败了,我被大食人抓去,后来跑回了安西。在安西守了三十多年。
赵小满:朝廷不知道还有我们。如今安西也快守不住了,将军放老的回家。
卢七:几个人?
赵小满:从龟兹出来的时候,十二个。走了四个月。
他看了看靠墙的同伴。
赵小满:还剩七个。
""",
shots=[
 S("18", "全景,固定", "火塘重新生了火,老兵们靠墙坐着,有人睡着", "火声", 7,
   "wide shot of the hall at noon, a fire burning again in the pit, the white-haired VETERANS sitting against the wall, some asleep, ZHAO XIAOMAN, AGE 51: [锚点], and LU QI, AGE 65: [锚点], by the fire", "static camera, the fire crackles"),
 S("19", "中景", "诺桑把糌粑口袋放在老兵中间,转身走了", "—", 6,
   "medium shot, NORSANG of the TIBETAN SOLDIERS (GAMPO, NORSANG) silently setting his leather tsampa bag down among the old soldiers and walking away", "static camera, he sets it down and leaves", key=True),
 S("20", "近景", "赵小满", "赵小满:“怛罗斯败了,我被大食人抓去,后来跑回了安西。在安西守了三十多年。”", 9,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], speaking plainly, firelight", "static camera, he tells it simply"),
 S("21", "近景", "赵小满", "赵小满:“朝廷不知道还有我们。如今安西也快守不住了,将军放老的回家。”", 8,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], looking into the fire", "static camera, he speaks without emotion"),
 S("22", "近景", "卢七", "卢七:“几个人?”", 3,
   "close shot, LU QI, AGE 65: [锚点], by the fire", "static camera, he asks"),
 S("23", "近景", "赵小满", "赵小满:“从龟兹出来的时候,十二个。走了四个月。”", 6,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], answering", "static camera, he answers"),
 S("24", "中景,缓横移", "他看了看靠墙的同伴", "赵小满:“还剩七个。”", 6,
   "medium lateral shot along the sleeping VETERANS against the wall, ZHAO XIAOMAN's voice", "slow lateral move along the sleeping old men"),
]),
dict(head="内景 后房 午(787)", short="后房 午(787)", era="787",
     env="LU QI's back room in 787, the chest open, the cloth shoes and the letter",
     tone="the letter reaches its writer",
script="""
后房。卢七打开木箱,取出那双布鞋和那封信,放在赵小满手里。
赵小满看着鞋帮上的“满”字,手开始抖。
赵小满:我不认字。
张归接过信。
张归:我念。
张归:阿娘:儿到瓜州了。这里风大,沙子比咱家麦子还多。驿里有个哥哥待儿好,给儿炖了羊。鞋儿合脚,儿没舍得穿。等儿立了功,就回家给阿娘扯一匹绢。
张归停了一下。
张归:不许哭。
赵小满低着头,肩膀一抽一抽的。
赵小满:我娘……不知道还在不在。
他把信折好,揣进怀里,按住。
赵小满:这信,我自己送。
""",
shots=[
 S("25", "中景", "卢七打开木箱,取出布鞋和信,放在赵小满手里", "—", 7,
   "medium shot of the back room, LU QI, AGE 65: [锚点], taking the CLOTH SHOES and the folded letter from the chest and placing them in the hands of ZHAO XIAOMAN, AGE 51: [锚点]", "static camera, the objects pass into the veteran's hands"),
 S("26", "特写", "鞋帮上的“满”字,手开始抖", "—", 5,
   "close-up, the red stitched character on the heel of a black cloth shoe in old scarred hands that begin to tremble", "static camera, the hands tremble", key=True),
 S("27", "双人", "赵小满;张归接过信", "赵小满:“我不认字。”张归:“我念。”", 5,
   "two-shot, ZHAO XIAOMAN, AGE 51: [锚点], holding out the letter helplessly, ZHANG GUI, AGE 18: [锚点], taking it", "static camera, the letter passes"),
 S("28", "近景", "张归念信", "张归:“阿娘:儿到瓜州了。这里风大,沙子比咱家麦子还多。驿里有个哥哥待儿好,给儿炖了羊。”", 9,
   "close shot, ZHANG GUI, AGE 18: [锚点], reading the old letter aloud carefully", "static camera, he reads steadily"),
 S("29", "近景", "赵小满听着", "张归:“鞋儿合脚,儿没舍得穿。等儿立了功,就回家给阿娘扯一匹绢。”", 8,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], listening with his eyes closed, the shoes in his lap", "static camera, he listens"),
 S("30", "近景", "张归停了一下", "张归:“不许哭。”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], pausing before the last line, then reading it", "static camera, a pause, then the line"),
 S("31", "近景", "赵小满低头,肩膀一抽一抽", "赵小满:“我娘……不知道还在不在。”", 7,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], head bowed, shoulders shaking, trying not to cry", "static camera, he shakes"),
 S("32", "特写", "他把信折好,揣进怀里,按住", "赵小满:“这信,我自己送。”", 6,
   "close-up, old scarred hands folding the letter, tucking it inside the patched armour and pressing a hand over it", "static camera, he tucks it in and presses", key=True),
]),
dict(head="外景 驿门 午后(787)", short="驿门 午后(787)", era="787",
     env="the gate of POST STATION 787 in the afternoon, the road east",
     tone="a young man chooses",
script="""
午后。张归和卢七站在门口,看着往东的驿道。
张归:往东,全是吐蕃的地界。关卡一道接一道。他们走不到。
卢七:你要报吗?
张归没有回答。
""",
shots=[
 S("33", "大远景,固定", "往东的驿道伸到天边", "风声", 6,
   "extreme long shot looking east along the empty road in afternoon light, the road running to the horizon", "static camera, dust drifts"),
 S("34", "双人", "张归和卢七站在门口", "张归:“往东,全是吐蕃的地界。关卡一道接一道。他们走不到。”", 8,
   "two-shot, ZHANG GUI, AGE 18: [锚点], and LU QI, AGE 65: [锚点], standing in the gate looking east", "static camera, he speaks, the old man listens"),
 S("35", "近景", "卢七", "卢七:“你要报吗?”", 3,
   "close shot, LU QI, AGE 65: [锚点], turning his head to the young man", "static camera, he asks"),
 S("36", "近景,极缓推", "张归没有回答", "—", 6,
   "close shot, ZHANG GUI, AGE 18: [锚点], silent, looking east, jaw tight", "extremely slow push in, he does not answer"),
]),
dict(head="内景 驿厅 午后(787)", short="驿厅 午后(787)", era="787",
     env="the hall of POST STATION 787, the copying table, paper and ink, the poem wall behind",
     tone="quiet treason",
script="""
驿厅。张归在矮几前铺开一张新纸,用吐蕃文一笔一笔地写。
写完,他从腰间解下一枚小小的铜印,呵了口气,盖了下去。
卢七站在他身后,看着。
""",
shots=[
 S("37", "特写", "张归用吐蕃文一笔一笔写", "笔声", 7,
   "close-up, a young hand writing lines of Tibetan script on a fresh sheet of paper with a brush, the poem wall soft behind", "static camera, the brush writes Tibetan letters"),
 S("38", "特写", "解下腰间小铜印,呵口气,盖下去", "印落", 6,
   "close-up, the young hand untying a small bronze seal from his belt, breathing on it, pressing it onto the paper to leave a red square", "static camera, the seal presses down", key=True),
 S("39", "近景", "卢七站在他身后看着", "—", 5,
   "close shot, LU QI, AGE 65: [锚点], standing behind the young man, looking at the sealed paper", "static camera, he watches in silence"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the old willow with red cords, the road east, the seven veterans ready to leave",
     tone="the most complete farewell in the series",
script="""
黄昏。老兵们收拾好了。
张归把折好的文书塞给赵小满。
张归:沿路有人查,给他们看这个。
赵小满看看文书,又看看张归身上的羊皮袍,点了点头。
他坐在门槛上,脱下破靴子,把那双布鞋穿上。鞋小了,脚后跟塞不进去。他把鞋后帮踩扁,趿着站起来,走了两步。
赵小满:合脚。
卢七转身走进院子,从驿厅门框上解下铜铃,拿到门口。
他举起铃,摇了三声。
三声铃响,荡过空空的驿道。
卢七:前头有水。
赵小满:哥,回去了。
七个老兵往东走。走出去老远,赵小满回过头,像三十六年前一样大喊。
赵小满:哥——!
""",
shots=[
 S("40", "中景", "张归把文书塞给赵小满", "张归:“沿路有人查,给他们看这个。”", 6,
   "medium shot at dusk, ZHANG GUI, AGE 18: [锚点], pressing a folded TIBETAN PASS into the hand of ZHAO XIAOMAN, AGE 51: [锚点], the other veterans behind", "static camera, the paper passes"),
 S("41", "近景", "赵小满看看文书,看看张归的羊皮袍,点头", "—", 5,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], looking at the paper, then at the young man's Tibetan sheepskin robe, then nodding once", "static camera, he looks and nods"),
 S("42", "特写", "坐在门槛上,脱下破靴,穿上布鞋,脚后跟塞不进去,把后帮踩扁", "—", 9,
   "close-up, old feet on the gate threshold pulling off worn-out boots and pushing into the black CLOTH SHOES, too small, the heels crushing the backs flat", "static camera, he squeezes in and treads the heels down", key=True),
 S("43", "近景", "他趿着鞋站起来,走两步", "赵小满:“合脚。”", 5,
   "close shot, ZHAO XIAOMAN, AGE 51: [锚点], standing in the shoes, taking two steps, grinning", "static camera, he walks two steps and grins"),
 S("44", "中景", "卢七从驿厅门框上解下铜铃,拿到门口", "—", 7,
   "medium shot through the gate, LU QI, AGE 65: [锚点], untying the bronze bell from the hall door and carrying it across the courtyard to the gate", "static camera, he carries the bell to the gate"),
 S("45", "近景,仰拍", "他举起铃,摇了三声", "铃声三响,清亮(与第 4 集卢父那三声呼应)", 6,
   "low-angle close shot, LU QI, AGE 65: [锚点], raising the bronze bell high and ringing it three times, dusk sky behind", "static camera, three clear rings", key=True),
 S("46", "双人", "卢七与赵小满", "卢七:“前头有水。”赵小满:“哥,回去了。”", 6,
   "two-shot at the gate, LU QI, AGE 65: [锚点], holding the bell, ZHAO XIAOMAN, AGE 51: [锚点], facing him", "static camera, they speak and part"),
 S("47", "大远景,固定", "七个老兵往东(画左)走远;赵小满回头大喊", "赵小满:“哥——!”", 10,
   "extreme long shot at dusk, seven old soldiers walking away east toward frame left, far down the road one turns back and waves both arms, the gate and willow on the right", "static camera, the line walks away, one figure turns and waves", key=True),
 S("48", "近景", "卢七抱着铜铃站在门口", "旁白:“第九日。老卒七人,东归。通行文书一纸,是我写的。这一行,我没有写进簿子。”", 9,
   "close shot, LU QI, AGE 65: [锚点], holding the bronze bell against his chest at the gate, watching the road east, ZHANG GUI, AGE 18: [锚点], beside him", "static camera, they watch until the end",
   out="hold, the dusk deepens; end of episode."),
]),
])
