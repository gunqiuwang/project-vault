EP = dict(
cn="五", title="胡商",
summary="第五集讲一枚剪过边的金币,和两个被迫换了衣裳的人。张归在箱底翻出金币,诺桑要抢,张归用吐蕃话把它报成“官物”挡了回去;站起来的时候,他腰间叠着的唐袍露了出来,卢七第一次看见。回忆线跨越二十年:粟特商人康萨保每年春秋各过一次,教卢七认星、算账;安史之乱后他最后一次来,穿着不合身的汉袍、改了姓,在驿门口被官兵盘查。临走,他把金币留给卢七:“钱比人走得远。”",
info=[("场次", "8 场:现实 2 场(开场、收尾),回忆 6 场(738、746、750、756)"),
      ("现实线人物", "卢七(65)、张归、甘布、诺桑"),
      ("回忆线人物", "卢七(16 / 24 / 28 / 34)、康萨保(32 / 40 / 44 / 50)、阿蘅、柳娘(3 岁)、盘查的唐兵"),
      ("钥匙物件", "东罗马金币(唐人称拂菻),边缘被剪过"),
      ("主题呼应", "被迫换了姓名、衣裳的康萨保,对应今天被迫穿吐蕃袍的张归"),
      ("与设定集的差别", "设定集写康萨保“改姓为安”。但安禄山起兵后,“安”恰恰是最犯忌的姓,史上不少姓安的胡人都改了姓(如安重璋改名李抱玉)。这里改为:康萨保把“康”改成发音相近的“姜”。")],
curve="紧(金子被抢)→ 惊(腰里的唐袍)→ 阔(屋顶看星)→ 暖(灯下算账)→ 热闹(驼队年年来)→ 冷(盘查)→ 自嘲(“鼻子换不了”)→ 静(“人是自己的”)。",
anchors="""
LU QI, AGE 16: thin Han Chinese youth, sun-darkened skin, short topknot tied with a hemp cord, coarse undyed hemp jacket, long limbs, curious eyes

LU QI, AGE 24: lean young Han Chinese man, sun-darkened face, faint beard, black futou cap, plain dark green round-collar robe, leather belt

KANG SABAO, AGE 32-44: Sogdian merchant, curly reddish beard, pointed white felt hat, red turned-down-collar kaftan with brocade trim, leather boots, booming laugh, gold ring on one hand

KANG SABAO, AGE 50: the same Sogdian merchant twenty years on, beard trimmed short and greying, no felt hat, wearing a Han round-collar robe that is too tight across the shoulders and too short at the wrists, a cloth cap, the laugh still there but tired

TANG SOLDIERS: Tang border soldiers in cloth-covered lamellar armour and red headscarves, spears, suspicious and nervous after the rebellion

BYZANTINE COIN: a small gold solidus with an emperor's profile, its edge clipped unevenly all around, worn smooth
""",
scenes=[
dict(head="内景 后房 午(787)", short="后房 午(787)", era="787",
     env="LU QI's small back room in 787 at noon, the poplar-wood chest nearly empty, objects with red cords laid out on the floor",
     tone="a sudden scuffle, then a long look",
script="""
字幕:第五日。
张归(旁白):第五日。箱底。
张归把手伸到箱底,摸出一个用红绳拴着的小布包。打开,是一枚金币,边缘被剪得坑坑洼洼,一面是一个外国皇帝的头像。
诺桑正从门口经过,眼睛一亮,一步跨进来,伸手就抢。
诺桑(吐蕃语,字幕):金子!
甘布也跟了进来。张归攥住金币,站起来,挡在两人面前。
张归(吐蕃语,字幕):这是驿中官物,要登簿,交给节儿。谁拿了,谁自己去跟节儿说。
两个吐蕃兵对视一眼,骂了一句,退了出去。
张归松了口气。站起来时,羊皮袍的前襟敞开了,腰间露出一叠青色的布,是一件叠好的唐式圆领袍。
卢七看见了。
卢七:你腰里是什么?
张归赶紧掩上前襟,没有回答。
卢七没有再问。他从张归手里拿过金币,在指间翻了一下。
卢七:钱比人走得远。
""",
shots=[
 S("1", "特写", "手伸到箱底,摸出一个拴红绳的小布包", "字幕“第五日”;旁白:“第五日。箱底。”", 6,
   "close-up, a young man's hand reaching to the very bottom of the old chest and lifting out a tiny cloth bundle tied with a red cord", "static camera, the hand finds the bundle and lifts it"),
 S("2", "大特写", "布包打开,是一枚边缘剪过的金币", "—", 5,
   "extreme close-up, a cloth opening on a palm to reveal a small BYZANTINE COIN with a clipped edge and an emperor's profile, a glint of light", "static camera, the cloth opens, the gold catches the light", key=True),
 S("3", "中景", "诺桑从门口经过,眼睛一亮,一步跨进来伸手就抢", "诺桑(吐蕃语):“金子!”", 5,
   "medium shot, NORSANG of the TIBETAN SOLDIERS (GAMPO, NORSANG) stopping in the doorway, eyes on the gold, lunging into the room with a hand out", "static camera, he steps in and grabs"),
 S("4", "中景", "张归攥住金币站起来,挡在两人面前;甘布也进来了", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], standing up with the coin in his fist, blocking NORSANG and GAMPO in the small room", "static camera, he rises and stands between them and the chest"),
 S("5", "近景", "张归用吐蕃话", "张归(吐蕃语):“这是驿中官物,要登簿,交给节儿。谁拿了,谁自己去跟节儿说。”", 8,
   "close shot, ZHANG GUI, AGE 18: [锚点], speaking firmly in Tibetan, chin up, fist closed", "static camera, he speaks without blinking"),
 S("6", "中景", "两个吐蕃兵对视,骂一句,退出去", "吐蕃语的咒骂", 4,
   "medium shot, TIBETAN SOLDIERS (GAMPO, NORSANG) exchanging a look, muttering, backing out of the doorway", "static camera, they turn and leave"),
 S("7", "特写", "羊皮袍前襟敞开,腰间露出叠好的青色唐袍", "—", 5,
   "close-up, the front of a sheepskin robe falling open at the waist, revealing a neatly folded blue-green Tang round-collar robe tucked against the young man's body", "static camera, the robe falls open and stays", key=True),
 S("8", "近景", "卢七看见了", "卢七:“你腰里是什么?”", 4,
   "close shot, LU QI, AGE 65: [锚点], sitting on the bed, his eyes on the young man's waist", "static camera, his eyes fix on it, he asks"),
 S("9", "近景", "张归赶紧掩上前襟,不答", "—", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], quickly pulling the sheepskin robe closed, looking away", "static camera, he covers it and turns his face"),
 S("10", "特写", "卢七拿过金币,在指间翻了一下", "卢七:“钱比人走得远。”", 6,
   "close-up, an old man's fingers taking the clipped gold coin and turning it over once", "static camera, the coin turns and catches the light"),
 S("11", "大特写,缓推", "金币上的皇帝头像,金光变暖、变成星光(转场)", "风声转为夜风", 6,
   "extreme close-up of the emperor's profile on the gold coin, its glint spreading into points of light", "slow push in, the gold glints multiply into stars",
   out="the gold glints spread across the frame and become stars in a night sky; the next segment opens on the station roof in 738."),
]),
dict(head="外景 驿厅屋顶 夜(回忆,738)", short="屋顶 夜(738)", era="开元",
     env="the flat earthen roof of the post station hall at night in 738, a sky crowded with stars, the desert dark below",
     tone="wide and wondering",
script="""
字幕:开元二十六年。
夜。驿厅的平顶上,康萨保仰面躺着,十六岁的卢七躺在他旁边。满天的星。
康萨保:那颗不动的,你们叫北辰。我们在碛里走夜路,就跟着它。
卢七:往西走,它在哪边?
康萨保:右手。
卢七:往东呢?
康萨保:左手。回家的时候,它在左手。
卢七:你家在哪边?
康萨保笑了,没有回答,伸手指了指西边。
""",
shots=[
 S("12", "大远景,固定", "满天星,驿站平顶上两个躺着的人影", "夜风;字幕“开元二十六年”", 8,
   "extreme long shot of a night sky crowded with stars over the dark desert, two tiny figures lying on the flat roof of the post station hall", "static camera, the stars wheel very slightly", key=True),
 S("13", "中景,俯拍", "康萨保仰面躺着,卢七躺在旁边", "—", 5,
   "top-down medium shot, KANG SABAO, AGE 32-44: [锚点], lying on his back on the earthen roof, LU QI, AGE 16: [锚点], lying beside him, both looking up, starlight", "static camera, they lie still"),
 S("14", "近景", "康萨保指着北方", "康萨保:“那颗不动的,你们叫北辰。我们在碛里走夜路,就跟着它。”", 8,
   "close shot, KANG SABAO, AGE 32-44: [锚点], lying on his back pointing one finger up at the sky", "static camera, he points and speaks"),
 S("15", "近景", "卢七", "卢七:“往西走,它在哪边?”康萨保:“右手。”", 5,
   "close shot, LU QI, AGE 16: [锚点], following the pointing finger with his eyes", "static camera, he asks"),
 S("16", "近景", "卢七", "卢七:“往东呢?”", 3,
   "close shot, LU QI, AGE 16: [锚点], turning his head toward the merchant", "static camera, he turns and asks"),
 S("17", "近景", "康萨保", "康萨保:“左手。回家的时候,它在左手。”", 5,
   "close shot, KANG SABAO, AGE 32-44: [锚点], smiling up at the stars", "static camera, he answers softly"),
 S("18", "双人,俯拍", "卢七问;康萨保笑了,指了指西边", "卢七:“你家在哪边?”", 6,
   "top-down two-shot of the two lying on the roof, LU QI, AGE 16: [锚点], asking, KANG SABAO, AGE 32-44: [锚点], laughing and lifting his arm to point west", "static camera, he laughs and points west"),
]),
dict(head="内景 驿厅 夜(回忆,746)", short="驿厅 夜(746)", era="天宝",
     env="the hall at night in 746, one table under an oil lamp, counting rods and coins spread out, merchants' bales stacked along the walls",
     tone="warm and teasing",
script="""
字幕:天宝五载。
灯下,桌上摆满了算筹和铜钱。康萨保教二十四岁的卢七算账。
康萨保:三十匹绢,换六十匹马的草料,再加十天的水……
卢七摆着算筹,摆错了一根,康萨保一巴掌拍在他手背上。
刚过门的阿蘅端着两碗汤过来,看着卢七挨打,笑出声。
康萨保:新娘子笑你呢。
阿蘅:他算错了,该打。
卢七算对了。康萨保把算筹一推。
康萨保:账要算清。人情,不用算。
""",
shots=[
 S("19", "全景,固定", "灯下一桌算筹铜钱,墙边堆着货包", "算筹碰响;字幕“天宝五载”", 7,
   "wide shot of the hall at night, one table under an oil lamp covered with counting rods and copper coins, merchant bales stacked along the walls, KANG SABAO, AGE 32-44: [锚点], and LU QI, AGE 24: [锚点], bent over it", "static camera, the lamp flickers"),
 S("20", "近景", "康萨保念账", "康萨保:“三十匹绢,换六十匹马的草料,再加十天的水……”", 7,
   "close shot, KANG SABAO, AGE 32-44: [锚点], reciting numbers with his finger raised", "static camera, he counts on his fingers"),
 S("21", "特写", "卢七摆错一根算筹,一巴掌拍在手背上", "啪", 4,
   "close-up, a young man's hand laying bamboo counting rods on the table, a big ringed hand slapping it lightly", "static camera, the rod goes down, the slap lands"),
 S("22", "中景", "阿蘅端汤过来,笑出声", "康萨保:“新娘子笑你呢。”阿蘅:“他算错了,该打。”", 7,
   "medium shot, A HENG, AGE 20-37: [锚点], young and newly married, carrying two bowls of soup to the table and laughing at the two men", "static camera, she sets down the bowls and laughs"),
 S("23", "特写", "算筹摆对了", "—", 4,
   "close-up, the counting rods now laid in a neat correct pattern on the table", "static camera, the last rod is placed"),
 S("24", "近景", "康萨保把算筹一推", "康萨保:“账要算清。人情,不用算。”", 6,
   "close shot, KANG SABAO, AGE 32-44: [锚点], sweeping the rods aside with one hand and lifting his soup bowl", "static camera, he sweeps the rods and drinks", key=True),
]),
dict(head="外景 驿门 春(回忆,750)", short="驿门 春(750)", era="天宝",
     env="the gate in spring 750, the willow now a young tree with new leaves and a few red cords, a long camel caravan stopped on the road",
     tone="abundant; the good years",
     crowd="a long Sogdian camel caravan with drivers, bells and bales",
script="""
字幕:天宝九载。
春天。驼铃响成一片。康萨保的驼队排了半条驿道。
三岁的柳娘坐在骆驼背上,被康萨保托着,咯咯直笑。
康萨保把一把葡萄干塞进她的小手里。
康萨保:比你爹小时候还能吃。
卢七站在柳树下数骆驼,数着数着笑了。
""",
shots=[
 S("25", "大远景,固定", "春天,驼队排了半条驿道,柳树发了新叶", "驼铃一片;字幕“天宝九载”", 8,
   "extreme long shot in spring, a long Sogdian camel caravan lined up along half the road, the young willow by the spring in fresh green leaf with a few red cords", "static camera, camels shift and bells swing", key=True),
 S("26", "中景", "柳娘坐在骆驼背上,被康萨保托着,咯咯直笑", "笑声", 6,
   "medium shot, LIU NIANG, AGE 4: [锚点], perched on a camel's back, held steady by KANG SABAO, AGE 32-44: [锚点], laughing", "static camera, the child laughs and the camel sways"),
 S("27", "近景", "康萨保把葡萄干塞进她手里", "康萨保:“比你爹小时候还能吃。”", 5,
   "close shot, KANG SABAO, AGE 32-44: [锚点], pouring raisins into a small child's hands", "static camera, he pours and grins"),
 S("28", "中景", "卢七站在柳树下数骆驼,数着数着笑了", "—", 6,
   "medium shot, LU QI, AGE 24: [锚点], standing under the young willow counting camels with his finger, starting to laugh", "static camera, he counts, then laughs"),
]),
dict(head="外景 驿门 冬(回忆,756)", short="驿门 冬(756)", era="乱后",
     env="the gate in winter 756 under a grey sky, the bare willow, a few Tang soldiers posted at the gate, a thin caravan of three camels",
     tone="cold suspicion",
     crowd="four Tang soldiers guarding the gate",
script="""
字幕:至德元载。
冬天。门口多了几个兵,挨个盘查过路的人。
一支只有三峰骆驼的小驼队慢慢走来。牵骆驼的人穿着一件不合身的汉式圆领袍,肩膀绷着,袖子短一截,胡子剪短了,没戴尖帽。
唐兵:站住!胡人?哪来的?叫什么?
康萨保:姓姜。姜萨保。
唐兵:姜?你这鼻子姓姜?
几个兵大笑,扯开他的货包,翻得满地都是。
卢七从门里出来。
卢七:他是我驿里二十年的老客。
唐兵看了卢七一眼,啐了一口,放了行。
康萨保蹲下去,一件一件把东西捡起来。卢七蹲下来帮他。
""",
shots=[
 S("29", "大远景,固定", "灰天下的冬日驿门,几个兵把守,一支三峰骆驼的小驼队走来", "寒风;字幕“至德元载”", 8,
   "extreme long shot under a grey winter sky, the bare willow and the gate guarded by TANG SOLDIERS, a thin caravan of only three camels approaching slowly", "static camera, the small caravan moves in from the right"),
 S("30", "中景", "牵骆驼的人穿着不合身的汉袍,胡子剪短了", "—", 6,
   "medium shot, KANG SABAO, AGE 50: [锚点], leading a camel, the Han robe straining at his shoulders, sleeves too short, cloth cap pulled low", "static camera, he walks toward the gate with his head down", key=True),
 S("31", "双人", "唐兵拦住他", "唐兵:“站住!胡人?哪来的?叫什么?”", 5,
   "two-shot, a TANG SOLDIERS spear lowered across the path of KANG SABAO, AGE 50: [锚点], at the gate", "static camera, the spear blocks him"),
 S("32", "近景", "康萨保", "康萨保:“姓姜。姜萨保。”", 4,
   "close shot, KANG SABAO, AGE 50: [锚点], answering carefully with a stiff smile", "static camera, he answers"),
 S("33", "中景", "几个兵大笑,扯开货包翻得满地", "唐兵:“姜?你这鼻子姓姜?”笑声", 7,
   "medium shot, TANG SOLDIERS laughing and tearing open the merchant's bales, cloth and small pouches spilling onto the frozen ground", "static camera, they laugh and dump the bags"),
 S("34", "中景", "卢七从门里出来", "卢七:“他是我驿里二十年的老客。”", 5,
   "medium shot, LU QI, AGE 33: [锚点], stepping out of the gate toward the soldiers", "static camera, he walks into frame and speaks"),
 S("35", "近景", "唐兵看了卢七一眼,啐一口,放行", "—", 4,
   "close shot, a TANG SOLDIERS sergeant looking at the station master, spitting aside, lifting his spear", "static camera, he spits and lifts the spear"),
 S("36", "中景,俯拍", "康萨保蹲下捡东西,卢七蹲下来帮他", "风声", 7,
   "high-angle medium shot, KANG SABAO, AGE 50: [锚点], kneeling to gather his scattered goods from the frozen ground, LU QI, AGE 33: [锚点], kneeling beside him to help", "static camera, the two men pick things up in silence"),
]),
dict(head="内景 驿厅 夜(回忆,756)", short="驿厅 夜(756)", era="乱后",
     env="the nearly empty hall at night in 756, a small fire, one oil lamp, the poem wall dim",
     tone="self-mocking and tender; a goodbye that pretends not to be one",
script="""
夜。驿厅里空了一大半。火塘边只有他们两个。
康萨保扯了扯绷紧的袖口,自己先笑了。
康萨保:康国的康,改成姜太公的姜。名字换了,鼻子换不了。
卢七:你往哪去?
康萨保:往西。回撒马尔罕。二十年,来了三十九回。这是最后一回。
他从怀里掏出一枚金币,放在卢七手里。
康萨保:拂菻的。我爷爷带过来的,边上剪了一圈,一路剪一路当盘缠。
卢七:我不要。
康萨保:不是给你的。替我在这儿待着。我回不来,它替我回来。
他把卢七的手合上。
康萨保:钱比人走得远。
""",
shots=[
 S("37", "全景,固定", "空了一大半的驿厅,火塘边只有两个人", "炭火噼啪", 7,
   "wide shot of the nearly empty hall at night, a small fire, KANG SABAO, AGE 50: [锚点], and LU QI, AGE 33: [锚点], sitting alone by it", "static camera, the small fire flickers"),
 S("38", "近景", "康萨保扯了扯绷紧的袖口,自己先笑了", "康萨保:“康国的康,改成姜太公的姜。名字换了,鼻子换不了。”", 9,
   "close shot, KANG SABAO, AGE 50: [锚点], tugging at the tight sleeve of his Han robe and laughing at himself, firelight", "static camera, he tugs the sleeve and laughs"),
 S("39", "近景", "卢七", "卢七:“你往哪去?”", 3,
   "close shot, LU QI, AGE 33: [锚点], looking at him across the fire", "static camera, he asks"),
 S("40", "近景", "康萨保", "康萨保:“往西。回撒马尔罕。二十年,来了三十九回。这是最后一回。”", 8,
   "close shot, KANG SABAO, AGE 50: [锚点], looking into the fire, the laugh gone", "extremely slow push in, he speaks quietly"),
 S("41", "特写", "金币放在卢七手里", "康萨保:“拂菻的。我爷爷带过来的,边上剪了一圈,一路剪一路当盘缠。”", 8,
   "close-up, a ringed hand placing the clipped BYZANTINE COIN in a rough open palm, firelight", "static camera, the coin is set down", key=True),
 S("42", "双人", "卢七推回去", "卢七:“我不要。”", 3,
   "two-shot, LU QI, AGE 33: [锚点], pushing the hand back, KANG SABAO, AGE 50: [锚点], shaking his head", "static camera, he pushes it back"),
 S("43", "近景", "康萨保", "康萨保:“不是给你的。替我在这儿待着。我回不来,它替我回来。”", 8,
   "close shot, KANG SABAO, AGE 50: [锚点], holding the other man's eyes", "static camera, he speaks slowly"),
 S("44", "特写", "他把卢七的手合上", "康萨保:“钱比人走得远。”", 5,
   "close-up, a big ringed hand closing a rough hand around the gold coin", "static camera, the fingers close"),
]),
dict(head="外景 驿门 清晨(回忆,756)", short="驿门 清晨(756)", era="乱后",
     env="the gate at a cold dawn in 756, the bare willow, the road west under thin snow",
     tone="light words, heavy weather",
script="""
清晨。薄雪。三峰骆驼往西走。
康萨保没有回头,只举了举手。
卢七:前头有水。
康萨保:前头的水,我比你熟。
他大笑,笑声被风吹散了。
""",
shots=[
 S("45", "中景,背面", "三峰骆驼往西(画右)走,康萨保没回头,举了举手", "驼铃三声", 6,
   "medium shot from behind, KANG SABAO, AGE 50: [锚点], leading three camels west toward frame right through thin snow, raising one hand without turning", "static camera, he walks away and lifts his hand"),
 S("46", "近景", "卢七在门口", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 33: [锚点], standing in the snowy gate", "static camera, he says the farewell line"),
 S("47", "中景,背面", "康萨保大笑", "康萨保:“前头的水,我比你熟。”", 5,
   "medium shot from behind, KANG SABAO, AGE 50: [锚点], laughing loudly as he walks, his breath steaming", "static camera, he laughs and keeps walking"),
 S("48", "大远景,固定", "雪里三峰骆驼向西远去,驼铃声被风吹散", "风声", 9,
   "extreme long shot at a cold dawn, three camels and one man growing small on the snowy road to the west, frame right, the bare willow and the gate on the left", "static camera, they fade into the snow haze", key=True,
   out="the snow haze cools to the blue-grey dusk of 787."),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the old willow with red cords, the road west",
     tone="a sentence that changes a young man",
script="""
黄昏。卢七和张归坐在门槛上。张归手里捏着那枚金币。
张归:他回到撒马尔罕了吗?
卢七:不知道。
沉默。
卢七看着驿道,没有看张归。
卢七:衣裳是穿给别人看的,人是自己的。
张归低下头,手按在腰间那叠唐袍上。
张归(旁白):金币一枚,拂菻国的,边上剪过。簿上写:官物,待交节儿。那天夜里,我把腰里的袍子拿出来,看了很久。
""",
shots=[
 S("49", "中景", "两人坐在门槛上,张归捏着金币", "风声", 6,
   "medium shot at dusk, LU QI, AGE 65: [锚点], and ZHANG GUI, AGE 18: [锚点], sitting side by side on the gate threshold, the young man turning the gold coin in his fingers", "static camera, the coin turns slowly"),
 S("50", "双人", "张归问", "张归:“他回到撒马尔罕了吗?”卢七:“不知道。”", 5,
   "two-shot, ZHANG GUI, AGE 18: [锚点], asking without looking up, LU QI, AGE 65: [锚点], looking at the road", "static camera, he asks, the old man answers"),
 S("51", "近景,极缓推", "卢七看着驿道", "卢七:“衣裳是穿给别人看的,人是自己的。”", 7,
   "close shot, LU QI, AGE 65: [锚点], looking down the empty road at dusk, not at the young man", "extremely slow push in, he speaks without turning", key=True),
 S("52", "特写", "张归的手按在腰间那叠唐袍上", "—", 5,
   "close-up, a young man's hand pressing flat over the folded robe hidden at his waist under the sheepskin", "static camera, the hand presses and stays"),
 S("53", "大远景,固定", "门槛上一老一少,驿道空空", "旁白:“簿上写:官物,待交节儿。那天夜里,我把腰里的袍子拿出来,看了很久。”羌笛", 10,
   "extreme long shot at dusk, two small figures on the threshold of the gate, the old willow with red cords, the empty road stretching west", "static camera, the light fades slowly", key=True,
   out="hold the final image as the dusk deepens; end of episode."),
]),
])
