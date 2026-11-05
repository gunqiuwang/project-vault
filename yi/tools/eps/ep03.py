EP = dict(
cn="三", title="西行",
summary="第三集讲墙上并排的两首诗。现实线里,张归开始照旧例登录壁上题咏,念到一半卡住,背后擦墙的卢七接着背了下去——张归这才知道老人识字。回忆线里,天宝八载,意气风发的诗人韦幼安西赴安西幕府,酒后题诗,手把手教卢七认了第一个字“西”;六年后他瘦成一把骨头东归,在自己的诗旁和了一首,卢七端来一盆苦泉水,让他照见了自己的白发。",
info=[("场次", "8 场:现实 2 场(开场、收尾),回忆 6 场(749、755)"),
      ("现实线人物", "卢七(65)、张归"),
      ("回忆线人物", "卢七(27 / 33)、韦幼安(25 / 31)、阿蘅、柳娘(8 岁,755)、同路的西行客"),
      ("钥匙物件", "墙上并排的两首诗(一浓一淡)、一盆水"),
      ("暗线", "韦幼安在幕府“抄了六年文书”,和今天替吐蕃人抄写的张归互为镜像")],
text_block="""**墙上的两首诗(原创拟作):**

韦幼安·西行题苦泉驿(749):万里西风吹马蹄,天山雪色入旌旗。男儿不作封侯梦,何事辞家过碛西。

韦幼安·东归再题(755):六年沙碛损征衣,再过苦泉认旧题。壁上少年豪气在,镜中人已鬓如丝。""",
curve="好奇(老人怎么会背诗)→ 热(满堂喝彩)→ 亲(教一个“西”字)→ 空(西去的背影)→ 冷(东归的瘦马)→ 痛(水里的白发)→ 静(两首诗挨在一起)。",
anchors="""
LU QI, AGE 27: lean Han Chinese man, weathered tanned face, short neat beard, black futou cap, dark green round-collar robe of a post-station master, leather belt, quiet attentive eyes

WEI YOUAN, AGE 25: tall lean young Tang scholar-poet, bright confident face, thin moustache, black futou cap with long ties, pale blue round-collar robe, a plain sword at his hip, ink on his fingers, laughs with his whole body

WEI YOUAN, AGE 31: the same man six years later, gaunt and sunburnt, grey streaks at the temples, cracked lips, the pale blue robe faded to grey and patched, no sword, leading a lame horse, eyes that no longer laugh

LIU NIANG, AGE 8: small Han Chinese girl, two tufts of hair tied with red string, plain indigo jacket, bare feet in straw sandals, charcoal on her fingers

A HENG, AGE 23-29: Han Chinese peasant woman from Guazhou, round warm face, quick smile, hair in a simple bun with a wooden pin, plain indigo jacket and skirt, sleeves rolled up, flour on her hands
""",
scenes=[
dict(head="内景 驿厅 晨(787)", short="驿厅 晨(787)", era="787",
     env="the low earthen hall of POST STATION 787 in morning light, POEM WALL 787 on the west side, a small low table with ink stone, brush and paper",
     tone="quiet surprise; the young man finally looks at the old man",
script="""
字幕:第三日。
张归(旁白):第三日。按旧例,拆驿之前,壁上题咏要登录在簿。我从西墙左起第二列开始。
张归在墙前摆了一张矮几,研墨,铺纸。卢七在墙的另一头擦着。
张归抬头,对着墙念。
张归:万里西风吹马蹄,天山雪色入旌旗。男儿……
下一个字褪得厉害,他凑近去看,看不清。
卢七没有停手,也没有回头。
卢七:男儿不作封侯梦,何事辞家过碛西。
张归愣住,转过身。
张归:你识字?
卢七:认得墙上的。
张归又看向旁边那首,墨色淡得多。
张归:六年沙碛损征衣……
卢七:再过苦泉认旧题。壁上少年豪气在,镜中人已鬓如丝。
张归:谁教你的?
卢七走过来,用手指点了点第一首诗里的一个字。
卢七:这个字,是他教的。
那是一个“西”字。
""",
shots=[
 S("1", "全景,固定", "晨光里的驿厅,张归在西墙前摆矮几,卢七在墙另一头擦墙", "字幕“第三日”;旁白:“第三日。按旧例,拆驿之前,壁上题咏要登录在簿。”", 9,
   "wide shot of the low earthen hall in cool morning light, ZHANG GUI, AGE 18: [锚点], setting a low table with ink stone and paper before POEM WALL 787, LU QI, AGE 65: [锚点], wiping the far end of the wall", "static camera, locked-off, dust floats in the window light", key=True),
 S("2", "特写", "研墨", "研墨声;旁白:“我从西墙左起第二列开始。”", 5,
   "close-up, a young man's ink-stained fingers grinding an ink stick on a stone, water darkening", "static camera, the ink stick circles slowly"),
 S("3", "近景,仰拍", "张归抬头念墙上的诗", "张归:“万里西风吹马蹄,天山雪色入旌旗。男儿……”", 8,
   "low-angle close shot, ZHANG GUI, AGE 18: [锚点], looking up at the wall and reading aloud, brush in hand", "static camera, he reads, then frowns and leans closer"),
 S("4", "大特写,缓推", "褪色的墨迹,一个字几乎看不清", "—", 4,
   "extreme close-up of faded calligraphy on cracked white plaster, one character almost gone", "slow push in on the faded character"),
 S("5", "近景", "卢七背对他擦墙,不回头", "卢七:“男儿不作封侯梦,何事辞家过碛西。”", 7,
   "close shot, LU QI, AGE 65: [锚点], wiping the wall with a soft cloth, his back half turned, speaking without looking", "static camera, the old man keeps wiping as he recites"),
 S("6", "近景", "张归愣住,转身", "张归:“你识字?”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], turning around in surprise, the brush stopped mid-air", "static camera, he turns and stares"),
 S("7", "近景", "卢七", "卢七:“认得墙上的。”", 3,
   "close shot, LU QI, AGE 65: [锚点], pausing the cloth, eyes on the wall", "static camera, he answers flatly"),
 S("8", "特写,缓横移", "两首诗并排,左浓右淡", "张归:“六年沙碛损征衣……”", 6,
   "close-up, two poems written side by side on the plaster, the left one in dark strong ink, the right one pale and thin", "slow lateral move from the dark poem to the pale one", key=True),
 S("9", "近景", "卢七接着背", "卢七:“再过苦泉认旧题。壁上少年豪气在,镜中人已鬓如丝。”", 8,
   "close shot, LU QI, AGE 65: [锚点], reciting softly with his eyes closed, the cloth resting on the wall", "extremely slow push in, he recites, then opens his eyes"),
 S("10", "近景", "张归", "张归:“谁教你的?”", 3,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking at the old man as if for the first time", "static camera, he asks quietly"),
 S("11", "特写", "卢七的手指点在一个字上", "卢七:“这个字,是他教的。”", 6,
   "close-up, an old man's finger touching one dark ink character on the wall", "static camera, the finger touches the character and stays"),
 S("12", "大特写,缓推", "“西”字的墨色晕开、变暖(转场)", "人声、酒令声渐入", 6,
   "extreme close-up of one dark ink character on white plaster, the ink edges starting to bleed and warm", "slow push in, the ink spreads and turns warm gold",
   out="the ink of the character bleeds and warms until the frame fills with warm lamplight; the next segment opens in the crowded hall of 749."),
]),
dict(head="内景 驿厅 夜(回忆,749)", short="驿厅 夜(749)", era="天宝",
     env="the hall of the post station in 749 at night, crowded and warm, POEM WALL partly covered with fresh calligraphy, oil lamps, a fire pit, wine jars",
     tone="loud, young, invincible",
     crowd="a dozen westbound travellers, officers and merchants drinking and cheering",
script="""
字幕:天宝八载。
驿厅里挤满了西去的人。炉火、油灯、酒气。
一个穿浅蓝圆领袍的年轻人跳上长凳,举着酒碗。
韦幼安:诸位!此去安西,不立功,不回来!
满屋子的人一起喊好。
阿蘅抱着酒坛给大家添酒,笑着躲开一只伸过来的手。
二十七岁的卢七站在门边,看着这一屋子人。
韦幼安跳下凳子,夺过一支笔,蘸满了墨,走到西墙前,一挥而就。
满屋喝彩。
""",
shots=[
 S("13", "全景,固定", "满屋西去的客人,炉火、油灯、酒气", "人声鼎沸;字幕“天宝八载”", 8,
   "wide shot of the crowded hall at night, westbound travellers drinking around a fire pit, oil lamps, wine jars, the poem wall partly covered with fresh calligraphy", "static camera, the crowd moves and laughs, firelight flickers", key=True),
 S("14", "中景,仰拍", "韦幼安跳上长凳举碗", "韦幼安:“诸位!此去安西,不立功,不回来!”", 6,
   "low-angle medium shot, WEI YOUAN, AGE 25: [锚点], jumping onto a bench with a wine bowl raised high, firelight on his face", "static camera, he jumps up and raises the bowl"),
 S("15", "全景", "满屋人举碗喊好", "众人喊好", 4,
   "wide shot, the travellers raising their bowls toward the young man on the bench", "static camera, everyone raises their bowls at once"),
 S("16", "中景", "阿蘅抱酒坛添酒,笑着躲开一只手", "笑声", 5,
   "medium shot, A HENG, AGE 23-29: [锚点], carrying a wine jar through the crowd, pouring, laughing as she steps away from a reaching hand", "static camera, she pours and slips past"),
 S("17", "近景", "卢七站在门边看着一屋子人", "—", 5,
   "close shot, LU QI, AGE 27: [锚点], standing by the door frame watching the noisy room, firelight on one side of his face", "static camera, he watches, a small smile"),
 S("18", "中景,跟", "韦幼安跳下凳,夺笔蘸墨,走向西墙", "—", 6,
   "medium tracking shot, WEI YOUAN, AGE 25: [锚点], jumping down, grabbing a brush, dipping it deep in ink and striding to the wall", "camera follows him to the wall"),
 S("19", "特写", "笔落在白墙上,一挥而就(书法后期合成)", "笔锋声", 7,
   "close-up, a brush heavy with black ink sweeping across fresh white plaster, a young man's wrist, lamp light", "static camera, the brush writes in fast confident strokes", key=True),
 S("20", "全景", "满屋喝彩", "喝彩声", 4,
   "wide shot, the crowd cheering as WEI YOUAN, AGE 25: [锚点], steps back from the wall with the brush raised", "static camera, the crowd cheers and toasts"),
]),
dict(head="内景 驿厅 深夜(回忆,749)", short="驿厅 深夜(749)", era="天宝",
     env="the same hall late at night, emptied, one oil lamp, overturned bowls, the fresh poem glistening on the west wall",
     tone="intimate and warm; a lesson",
script="""
深夜。客人都睡了。卢七收拾满地的碗。
韦幼安坐在墙根,仰头看自己的诗,酒还没醒。
韦幼安:你识字吗?
卢七:不识。
韦幼安:来。
他拉过卢七的手,蘸了一点墨,在墙脚的空白处一笔一笔写。
韦幼安:西。一横。一竖。里面一个口。口里两笔——
韦幼安:像不像一扇门,门里站着两个人?往西走的人。
卢七跟着他的手描了一遍,又自己描了一遍。
韦幼安:记住这个字。认得它,就知道我去哪儿了。
卢七:那“东”呢?
韦幼安大笑。
韦幼安:东不用认。东是回家的路,闭着眼睛也走得回去。
韦幼安靠着墙睡着了。卢七给他盖上一件袍子,走出门去。
门外,满天星。卢七蹲在地上,用手指在沙上写了一个“西”字。风吹过来,沙字慢慢平了。他又写了一个。
""",
shots=[
 S("21", "全景,固定", "空了的驿厅,卢七收拾碗,韦幼安坐在墙根", "炭火噼啪", 7,
   "wide shot of the emptied hall late at night, one oil lamp, LU QI, AGE 27: [锚点], picking up bowls, WEI YOUAN, AGE 25: [锚点], sitting on the floor against the poem wall", "static camera, the lamp flame sways"),
 S("22", "近景", "韦幼安仰头看自己的诗", "韦幼安:“你识字吗?”卢七:“不识。”", 6,
   "close shot, WEI YOUAN, AGE 25: [锚点], head tilted back against the wall, looking up at his own poem, flushed", "static camera, he asks without looking down"),
 S("23", "双人", "韦幼安拉过卢七的手", "韦幼安:“来。”", 4,
   "two-shot at the foot of the wall, WEI YOUAN, AGE 25: [锚点], pulling LU QI, AGE 27: [锚点], down beside him by the wrist", "static camera, he pulls the other man down to sit"),
 S("24", "特写", "两只手叠在一起,蘸墨在墙脚写字", "韦幼安:“西。一横。一竖。里面一个口。口里两笔——”", 8,
   "close-up, a scholar's hand guiding a rougher hand holding a brush, writing one large character near the bottom of the white wall, lamp light", "static camera, the guided brush makes the strokes one by one", key=True),
 S("25", "近景", "韦幼安说得眉飞色舞", "韦幼安:“像不像一扇门,门里站着两个人?往西走的人。”", 6,
   "close shot, WEI YOUAN, AGE 25: [锚点], explaining with delight, lamp light in his eyes", "static camera, he talks with his hands"),
 S("26", "特写", "卢七独自描一遍", "—", 5,
   "close-up, a rough hand tracing the same character again alone with a brush, slowly", "static camera, the hand traces the strokes carefully"),
 S("27", "近景", "韦幼安", "韦幼安:“记住这个字。认得它,就知道我去哪儿了。”", 6,
   "close shot, WEI YOUAN, AGE 25: [锚点], leaning his head back against the wall, eyes half closed", "static camera, he speaks, smiling"),
 S("28", "近景", "卢七", "卢七:“那‘东’呢?”", 3,
   "close shot, LU QI, AGE 27: [锚点], holding the brush, looking at him", "static camera, he asks simply"),
 S("29", "近景", "韦幼安大笑", "韦幼安:“东不用认。东是回家的路,闭着眼睛也走得回去。”", 7,
   "close shot, WEI YOUAN, AGE 25: [锚点], laughing loudly, head thrown back", "static camera, he laughs and answers"),
]),
dict(head="外景 驿门 清晨(回忆,749)", short="驿门 清晨(749)", era="天宝",
     env="the gate of the post station at sunrise in 749, the young willow tree about two metres tall by the spring, the road running west",
     tone="bright and careless",
script="""
清晨。韦幼安骑马出门,向西。走出几步,他回头挥手。
韦幼安:等我封了侯,回来请你喝酒!
卢七站在门口,只说了一句。
卢七:前头有水。
韦幼安大笑,打马走了。
""",
shots=[
 S("29a", "近景", "韦幼安靠墙睡着,卢七给他盖上袍子", "—", 5,
   "close shot, WEI YOUAN, AGE 25: [锚点], asleep against the poem wall, LU QI, AGE 27: [锚点], laying a robe over him", "static camera, the robe settles over the sleeping man"),
 S("29b", "大远景,固定", "星空下的驿门,一个人蹲在沙地上", "风声", 7,
   "extreme long shot at night, the gate of the post station under a sky full of stars, a single man crouching on the sand outside, the young willow beside the spring", "static camera, stars, the figure barely moves"),
 S("29c", "特写,俯拍", "手指在沙上写“西”,风吹平,又写一个", "风声", 8,
   "top-down close-up, a finger writing one large character in the sand by starlight, wind blowing grains across it until it fades, the finger writing it again", "static camera, the finger writes, the wind erases, the finger writes again", key=True),
 S("30", "中景", "韦幼安骑马出门,回头挥手", "韦幼安:“等我封了侯,回来请你喝酒!”", 6,
   "medium shot at sunrise, WEI YOUAN, AGE 25: [锚点], riding out of the gate toward frame right, turning in the saddle to wave, the young willow by the spring", "static camera, he rides out and waves back"),
 S("31", "近景", "卢七在门口", "卢七:“前头有水。”", 4,
   "close shot, LU QI, AGE 27: [锚点], standing in the gate, morning light", "static camera, he speaks the farewell line"),
 S("32", "大远景,固定", "一人一马向西(画右)远去,驿道金光", "马蹄声远去", 9,
   "extreme long shot at sunrise, a single rider growing small on the golden road to the west, frame right, the station and the young willow on the left", "static camera, the rider recedes to the right", key=True),
]),
dict(head="外景 驿道 黄昏(回忆,755)", short="驿道 黄昏(755)", era="天宝",
     env="the road west of the post station at dusk in 755, the willow now a young tree about four metres tall, a dusty cold wind",
     tone="weary and grey under a still-warm sky",
script="""
字幕:天宝十四载。
黄昏。西边驿道上,一个人牵着一匹瘸马,一步一步走过来。往东。
卢七在门口扫沙,抬头看了一眼,又低头扫。再抬头。
那人在门前停住,看着柳树。
韦幼安:这柳树……长这么大了。
卢七的扫帚停了。
卢七:韦郎?
韦幼安笑了一下,嘴唇是裂的。
""",
shots=[
 S("33", "大远景,固定", "黄昏,一人牵瘸马从西边(画右)走来,往东(画左)", "风声;字幕“天宝十四载”", 9,
   "extreme long shot at dusk, a lone thin man leading a limping horse along the road from frame right toward the station on the left, the willow now a young tree", "static camera, the man and horse move slowly from right to left", key=True),
 S("34", "中景", "卢七在门口扫沙,抬头,低头,再抬头", "扫帚声", 6,
   "medium shot, LU QI, AGE 33: [锚点], sweeping sand at the gate, glancing up, going back to sweeping, then looking up again", "static camera, he looks up twice"),
 S("35", "近景", "韦幼安看着柳树", "韦幼安:“这柳树……长这么大了。”", 6,
   "close shot, WEI YOUAN, AGE 31: [锚点], stopping by the young willow and looking up at it, dust on his face", "static camera, he looks up at the tree and speaks"),
 S("36", "近景", "卢七的扫帚停了", "卢七:“韦郎?”", 4,
   "close shot, LU QI, AGE 33: [锚点], the broom stopped, recognising him", "static camera, he speaks the name carefully"),
 S("37", "近景", "韦幼安笑了一下,嘴唇是裂的", "—", 4,
   "close shot, WEI YOUAN, AGE 31: [锚点], a tired smile with cracked lips", "static camera, he smiles and looks down"),
]),
dict(head="内景 驿厅 夜(回忆,755)", short="驿厅 夜(755)", era="天宝",
     env="the hall at night in 755, half-empty, one oil lamp, the poem wall now covered to about two thirds, the 749 poem still dark and fresh-looking",
     tone="shame and tenderness; nobody says the word failure",
script="""
夜。驿厅里只有几个过路的人在睡。
韦幼安站在自己当年的诗前,看了很久。
韦幼安:“男儿不作封侯梦”……
他笑出声,笑着笑着停下来。
韦幼安:在幕府里,抄了六年文书。封侯?连个名字都没人记得。
柳娘从门后探出头,手里攥着一块炭。阿蘅把她拉了回去。
韦幼安:笔。
卢七把笔递给他。他在旧诗旁边写,手在抖,写得很慢。
卢七看着墙,一个字一个字地认,停在一个字上。
卢七:西。
韦幼安:……你认得了。
卢七:认得一个。
卢七出去,端回来一盆苦泉水,放在他面前。
卢七:水是苦的,照人倒清楚。
韦幼安低头。水里是一张晒黑的脸,两鬓全白了。
韦幼安:我去的时候,头发是黑的。
他捧起水洗脸,洗了很久。
""",
shots=[
 S("38", "全景,固定", "半空的驿厅,几个过客在睡,韦幼安站在墙前", "鼾声、风声", 7,
   "wide shot of the half-empty hall at night, a few travellers asleep on mats, WEI YOUAN, AGE 31: [锚点], standing alone before the poem wall with an oil lamp", "static camera, he stands still before the wall"),
 S("39", "近景,仰拍", "韦幼安看自己的旧诗", "韦幼安:“‘男儿不作封侯梦’……”", 6,
   "low-angle close shot, WEI YOUAN, AGE 31: [锚点], looking up at his own old poem, lamp light from below", "static camera, he reads his own line in a whisper"),
 S("40", "近景", "他笑出声,笑着停下", "韦幼安:“在幕府里,抄了六年文书。封侯?连个名字都没人记得。”", 9,
   "close shot, WEI YOUAN, AGE 31: [锚点], laughing bitterly, then the laugh stopping, eyes on the wall", "static camera, he laughs, stops, speaks flatly"),
 S("41", "中景", "柳娘从门后探头,手里攥着炭;阿蘅把她拉回去", "—", 5,
   "medium shot, LIU NIANG, AGE 8: [锚点], peeking around the door frame clutching a piece of charcoal, A HENG, AGE 23-29: [锚点], gently pulling her back", "static camera, the girl peeks, the mother's hand draws her away"),
 S("42", "双人", "卢七把笔递给他", "韦幼安:“笔。”", 4,
   "two-shot, LU QI, AGE 33: [锚点], handing a brush to WEI YOUAN, AGE 31: [锚点], before the wall", "static camera, the brush passes from hand to hand"),
 S("43", "特写", "颤抖的手在旧诗旁写新诗(书法后期合成)", "笔锋声,很慢", 8,
   "close-up, a thin trembling hand writing slowly with a brush on the plaster right beside an older dark poem, the new ink pale", "static camera, the brush moves slowly and shakes", key=True),
 S("44", "近景", "卢七一个字一个字地认,停在一个字上", "卢七:“西。”", 5,
   "close shot, LU QI, AGE 33: [锚点], reading the wall character by character, lips moving, stopping on one", "static camera, his eyes move and stop"),
 S("45", "双人", "两人对视", "韦幼安:“……你认得了。”卢七:“认得一个。”", 6,
   "two-shot, WEI YOUAN, AGE 31: [锚点], turning to LU QI, AGE 33: [锚点], the lamp between them", "static camera, they look at each other"),
 S("46", "中景", "卢七端来一盆水,放在他面前", "卢七:“水是苦的,照人倒清楚。”", 7,
   "medium shot, LU QI, AGE 33: [锚点], setting a wooden basin of water on the floor before WEI YOUAN, AGE 31: [锚点], who sits against the wall", "static camera, he sets down the basin and steps back"),
 S("47", "特写,俯拍", "水面里一张晒黑的脸,两鬓全白", "—", 6,
   "top-down close-up of still water in a wooden basin reflecting a sunburnt gaunt face with white temples, lamp light", "static camera, the reflection trembles slightly then settles", key=True),
 S("48", "近景", "韦幼安", "韦幼安:“我去的时候,头发是黑的。”", 5,
   "close shot, WEI YOUAN, AGE 31: [锚点], looking down into the basin", "static camera, he speaks very quietly"),
 S("49", "特写", "他捧水洗脸,洗了很久", "水声", 6,
   "close-up, two thin hands lifting water to a bowed face again and again", "static camera, he washes his face slowly, again and again"),
]),
dict(head="外景 驿门 清晨(回忆,755)", short="驿门 清晨(755)", era="天宝",
     env="the gate at grey dawn in 755, the young willow by the spring, the road running east into haze",
     tone="plain; a man who does not look back",
script="""
清晨。韦幼安牵着瘸马出门,往东。他没有回头。
卢七:前头有水。
韦幼安停了一步。
韦幼安:东边的水,不苦吧。
卢七没有答。韦幼安走了。
""",
shots=[
 S("50", "中景,背面", "韦幼安牵瘸马出门,往东(画左)", "马蹄一深一浅", 6,
   "medium shot from behind, WEI YOUAN, AGE 31: [锚点], leading the limping horse out of the gate toward frame left, grey dawn", "static camera, he walks out without turning"),
 S("51", "近景", "卢七", "卢七:“前头有水。”", 3,
   "close shot, LU QI, AGE 33: [锚点], standing in the gate", "static camera, he speaks once"),
 S("52", "近景,背面", "韦幼安停了一步,没回头", "韦幼安:“东边的水,不苦吧。”", 5,
   "close shot from behind, WEI YOUAN, AGE 31: [锚点], pausing mid-step on the road without turning his head", "static camera, he stops, speaks, and walks on"),
 S("53", "大远景,固定", "一人一马向东(画左)走进灰雾(全剧第一个向东的背影)", "风声", 8,
   "extreme long shot at grey dawn, a man and a limping horse walking away to the east toward frame left into haze, the station small on the right", "static camera, they fade into the haze", key=True,
   out="the figures dissolve into the grey haze; the haze cools into the blue-grey of 787."),
]),
dict(head="内景 驿厅 黄昏(787)", short="驿厅 黄昏(787)", era="787",
     env="the hall of POST STATION 787 at dusk, the low table with ink and a growing paper scroll before POEM WALL 787",
     tone="still; history in one sentence",
script="""
黄昏。张归把两首诗抄进纸卷,并排写,中间没有留空。
卢七在旁边看着。
张归:他后来呢?
卢七:往东走了。那年冬天,东边就乱了。
张归停笔。
张归(旁白):两首诗中间,隔着六年。我把它们抄在一起,中间没有留空。
墙上的两首诗,一浓一淡。
""",
shots=[
 S("54", "特写", "张归抄诗,两首并排,中间不留空", "笔锋声", 6,
   "close-up, a young man's hand copying two short poems side by side onto a paper scroll with no gap between them, dusk light", "static camera, the brush moves down the column"),
 S("55", "双人", "张归问,卢七在旁边看", "张归:“他后来呢?”", 4,
   "two-shot, ZHANG GUI, AGE 18: [锚点], at the low table looking up at LU QI, AGE 65: [锚点], who stands beside the wall", "static camera, he asks without stopping the brush"),
 S("56", "近景", "卢七", "卢七:“往东走了。那年冬天,东边就乱了。”", 6,
   "close shot, LU QI, AGE 65: [锚点], looking at the two poems on the wall, dusk light", "static camera, he speaks simply"),
 S("57", "特写", "张归停笔", "—", 3,
   "close-up, the brush stopping above the paper, a drop of ink gathering at its tip", "static camera, the brush stops"),
 S("58", "特写,极缓推", "墙上两首诗,一浓一淡", "旁白:“两首诗中间,隔着六年。我把它们抄在一起,中间没有留空。”羌笛", 10,
   "close-up, the two poems side by side on cracked white plaster, the left in dark ink, the right pale and thin, dusk light fading", "extremely slow push in, the light slowly dims", key=True,
   out="hold on the two poems while the light fades to dark; end of episode."),
]),
])
