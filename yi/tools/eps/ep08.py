EP = dict(
cn="八", title="孤灯",
summary="第八集讲一个人守驿的十七年。吐蕃节儿亲自来查,发现十天过了七天,驿站一砖未动。张归第一次撒谎:他说墙上有当年金城公主西嫁时的题字,须先抄录呈给赞普。节儿只给了三天。回忆线从广德二年最后一个驿卒离开讲起:卢七把铜铃从门楼摘下,挂进驿厅门内;此后十七年,他每夜点灯,对着马说话。建中元年一个风雪夜,安西信使李承知独骑而来,怀里揣着给朝廷的奏报,问:“长安还在吗?”卢七把最后一匹好马换给了他。",
info=[("场次", "10 场:现实 3 场,回忆 7 场(764–780)"),
      ("现实线人物", "卢七(65)、张归、节儿、甘布、诺桑、节儿的随从"),
      ("回忆线人物", "卢七(42–58)、最后一个驿卒老周、马“灰”、安西信使李承知"),
      ("钥匙物件", "作废的驿券(建中元年,已过期一年);铜铃移进驿厅"),
      ("补上的连续性", "本集第 5、6 场交代铜铃从门楼移进驿厅门内,接上第 1 集第 3 场诺桑在驿厅门框碰响铜铃。"),
      ("张归的谎", "金城公主是真实人物:景龙四年(710)嫁吐蕃赞普,吐蕃人敬重她。张归借她的名义保墙,节儿不敢轻易拆。墙上其实没有她的字。")],
curve="紧(节儿来了)→ 险(张归撒谎)→ 问(“撒谎要掉脑袋的”)→ 散(最后一个驿卒走了)→ 孤(十七年的灯)→ 急(风雪夜的信使)→ 痛(“长安还在吗”)→ 悬(西边山口来了人)。",
anchors="""
THE JIER: middle-aged Tibetan district official of the Tibetan Empire, broad weathered face, long braided hair under a tall felt hat with fur trim, fine brocade-edged sheepskin robe, a gold-inlaid belt, calm and watchful, riding with four armed attendants

LU QI, AGE 42-58: the station master aging alone, beard going from grey to almost white, face growing thinner, the same faded dark green round-collar robe more and more patched, a felt wine skin always at his belt

OLD ZHOU: the last post soldier, a stooped Han Chinese man in his fifties, worn padded jacket, a cloth bundle on his back, ashamed eyes

HUI (THE HORSE): a grey horse, in 764 about ten years old and strong, by 780 old and thin with a white muzzle

LI CHENGZHI: Tang courier from Anxi in his forties, gaunt face cracked by frost, ice in his beard, a fur cloak over a stained green official robe, a sealed bamboo document tube strapped across his chest, desperate eyes

POST VOUCHER: a small sheet of paper with a red seal and a date, creased and water-stained
""",
scenes=[
dict(head="外景 驿门 午(787)", short="驿门 午(787)", era="787",
     env="the gate of POST STATION 787 at noon under a flat grey sky, the old willow, the road from the west",
     tone="danger arriving on horseback",
     crowd="four Tibetan mounted attendants of the Jier",
script="""
字幕:第八日。
正午。西边驿道上来了五匹马。领头的人戴着镶毛边的高毡帽。
甘布和诺桑正躺在柳树下晒太阳,一骨碌爬起来,一个抓斧子,一个去搬马厩的栏杆,装作在干活。
节儿在门前勒马,看看完好的门楼,看看完好的围墙。
节儿(吐蕃语,字幕):七天了。一块砖都没动?
张归从院里快步出来,躬身行礼。
""",
shots=[
 S("1", "大远景,固定", "灰天,西边驿道上来了五匹马", "马蹄;字幕“第八日”", 7,
   "extreme long shot at noon under a flat grey sky, five riders coming along the road from frame right toward POST STATION 787 and the old willow, the leader in a tall fur-trimmed hat", "static camera, the riders approach from the right"),
 S("2", "中景", "甘布和诺桑一骨碌爬起来,一个抓斧子一个搬栏杆", "—", 5,
   "medium shot, TIBETAN SOLDIERS (GAMPO, NORSANG) scrambling up from a nap under the willow, one grabbing an axe, the other hauling at a stable rail, pretending to work", "static camera, they scramble comically"),
 S("3", "中景,仰拍", "节儿在门前勒马,看完好的门楼", "—", 5,
   "low-angle medium shot, THE JIER reining in before the gate on horseback, looking up at the untouched gate tower", "static camera, he looks up slowly"),
 S("4", "近景", "节儿", "节儿(吐蕃语):“七天了。一块砖都没动?”", 5,
   "close shot, THE JIER, calm and cold, looking down from the saddle", "static camera, he speaks quietly", key=True),
 S("5", "中景", "张归从院里快步出来,躬身行礼", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], hurrying out of the gate and bowing deeply before the mounted official", "static camera, he hurries out and bows"),
]),
dict(head="内景 驿厅 午(787)", short="驿厅 午(787)", era="787",
     env="the hall of POST STATION 787 at noon, POEM WALL 787, the copying table with a long paper scroll",
     tone="a lie told calmly in front of the man it protects",
     crowd="two Tibetan attendants at the door",
script="""
驿厅。节儿站在西墙前。卢七在墙的另一头擦着,没有停手。
节儿(吐蕃语,字幕):这面墙是什么?
张归(吐蕃语,字幕):回节儿:墙上有金城公主当年西嫁时留的字。小人正在抄录,要呈给赞普。公主的字,不敢毁。
卢七的手停了一下。他回头看了张归一眼。
节儿看着满墙的字,看了很久。他伸手摸了摸墙面。
节儿(吐蕃语,字幕):三天。三天后,不管抄完没抄完,拆。
他转身走了。
""",
shots=[
 S("6", "全景,固定", "节儿站在西墙前,卢七在墙另一头擦墙", "擦墙声", 7,
   "wide shot of the hall, THE JIER standing before POEM WALL 787, ZHANG GUI, AGE 18: [锚点], beside him, LU QI, AGE 65: [锚点], wiping the far end of the wall without stopping", "static camera, the old man keeps wiping"),
 S("7", "近景", "节儿", "节儿(吐蕃语):“这面墙是什么?”", 4,
   "close shot, THE JIER, looking up at the wall of calligraphy", "static camera, he asks"),
 S("8", "近景,极缓推", "张归平静地撒谎", "张归(吐蕃语):“回节儿:墙上有金城公主当年西嫁时留的字。小人正在抄录,要呈给赞普。公主的字,不敢毁。”", 10,
   "close shot, ZHANG GUI, AGE 18: [锚点], speaking calmly and respectfully, eyes lowered, only his hand tight on his belt betraying him", "extremely slow push in, he speaks steadily", key=True),
 S("9", "近景", "卢七的手停了一下,回头看张归", "—", 4,
   "close shot, LU QI, AGE 65: [锚点], the cloth stopping on the wall, turning his head to look at the young man", "static camera, he stops and looks"),
 S("10", "主观,缓横移", "节儿的目光扫过满墙的字", "—", 6,
   "point-of-view lateral move across dense layered calligraphy on the old wall, the ghosts of faded lines", "slow lateral move across the wall"),
 S("11", "特写", "节儿伸手摸了摸墙面", "—", 4,
   "close-up, a hand with a gold ring and brocade cuff touching the cracked plaster between lines of writing", "static camera, the hand rests on the wall"),
 S("12", "近景", "节儿转身", "节儿(吐蕃语):“三天。三天后,不管抄完没抄完,拆。”", 6,
   "close shot, THE JIER, taking his hand from the wall and turning to the young man", "static camera, he speaks and turns away"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the hall door visible across the courtyard with the bronze bell hanging inside it",
     tone="two people now on the same side",
script="""
黄昏。节儿的马队已经走远了。
卢七:墙上没有金城公主。
张归:我知道。
卢七:撒谎是要掉脑袋的。
张归:……三天,够抄完了。
卢七看了他很久,转身走进院子,停在驿厅门口,抬头看门内挂着的铜铃。
卢七:这只铃,原来挂在门楼上。
""",
shots=[
 S("13", "大远景,固定", "节儿的马队往西远去", "马蹄远去", 6,
   "extreme long shot at dusk, five riders growing small along the road to the west, the gate and willow in the foreground", "static camera, they shrink into the distance"),
 S("14", "双人", "卢七和张归站在门口", "卢七:“墙上没有金城公主。”张归:“我知道。”", 6,
   "two-shot at the gate at dusk, LU QI, AGE 65: [锚点], and ZHANG GUI, AGE 18: [锚点], side by side watching the riders go", "static camera, they speak without looking at each other"),
 S("15", "近景", "卢七", "卢七:“撒谎是要掉脑袋的。”", 3,
   "close shot, LU QI, AGE 65: [锚点], turning to the young man", "static camera, he turns and says it"),
 S("16", "近景", "张归", "张归:“……三天,够抄完了。”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], a stubborn small smile", "static camera, he answers"),
 S("17", "全景,门框构图", "卢七穿过院子,停在驿厅门口,抬头看门内的铜铃", "—", 7,
   "wide shot through the gate across the courtyard, LU QI, AGE 65: [锚点], walking to the hall door and stopping to look up at the bronze bell hanging just inside it", "static camera, he walks and stops"),
 S("18", "近景,仰拍", "铜铃", "卢七:“这只铃,原来挂在门楼上。”", 5,
   "low-angle close shot of the bronze bell hanging inside the hall door, its clapper tied with a faded red cord, an old man's face below it", "slow push in on the bell",
   out="push into the bronze of the bell until its dull gleam warms into autumn light; the next segment opens in 764."),
]),
dict(head="外景 驿门 秋(回忆,764)", short="驿门 秋(764)", era="乱后",
     env="the gate in autumn 764, the bell hanging outside the gate tower from a long cord, the willow with twenty red cords and yellow leaves, an empty stable but for one grey horse",
     tone="the last one leaves",
script="""
字幕:广德二年,秋。
最后一个驿卒老周背着包袱站在门口,不敢抬头。
老周:七郎,对不住。家里还有老娘。
卢七:前头有水。
老周往东走了。
卢七站在门口。门楼下的铜铃在风里轻轻晃。
他搬来梯子,爬上去,把铃从门楼上解了下来。
""",
shots=[
 S("19", "中景", "老周背着包袱站在门口,不敢抬头", "老周:“七郎,对不住。家里还有老娘。”", 7,
   "medium shot in autumn, OLD ZHOU with a cloth bundle on his back standing at the gate, head bowed, LU QI, AGE 42-58: [锚点], facing him", "static camera, the old soldier speaks to the ground"),
 S("20", "近景", "卢七", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 42-58: [锚点], nodding once", "static camera, he says the farewell line"),
 S("21", "大远景,固定", "老周往东(画左)走远;门口只剩一个人", "风声;字幕“广德二年,秋”", 8,
   "extreme long shot, a single stooped figure walking away east toward frame left, a lone man left at the gate under the willow with yellow leaves", "static camera, the figure shrinks", key=True),
 S("22", "近景,仰拍", "门楼下的铜铃在风里轻轻晃", "铃舌轻碰,不响", 4,
   "low-angle close shot of the bronze bell hanging from its long cord under the gate tower, swinging slightly in the wind", "static camera, the bell sways"),
 S("23", "中景", "卢七搬梯子爬上去,把铃解下来", "—", 8,
   "medium shot, LU QI, AGE 42-58: [锚点], climbing a ladder against the gate tower and untying the bell from its cord", "static camera, he climbs and unties it"),
]),
dict(head="内景 驿厅 夜(回忆,764)", short="驿厅 夜(764)", era="乱后",
     env="the empty hall at night in 764, the door to the courtyard, one oil lamp",
     tone="a man making his solitude livable",
script="""
夜。卢七站在驿厅门内,踮着脚,把铜铃系在门框上方的横木上。
他用手指碰了一下铃舌。“叮。”
卢七:一个人守,夜里在屋里得听得见。
他提着灯走到马厩。灰站在暗处。
卢七:今天也没有人来。
""",
shots=[
 S("24", "中景", "卢七踮脚把铜铃系在驿厅门框上方", "—", 7,
   "medium shot, LU QI, AGE 42-58: [锚点], standing on his toes inside the hall door, tying the bronze bell to the beam above the door frame, one oil lamp", "static camera, he ties the knot"),
 S("25", "特写", "手指碰了一下铃舌", "“叮”", 4,
   "close-up, a fingertip tapping the clapper of the bell, the bell ringing once in the dark", "static camera, the bell rings once", key=True),
 S("26", "近景", "卢七", "卢七:“一个人守,夜里在屋里得听得见。”", 5,
   "close shot, LU QI, AGE 42-58: [锚点], looking up at the bell, talking to himself", "static camera, he speaks to nobody"),
 S("27", "中景", "他提灯走进马厩,灰站在暗处", "卢七:“今天也没有人来。”", 6,
   "medium shot, LU QI, AGE 42-58: [锚点], carrying a lamp into the dark stable where HUI (THE HORSE) stands alone, stroking its neck", "static camera, he strokes the horse and speaks"),
]),
dict(head="内景 驿厅 夜(回忆,765–779)", short="十七年 夜(765–779)", era="乱后",
     env="the same corner of the hall at night across many years, one table, one oil lamp, the door with the bell, seasons changing outside",
     tone="time passing in the same frame",
script="""
同一个机位,同一盏灯。一年又一年。
卢七点灯。窗外是雪。
卢七(对马):西墙又掉了一块灰,我补上了。
卢七点灯。窗外是风沙。他的胡子更白了。
卢七(对马):柳树系到第三十根了。
卢七点灯。窗外是雨。他点灯的手有点抖。
卢七(对马):你也老了。
""",
shots=[
 S("28", "中景,固定", "卢七点灯,窗外是雪", "卢七(对马):“西墙又掉了一块灰,我补上了。”", 7,
   "medium shot, the same corner of the dark hall, LU QI, AGE 42-58: [锚点], lighting an oil lamp on the table, snow falling outside the window", "static camera, locked-off; he lights the lamp", key=True),
 S("29", "中景,固定,同机位", "卢七点灯,窗外风沙,胡子更白了", "卢七(对马):“柳树系到第三十根了。”", 7,
   "medium shot, the identical framing, LU QI, AGE 42-58: [锚点], older, beard greyer, lighting the same lamp, sand blowing past the window", "static camera, locked-off, identical framing; he lights the lamp"),
 S("30", "中景,固定,同机位", "卢七点灯,窗外下雨,点灯的手有点抖", "卢七(对马):“你也老了。”", 7,
   "medium shot, the identical framing, LU QI, AGE 42-58: [锚点], older still, beard nearly white, lighting the lamp with a trembling hand, rain outside", "static camera, locked-off, identical framing; his hand trembles"),
 S("31", "大远景,固定", "夜里的驿站,只有一扇窗亮着灯", "风声", 7,
   "extreme long shot at night, the dark post station in the empty desert, one small lit window, the tall willow", "static camera, the lamp glows"),
]),
dict(head="外景 驿门 风雪夜(回忆,780)", short="驿门 风雪夜(780)", era="乱后",
     env="the gate in a blizzard at night in 780, the willow bent in the wind, deep snow",
     tone="sudden urgency in a dead place",
script="""
字幕:建中元年。
风雪夜。驿厅门内的铜铃忽然被风吹响。卢七抬起头。
门外传来马蹄,又停了。
卢七提着灯冲出去。门口,一匹马倒在雪里,马上的人滚下来,爬不起来。他胸前绑着一只竹筒。
卢七把他架进门。
""",
shots=[
 S("32", "近景", "铜铃被风吹响,卢七抬头", "铃声;字幕“建中元年”", 4,
   "close shot, LU QI, AGE 42-58: [锚点], nearly white-bearded, looking up sharply from the lamp toward the ringing bell", "static camera, he looks up"),
 S("33", "大远景,固定", "风雪里一骑踉跄而来,倒在门口", "风雪、马嘶", 7,
   "extreme long shot in a blizzard at night, a single rider staggering out of the snow toward the gate, the horse collapsing", "static camera, the horse goes down in the snow"),
 S("34", "中景", "卢七提灯冲出门;那人滚下马,胸前绑着竹筒", "—", 6,
   "medium shot, LU QI, AGE 42-58: [锚点], running out with a lamp, LI CHENGZHI rolling off the dead horse into the snow, a bamboo document tube strapped to his chest", "static camera, the old man reaches him"),
 S("35", "中景", "卢七把他架进门", "风雪", 5,
   "medium shot, LU QI, AGE 42-58: [锚点], hauling LI CHENGZHI to his feet and half-carrying him into the gate", "static camera, they struggle through the gate"),
]),
dict(head="内景 驿厅 夜(回忆,780)", short="驿厅 夜(780)", era="乱后",
     env="the hall at night in 780, a revived fire, one oil lamp, snow blowing at the door",
     tone="the loneliest question in the series",
script="""
火塘边。李承知裹着毯子发抖,双手死死抱着竹筒。
李承知:安西……北庭……还在。还守着。朝廷不知道。我要去长安报信。
他抬起头。
李承知:长安……还在吗?
卢七:不知道。十几年,没有驿骑从东边来了。
李承知闭上眼。过了一会儿,他从怀里掏出一张纸。
李承知:驿券。建中元年正月的……过期了。
卢七接过来,看了看上面的红印,折好,揣进怀里。
卢七:马在后院。
""",
shots=[
 S("36", "中景", "李承知裹着毯子发抖,死死抱着竹筒", "牙齿打战", 6,
   "medium shot by the fire, LI CHENGZHI wrapped in a blanket, shaking, clutching the bamboo tube to his chest, LU QI, AGE 42-58: [锚点], feeding the fire", "static camera, he shakes"),
 S("37", "近景", "李承知", "李承知:“安西……北庭……还在。还守着。朝廷不知道。我要去长安报信。”", 9,
   "close shot, LI CHENGZHI, frost melting in his beard, speaking in short urgent gasps", "static camera, he speaks between breaths"),
 S("38", "近景,极缓推", "他抬起头", "李承知:“长安……还在吗?”", 6,
   "close shot, LI CHENGZHI, lifting his eyes to the old man, firelight", "extremely slow push in, he asks", key=True),
 S("39", "近景", "卢七", "卢七:“不知道。十几年,没有驿骑从东边来了。”", 6,
   "close shot, LU QI, AGE 42-58: [锚点], answering honestly, firelight", "static camera, he answers"),
 S("40", "特写", "李承知从怀里掏出一张驿券", "李承知:“驿券。建中元年正月的……过期了。”", 6,
   "close-up, a frost-cracked hand holding out a creased POST VOUCHER with a red seal", "static camera, the hand offers the voucher"),
 S("41", "特写", "卢七看看红印,折好,揣进怀里", "卢七:“马在后院。”", 6,
   "close-up, an old man's hands taking the voucher, looking at the red seal, folding it and tucking it inside his robe", "static camera, he folds and pockets it"),
]),
dict(head="外景 驿门 风雪夜(回忆,780)", short="驿门 风雪夜(780)", era="乱后",
     env="the gate in the blizzard at night in 780, the stable lit by one lantern, a strong bay horse and the old grey horse HUI",
     tone="a gift with nothing to gain",
script="""
马厩里有两匹马:一匹壮实的枣红马,和老了的灰。
卢七把枣红马牵出来,把缰绳交给李承知。
李承知:这是你最后一匹?
卢七:还有一匹老的。
李承知翻身上马,在门口回头。
李承知:长安要是还在,我替你问一声。
卢七:前头有水。
李承知冲进了风雪里,往东。
""",
shots=[
 S("42", "中景", "马厩里一匹壮实的枣红马和老了的灰", "马喷鼻", 5,
   "medium shot of the stable lit by a lantern, a strong bay horse and the old HUI (THE HORSE) side by side", "static camera, the horses shift in the cold"),
 S("43", "中景", "卢七把枣红马牵出来,缰绳交给李承知", "李承知:“这是你最后一匹?”卢七:“还有一匹老的。”", 8,
   "medium shot, LU QI, AGE 42-58: [锚点], leading the bay horse out and putting the reins in the hand of LI CHENGZHI", "static camera, the reins change hands"),
 S("44", "中景", "李承知翻身上马,在门口回头", "李承知:“长安要是还在,我替你问一声。”", 6,
   "medium shot, LI CHENGZHI swinging up onto the bay horse at the gate and turning back in the saddle, snow whirling", "static camera, he mounts and turns"),
 S("45", "近景", "卢七", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 42-58: [锚点], snow on his white beard", "static camera, he says the farewell line"),
 S("46", "大远景,固定", "一骑冲进风雪,往东(画左)", "风雪", 7,
   "extreme long shot, a rider galloping away east toward frame left into the blizzard, the small lit gate on the right", "static camera, the rider is swallowed by the snow", key=True,
   out="the blizzard fades to white and the white cools into the grey dusk of 787."),
 S("47", "近景", "空了的马厩里,只剩灰", "—", 5,
   "close shot, HUI (THE HORSE) standing alone in the stable, old and thin, looking at the door", "static camera, the old horse waits"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the old willow, the road west toward a distant mountain pass",
     tone="still, then a shiver of hope",
script="""
黄昏。卢七把那张驿券递给张归。
卢七:他没有再回来。
张归接过来,在簿子上写了一行。
他抬起头,看见西边。
西边的山口,出现了一队人影。很慢,很慢地,朝驿站走过来。
张归(旁白):第八日。驿券一张,作废。黄昏,西边山口,来了人。
""",
shots=[
 S("48", "特写", "卢七把驿券递给张归", "卢七:“他没有再回来。”", 5,
   "close-up, an old man's hand passing the creased POST VOUCHER with its faded red seal to a young hand, dusk light", "static camera, the voucher passes"),
 S("49", "中景", "张归在簿子上写一行,抬起头", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], writing in the register on his knee at the gate, then lifting his head toward the west", "static camera, he writes, then looks up"),
 S("50", "近景", "张归愣住", "—", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], staring west, eyes widening", "static camera, he stares"),
 S("51", "大远景,固定", "西边山口出现一队人影,很慢地朝驿站走来", "旁白:“第八日。驿券一张,作废。黄昏,西边山口,来了人。”风声", 10,
   "extreme long shot at dusk looking west, far away at a mountain pass a short line of small human figures appearing and walking very slowly toward the station along the road", "static camera, the figures inch closer", key=True,
   out="hold on the distant figures; cut to black; end of episode."),
]),
])
