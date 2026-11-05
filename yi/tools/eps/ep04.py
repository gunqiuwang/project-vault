EP = dict(
cn="四", title="家书",
summary="第四集讲木箱里的一封信和一双鞋。张归登记木箱,翻出一双从没穿过的布鞋和一封发黄的信,信上的字歪歪扭扭,每个字都像描出来的。回忆线回到天宝十载:十五岁的赵小满顶替瘸腿的哥哥从军西去,在驿里叫卢七“哥”,求他代写家书。卢七不会写字,两个人举着灯在题诗壁上一个字一个字地找。半年后怛罗斯败报传来,往东的驿骑来了,卢七却没把信交出去。",
info=[("场次", "7 场:现实 2 场(开场、收尾),回忆 5 场(751)"),
      ("现实线人物", "卢七(65)、张归"),
      ("回忆线人物", "卢七(29)、赵小满(15)、阿蘅、柳娘(4 岁)、募兵队正、一名负伤的驿骑、一名东去的驿骑"),
      ("钥匙物件", "未寄出的家书、一双没穿过的布鞋(鞋帮缝着“满”字)"),
      ("与设定集的差别", "大纲写“寄信的驿骑一直没有等到”。这里改为:驿骑来了,卢七没交出去——败报之后,他不知道该不该让一个母亲读到可能已经死去的儿子的信。这个犹豫是本集的落点,也给第 9 集留了位置。")],
text_block="""**赵小满的家书(751,卢七照墙上的字一个一个描):**

阿娘:儿到瓜州了。这里风大,沙子比咱家麦子还多。驿里有个哥哥待儿好,给儿炖了羊。鞋儿合脚,儿没舍得穿。等儿立了功,就回家给阿娘扯一匹绢。不许哭。

注:设定集原文作“扣一匹绢”,疑为“扯一匹绢”(买布论“扯”),剧本按“扯”写,请确认。""",
curve="好奇(箱底的信)→ 酸(“那是我写的”)→ 热(苦水、羊肉、叫“哥”)→ 笑(满墙找字)→ 亮(少年追队伍)→ 冷(败报)→ 悬(信没交出去)→ 无解(“我也不知道哪样好”)。",
anchors="""
LU QI, AGE 29: lean Han Chinese man, weathered tanned face, short neat beard, black futou cap, dark green round-collar robe of a post-station master, leather belt, calm attentive eyes, calloused hands

ZHAO XIAOMAN, AGE 15: skinny Guanzhong peasant boy in an oversized cloth-covered armour that slips off one shoulder, a bamboo hat hanging on his back, sunburnt cheeks, big ears, nervous gap-toothed grin

LIU NIANG, AGE 4: small Han Chinese girl, two tufts of hair tied with red string, plain indigo jacket, round cheeks

RECRUIT OFFICER: Tang army squad leader in worn lamellar armour and red headscarf, hoarse voice, a whip at his belt

WOUNDED COURIER: Tang post rider with a bloodied bandage around his head, torn red jacket, collapsing from an exhausted horse

CLOTH SHOES: a pair of black cloth shoes with thick white thousand-layer soles, never worn, the character for "full" stitched in red on one heel
""",
scenes=[
dict(head="内景 后房 晨(787)", short="后房 晨(787)", era="787",
     env="LU QI's small back room in 787, the old poplar-wood chest open, objects tied with faded red cords, morning light from a high window",
     tone="careful and quiet",
script="""
字幕:第四日。
张归(旁白):第四日。木箱一只,胡杨木。箱里的东西,每件都拴着一根红绳。
张归跪在木箱前,一件一件拿出来登记。卢七坐在床沿上。
张归拿起一双黑面布鞋。鞋底是千层底,白得发黄,一点泥都没有。鞋帮上用红线缝着一个字。
张归:满。
他又拿起一封折得方方正正的信,纸已经发黄。
张归:能看吗?
卢七点点头。
张归展开信。上面的字歪歪扭扭,大小不一,每一笔都很用力,像是照着什么描下来的。
张归:“阿娘:儿到瓜州了。”……这字……
卢七:那是我写的。
张归:你写的?
卢七:照着墙上描的。
""",
shots=[
 S("1", "全景,固定", "后房,张归跪在打开的木箱前,卢七坐在床沿", "字幕“第四日”;旁白:“第四日。木箱一只,胡杨木。”", 8,
   "wide shot of the small back room in morning light, ZHANG GUI, AGE 18: [锚点], kneeling before the open poplar-wood chest with the register book, LU QI, AGE 65: [锚点], sitting on the edge of the narrow bed", "static camera, locked-off, dust drifts in the window light", key=True),
 S("2", "特写", "张归登记,毛笔在簿子上写(文字后期合成)", "旁白:“箱里的东西,每件都拴着一根红绳。”", 5,
   "close-up, a brush writing a line on the register book, faded red cords on objects in the chest beside it", "static camera, the brush writes one line"),
 S("3", "特写", "一双没穿过的黑面布鞋,鞋帮缝着红线“满”字", "张归:“满。”", 6,
   "close-up, CLOTH SHOES lifted out of the chest in a young man's hands, the clean thousand-layer soles, the red stitched character on the heel", "static camera, the hands turn the shoes to show the heel", key=True),
 S("4", "特写", "折得方方正正的发黄的信,拴着红绳", "张归:“能看吗?”", 4,
   "close-up, a small square-folded yellowed letter tied with a faded red cord in a young man's hands", "static camera, he holds it up"),
 S("5", "近景", "卢七点头", "—", 3,
   "close shot, LU QI, AGE 65: [锚点], sitting on the bed, nodding once", "static camera, he nods"),
 S("6", "特写,俯拍", "信纸展开,字歪歪扭扭,一笔一笔很用力", "纸声;张归:“‘阿娘:儿到瓜州了。’……这字……”", 8,
   "top-down close-up, an old letter unfolding on a knee, clumsy uneven large characters pressed hard into the paper, each stroke careful as if traced", "static camera, the letter unfolds and lies flat"),
 S("7", "近景", "卢七", "卢七:“那是我写的。”", 3,
   "close shot, LU QI, AGE 65: [锚点], looking at the letter in the young man's hands", "static camera, he speaks quietly"),
 S("8", "双人", "张归抬头;卢七", "张归:“你写的?”卢七:“照着墙上描的。”", 6,
   "two-shot, ZHANG GUI, AGE 18: [锚点], looking up from the letter at LU QI, AGE 65: [锚点], morning light between them", "static camera, he looks up and the old man answers"),
 S("9", "大特写,缓推", "信上一个笨拙的“娘”字,墨色晕开变暖(转场)", "马蹄、号角渐入", 6,
   "extreme close-up of one clumsy ink character on yellowed paper, the ink starting to bleed and warm", "slow push in, the ink spreads and turns warm",
   out="the ink bleeds into warm dusty sunlight; the next segment opens on the road in 751."),
]),
dict(head="外景 驿门 正午(回忆,751)", short="驿门 正午(751)", era="天宝",
     env="the gate and spring of the post station at noon in 751, the willow a young tree about three metres tall, a dusty road crowded with marching recruits",
     tone="hot, crowded, young",
     crowd="a column of forty young recruits in oversized armour with banners, marching west",
script="""
字幕:天宝十载。
正午,一队新募的兵从东边过来,往西走。旗子垂着,一个个都是半大孩子,甲穿在身上晃荡。
队伍在驿前停下饮马。一个瘦小的少年一头栽在苦泉边上。
卢七把他扶起来,舀了一瓢水喂他。
少年喝了一大口,脸皱成一团。
赵小满:哥,这水咋是苦的?
卢七:苦泉。往西就没有水了。
少年又喝了一大口。
队正(画外):赵大满!归队!
少年慌忙爬起来,又回头看了卢七一眼。
""",
shots=[
 S("10", "大远景,固定", "正午,一队新兵从东边(画左)走来,往西(画右)", "脚步、号角;字幕“天宝十载”", 8,
   "extreme long shot at harsh noon, a column of young recruits with drooping banners marching along the road from frame left toward the post station and the young willow", "static camera, the column moves slowly from left to right", key=True),
 S("11", "中景", "半大孩子们,甲在身上晃荡", "—", 5,
   "medium shot, a row of teenage recruits in oversized armour stopping at the spring, sweaty, dusty, some drinking from their hands", "static camera, the boys crowd to the water"),
 S("12", "中景", "一个瘦小的少年栽倒在苦泉边", "扑通一声", 4,
   "medium shot, ZHAO XIAOMAN, AGE 15: [锚点], stumbling and collapsing against the stone rim of the spring, the bamboo hat rolling away", "static camera, the boy falls and lies still"),
 S("13", "中景", "卢七扶起他,舀一瓢水喂他", "水声", 6,
   "medium shot, LU QI, AGE 29: [锚点], kneeling and lifting the boy's head, holding a gourd ladle of water to his lips", "static camera, he lifts the boy and gives him water"),
 S("14", "近景", "少年喝一大口,脸皱成一团", "赵小满:“哥,这水咋是苦的?”", 5,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], gulping water and screwing up his face at the taste", "static camera, he drinks, grimaces, asks"),
 S("15", "近景", "卢七", "卢七:“苦泉。往西就没有水了。”", 5,
   "close shot, LU QI, AGE 29: [锚点], holding the ladle, the young willow behind him", "static camera, he answers plainly"),
 S("16", "近景", "少年又喝一大口", "队正(画外):“赵大满!归队!”", 4,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], drinking again greedily, then flinching at a shout", "static camera, he gulps and startles"),
 S("17", "中景", "少年慌忙爬起来,跑两步又回头看卢七", "—", 5,
   "medium shot, ZHAO XIAOMAN, AGE 15: [锚点], scrambling up and running toward the column, turning back once to look at LU QI, AGE 29: [锚点]", "static camera, he runs, stops, looks back, runs on"),
]),
dict(head="内景 驿厅 夜(回忆,751)", short="驿厅 夜(751)", era="天宝",
     env="the hall at night in 751, crowded with sleeping recruits on mats, a fire pit with a mutton stew pot, oil lamps, the poem wall covered about halfway",
     tone="warm and funny; a boy far from home",
     crowd="recruits eating and sleeping on mats",
script="""
夜。新兵挤满了驿厅。阿蘅在火塘上炖了一锅羊肉,四岁的柳娘蹲在锅边看。
赵小满捧着碗吃得满头大汗。
赵小满:哥,我叫赵小满。名册上那个赵大满,是我哥。
卢七:你哥呢?
赵小满:腿瘸了,去不了。名字是他的,人是我。
他嘿嘿笑,又压低声音。
赵小满:哥,你会写字不?我想给我娘捎个信。
卢七:我不会写。
赵小满的笑僵了一下。他抬头看着满墙的字。
赵小满:那这墙上……这么多字……
卢七顺着他的目光看过去。
""",
shots=[
 S("18", "全景,固定", "挤满新兵的驿厅,火塘上炖着羊肉", "人声、锅响", 7,
   "wide shot of the hall at night packed with young recruits on mats, a big stew pot over the fire pit, A HENG, AGE 20-37: [锚点], stirring it, LIU NIANG, AGE 4: [锚点], squatting beside the pot", "static camera, steam rises, the crowd shifts"),
 S("19", "近景", "赵小满捧碗吃得满头大汗", "赵小满:“哥,我叫赵小满。名册上那个赵大满,是我哥。”", 7,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], eating mutton stew from a big bowl, sweating, talking with his mouth full, firelight", "static camera, he eats and talks"),
 S("20", "近景", "卢七", "卢七:“你哥呢?”", 3,
   "close shot, LU QI, AGE 29: [锚点], sitting beside him on the floor", "static camera, he asks"),
 S("21", "近景", "赵小满", "赵小满:“腿瘸了,去不了。名字是他的,人是我。”", 6,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], grinning with a gap in his teeth, then the grin fading", "static camera, he answers and grins"),
 S("22", "近景", "他压低声音", "赵小满:“哥,你会写字不?我想给我娘捎个信。”", 6,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], leaning in and lowering his voice, bowl in his lap", "static camera, he leans close"),
 S("23", "近景", "卢七", "卢七:“我不会写。”", 3,
   "close shot, LU QI, AGE 29: [锚点], looking down", "static camera, he answers"),
 S("24", "近景,仰拍", "少年的笑僵住,抬头看满墙的字", "赵小满:“那这墙上……这么多字……”", 6,
   "low-angle close shot, ZHAO XIAOMAN, AGE 15: [锚点], looking up at the poem wall covered with calligraphy, firelight on it", "static camera, he looks up slowly"),
 S("25", "主观,缓摇", "满墙的字在火光里", "—", 6,
   "point-of-view shot of the poem wall half covered with many different handwritings in warm firelight", "slow pan across the wall"),
]),
dict(head="内景 驿厅 深夜(回忆,751)", short="驿厅 深夜(751)", era="天宝",
     env="the hall late at night in 751, recruits asleep, two oil lamps moving along the poem wall, a sheet of paper on a board",
     tone="tender comedy; two people hunting for words",
script="""
深夜。新兵们都睡了。卢七举着灯,赵小满举着另一盏,两个人贴着墙找字。
赵小满:“阿娘”。
卢七:“娘”……这儿有一个。
他把纸贴在墙边,照着描。
赵小满:“儿到瓜州了。”
卢七找到“瓜”,又找到“州”,一个一个描下来。
赵小满:“驿里有个哥哥待儿好,给儿炖了羊。”
卢七:“羊”……没有。
两个人举着灯满墙找。赵小满急得抓头。卢七在墙角最高处停住。
卢七:有。“牧羊”的羊。
赵小满笑出了声,赶紧捂住嘴。
赵小满:“等儿立了功,就回家给阿娘扯一匹绢。”
赵小满停了一下。
赵小满:最后写“不许哭”。
卢七找了很久。在一首很淡的诗里,找到了“哭”字。他描下来,手停在纸上。
""",
shots=[
 S("26", "全景,固定", "睡满新兵的驿厅,两盏灯贴着墙移动", "鼾声", 7,
   "wide shot of the dark hall full of sleeping recruits, two small oil lamps moving along the poem wall held by LU QI, AGE 29: [锚点], and ZHAO XIAOMAN, AGE 15: [锚点]", "static camera, the two lamps drift slowly along the wall", key=True),
 S("27", "双人", "赵小满念,卢七找", "赵小满:“阿娘。”卢七:“娘……这儿有一个。”", 6,
   "two-shot at the wall, ZHAO XIAOMAN, AGE 15: [锚点], whispering, LU QI, AGE 29: [锚点], holding a lamp close to the calligraphy and searching", "static camera, the man's lamp stops on one spot"),
 S("28", "特写", "纸贴在墙边,照着描", "笔声", 6,
   "close-up, a sheet of paper pressed against the plaster beside a written character, a rough hand copying it stroke by stroke with a brush, lamp light", "static camera, the brush copies the character", key=True),
 S("29", "近景", "赵小满念下一句", "赵小满:“儿到瓜州了。”", 4,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], whispering the words, lamp light under his chin", "static camera, he whispers"),
 S("30", "特写,横移", "灯光在墙上移动,停在一个字上,又移到另一个字", "—", 6,
   "close-up, a lamp flame moving across dense calligraphy, stopping on one character, then moving on to another", "slow lateral move following the lamp"),
 S("31", "近景", "赵小满", "赵小满:“驿里有个哥哥待儿好,给儿炖了羊。”", 6,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], dictating with a shy smile", "static camera, he speaks the line"),
 S("32", "近景", "卢七", "卢七:“羊……没有。”", 3,
   "close shot, LU QI, AGE 29: [锚点], searching the wall, frowning", "static camera, he searches and shakes his head"),
 S("33", "全景", "两盏灯满墙找,赵小满急得抓头", "—", 6,
   "wide shot, two lamps sweeping up and down the whole wall, the boy scratching his head, the man climbing onto a bench to reach the top", "static camera, the lamps search everywhere"),
 S("34", "近景,仰拍", "卢七站在长凳上,停在墙最高处", "卢七:“有。‘牧羊’的羊。”", 5,
   "low-angle close shot, LU QI, AGE 29: [锚点], standing on a bench, lamp raised to the highest corner of the wall", "static camera, he finds it and points"),
 S("35", "近景", "赵小满笑出声,赶紧捂住嘴", "笑声闷住", 4,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], bursting into laughter and clapping both hands over his mouth, sleepers around", "static camera, he laughs and covers his mouth"),
 S("36", "近景", "赵小满", "赵小满:“等儿立了功,就回家给阿娘扯一匹绢。”", 6,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], dictating proudly, chin up", "static camera, he says it proudly"),
 S("37", "近景", "他停了一下", "赵小满:“最后写‘不许哭’。”", 5,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], the pride fading, looking at the floor", "static camera, he pauses and says it quietly"),
 S("38", "特写,缓推", "一首很淡的诗里,灯光找到“哭”字", "—", 6,
   "close-up, the lamp flame stopping beside one character inside a very faded poem low on the wall", "slow push in on the faded character"),
 S("39", "特写", "卢七描完“哭”字,手停在纸上", "羌笛", 6,
   "close-up, a rough hand finishing a character on the letter paper with a brush, then resting still on the paper", "static camera, the brush lifts, the hand stays", key=True),
]),
dict(head="外景 驿门 清晨(回忆,751)", short="驿门 清晨(751)", era="天宝",
     env="the gate at dawn in 751, the young willow by the spring, the recruit column forming up on the road to the west",
     tone="cheerful on the surface",
     crowd="the recruit column marching off west",
script="""
清晨。队伍集合,往西开拔。
赵小满跑回来,从包袱里掏出一双黑面布鞋,塞给卢七。
赵小满:哥,鞋你替我收着。我娘纳的,打仗穿可惜了。回来我穿着回家。
他又把那封信塞过去。
赵小满:有往东的驿骑,你替我寄。
卢七:前头有水。
赵小满一愣,笑了,转身追队伍。跑出去老远,他回头大喊。
赵小满:哥——!
""",
shots=[
 S("40", "全景", "清晨,队伍集合往西开拔", "号角", 6,
   "wide shot at dawn, the recruit column forming up on the road and starting to march west toward frame right, the gate and young willow on the left", "static camera, the column begins to move"),
 S("41", "中景", "赵小满跑回来,掏出布鞋塞给卢七", "赵小满:“哥,鞋你替我收着。我娘纳的,打仗穿可惜了。回来我穿着回家。”", 9,
   "medium shot, ZHAO XIAOMAN, AGE 15: [锚点], running back and pushing a pair of CLOTH SHOES into the hands of LU QI, AGE 29: [锚点], at the gate", "static camera, the boy presses the shoes into his hands and talks fast"),
 S("42", "特写", "信塞进卢七手里", "赵小满:“有往东的驿骑,你替我寄。”", 5,
   "close-up, a boy's hand putting a square-folded letter on top of the shoes in a man's hands", "static camera, the letter is placed on the shoes"),
 S("43", "近景", "卢七", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 29: [锚点], holding the shoes and the letter", "static camera, he says the farewell line"),
 S("44", "近景", "赵小满一愣,笑了", "—", 4,
   "close shot, ZHAO XIAOMAN, AGE 15: [锚点], blinking, then breaking into his gap-toothed grin", "static camera, he grins and turns to run"),
 S("45", "大远景,固定", "少年追着队伍往西(画右)跑,跑出老远回头大喊", "赵小满:“哥——!”", 9,
   "extreme long shot at dawn, a small boy running along the road after the departing column toward frame right, stopping far away to turn and wave, the gate on the left", "static camera, the boy runs, stops, waves both arms, runs on", key=True),
]),
dict(head="外景 驿门 秋(回忆,751)", short="驿门 秋(751)", era="天宝",
     env="the gate in autumn 751 under a low grey sky, yellow willow leaves blowing, the road west",
     tone="the floor drops out",
script="""
秋。西风。
一匹马从西边狂奔而来,马上的驿骑头上缠着血布,冲到苦泉边,连人带马栽倒。
卢七冲过去扶他。
驿骑:败了……怛罗斯……全没了……
卢七的手按在胸口。衣襟里鼓着一块,是那封信。
第二天。一个往东去的驿骑在门前换马。
驿骑(东去):有往东的信没有?
卢七把手伸进怀里,摸到那封信。他站了很久。
卢七:……没有。
驿骑上马走了。卢七站在门口,手还在怀里。
""",
shots=[
 S("46", "大远景,固定", "灰天,黄叶,一骑从西边(画右)狂奔而来", "急促马蹄、西风", 6,
   "extreme long shot under a low grey autumn sky, yellow willow leaves blowing, a single rider galloping hard along the road from frame right toward the station", "static camera, the rider races toward the gate"),
 S("47", "中景", "驿骑冲到泉边,连人带马栽倒", "马嘶、倒地声", 5,
   "medium shot, WOUNDED COURIER and his horse collapsing beside the spring, dust flying", "static camera, horse and rider go down"),
 S("48", "双人", "卢七扶起他", "驿骑:“败了……怛罗斯……全没了……”", 7,
   "two-shot, LU QI, AGE 29: [锚点], holding up the head of the WOUNDED COURIER, who gasps out words", "static camera, the courier speaks with his last strength"),
 S("49", "特写", "卢七的手按在胸口,衣襟里鼓着一块", "风声", 5,
   "close-up, a man's hand pressing against the front of his robe where a small square shape shows underneath", "static camera, the hand presses and stays", key=True),
 S("50", "中景", "第二天,东去的驿骑在门前换马", "驿骑:“有往东的信没有?”", 6,
   "medium shot on a grey morning, an eastbound post rider changing horses at the gate, LU QI, AGE 29: [锚点], holding the reins", "static camera, the rider tightens the girth and asks"),
 S("51", "近景,极缓推", "卢七把手伸进怀里,摸到信,站了很久", "—", 8,
   "close shot, LU QI, AGE 29: [锚点], his hand inside his robe, frozen, eyes looking east down the road", "extremely slow push in, he does not move"),
 S("52", "近景", "卢七", "卢七:“……没有。”", 3,
   "close shot, LU QI, AGE 29: [锚点], taking his empty hand out of his robe", "static camera, he answers and lowers his hand"),
 S("53", "大远景,固定", "驿骑向东(画左)远去,卢七站在门口,手还在怀里", "马蹄远去,风声", 8,
   "extreme long shot, the post rider galloping away east toward frame left, LU QI, AGE 29: [锚点], small at the gate with one hand inside his robe, yellow leaves blowing", "static camera, the rider vanishes, the man stays", key=True,
   out="the scene drains to grey and cools to the blue-grey of 787."),
]),
dict(head="内景 后房 晨(787)", short="后房 晨(787)", era="787",
     env="LU QI's small back room in 787, the chest open, the letter and shoes on the floor",
     tone="an honest question with no answer",
script="""
张归读完最后一行。
张归:“……不许哭。”
屋里很静。
张归:他回来了吗?
卢七摇头。
卢七:我一直没寄。寄了,他娘就以为他还活着。
张归:不寄,她就以为他死了。
卢七:……我也不知道哪样好。
张归把信照原来的折痕折好,把红绳系回去,和布鞋放在一起。
张归(旁白):家书一封,未寄。布鞋一双,未穿。
""",
shots=[
 S("54", "特写", "信的最后两个字", "张归:“……不许哭。”", 5,
   "close-up, the last clumsy characters at the end of the old letter, a young man's thumb at the edge of the paper", "static camera, the thumb holds still"),
 S("55", "全景,固定", "很静的后房", "风声", 5,
   "wide shot of the small back room, ZHANG GUI, AGE 18: [锚点], kneeling with the letter, LU QI, AGE 65: [锚点], on the bed, neither moving", "static camera, silence"),
 S("56", "近景", "张归", "张归:“他回来了吗?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking up from the letter", "static camera, he asks"),
 S("57", "近景", "卢七摇头", "卢七:“我一直没寄。寄了,他娘就以为他还活着。”", 7,
   "close shot, LU QI, AGE 65: [锚点], shaking his head slowly, then speaking", "static camera, he shakes his head and speaks"),
 S("58", "近景", "张归", "张归:“不寄,她就以为他死了。”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], answering quietly, not accusing", "static camera, he speaks gently"),
 S("59", "近景,极缓推", "卢七", "卢七:“……我也不知道哪样好。”", 7,
   "close shot, LU QI, AGE 65: [锚点], looking at his own hands", "extremely slow push in, he speaks and looks down", key=True),
 S("60", "特写", "张归照原折痕折好信,系回红绳,放在布鞋上", "旁白:“家书一封,未寄。布鞋一双,未穿。”", 9,
   "close-up, young hands folding the old letter along its original creases, tying the faded red cord back, and laying it on top of the black cloth shoes", "static camera, the hands fold, tie and place",
   out="hold on the letter resting on the shoes; light fades; end of episode."),
]),
])
