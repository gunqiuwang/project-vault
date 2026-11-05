EP = dict(
cn="十", title="归途",
summary="第十集是第十天。墙擦完了,也抄完了。卢七研墨,在墙上写下一生唯一的一首诗,张归把它抄在长卷最后。张归说出自己名字的来历:“归来的归。”卢七说:跟我诗里那个归,是一个字。临行前,张归换上父亲那件偏大的唐袍,向墙、向柳、向卢七各拜一拜,再换回吐蕃袍,带着长卷往西回沙州。拆驿的人明天就到,卢七没有走。入夜,他照旧点灯,摇了一下铃,门外空无一人。尾声:1900 年,敦煌藏经洞里,一卷《苦泉驿壁诗》重见天日。",
info=[("场次", "8 场:现实 7 场,尾声 1 场(1900)"),
      ("现实线人物", "卢七(65)、张归、甘布、诺桑、马“灰”"),
      ("尾声", "只出现一只手和一卷写本;不点名发现者"),
      ("钥匙物件", "长卷《苦泉驿壁诗》、卢七的题诗、张归父亲的唐袍、铜铃"),
      ("方向", "张归回沙州(敦煌),在苦泉驿以西,所以他向西走(画面向右)。长卷跟着他到了敦煌,这就是它出现在藏经洞的原因。"),
      ("回收", "卢七哼阿蘅的曲子只哼前半句(第 7 集);“今天也没有人来”(第 8 集);一声铃(第 1 集第一声铃,本集最后一声铃);“前头有水”(全剧)。")],
text_block="""**卢七的题诗(787,他一生唯一的诗):**

迎来复送往,五十度春风。人各有归路,吾归在此中。""",
curve="静(擦完了,抄完了)→ 郑重(一生唯一的诗)→ 认(同一个“归”字)→ 庄重(三拜)→ 别(往西)→ 独(点灯、半句曲子)→ 空(一声铃,门外无人)→ 远(写本重见天日)。",
anchors="""
ZHANG GUI IN TANG ROBE: ZHANG GUI, AGE 18, wearing his dead father's blue-green Tang round-collar robe over his clothes, too big at the shoulders and too long in the sleeves, Tibetan braids still in his hair

THE SCROLL: a long hand-copied paper scroll on a thin wooden roller, dense columns of Chinese poems in a young careful hand, the title at its head, tied with a faded red cord

LIBRARY CAVE 1900: a small dark chamber in the Mogao caves at Dunhuang, floor-to-ceiling bundles of ancient scrolls wrapped in cloth, dust in the air, a single shaft of daylight from a narrow opening
""",
scenes=[
dict(head="内景 驿厅 晨(787)", short="驿厅 晨(787)", era="787",
     env="the hall of POST STATION 787 in morning light, POEM WALL 787 freshly wiped, a long paper scroll unrolled across the floor",
     tone="two jobs finished at the same moment",
script="""
字幕:第十日。
清晨。张归跪在地上,写完长卷的最后一列。长卷从矮几一直铺到门口。
卢七擦完墙脚最后一块。他直起腰,把布叠好。
卢七:擦完了。
张归放下笔。
张归:抄完了。
两个人看着对方。谁也没有笑。
""",
shots=[
 S("1", "大远景,固定", "清晨的驿厅,长卷从矮几一直铺到门口", "字幕“第十日”", 8,
   "extreme wide shot of the hall in clear morning light, a long hand-copied scroll unrolled across the floor from the low table to the door, POEM WALL 787 clean behind, ZHANG GUI, AGE 18: [锚点], kneeling at the end of it, LU QI, AGE 65: [锚点], at the foot of the wall", "static camera, dust floats in the light", key=True),
 S("2", "特写", "写完最后一列", "笔声", 5,
   "close-up, a brush finishing the last column of characters at the end of THE SCROLL", "static camera, the last stroke"),
 S("3", "中景", "卢七擦完墙脚最后一块,直起腰,把布叠好", "卢七:“擦完了。”", 7,
   "medium shot, LU QI, AGE 65: [锚点], finishing the last patch at the foot of the wall, straightening his back slowly and folding the cloth", "static camera, he straightens and folds the cloth"),
 S("4", "近景", "张归放下笔", "张归:“抄完了。”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], laying down the brush", "static camera, he lays it down"),
 S("5", "双人", "两个人看着对方,谁也没有笑", "—", 5,
   "two-shot, ZHANG GUI, AGE 18: [锚点], kneeling by the scroll and LU QI, AGE 65: [锚点], standing by the wall, looking at each other across the hall", "static camera, they look at each other"),
]),
dict(head="内景 驿厅 午(787)", short="驿厅 午(787)", era="787",
     env="the hall at noon, POEM WALL 787, one bare patch of plaster low near the door, an ink stone",
     tone="the only poem of a life",
script="""
卢七蹲下来,研墨。研得很慢。
他拿起笔,走到西墙最靠门的地方。那里有一小块空白。
他一笔一笔地写。每写一个字,都要停一下。
张归站在他身后,跟着念。
张归:迎来复送往,五十度春风。
张归:人各有归路……吾归在此中。
卢七放下笔。
卢七:字是跟墙学的。丑。
张归蹲到长卷末尾,把这首诗抄上去。抄完,他在卷首写了五个字:苦泉驿壁诗。
张归:署名怎么写?卢守安?
卢七:写卢七就行。
""",
shots=[
 S("6", "特写", "卢七研墨,研得很慢", "研墨声", 6,
   "close-up, an old man's hands grinding an ink stick on the stone very slowly", "static camera, the ink stick circles"),
 S("7", "中景", "他拿笔走到西墙最靠门的一小块空白前", "—", 6,
   "medium shot, LU QI, AGE 65: [锚点], carrying a brush to a small bare patch of plaster low on the wall near the door", "static camera, he walks and stops"),
 S("8", "特写", "一笔一笔写,每个字都停一下(书法后期合成)", "笔声,停顿", 9,
   "close-up, an old trembling hand writing characters one at a time on the bare plaster, pausing after each, the brush lifting and lowering", "static camera, the brush writes slowly with pauses", key=True),
 S("9", "近景", "张归站在他身后,跟着念", "张归:“迎来复送往,五十度春风。”", 6,
   "close shot, ZHANG GUI, AGE 18: [锚点], behind the old man's shoulder, reading aloud as the characters appear", "static camera, he reads softly"),
 S("10", "近景,极缓推", "张归", "张归:“人各有归路……吾归在此中。”", 7,
   "close shot, ZHANG GUI, AGE 18: [锚点], reading the last line slowly, his voice catching", "extremely slow push in, he reads", key=True),
 S("11", "近景", "卢七放下笔", "卢七:“字是跟墙学的。丑。”", 5,
   "close shot, LU QI, AGE 65: [锚点], lowering the brush and looking at what he wrote", "static camera, he lowers the brush"),
 S("12", "特写", "张归在长卷末尾抄诗,再在卷首写“苦泉驿壁诗”", "笔声", 7,
   "close-up, a young hand copying a short poem at the end of THE SCROLL, then writing five characters at its head", "static camera, the brush writes"),
 S("13", "双人", "署名", "张归:“署名怎么写?卢守安?”卢七:“写卢七就行。”", 6,
   "two-shot, ZHANG GUI, AGE 18: [锚点], brush poised over the scroll, LU QI, AGE 65: [锚点], sitting down beside him", "static camera, he asks, the old man answers"),
]),
dict(head="外景 苦泉边 午后(787)", short="苦泉边 午后(787)", era="787",
     env="the stone-lined spring under the old willow with forty-three red cords, afternoon light",
     tone="one word shared",
script="""
午后。两人坐在苦泉边。
卢七:你叫张归。哪个归?
张归:归来的归。我爹起的。他盼唐兵回来。
张归:唐兵没回来。他死在沙州城上。
卢七:回来的不一定是兵。
他抬手,指了指驿厅的方向。
卢七:跟我诗里那个归,是一个字。
张归:……是一个字。
""",
shots=[
 S("14", "中景", "两人坐在苦泉边", "风声", 5,
   "medium shot in afternoon light, LU QI, AGE 65: [锚点], and ZHANG GUI, AGE 18: [锚点], sitting on the rim of the spring under the old willow", "static camera, the willow sways"),
 S("15", "近景", "卢七", "卢七:“你叫张归。哪个归?”", 4,
   "close shot, LU QI, AGE 65: [锚点], turning to the young man", "static camera, he asks"),
 S("16", "近景", "张归", "张归:“归来的归。我爹起的。他盼唐兵回来。”", 6,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking at the water", "static camera, he answers"),
 S("17", "近景", "张归", "张归:“唐兵没回来。他死在沙州城上。”", 5,
   "close shot, ZHANG GUI, AGE 18: [锚点], his jaw tight", "static camera, he says it flatly"),
 S("18", "近景", "卢七抬手指了指驿厅方向", "卢七:“回来的不一定是兵。跟我诗里那个归,是一个字。”", 8,
   "close shot, LU QI, AGE 65: [锚点], lifting his hand to point toward the hall", "static camera, he points and speaks", key=True),
 S("19", "近景", "张归", "张归:“……是一个字。”", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking toward the hall, eyes wet", "static camera, he repeats it"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏(787)", era="787",
     env="the gate of POST STATION 787 at dusk, the old willow, the hall door visible through the gate",
     tone="a private ceremony",
script="""
黄昏。张归走到柳树后面,从腰间取出那件叠好的唐袍,抖开,穿在身上。肩膀宽了,袖子长了一截。
他走出来。卢七看着他,伸手替他把领子翻过来,右衽。
卢七:领子,右衽。
张归转身,对着驿厅那面墙的方向,深深一拜。
对着柳树,一拜。
对着卢七,一拜。
远处,甘布和诺桑牵着马站着。诺桑把脸转开了。
张归脱下唐袍,叠好,塞回腰间,重新穿上羊皮袍。
""",
shots=[
 S("20", "中景", "张归在柳树后取出唐袍,抖开,穿上;肩宽了,袖子长了", "布声", 8,
   "medium shot at dusk, ZHANG GUI, AGE 18: [锚点], behind the willow, taking the folded Tang robe from his waist, shaking it open and putting it on, too wide at the shoulders, sleeves too long", "static camera, he dresses slowly", key=True),
 S("21", "双人", "卢七伸手替他把领子翻过来", "卢七:“领子,右衽。”", 6,
   "two-shot, LU QI, AGE 65: [锚点], reaching up to fold the collar of ZHANG GUI IN TANG ROBE to the right side", "static camera, the old hands fix the collar"),
 S("22", "全景,门框构图", "张归对着驿厅那面墙的方向,深深一拜", "—", 6,
   "wide shot through the gate, ZHANG GUI IN TANG ROBE bowing deeply toward the hall and its wall across the courtyard", "static camera, he bows and rises"),
 S("23", "全景", "对着柳树,一拜", "—", 5,
   "wide shot, ZHANG GUI IN TANG ROBE bowing deeply to the old willow hung with red cords", "static camera, he bows and rises"),
 S("24", "全景", "对着卢七,一拜", "—", 6,
   "wide shot, ZHANG GUI IN TANG ROBE bowing deeply to LU QI, AGE 65: [锚点], who stands still and lets him", "static camera, he bows and rises", key=True),
 S("25", "中景", "远处甘布和诺桑牵着马,诺桑把脸转开", "—", 4,
   "medium shot, TIBETAN SOLDIERS (GAMPO, NORSANG) holding the horses at a distance, NORSANG turning his face away", "static camera, he looks away"),
 S("26", "中景", "张归脱下唐袍,叠好,塞回腰间,穿回羊皮袍", "—", 7,
   "medium shot, ZHANG GUI, AGE 18: [锚点], taking off the Tang robe, folding it carefully, tucking it back at his waist and pulling on the sheepskin robe", "static camera, he changes back"),
]),
dict(head="外景 驿门 黄昏(787)", short="驿门 黄昏 · 别(787)", era="787",
     env="the gate of POST STATION 787 at late dusk, three saddled horses, the road west toward Shazhou",
     tone="the last guest",
script="""
三匹马备好了。长卷用红绳系着,背在张归身后。
张归:明天,拆驿的人就到了。你跟我走。
卢七:驿里不能没有人。
张归看着他,没有再劝。
卢七:前头有水。
张归上马,往西走。走出去几步,他在马上回头。卢七站在门口,身边是柳树。
""",
shots=[
 S("27", "中景", "三匹马备好了,长卷用红绳系着背在张归身后", "马喷鼻", 5,
   "medium shot at late dusk, three saddled horses at the gate, ZHANG GUI, AGE 18: [锚点], with THE SCROLL tied across his back with a red cord, GAMPO and NORSANG already mounted", "static camera, the horses shift"),
 S("28", "近景", "张归", "张归:“明天,拆驿的人就到了。你跟我走。”", 5,
   "close shot, ZHANG GUI, AGE 18: [锚点], facing the old man at the gate", "static camera, he asks"),
 S("29", "近景", "卢七", "卢七:“驿里不能没有人。”", 4,
   "close shot, LU QI, AGE 65: [锚点], in the gate, calm", "static camera, he answers"),
 S("30", "近景", "张归看着他,没再劝", "—", 4,
   "close shot, ZHANG GUI, AGE 18: [锚点], looking at the old man and accepting it", "static camera, he nods slightly"),
 S("31", "近景", "卢七", "卢七:“前头有水。”", 4,
   "close shot, LU QI, AGE 65: [锚点], saying the farewell line one more time", "static camera, he says it", key=True),
 S("32", "大远景,固定", "三骑往西(画右)走;张归在马上回头,卢七站在门口,身边是柳树", "马蹄远去", 10,
   "extreme long shot at dusk, three riders moving away west toward frame right, the last one turning in the saddle to look back, LU QI, AGE 65: [锚点], small in the gate beside the old willow", "static camera, the riders recede; one looks back", key=True),
]),
dict(head="内景 驿厅 夜(787)", short="驿厅 夜(787)", era="787",
     env="the hall of POST STATION 787 at night, the poem wall with Lu Qi's new poem near the door, one oil lamp, the stable across the courtyard",
     tone="routine as faith",
script="""
夜。卢七点亮桌上的油灯。
他低声哼起来。
卢七(哼):柳条青,柳条长……
哼了半句,停住了。
他提着灯走到马厩。灰站在暗处。他摸了摸它的脖子。
卢七:今天也没有人来。
""",
shots=[
 S("33", "中景,固定", "卢七点亮油灯(与第 8 集同机位)", "—", 6,
   "medium shot of the same corner of the hall as in the lonely years, LU QI, AGE 65: [锚点], lighting the oil lamp on the table", "static camera, locked-off, identical framing; the flame catches"),
 S("34", "近景", "他低声哼,哼了半句停住", "卢七(哼):“柳条青,柳条长……”", 7,
   "close shot, LU QI, AGE 65: [锚点], humming under his breath by the lamp, then stopping", "static camera, he hums and stops"),
 S("35", "中景", "提灯走到马厩,摸了摸灰的脖子", "卢七:“今天也没有人来。”", 7,
   "medium shot, LU QI, AGE 65: [锚点], carrying the lamp into the stable and stroking the neck of the very old HUI (THE HORSE)", "static camera, he strokes the horse and speaks"),
]),
dict(head="外景 驿门 夜(787)", short="驿门 夜 · 最后一声铃(787)", era="787",
     env="the gate of POST STATION 787 at night, stars, the old willow, the empty road running east and west",
     tone="the last bell",
script="""
夜。卢七拿着铜铃走到门口。
他举起铃,摇了一下。
“叮——”
铃声荡出去,很远。门外空无一人。
他看着空空的驿道,轻声说。
卢七:前头有水。
""",
shots=[
 S("36", "中景", "卢七拿着铜铃走到门口", "—", 5,
   "medium shot at night, LU QI, AGE 65: [锚点], carrying the bronze bell out to the gate under the stars", "static camera, he walks to the gate"),
 S("37", "近景,仰拍", "他举起铃,摇了一下", "“叮——”", 5,
   "low-angle close shot, the bronze bell raised against the night sky in an old hand, ringing once", "static camera, it rings once", key=True),
 S("38", "大远景,固定", "铃声荡出去,门外空无一人", "铃声尾音,风声", 7,
   "extreme long shot at night, the empty road stretching away under the stars, nobody, a tiny figure at the gate", "static camera, nothing moves"),
 S("39", "近景,极缓推", "卢七看着空驿道,轻声说", "卢七:“前头有水。”", 7,
   "close shot, LU QI, AGE 65: [锚点], looking down the empty road, speaking softly to nobody", "extremely slow push in, he says it to the dark", key=True),
 S("40", "大远景,固定", "最后一个镜头:一盏灯、一棵柳、一条向东的路,风声渐弱", "风声渐弱,直至无声", 12,
   "extreme long shot at night from high ground looking east, one small lit window, one old willow, one road running east to the horizon, stars", "static camera, the wind slowly dies away", key=True,
   out="hold until the wind is silent; cut to black."),
 S("41", "黑场", "黑场", "无声", 3, "", ""),
]),
dict(head="尾声 内景 莫高窟藏经洞 日(1900)", short="尾声 藏经洞(1900)", era="1900",
     env="LIBRARY CAVE 1900, piles of ancient scrolls, a single shaft of daylight, dust",
     tone="silence across a thousand years",
script="""
字幕:光绪二十六年,敦煌。
一束光从窄窄的洞口照进来,灰尘在光里浮着。四壁堆满了经卷。
一只手伸进经卷堆里,抽出一卷,轴头是一根细木棍,系着一根褪了色的红绳。
红绳解开。写本展开。卷首五个字:苦泉驿壁诗。
镜头顺着一列列字往后移,移到最后一首。
人各有归路,吾归在此中。
风声,很轻。
""",
shots=[
 S("42", "全景,固定", "一束光从洞口照进来,四壁堆满经卷", "极轻的风声;字幕“光绪二十六年,敦煌”", 8,
   "wide shot of LIBRARY CAVE 1900, a single shaft of daylight falling through a narrow opening onto floor-to-ceiling bundles of ancient scrolls, dust floating in the light", "static camera, dust drifts in the light beam", key=True),
 S("43", "特写", "一只手抽出一卷,细木轴头系着褪色的红绳", "—", 6,
   "close-up, a hand reaching into the pile and drawing out a scroll on a thin wooden roller tied with a faded red cord", "static camera, the hand draws the scroll out"),
 S("44", "特写", "红绳解开,写本展开,卷首“苦泉驿壁诗”(文字后期合成)", "纸声", 7,
   "close-up, the faded red cord untied and the old scroll unrolling in the light beam, five characters at its head", "static camera, the scroll unrolls", key=True),
 S("45", "特写,缓横移", "镜头顺着一列列字往后移", "—", 8,
   "close-up lateral move along columns of hand-copied poems on aged yellow paper", "slow lateral move along the columns"),
 S("46", "大特写,极缓推", "停在最后一首:“人各有归路,吾归在此中。”", "风声渐止", 8,
   "extreme close-up of the last short poem on the aged scroll, the light beam resting on it", "extremely slow push in, then hold", key=True,
   out="hold on the last poem; fade to black; end of the series."),
]),
])
