EP = dict(
cn="六", title="东去",
summary="第六集是全剧的转折:方向从向西变成向东。张归终于问出那句话:“你为什么不走?”回忆线回到天宝十四载冬:安禄山起兵的消息从东边传来,河西大军连夜东调,驿站一夜之间挤满兵马,驿马全被征走。儿时玩伴王进拉卢七一起去长安勤王,两人爬上汉代烽燧,看火把的河流往东淌。天亮时卢七站在门口,身后是妻女和空马厩,他没有走。王进把喝空的酒囊扔给他:“回来再满上。”",
info=[("场次", "8 场:现实 2 场(开场、收尾),回忆 6 场(755)"),
      ("现实线人物", "卢七(65)、张归、甘布、诺桑(画外)"),
      ("回忆线人物", "卢七(33)、王进(33)、阿蘅、柳娘(8 岁)、报信的驿骑、征马的军官、东调的大军"),
      ("钥匙物件", "毛毡酒囊(空的)"),
      ("老马灰", "第 3 场被军官嫌小留下的那匹小灰驹,就是后来驿中最后一匹马“灰”。787 年它已三十多岁,是匹极老的马,这也是它总在马厩暗处站着的原因。"),
      ("方向规则", "本集起,过客改为向东走(画面向左)。第 7 场是全剧第一个向东的全景:只有车辙,没有人。")],
curve="问(你为什么不走)→ 惊(范阳反了)→ 乱(火把、征马)→ 热(老友重逢)→ 远(烽燧上看火河)→ 停(门口的沉默)→ 空(只剩车辙)→ 答(驿里不能没有人)。",
anchors="""
WANG JIN, AGE 33: broad-shouldered Han Chinese soldier, Hexi army squad leader, square sunburnt face, thick black beard, red headscarf under an iron helmet, cloth-covered lamellar armour, a felt wine skin at his belt, a loud laugh

LIU NIANG, AGE 8: small Han Chinese girl, two tufts of hair tied with red string, plain indigo jacket, bare feet in straw sandals, charcoal on her fingers

HEXI ARMY: thousands of Tang soldiers of the Hexi army marching east at night with torches, banners, cavalry and supply carts, cloth-covered lamellar armour

FELT WINE SKIN: a worn brown felt-and-leather wine skin with a wooden stopper and a leather strap, empty and flat

HAN BEACON TOWER: a ruined Han dynasty rammed-earth beacon tower on a rise near the post station, crumbling edges, a flat top reachable by footholds
""",
scenes=[
dict(head="外景 苦泉边 夜(787)", short="苦泉边 夜(787)", era="787",
     env="the stone-lined spring and the old willow outside POST STATION 787 at night, firelight and Tibetan singing from inside the gate, cold stars",
     tone="the question finally asked",
script="""
字幕:第六日。
夜。驿厅里,甘布和诺桑围着火唱吐蕃歌。
张归和卢七坐在苦泉的石沿上。张归手里捧着一碗苦泉水。
张归:你为什么不走?
卢七没有动。
张归:河西陷了二十多年了。唐人能走的都走了。你一个人,守着一个没有人来的驿。
卢七从怀里摸出一只扁扁的毛毡酒囊,拔开塞子,倒过来晃了晃。什么也没有。
卢七:有人说好了,回来再满上。
""",
shots=[
 S("1", "大远景,固定", "夜里的驿站,门里透出火光和吐蕃歌声", "吐蕃歌声;字幕“第六日”", 7,
   "extreme long shot at night, POST STATION 787 dark under cold stars, warm firelight and shadows spilling from the gate, the old willow by the spring", "static camera, the firelight flickers in the gate"),
 S("2", "中景", "张归和卢七坐在苦泉石沿上", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], and LU QI, AGE 65: [锚点], sitting on the stone rim of the spring at night, the young man holding a bowl of water", "static camera, they sit in silence"),
 S("3", "近景", "张归", "张归:“你为什么不走?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking at the old man, starlight", "static camera, he asks"),
 S("4", "近景", "卢七没有动", "—", 3,
   "close shot, LU QI, AGE 65: [锚点], looking at the road, not moving", "static camera, he stays still"),
 S("5", "近景", "张归", "张归:“河西陷了二十多年了。唐人能走的都走了。你一个人,守着一个没有人来的驿。”", 9,
   "close shot, ZHANG GUI, AGE 18: [锚点], speaking with frustration, the bowl tilting in his hands", "static camera, he speaks, then looks down"),
 S("6", "特写", "卢七摸出扁扁的酒囊,拔塞,倒过来晃了晃,空的", "—", 6,
   "close-up, an old man's hands taking a flat FELT WINE SKIN from his robe, pulling the wooden stopper and turning it upside down, nothing comes out", "static camera, he shakes it upside down once", key=True),
 S("7", "近景", "卢七", "卢七:“有人说好了,回来再满上。”", 5,
   "close shot, LU QI, AGE 65: [锚点], holding the empty wine skin on his knee", "static camera, he speaks quietly"),
 S("8", "大特写,缓推", "空酒囊的塞口,火光变成火把(转场)", "风声里渐入急促马蹄", 6,
   "extreme close-up of the open mouth of the empty wine skin, firelight on the worn leather", "slow push in, the firelight swells into torchlight",
   out="the firelight swells into dusk light on the road; the next segment opens in 755."),
]),
dict(head="外景 驿门 黄昏(回忆,755)", short="驿门 黄昏(755)", era="乱后",
     env="the gate of the post station at winter dusk in 755, the willow a young tree about four metres tall and bare, the road from the east",
     tone="the world tilts",
script="""
字幕:天宝十四载,冬。
黄昏。卢七在门口劈柴。阿蘅在泉边洗衣,柳娘蹲在旁边玩。
一匹快马从东边狂奔而来,马上的驿骑嗓子都喊哑了。
驿骑:范阳反了!安禄山反了!
斧子停在半空。阿蘅手里的衣裳掉进水里。
驿骑换了马,一刻不停地往西去了。
""",
shots=[
 S("9", "中景", "黄昏,卢七在门口劈柴,阿蘅在泉边洗衣,柳娘蹲着玩", "劈柴声;字幕“天宝十四载,冬”", 7,
   "medium shot at winter dusk, LU QI, AGE 33: [锚点], splitting wood at the gate, A HENG, AGE 20-37: [锚点], washing clothes at the spring, LIU NIANG, AGE 8: [锚点], squatting beside her playing", "static camera, the axe falls, the water ripples"),
 S("10", "大远景,固定", "一匹快马从东边(画左)狂奔而来", "急促马蹄", 5,
   "extreme long shot at dusk, a single rider galloping hard along the road from frame left toward the station, dust trailing", "static camera, the rider races toward the gate"),
 S("11", "中景", "驿骑勒马,嗓子喊哑了", "驿骑:“范阳反了!安禄山反了!”", 5,
   "medium shot, an exhausted post rider reining in hard at the gate and shouting, his horse foaming", "static camera, he shouts from the saddle"),
 S("12", "近景", "斧子停在半空", "—", 3,
   "close shot, LU QI, AGE 33: [锚点], the axe frozen above his head", "static camera, he freezes"),
 S("13", "特写", "衣裳掉进水里", "水声", 3,
   "close-up, a wet indigo garment slipping from a woman's hands into the spring", "static camera, the cloth sinks slowly"),
 S("14", "大远景,固定", "驿骑换马,一刻不停往西(画右)去了", "马蹄远去", 6,
   "extreme long shot, the rider on a fresh horse galloping away west toward frame right, the family small and still at the gate", "static camera, the rider vanishes west"),
]),
dict(head="外景 驿站 夜(回忆,755)", short="驿站 夜(755)", era="乱后",
     env="the post station at night in 755, flooded with the HEXI ARMY, torches everywhere, the stable being emptied, the road east a river of fire",
     tone="chaos and gravity",
     crowd="the HEXI ARMY marching east with torches, officers, grooms and supply carts",
script="""
夜。火把从西边一直排到天边。河西的大军连夜往东开。
驿站里挤满了兵,马厩前一个军官拿着簿子大喊。
军官:驿马全部征用!一匹不留!
卢七一匹一匹把马牵出来,交给兵。最后一匹是一匹小灰驹,他摸了摸它的头,又把缰绳交出去。
军官看了一眼小灰驹。
军官:太小,留着吧。
阿蘅抱着柳娘站在灶房门口。
""",
shots=[
 S("15", "大远景,固定", "火把的河流从西边排到天边,往东(画左)流", "千军脚步、号角", 9,
   "extreme long shot at night, an endless river of torches of the HEXI ARMY flowing along the road from frame right to frame left past the small post station", "static camera, the river of torches flows left", key=True),
 S("16", "全景", "驿站里挤满了兵,马厩前军官举簿大喊", "军官:“驿马全部征用!一匹不留!”", 6,
   "wide shot of the courtyard packed with soldiers and torches, an officer with a register shouting in front of the stable", "static camera, the crowd churns, the officer shouts"),
 S("17", "中景", "卢七一匹一匹把马牵出来交给兵", "马嘶", 7,
   "medium shot, LU QI, AGE 33: [锚点], leading horses out of the stable one by one and handing the reins to soldiers, torchlight", "static camera, horse after horse is led away"),
 S("18", "近景", "最后一匹小灰驹,他摸了摸它的头,又把缰绳交出去", "—", 6,
   "close shot, LU QI, AGE 33: [锚点], stroking the forehead of a small grey foal, then holding out its rope", "static camera, he strokes it once and offers the rope"),
 S("19", "中景", "军官看了一眼", "军官:“太小,留着吧。”", 4,
   "medium shot, the officer glancing at the small grey foal and waving it off", "static camera, he waves and turns away"),
 S("20", "中景", "阿蘅抱着柳娘站在灶房门口", "—", 5,
   "medium shot, A HENG, AGE 20-37: [锚点], holding LIU NIANG, AGE 8: [锚点], in the kitchen doorway, torchlight crossing their faces", "static camera, they watch, the girl hides her face"),
]),
dict(head="内景 驿厅 夜(回忆,755)", short="驿厅 夜(755)", era="乱后",
     env="the hall at night in 755, crowded with resting soldiers in armour, torches, the poem wall behind",
     tone="loud warmth over a hard question",
     crowd="soldiers resting in armour",
script="""
驿厅里坐满了兵。一个大嗓门的队正挤进来,一把抱住卢七。
王进:七郎!
卢七:王进?
王进拔下腰间的酒囊,塞给卢七。两人对着喝。
王进:跟我走。去长安,打安禄山。立了功,你这辈子就不用守这破驿了。
卢七没有说话,把酒囊递回去。
灶房门口,阿蘅站着,听见了。
""",
shots=[
 S("21", "全景", "驿厅里坐满了兵,一个大嗓门的队正挤进来", "人声嘈杂", 5,
   "wide shot of the hall full of soldiers resting in armour, WANG JIN, AGE 33: [锚点], pushing through the crowd toward the door", "static camera, he shoulders through"),
 S("22", "双人", "王进一把抱住卢七", "王进:“七郎!”卢七:“王进?”", 5,
   "two-shot, WANG JIN, AGE 33: [锚点], throwing his arms around LU QI, AGE 33: [锚点], lifting him off his feet", "static camera, the big man hugs him and laughs"),
 S("23", "双人", "两人对着喝酒囊", "—", 5,
   "two-shot, WANG JIN, AGE 33: [锚点], and LU QI, AGE 33: [锚点], passing a FELT WINE SKIN back and forth, drinking", "static camera, the wine skin passes twice"),
 S("24", "近景", "王进", "王进:“跟我走。去长安,打安禄山。立了功,你这辈子就不用守这破驿了。”", 9,
   "close shot, WANG JIN, AGE 33: [锚点], leaning close with his hand on the other man's shoulder, eyes bright", "static camera, he speaks with conviction", key=True),
 S("25", "近景", "卢七没说话,把酒囊递回去", "—", 4,
   "close shot, LU QI, AGE 33: [锚点], silent, handing the wine skin back", "static camera, he hands it back without a word"),
 S("26", "中景", "灶房门口,阿蘅听见了", "—", 4,
   "medium shot, A HENG, AGE 20-37: [锚点], standing in the dark kitchen doorway, listening, a bowl in her hands", "static camera, she stands still"),
]),
dict(head="外景 汉烽燧顶 夜(回忆,755)", short="烽燧顶 夜(755)", era="乱后",
     env="the flat top of the HAN BEACON TOWER at night in 755, stars above, below the river of torches flowing east past the small post station",
     tone="two boys again, for one night",
script="""
夜。卢七和王进爬上汉代的废烽燧,就像小时候一样。
脚下,火把的河流一直往东淌。
王进:小时候咱俩在这儿看星,你说长大了要去长安看看。
卢七:我说过?
王进:说过。你说要看看灞桥的柳,是不是跟公主那根一样。
卢七笑了一下。
王进:现在去,正好。
卢七低头看驿站。灶房的窗户亮着一盏灯。马厩是黑的,空的。
""",
shots=[
 S("27", "大远景,固定", "烽燧剪影,两个人影爬上顶;脚下火把的河流", "风声、远处号角", 8,
   "extreme long shot at night, the dark silhouette of the HAN BEACON TOWER with two small figures climbing to its top, the river of torches flowing east below", "static camera, the figures reach the top"),
 S("28", "双人", "两人并肩坐在烽燧顶", "王进:“小时候咱俩在这儿看星,你说长大了要去长安看看。”", 8,
   "two-shot, WANG JIN, AGE 33: [锚点], and LU QI, AGE 33: [锚点], sitting side by side on the crumbling top of the beacon tower, torchlight glow from below, stars above", "static camera, they sit, the big man talks"),
 S("29", "近景", "卢七", "卢七:“我说过?”", 3,
   "close shot, LU QI, AGE 33: [锚点], looking down at the torches", "static camera, he asks"),
 S("30", "近景", "王进", "王进:“说过。你说要看看灞桥的柳,是不是跟公主那根一样。”", 7,
   "close shot, WANG JIN, AGE 33: [锚点], grinning, nudging him with an elbow", "static camera, he grins and nudges"),
 S("31", "近景", "卢七笑了一下", "王进:“现在去,正好。”", 5,
   "close shot, LU QI, AGE 33: [锚点], a brief smile fading", "static camera, he smiles, then the smile goes"),
 S("32", "主观,俯拍", "脚下的驿站:灶房窗户亮着一盏灯,马厩黑着,空的", "—", 7,
   "high-angle point-of-view shot down at the small post station at night, one lit window in the kitchen, the stable dark and empty, the young willow by the spring, torches flowing past", "very slow push in toward the lit window", key=True),
]),
dict(head="外景 驿门 黎明(回忆,755)", short="驿门 黎明(755)", era="乱后",
     env="the gate at grey dawn in 755, the last of the army leaving east, the empty stable visible through the gate, the bare willow",
     tone="a decision made without words",
     crowd="the tail of the army marching east",
script="""
黎明。大军的尾巴正在出发。王进骑在马上,停在门前。
王进:走不走?
卢七站在门口。他身后,阿蘅抱着柳娘,小灰驹站在空空的马厩里。
很久。
卢七:驿里不能没有人。
王进看着他,把酒囊里剩下的一口喝干,扔给他。
王进:空了。回来再满上。
卢七接住。
卢七:前头有水。
王进大笑,打马往东去了。
""",
shots=[
 S("33", "中景", "王进骑在马上停在门前", "王进:“走不走?”", 5,
   "medium shot at grey dawn, WANG JIN, AGE 33: [锚点], on horseback at the gate, the tail of the army passing behind him", "static camera, he reins in and asks"),
 S("34", "全景,门框构图", "卢七站在门口;身后阿蘅抱着柳娘,小灰驹站在空马厩里", "风声", 8,
   "wide shot framed by the gate from outside, LU QI, AGE 33: [锚点], standing in the gate, behind him in the courtyard A HENG, AGE 20-37: [锚点], holding LIU NIANG, AGE 8: [锚点], and a small grey foal alone in the empty stable", "static camera, nobody moves", key=True),
 S("35", "近景,极缓推", "卢七,很久", "卢七:“驿里不能没有人。”", 8,
   "close shot, LU QI, AGE 33: [锚点], silent for a long time, then speaking", "extremely slow push in, a long silence, then the line"),
 S("36", "近景", "王进看着他,把酒囊里最后一口喝干", "—", 4,
   "close shot, WANG JIN, AGE 33: [锚点], looking down at him, then tipping back the wine skin to drain the last mouthful", "static camera, he drinks it dry"),
 S("37", "中景", "王进把空酒囊扔给他,卢七接住", "王进:“空了。回来再满上。”", 6,
   "medium shot, WANG JIN, AGE 33: [锚点], tossing the empty FELT WINE SKIN, LU QI, AGE 33: [锚点], catching it against his chest", "static camera, the wine skin flies and is caught"),
 S("38", "近景", "卢七", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 33: [锚点], holding the empty wine skin", "static camera, he says the farewell line"),
 S("39", "大远景,固定", "王进大笑,打马往东(画左)追上大军", "笑声、马蹄", 7,
   "extreme long shot at dawn, a single rider galloping east toward frame left after the dusty tail of the army, the small gate on the right", "static camera, the rider joins the dust and vanishes"),
]),
dict(head="外景 驿道 清晨(回忆,755)", short="驿道 清晨(755)", era="乱后",
     env="the road east of the post station on a still morning in 755, deep cart ruts and hoofprints running to the horizon, nobody",
     tone="emptiness after a flood",
script="""
第二天清晨。驿道上一个人都没有。车辙和蹄印一直往东,伸到天边。
卢七站在路中间。阿蘅牵着柳娘走到他身边。
柳娘:王叔叔什么时候回来?
卢七没有回答,把空酒囊挂在腰上。
""",
shots=[
 S("40", "大远景,固定", "全剧第一个向东的全景:空驿道,深深的车辙伸到天边", "风声,极静", 10,
   "extreme long shot looking east along the empty road at a still morning, deep cart ruts and thousands of hoofprints running straight to the horizon, nobody at all", "static camera, nothing moves but a little dust", key=True),
 S("41", "中景,背面", "卢七站在路中间;阿蘅牵着柳娘走到他身边", "—", 7,
   "medium shot from behind, LU QI, AGE 33: [锚点], standing in the middle of the rutted road facing east, A HENG, AGE 20-37: [锚点], walking up beside him holding LIU NIANG, AGE 8: [锚点], by the hand", "static camera, they come to stand beside him"),
 S("42", "近景", "柳娘仰头问", "柳娘:“王叔叔什么时候回来?”", 4,
   "close shot, LIU NIANG, AGE 8: [锚点], looking up at her father", "static camera, she asks"),
 S("43", "特写", "卢七没回答,把空酒囊挂在腰上", "—", 5,
   "close-up, a man's hands tying the empty FELT WINE SKIN onto his belt", "static camera, he ties the knot",
   out="the ruts and the dust fade and cool to the night of 787."),
]),
dict(head="外景 苦泉边 夜(787)", short="苦泉边 夜(787)", era="787",
     env="the stone-lined spring and the old willow outside POST STATION 787 at night, the Tibetan singing now quiet",
     tone="an answer that is also a confession",
script="""
夜。驿厅里的歌声停了。
张归:他回来了吗?
卢七摇头。
卢七:驿里不能没有人。有人从西边回来,得有一碗水。
张归看着他手里的空酒囊。
张归(旁白):酒囊一只,空的。他说,驿里不能没有人。我那时候还不知道,他在等谁。
""",
shots=[
 S("44", "近景", "张归", "张归:“他回来了吗?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], at the spring at night, the singing from the gate stopped", "static camera, he asks softly"),
 S("45", "近景", "卢七摇头", "卢七:“驿里不能没有人。有人从西边回来,得有一碗水。”", 8,
   "close shot, LU QI, AGE 65: [锚点], shaking his head, then looking west along the dark road", "static camera, he shakes his head and speaks", key=True),
 S("46", "特写", "空酒囊在卢七膝上", "—", 4,
   "close-up, the flat empty wine skin lying on the old man's knee, starlight", "static camera, still"),
 S("47", "大远景,固定", "星空下,泉边一老一少,驿道向西伸进黑暗", "旁白:“酒囊一只,空的。他说,驿里不能没有人。我那时候还不知道,他在等谁。”", 10,
   "extreme long shot at night, two small figures at the spring under the old willow, the road running west into darkness under the stars", "static camera, the stars, the willow stirs", key=True,
   out="hold the final image under the stars; end of episode."),
]),
])
