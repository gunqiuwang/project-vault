EP = dict(
cn="七", title="阿蘅",
summary="第七集是全剧的情感最低点。张归在卢七的枕头底下翻出一只绣了一半的荷包,针还别在上面;卢七第一次主动讲起自己。回忆线从天宝五载阿蘅嫁进驿站讲起:她在灶房里唱曲,柳娘出生,九岁时在墙脚用炭画了那匹小灰驹。广德元年吐蕃逼近,卢七让妻女去凉州投亲。临别前夜,阿蘅问他:“你自己想去哪里?”他答不上来。第二年,凉州陷落。",
info=[("场次", "8 场:现实 2 场(开场、收尾),回忆 6 场(746、749、756、763、764)"),
      ("现实线人物", "卢七(65)、张归"),
      ("回忆线人物", "卢七(24 / 27 / 34 / 41 / 42)、阿蘅(20–37)、柳娘(婴儿 / 9 岁 / 16 岁)、小灰驹、东来的逃难人"),
      ("钥匙物件", "半只荷包(青线绣柳,针还别着)、墙脚的炭画马"),
      ("揭晓", "墙脚那匹炭画马是柳娘九岁时画的,画的是大军征马后唯一留下的小灰驹——也就是今天的老马“灰”。第 1 集张归在墙脚看到的就是它。"),
      ("阿蘅的曲子", "本集唱完整;第 10 集卢七只哼前半句")],
text_block="""**阿蘅的曲子(原创瓜州小调,无伴奏):**

柳条青,柳条长,折一枝柳送情郎。
情郎走到天边上,柳条插在水中央。
水是苦,柳是长,等到柳条过了墙。""",
curve="窘(枕下的荷包)→ 开口(“我女人绣的”)→ 亮(红衣新娘)→ 暖(灶房的曲子)→ 甜(墙脚画马)→ 问(你自己想去哪里)→ 断(车往东走)→ 塌(凉州陷了)→ 底(手指描马)。",
anchors="""
LU QI, AGE 41: lean Han Chinese man going grey, deep lines around the eyes, short greying beard, black futou cap, faded dark green round-collar robe, a felt wine skin at his belt, tired steady eyes

A HENG, AGE 20: young Han Chinese peasant bride from Guazhou, round warm face, wide laughing mouth, hair in a simple bun with a red wooden pin, a plain red wedding jacket over an indigo skirt

A HENG, AGE 37: the same woman at thirty-seven, round face thinner, a few grey hairs at the temple, wooden pin, plain indigo jacket, needle and green thread in her hands, eyes that ask directly

LIU NIANG, AGE 9: small Han Chinese girl, two tufts of hair tied with red string, indigo jacket, charcoal-black fingers, kneeling with total concentration

LIU NIANG, AGE 16: slender Han Chinese girl of sixteen, hair in a single braid tied with red string, indigo jacket, her mother's round face, stubborn eyes

GREY FOAL: a small grey foal about one year old, thin legs, pale muzzle, gentle dark eyes

HALF POUCH: a small cloth pouch of pale indigo, a willow branch embroidered in green thread on it only half finished, a needle with green thread still stuck through the cloth
""",
scenes=[
dict(head="内景 后房 夜(787)", short="后房 夜(787)", era="787",
     env="LU QI's small back room at night in 787, one oil lamp, the narrow bed with a thin pillow, the chest closed",
     tone="intrusion, then the first confession",
script="""
字幕:第七日。
张归(旁白):第七日。床一张。枕一个。
夜。张归拿着簿子进后房,登记最后几样东西。卢七不在屋里。
张归掀起枕头。枕头底下压着一只小小的荷包,青线绣着一枝柳,只绣了一半,一根针还别在布上,针上还穿着线。
卢七进门,看见他手里的东西,站住了。
张归:这个……也登吗?
卢七走过去,从他手里拿过荷包,在床沿坐下。
很久。
卢七:我女人绣的。绣了一半。
卢七:针还别在上面。她说,回来接着绣。
""",
shots=[
 S("1", "全景,固定", "油灯下的后房,张归拿着簿子进来", "字幕“第七日”;旁白:“第七日。床一张。枕一个。”", 7,
   "wide shot of the small back room at night lit by one oil lamp, ZHANG GUI, AGE 18: [锚点], entering with the register book, the narrow bed and thin pillow", "static camera, he walks to the bed"),
 S("2", "特写", "掀起枕头,底下压着一只荷包", "—", 5,
   "close-up, a young hand lifting a thin pillow to reveal a small HALF POUCH lying on the bed board", "static camera, the pillow lifts slowly"),
 S("3", "大特写", "青线绣柳只绣了一半,一根针还别在布上", "—", 6,
   "extreme close-up of the HALF POUCH, a willow branch in green thread stopping halfway, a needle with green thread still pushed through the cloth, lamp light", "very slow push in on the needle", key=True),
 S("4", "中景", "卢七进门看见,站住了", "—", 4,
   "medium shot, LU QI, AGE 65: [锚点], stopping in the doorway, his eyes on the pouch in the young man's hand", "static camera, he stops"),
 S("5", "近景", "张归", "张归:“这个……也登吗?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], holding the pouch out awkwardly", "static camera, he asks, embarrassed"),
 S("6", "中景", "卢七拿过荷包,在床沿坐下", "—", 6,
   "medium shot, LU QI, AGE 65: [锚点], taking the pouch from the young man's hand and sitting down slowly on the edge of the bed", "static camera, he takes it and sits"),
 S("7", "近景,极缓推", "卢七低头看荷包,很久", "卢七:“我女人绣的。绣了一半。”", 8,
   "close shot, LU QI, AGE 65: [锚点], looking down at the pouch in both hands, lamp light", "extremely slow push in, a long pause, then he speaks", key=True),
 S("8", "特写", "老人的拇指碰了碰那根针", "卢七:“针还别在上面。她说,回来接着绣。”", 7,
   "close-up, an old man's thumb touching the needle stuck in the half-finished embroidery", "static camera, the thumb touches the needle and stays"),
 S("9", "大特写,缓推", "青线绣的柳枝,颜色变鲜、变暖(转场)", "唢呐、笑声渐入", 6,
   "extreme close-up of the green-thread willow embroidery, the thread colors brightening and warming", "slow push in, the green brightens into spring light",
   out="the green thread brightens into spring sunlight; the next segment opens on a wedding in 746."),
]),
dict(head="外景 驿门 春(回忆,746)", short="驿门 春(746)", era="天宝",
     env="the gate of the post station in spring 746, the willow a slim young tree two metres tall with one red cord, travellers gathered",
     tone="bright and noisy",
     crowd="a handful of travellers and post soldiers cheering, one playing a suona horn",
script="""
字幕:天宝五载。
春天。一辆驴车从东边慢慢过来,车上坐着一个穿红衣的姑娘。
驿卒和过路的客人站在门口起哄,有人吹起了唢呐。
二十四岁的卢七站在门口,手不知道往哪里放。
驴车还没停稳,姑娘自己跳了下来,差点摔一跤,自己先笑出了声。
阿蘅:你就是卢驿长?
卢七:……是。
阿蘅:比我爹说的黑。
满门口的人哄笑。
""",
shots=[
 S("10", "大远景,固定", "春天,一辆驴车从东边(画左)慢慢过来,车上一点红", "唢呐;字幕“天宝五载”", 8,
   "extreme long shot in spring, a donkey cart coming slowly along the road from frame left, a girl in red on it, the post station and a slim young willow ahead", "static camera, the cart approaches"),
 S("11", "中景", "门口起哄的人群,有人吹唢呐", "唢呐、起哄", 5,
   "medium shot, post soldiers and travellers crowding the gate, one blowing a suona horn, laughing", "static camera, the crowd jostles and cheers"),
 S("12", "近景", "卢七站在门口,手不知道往哪放", "—", 4,
   "close shot, LU QI, AGE 24: [锚点], standing stiffly in the gate, hands moving to his belt and away again", "static camera, he fidgets"),
 S("13", "中景", "驴车没停稳,姑娘自己跳下来,差点摔一跤,自己先笑", "笑声", 6,
   "medium shot, A HENG, AGE 20: [锚点], jumping down from the donkey cart before it stops, stumbling, catching herself and laughing", "static camera, she jumps, stumbles, laughs", key=True),
 S("14", "双人", "阿蘅走到卢七面前", "阿蘅:“你就是卢驿长?”卢七:“……是。”", 5,
   "two-shot, A HENG, AGE 20: [锚点], walking straight up to LU QI, AGE 24: [锚点], and looking him in the face", "static camera, she looks him over"),
 S("15", "近景", "阿蘅", "阿蘅:“比我爹说的黑。”", 3,
   "close shot, A HENG, AGE 20: [锚点], grinning", "static camera, she says it and grins"),
 S("16", "全景", "满门口的人哄笑,卢七也笑了", "哄笑", 5,
   "wide shot, the whole crowd at the gate roaring with laughter, LU QI, AGE 24: [锚点], laughing despite himself", "static camera, everyone laughs"),
]),
dict(head="内景 灶房 日(回忆,749)", short="灶房 日(749)", era="天宝",
     env="the station kitchen in 749, a big earthen stove, clay jars, a hu-bread oven, flour on the board, a baby basket by the door, warm light through steam",
     tone="ordinary happiness",
script="""
灶房。热气腾腾。阿蘅一边揉面一边唱。门边的竹篮里,刚满两岁的柳娘睡着。
阿蘅(唱):柳条青,柳条长,折一枝柳送情郎。
卢七靠在门框上听。
阿蘅(唱):情郎走到天边上,柳条插在水中央。
她回头看见他。
阿蘅:听什么?去干活。
卢七没走。
阿蘅(唱):水是苦,柳是长,等到柳条过了墙。
""",
shots=[
 S("17", "全景,固定", "热气腾腾的灶房,阿蘅揉面,门边竹篮里睡着孩子", "灶火声", 7,
   "wide shot of the warm station kitchen full of steam, A HENG, AGE 20-37: [锚点], kneading dough at a floury board, a baby asleep in a basket by the door", "static camera, steam drifts"),
 S("18", "近景", "阿蘅一边揉面一边唱", "阿蘅(唱):“柳条青,柳条长,折一枝柳送情郎。”", 8,
   "close shot, A HENG, AGE 20-37: [锚点], kneading dough and singing, flour on her cheek", "static camera, she sings as she works", key=True),
 S("19", "中景", "卢七靠在门框上听", "—", 5,
   "medium shot, LU QI, AGE 27: [锚点], leaning in the kitchen doorway, listening, the baby basket at his feet", "static camera, he leans and listens"),
 S("20", "近景", "阿蘅接着唱", "阿蘅(唱):“情郎走到天边上,柳条插在水中央。”", 8,
   "close shot, A HENG, AGE 20-37: [锚点], slapping dough into a round flat bread, still singing", "static camera, she sings and shapes the bread"),
 S("21", "双人", "她回头看见他", "阿蘅:“听什么?去干活。”", 4,
   "two-shot, A HENG, AGE 20-37: [锚点], turning to see LU QI, AGE 27: [锚点], in the doorway, waving a floury hand at him", "static camera, she turns and shoos him"),
 S("22", "特写", "篮子里的婴儿;卢七没走", "阿蘅(唱):“水是苦,柳是长,等到柳条过了墙。”", 8,
   "close-up, a sleeping baby in a basket by the door, a man's hand resting on the rim of the basket", "static camera, the baby sleeps, the hand stays"),
]),
dict(head="内景 驿厅 日(回忆,756)", short="驿厅 日(756)", era="乱后",
     env="the half-empty hall in 756, the poem wall about two thirds covered, a bare patch at the foot of the wall, the door open to the courtyard",
     tone="a small secret victory",
script="""
字幕:至德元载。
驿厅里空空的。九岁的柳娘跪在西墙脚,攥着一块炭,一笔一笔地画。门口,小灰驹探进头来看她。
墙脚多了一匹马,腿画歪了,脖子画长了。
卢七进门,看见了,脸一沉。
卢七:墙是给客人题诗的——
阿蘅在他身后。
阿蘅:让她画。
阿蘅:墙上都是走了的人写的。也该有个留下的。
卢七看着那匹马,又看看门口的小灰驹,没说话。柳娘冲他咧嘴一笑,脸上一道炭黑。
""",
shots=[
 S("23", "全景,固定", "空空的驿厅,柳娘跪在西墙脚画画,小灰驹从门口探头", "炭笔沙沙;字幕“至德元载”", 7,
   "wide shot of the nearly empty hall in daylight, LIU NIANG, AGE 9: [锚点], kneeling at the foot of the poem wall drawing with charcoal, a GREY FOAL poking its head through the open door", "static camera, the girl draws, the foal watches"),
 S("24", "特写", "攥着炭的小手一笔一笔画", "—", 6,
   "close-up, a small charcoal-black hand drawing a horse on the bare white plaster at the foot of the wall, crooked legs, a long neck", "static camera, the hand draws the legs one by one", key=True),
 S("25", "近景", "小灰驹在门口看她", "小马喷鼻", 4,
   "close shot, the GREY FOAL standing in the doorway, ears forward, looking at the girl", "static camera, the foal snorts and blinks"),
 S("26", "中景", "卢七进门,看见了,脸一沉", "卢七:“墙是给客人题诗的——”", 5,
   "medium shot, LU QI, AGE 34: [锚点], stepping into the hall, seeing the drawing, his face darkening", "static camera, he stops and frowns"),
 S("27", "近景", "阿蘅在他身后", "阿蘅:“让她画。”", 3,
   "close shot, A HENG, AGE 20-37: [锚点], behind his shoulder, calm", "static camera, she speaks"),
 S("28", "近景", "阿蘅", "阿蘅:“墙上都是走了的人写的。也该有个留下的。”", 6,
   "close shot, A HENG, AGE 20-37: [锚点], looking past him at the girl and the drawing", "static camera, she says it gently", key=True),
 S("29", "特写", "墙脚的炭画马,旁边门口站着真的小灰驹", "—", 5,
   "close-up, the childish charcoal horse at the foot of the wall, the real GREY FOAL standing in the doorway behind in soft focus", "static camera, still"),
 S("30", "近景", "柳娘冲他咧嘴一笑,脸上一道炭黑", "—", 4,
   "close shot, LIU NIANG, AGE 9: [锚点], grinning up at her father, a streak of charcoal across her cheek", "static camera, she grins"),
]),
dict(head="内景 后房 夜(回忆,763)", short="后房 夜(763)", era="乱后",
     env="the back room at night in 763, one oil lamp, a packed cloth bundle by the door, the narrow bed",
     tone="the question of the whole series",
script="""
字幕:广德元年。
夜。门边放着收拾好的包袱。阿蘅坐在油灯下绣荷包,青线,一枝柳。
卢七:吐蕃人过了陇山。凉州有你舅家,城大,墙高。明天有一队往东的车,你带柳娘跟着走。
阿蘅没有抬头。
阿蘅:那你呢?
卢七:驿里不能没有人。
阿蘅停了针。
阿蘅:你自己想去哪里?
卢七张了张嘴,没有声音。
很久。
阿蘅:我就问问。
她把针别在布上,把荷包塞进他手里。
阿蘅:绣了一半。你先拿着,我回来接着绣。
""",
shots=[
 S("31", "全景,固定", "油灯下,门边放着包袱,阿蘅坐在灯下绣荷包", "字幕“广德元年”", 7,
   "wide shot of the back room at night, a packed cloth bundle by the door, A HENG, AGE 37: [锚点], sewing a small pouch under the oil lamp, LU QI, AGE 41: [锚点], standing", "static camera, the lamp flame trembles"),
 S("32", "近景", "卢七", "卢七:“吐蕃人过了陇山。凉州有你舅家,城大,墙高。明天有一队往东的车,你带柳娘跟着走。”", 10,
   "close shot, LU QI, AGE 41: [锚点], speaking in a low steady voice, not looking at her", "static camera, he speaks the plan"),
 S("33", "特写", "针穿过布,青线拉长", "阿蘅:“那你呢?”", 4,
   "close-up, a needle with green thread passing through pale indigo cloth, a woman's fingers", "static camera, the needle goes through and pulls"),
 S("34", "近景", "卢七", "卢七:“驿里不能没有人。”", 3,
   "close shot, LU QI, AGE 41: [锚点], looking at the floor", "static camera, he answers"),
 S("35", "特写", "针停了", "—", 3,
   "close-up, the needle stopping halfway through the cloth", "static camera, the needle stops"),
 S("36", "近景,极缓推", "阿蘅抬起头", "阿蘅:“你自己想去哪里?”", 7,
   "close shot, A HENG, AGE 37: [锚点], lifting her eyes to him, lamp light, asking plainly", "extremely slow push in, she looks up and asks", key=True),
 S("37", "近景", "卢七张了张嘴,没有声音", "—", 7,
   "close shot, LU QI, AGE 41: [锚点], opening his mouth to answer and finding nothing, the lamp flame in his eyes", "static camera, a long silence"),
 S("38", "近景", "阿蘅", "阿蘅:“我就问问。”", 4,
   "close shot, A HENG, AGE 37: [锚点], a small tired smile, looking back down at the cloth", "static camera, she smiles and looks down"),
 S("39", "特写", "她把针别在布上,把荷包塞进他手里", "阿蘅:“绣了一半。你先拿着,我回来接着绣。”", 8,
   "close-up, a woman's hands pushing the needle into the HALF POUCH to keep it there and pressing the pouch into a man's rough hand", "static camera, she pins the needle and closes his hand around it"),
]),
dict(head="外景 驿门 清晨(回忆,763)", short="驿门 清晨(763)", era="乱后",
     env="the gate at grey dawn in 763, the willow now a tall young tree with nineteen red cords, a line of refugee carts going east",
     tone="a goodbye in someone else's song",
     crowd="a short line of refugee carts and walkers heading east",
script="""
清晨。一队往东去的车停在门口。阿蘅和柳娘上了车。
十六岁的柳娘回头看着驿门。
柳娘:爹,别擦我的马。
卢七:……不擦。
卢七:前头有水。
车动了。阿蘅没有回头,唱起来。
阿蘅(唱):柳条青,柳条长……
歌声越来越远。
""",
shots=[
 S("40", "全景", "一队往东的车停在门口,阿蘅和柳娘上车", "车轴声", 6,
   "wide shot at grey dawn, a short line of refugee carts on the road heading east, A HENG, AGE 37: [锚点], and LIU NIANG, AGE 16: [锚点], climbing onto one, LU QI, AGE 41: [锚点], at the gate", "static camera, they climb up"),
 S("41", "近景", "柳娘回头看驿门", "柳娘:“爹,别擦我的马。”", 4,
   "close shot, LIU NIANG, AGE 16: [锚点], turning back on the cart to look at her father", "static camera, she turns and says it"),
 S("42", "近景", "卢七", "卢七:“……不擦。”卢七:“前头有水。”", 5,
   "close shot, LU QI, AGE 41: [锚点], at the gate, the willow with red cords behind him", "static camera, he answers, then says the farewell line"),
 S("43", "中景,背面", "车动了,阿蘅没有回头,唱起来", "阿蘅(唱):“柳条青,柳条长……”", 6,
   "medium shot from behind, the cart starting to roll east toward frame left, A HENG, AGE 37: [锚点], sitting straight without turning, singing", "static camera, the cart rolls away"),
 S("44", "大远景,固定", "车队往东(画左)远去,卢七一个人站在门口,歌声越来越远", "歌声渐远,风声", 10,
   "extreme long shot at dawn, the line of carts growing small along the road east toward frame left, a single man at the gate beside the tall willow", "static camera, the carts fade into the haze", key=True),
]),
dict(head="外景 驿门 冬(回忆,764)", short="驿门 冬(764)", era="乱后",
     env="the gate in heavy snow in 764, the willow bare and white, the road east buried",
     tone="the fall",
script="""
字幕:广德二年,冬。
大雪。一个裹着破毯的人从东边踉踉跄跄走来,倒在门口。
卢七把他扶进门洞。那人嘴唇冻得发紫。
逃难人:凉州……陷了……
卢七的手松开了。
雪落在他肩上,他站着没有动。
""",
shots=[
 S("45", "大远景,固定", "大雪,一个裹着破毯的人从东边(画左)踉跄走来", "风雪;字幕“广德二年,冬”", 7,
   "extreme long shot in heavy snow, a lone figure wrapped in a torn blanket stumbling along the buried road from frame left toward the snowy gate", "static camera, the figure staggers closer"),
 S("46", "中景", "那人倒在门口,卢七扶他进门洞", "—", 5,
   "medium shot, a frozen refugee collapsing at the gate, LU QI, AGE 42: [锚点], catching him and dragging him into the shelter of the gateway", "static camera, he catches him"),
 S("47", "近景", "那人嘴唇冻得发紫", "逃难人:“凉州……陷了……”", 5,
   "close shot, the refugee's frost-bitten face with purple lips, whispering", "static camera, he whispers"),
 S("48", "特写", "卢七的手松开了", "—", 4,
   "close-up, a man's hands slowly letting go of the refugee's blanket", "static camera, the fingers open"),
 S("49", "中景,极缓推", "雪落在他肩上,他站着没动", "风雪", 8,
   "medium shot, LU QI, AGE 42: [锚点], standing still in the open gate, snow settling on his shoulders and cap, the empty white road behind", "extremely slow push in, he does not move", key=True,
   out="the falling snow slows and the white turns to the cold blue of 787 night."),
]),
dict(head="内景 驿厅 夜(787)", short="驿厅 夜(787)", era="787",
     env="the hall of POST STATION 787 at night, POEM WALL 787, the charcoal horse at the foot of the wall, one oil lamp on the floor",
     tone="the lowest point; no words",
script="""
夜。卢七坐在西墙脚,油灯放在地上。
他伸出一根手指,顺着那匹炭画马的线条慢慢描:腿,脖子,歪歪的耳朵。描得很轻,炭一点也没有掉。
张归站在门口,没有进去。
张归(旁白):荷包一只,绣了一半,针还在上面。墙脚炭画马一匹。不擦。
""",
shots=[
 S("50", "全景,固定", "夜,卢七坐在西墙脚,油灯在地上", "风声", 8,
   "wide shot of the dark hall, LU QI, AGE 65: [锚点], sitting on the floor at the foot of POEM WALL 787, one oil lamp on the floor beside him", "static camera, still", key=True),
 S("51", "大特写", "一根手指顺着炭画马的线条慢慢描,很轻", "—", 9,
   "extreme close-up, an old man's fingertip tracing the lines of the childish charcoal horse on the plaster without touching hard, leg, neck, crooked ear, lamp light", "static camera, the finger traces slowly", key=True),
 S("52", "中景", "张归站在门口,没有进去", "—", 5,
   "medium shot, ZHANG GUI, AGE 18: [锚点], standing in the dark doorway of the hall, not coming in", "static camera, he stands and watches"),
 S("53", "近景", "卢七的侧脸,灯光从下面照上来", "旁白:“荷包一只,绣了一半,针还在上面。”", 6,
   "close shot, LU QI, AGE 65: [锚点], profile lit from below by the floor lamp, eyes on the drawing", "static camera, he keeps tracing"),
 S("54", "大远景,固定", "空旷的驿厅,一盏灯,墙脚一个人", "旁白:“墙脚炭画马一匹。不擦。”羌笛一个长音", 9,
   "extreme long shot from the far end of the dark hall, one tiny oil lamp at the foot of the vast poem wall, an old man sitting beside it", "static camera, the lamp flickers", key=True,
   out="hold, then the lamp gutters out to black; end of episode."),
]),
])
