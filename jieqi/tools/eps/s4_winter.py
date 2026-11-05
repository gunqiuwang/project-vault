ENV_FERRY = "LU PU VILLAGE ferry landing under the enormous old camphor tree, the stone steps, the FERRY BOAT, the thatched tea pavilion, the slow green river"

EPS = {}

EPS["19"] = dict(cn="十九", jq="立冬", title="补冬",
summary="立冬。阿禾一个人守着茶亭,每天天不亮就生火。村里的人一个接一个来喝茶,走的时候都留下点东西:一筐炭、一坛冬酿酒、一把晒干的桂花。最后来的是桑娘,挺着七个月的肚子,给阿禾带来一件新棉袄。“婆婆不在了,补冬的事,大家补。”",
info=[("物候", "水始冰,地始冻,雉入大水为蜃"), ("人物", "阿禾、桑娘、石生、许秀才、陈先生、周老篙、村民"),
      ("风俗", "立冬“补冬”:江南人家进补御寒,酿冬酒,做新棉衣。"),
      ("这一集", "王婆走后,全村接过了照看阿禾的事。")],
curve="冷(一个人守茶亭)→ 暖(一样样东西)→ 满(新棉袄)。",
scenes=[
dict(head="内景 茶亭 立冬一日", short="茶亭 一日", era="冬", env="the tea pavilion by the ferry on the first cold day of winter, the clay stove lit, the empty bamboo chair kept in its place, grey river",
     tone="small kindnesses piling up", crowd="villagers coming and going one by one",
script="""
字幕:立冬。水始冰,地始冻,雉入大水为蜃。
天不亮,阿禾就生起了茶亭的炉子。王婆的竹椅还放在老地方,上面搁着那把扇子。
石生来喝茶。走的时候,门口多了一筐炭。
许秀才来喝茶。走的时候,桌上多了一坛冬酿酒。
陈先生来喝茶。走的时候,窗台上多了一包晒干的桂花,纸包上写着字。
阿禾:先生,这写的什么?
陈先生:泡茶用。
""",
shots=[
 S("1", "大远景,固定", "立冬,灰白的河,茶亭冒着烟", "寒风;字幕“立冬”与三候", 8,
   "extreme long shot of the ferry landing on the first cold day of winter, the river grey, thin ice at the edges, smoke rising from the tea pavilion", "static camera, smoke drifts", key=True),
 S("2", "中景", "天不亮阿禾生起炉子;王婆的竹椅还在老地方,上面搁着扇子", "—", 6,
   "medium shot of the tea pavilion before dawn, A HE, AGE 8: [锚点], lighting the clay stove, the empty bamboo chair beside it with a fan resting on the seat", "static camera, the fire catches"),
 S("3", "中景,固定", "石生喝完茶走了,门口多了一筐炭", "—", 6,
   "medium shot, SHI SHENG, AGE 22: [锚点], finishing his tea and leaving, a basket of charcoal left by the door", "static camera, locked-off; he leaves, the basket remains"),
 S("4", "中景,固定,同机位", "许秀才走了,桌上多了一坛冬酿酒", "—", 6,
   "medium shot from the identical position, XU XIUCAI, AGE 20: [锚点], leaving, a sealed wine jar now on the table", "static camera, identical framing; he leaves, the jar remains"),
 S("5", "中景,固定,同机位", "陈先生走了,窗台上多了一包桂花", "阿禾:“先生,这写的什么?”陈先生:“泡茶用。”", 7,
   "medium shot from the identical position, MR CHEN, AGE 46: [锚点], pausing at the door to answer the girl, a small paper packet of dried osmanthus on the window ledge", "static camera, identical framing; he answers and leaves"),
]),
dict(head="内景 茶亭 黄昏", short="茶亭 黄昏", era="冬", env="the tea pavilion at dusk, the small gifts gathered, the stove glowing",
     tone="being cared for",
script="""
黄昏。桑娘挺着七个月的肚子,扶着门框进来,手里抱着一件新棉袄。
桑娘:来,试试。
阿禾穿上。袖子长了一截,桑娘给她挽起来。
桑娘:婆婆不在了,补冬的事,大家补。
阿禾看着满屋子的东西:一筐炭,一坛酒,一包桂花。
周老篙撑船回来,看见孙女穿着新棉袄站在炉子边,停了篙。
阿禾(旁白):立冬。我有新棉袄了。还有三个节气。
""",
shots=[
 S("6", "中景", "桑娘挺着肚子扶着门框进来,抱着一件新棉袄", "桑娘:“来,试试。”", 6,
   "medium shot at dusk, SANG NIANG, AGE 19: [锚点], seven months pregnant, stepping in holding the door frame, a new indigo padded jacket in her arms", "static camera, she steps in"),
 S("7", "双人", "阿禾穿上,袖子长了一截,桑娘给她挽起来", "—", 6,
   "two-shot, A HE, AGE 8: [锚点], pulling on the padded jacket, sleeves too long, SANG NIANG, AGE 19: [锚点], rolling them up for her", "static camera, she rolls the sleeves"),
 S("8", "近景", "桑娘", "桑娘:“婆婆不在了,补冬的事,大家补。”", 5,
   "close shot, SANG NIANG, AGE 19: [锚点], smoothing the jacket's collar, stove light", "static camera, she speaks", key=True),
 S("9", "主观,缓横移", "满屋的东西:一筐炭、一坛酒、一包桂花", "—", 6,
   "point-of-view slow lateral move across the little gifts in the pavilion, a basket of charcoal, a wine jar, a paper packet of osmanthus, the empty bamboo chair", "slow lateral move"),
 S("10", "大远景,固定", "周老篙撑船回来,看见孙女穿着新棉袄站在炉边,停了篙", "阿禾(旁白):“立冬。我有新棉袄了。还有三个节气。”", 9,
   "extreme long shot at dusk, the ferry boat drifting in to the steps, the old ferryman stopping his pole to look at the lit tea pavilion where a small girl in a new jacket stands by the stove", "static camera, the boat drifts and stops", key=True,
   out="hold; end of episode."),
]),
])

EPS["20"] = dict(cn="二十", jq="小雪", title="腌菜",
summary="小雪,家家腌菜。桑娘教阿禾踩菜:光着脚站进大缸,一层菜一层盐,一脚一脚踩实。冷得阿禾直跳。桑娘说这是王婆教她的法子。“等你爹回来,正好开缸。”",
info=[("物候", "虹藏不见,天气上升地气下降,闭塞而成冬"), ("人物", "阿禾、桑娘、石生、周老篙"),
      ("风俗", "小雪腌菜:江南冬日腌雪里蕻、白菜,入缸踩实,封坛过冬。")],
curve="冷(光脚下缸)→ 闹(跳着踩)→ 传(婆婆的法子)→ 盼(正好开缸)。",
scenes=[
dict(head="外景 桑娘家院子 午", short="院子 午", era="冬", env="a small village courtyard in early winter, a huge glazed earthen vat, piles of washed green mustard greens drying on bamboo racks, coarse salt in a basket, pale sun",
     tone="cold, comic, warm",
script="""
字幕:小雪。虹藏不见,天气上升地气下降,闭塞而成冬。
院子里晾满了洗好的雪里蕻。一口大缸立在当中。
桑娘撑着腰,指挥。
桑娘:脱鞋,洗脚,进去。
阿禾光着脚站进缸里。缸底冰凉,她“哇”地叫了一声。
桑娘往里铺一层菜,撒一把盐。
桑娘:踩!一脚一脚,踩实,踩出水来。
阿禾在缸里跳着踩,冻得直叫。石生在旁边笑得直不起腰。
""",
shots=[
 S("1", "大远景,固定", "初冬的村子,家家院里晾着青菜", "风声;字幕“小雪”与三候", 8,
   "extreme long shot of LU PU VILLAGE in early winter under a pale sun, green vegetables drying on racks in every courtyard, a few bare trees", "static camera, still", key=True),
 S("2", "全景", "院子里晾满了雪里蕻,一口大缸立在当中", "—", 5,
   "wide shot of a small courtyard, racks of washed green mustard greens, a huge glazed earthen vat in the middle, SANG NIANG, AGE 19: [锚点], heavily pregnant, hands on her back", "static camera, still"),
 S("3", "双人", "桑娘撑着腰指挥;阿禾光脚站进缸里,“哇”地一声", "桑娘:“脱鞋,洗脚,进去。”", 6,
   "two-shot, SANG NIANG, AGE 19: [锚点], pointing at the vat, A HE, AGE 8: [锚点], barefoot, stepping into it and yelping at the cold", "static camera, she steps in and yelps"),
 S("4", "特写", "一层菜一层盐", "撒盐沙沙", 5,
   "close-up, hands laying green mustard greens into the vat and scattering a fistful of coarse salt over them", "static camera, the salt scatters"),
 S("5", "中景", "阿禾在缸里跳着踩,冻得直叫;石生笑得直不起腰", "桑娘:“踩!一脚一脚,踩实,踩出水来。”", 7,
   "medium shot, A HE, AGE 8: [锚点], stamping up and down inside the vat, shrieking with the cold, SHI SHENG, AGE 22: [锚点], doubled over laughing", "static camera, she stamps, he laughs", key=True),
]),
dict(head="外景 桑娘家院子 傍晚", short="院子 傍晚", era="冬", env="the courtyard at dusk, the vat sealed with a stone and a cloth, a lamp in the window",
     tone="an inheritance in a recipe",
script="""
傍晚,缸满了。桑娘压上一块大石头,封上布。
阿禾坐在门槛上,脚冻得通红,桑娘把她的脚揣进自己的围裙里。
桑娘:这是王婆教我的法子。我嫁过来那年,也是她把我推进缸里的。
阿禾:婆婆也踩过吗?
桑娘:踩了七十年。
桑娘拍拍那口缸。
桑娘:一个月以后,正好开缸。等你爹回来,吃新腌的菜泡饭。
阿禾(旁白):小雪。我踩了一缸菜。还有两个节气。
""",
shots=[
 S("6", "中景", "缸满了,桑娘压上一块大石头,封上布", "—", 6,
   "medium shot at dusk, SANG NIANG, AGE 19: [锚点], with SHI SHENG, AGE 22: [锚点], helping, setting a heavy stone on the full vat and tying a cloth over it", "static camera, the stone goes on"),
 S("7", "双人", "阿禾坐门槛上,脚冻得通红,桑娘把她的脚揣进围裙里", "—", 6,
   "two-shot on the threshold, A HE, AGE 8: [锚点], with bright red bare feet, SANG NIANG, AGE 19: [锚点], wrapping the girl's feet in her apron", "static camera, the feet are wrapped"),
 S("8", "近景", "桑娘", "桑娘:“这是王婆教我的法子。我嫁过来那年,也是她把我推进缸里的。”", 8,
   "close shot, SANG NIANG, AGE 19: [锚点], smiling at a memory, lamp light from the window", "static camera, she remembers"),
 S("9", "双人", "阿禾问", "阿禾:“婆婆也踩过吗?”桑娘:“踩了七十年。”", 5,
   "two-shot, A HE, AGE 8: [锚点], and SANG NIANG, AGE 19: [锚点], on the threshold", "static camera, she asks, the woman answers"),
 S("10", "特写", "桑娘拍拍那口缸", "桑娘:“一个月以后,正好开缸。等你爹回来,吃新腌的菜泡饭。”", 7,
   "close-up, a woman's hand patting the cloth-covered top of the big earthen vat", "static camera, she pats it twice"),
 S("11", "大远景,固定", "暮色里的院子,一口封好的缸,窗里一盏灯", "阿禾(旁白):“小雪。我踩了一缸菜。还有两个节气。”", 8,
   "extreme long shot at dusk of the small courtyard, a sealed vat with a stone on top, one lit window, smoke from the chimney", "static camera, the light fades", key=True,
   out="hold; end of episode."),
]),
])

EPS["21"] = dict(cn="二十一", jq="大雪", title="伞上的字",
summary="大雪。许秀才决定三年后再考。陈先生把那把旧油纸伞要了回来,在伞面上题了五个字:“鹭浦一夜雨”,又把伞送给他:“下回去临安,带着它。下雨就撑开,看看家里。”阿禾在渡口扫了一上午雪,把台阶扫得干干净净。明天就是冬至。",
info=[("物候", "鹖鴠不鸣,虎始交,荔挺出"), ("人物", "陈先生、许秀才、阿禾、周老篙"),
      ("典故", "映雪读书:晋人孙康家贫,冬夜映雪读书。"),
      ("回收", "第 2、6 集的旧油纸伞。")],
curve="白(大雪)→ 定(三年后再考)→ 赠(伞上的字)→ 净(扫干净的台阶)→ 等(明天)。",
scenes=[
dict(head="外景 私塾 雪夜", short="私塾 雪夜", era="冬", env="the village school at night in heavy snow, a paper window glowing, snow piled on the eaves, the courtyard white",
     tone="quiet resolve",
script="""
字幕:大雪。鹖鴠不鸣,虎始交,荔挺出。
雪夜。私塾的窗还亮着。许秀才坐在窗边,就着窗外的雪光读书,灯没点。
陈先生推门进来,带进一阵雪。
陈先生:省灯油,学孙康?
许秀才:先生,我想好了。三年后,再考一回。
陈先生看了他一会儿,没说话。他从墙角拿起那把旧油纸伞,在灯下展开,研墨,提笔,在伞面上写了五个字。
陈先生:鹭浦一夜雨。
他把伞合上,递给许秀才。
陈先生:下回去临安,带着它。下雨就撑开,看看家里。
""",
shots=[
 S("1", "大远景,固定", "大雪的鹭浦,屋顶全白,私塾的窗还亮着", "雪落无声;字幕“大雪”与三候", 9,
   "extreme long shot of LU PU VILLAGE under heavy snow at night, white roofs, the stone bridge white, one paper window of the school glowing", "static camera, snow falls", key=True),
 S("2", "中景", "许秀才坐在窗边就着雪光读书,灯没点", "—", 6,
   "medium shot, XU XIUCAI, AGE 20: [锚点], sitting by an open window reading by the pale glow of snow, no lamp lit, breath visible", "static camera, he turns a page"),
 S("3", "双人", "陈先生推门进来带进一阵雪", "陈先生:“省灯油,学孙康?”", 5,
   "two-shot, MR CHEN, AGE 46: [锚点], stepping in with a gust of snow, XU XIUCAI, AGE 20: [锚点], looking up", "static camera, the door opens, snow blows in"),
 S("4", "近景", "许秀才", "许秀才:“先生,我想好了。三年后,再考一回。”", 6,
   "close shot, XU XIUCAI, AGE 20: [锚点], closing the book, steady", "static camera, he says it firmly"),
 S("5", "近景", "陈先生看了他一会儿,没说话", "—", 4,
   "close shot, MR CHEN, AGE 46: [锚点], looking at his student, snow melting on his cap", "static camera, he looks"),
 S("6", "特写", "旧油纸伞在灯下展开,笔在伞面上写字(文字后期合成)", "陈先生:“鹭浦一夜雨。”", 8,
   "close-up, the old patched oil-paper umbrella opened under a lamp, a brush writing a line of five characters on its yellowed paper", "static camera, the brush writes", key=True),
 S("7", "双人", "他把伞合上递给许秀才", "陈先生:“下回去临安,带着它。下雨就撑开,看看家里。”", 7,
   "two-shot, MR CHEN, AGE 46: [锚点], closing the umbrella and handing it to XU XIUCAI, AGE 20: [锚点], who takes it with both hands", "static camera, the umbrella is handed over"),
]),
dict(head="外景 渡口 雪后 晨", short="渡口 雪后", era="冬", env=ENV_FERRY + ", deep snow, the camphor tree white, the river dark and still",
     tone="getting ready",
script="""
雪停了。渡口的台阶被雪埋了。
阿禾拿着一把比她还高的扫帚,一级一级地扫。扫完一级,回头看看河,再扫下一级。
周老篙在船上铲雪,看着她。
周老篙:扫这么干净干什么?
阿禾:爹回来要走。
她扫到最下面一级,站在水边,往下游看。河面上什么也没有。
阿禾(旁白):大雪。台阶扫干净了。明天就是冬至。
""",
shots=[
 S("8", "大远景,固定", "雪停了,渡口的台阶被雪埋了,老樟树一身白", "—", 7,
   "extreme long shot of the ferry landing after heavy snow, the stone steps buried, the camphor tree white, the dark river still", "static camera, a branch drops its snow"),
 S("9", "中景", "阿禾拿着比她还高的扫帚,一级一级地扫", "扫雪声", 7,
   "medium shot, A HE, AGE 8: [锚点], in her new padded jacket, sweeping the snowy steps one by one with a broom taller than she is, glancing at the river after each step", "static camera, she sweeps down step by step"),
 S("10", "双人", "周老篙在船上铲雪,看着她", "周老篙:“扫这么干净干什么?”阿禾:“爹回来要走。”", 6,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], shovelling snow off the FERRY BOAT, A HE, AGE 8: [锚点], on the steps", "static camera, he asks, she answers without stopping"),
 S("11", "近景", "她扫到最下面一级,站在水边往下游看", "—", 5,
   "close shot, A HE, AGE 8: [锚点], at the bottom step by the water, looking downstream, breath steaming", "static camera, she looks"),
 S("12", "大远景,固定", "干干净净的一列台阶,通向空空的河", "阿禾(旁白):“大雪。台阶扫干净了。明天就是冬至。”", 9,
   "extreme long shot, a single swept path of clean stone steps down through the snow to the dark empty river, a small girl at the bottom", "static camera, still", key=True,
   out="hold; end of episode."),
]),
])

EPS["22"] = dict(cn="二十二", jq="冬至", title="团圆",
summary="冬至。阿禾从天亮就坐在渡口等。一条船过去,不是;又一条船过去,不是。天黑了,爷爷叫她回家,她不走,把茶亭的炉子烧得旺旺的。很晚很晚,河上来了一点灯光。船靠岸,一个人跳下来。阿禾冲下扫干净的台阶。“婆婆说要看看你胖了还是瘦了。”“瘦了。”那天夜里,周家门口挂起了灯,一家人吃汤圆。",
info=[("物候", "蚯蚓结,麋角解,水泉动"), ("人物", "阿禾、周大、周老篙、桑娘、石生、陈先生、许秀才、村民"),
      ("风俗", "冬至大如年:江南冬至夜家人团聚,吃汤圆、冬酿酒。"),
      ("回收", "第 1 集“冬至就回来”;第 16 集信里“胖了”;第 15 集王婆“看看他胖了还是瘦了”;第 20 集新腌的菜;第 21 集扫干净的台阶。")],
curve="盼(一条条船)→ 冷(天黑了)→ 执(不走)→ 亮(河上一点灯)→ 圆。",
scenes=[
dict(head="外景 渡口 冬至一日", short="渡口 白天", era="冬", env=ENV_FERRY + ", winter solstice, thin snow on the banks, the swept steps, the tea pavilion stove lit",
     tone="waiting stretched across a day",
script="""
字幕:冬至。蚯蚓结,麋角解,水泉动。
天刚亮,阿禾就坐在渡口最上面一级台阶上,裹着新棉袄。
一条船从下游过来。阿禾站起来。船过去了,不是。
日头到了头顶。又一条船。阿禾站起来。不是。
桑娘送来一碗汤圆,阿禾捧着,没吃,眼睛盯着河。
""",
shots=[
 S("1", "大远景,固定", "冬至清晨,渡口,扫干净的台阶,一个小人坐在最上面", "寒风;字幕“冬至”与三候", 9,
   "extreme long shot at winter-solstice dawn of the ferry landing, the swept steps, a tiny figure sitting at the top, the river empty", "static camera, mist on the water", key=True),
 S("2", "中景,固定", "一条船从下游来,阿禾站起来;船过去了,不是", "橹声", 7,
   "medium shot, A HE, AGE 8: [锚点], standing up on the steps as a cargo boat comes upstream, then slowly sitting back down as it passes by", "static camera, locked-off; she rises and sits"),
 S("3", "中景,固定,同机位", "日头到了头顶,又一条船,站起来,不是", "—", 6,
   "medium shot from the identical position at noon, A HE, AGE 8: [锚点], rising again as another boat passes, then sitting", "static camera, identical framing; she rises and sits"),
 S("4", "中景", "桑娘送来一碗汤圆,阿禾捧着没吃,眼睛盯着河", "—", 6,
   "medium shot, SANG NIANG, AGE 19: [锚点], heavily pregnant, handing a bowl of glutinous rice balls to A HE, AGE 8: [锚点], who holds it without eating, eyes on the river", "static camera, the bowl is handed over"),
]),
dict(head="外景 渡口 冬至夜", short="渡口 夜", era="冬", env=ENV_FERRY + ", night, the tea pavilion stove glowing, a lantern at the landing, stars, the dark river",
     tone="the longest night, then light",
script="""
天黑了。冬至的夜最长。
周老篙提着灯笼走下来。
周老篙:回家吧。明天再等。
阿禾:他说必回。
她跑进茶亭,往炉子里塞炭,把火烧得旺旺的。
很晚很晚。河面上,远远地,出现了一点灯光。越来越近。
一条漕船的小舢板靠了岸。一个人跳下来,背着包袱,站在扫干净的台阶下面。
周大:阿禾。
阿禾从茶亭里冲出来,冲下台阶,一头扎进他怀里。
半天,她抬起头,仔细看他的脸。
阿禾:婆婆说,要看看你胖了还是瘦了。
周大:……瘦了。
阿禾:信上说你胖了。
周大:骗你的。
阿禾哭了。这一年她第一次哭。
""",
shots=[
 S("5", "大远景,固定", "天黑了,渡口一盏灯笼,茶亭的炉火", "风声", 7,
   "extreme long shot at night of the ferry landing, one lantern at the steps, the tea pavilion glowing orange, the river black", "static camera, the lantern sways"),
 S("6", "双人", "周老篙提灯笼走下来", "周老篙:“回家吧。明天再等。”阿禾:“他说必回。”", 6,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], coming down the steps with a lantern, A HE, AGE 8: [锚点], refusing to stand up", "static camera, he speaks, she refuses"),
 S("7", "近景", "她跑进茶亭往炉里塞炭,把火烧得旺旺的", "火声", 5,
   "close shot, A HE, AGE 8: [锚点], stuffing charcoal into the tea pavilion stove, the fire roaring up and lighting her stubborn face", "static camera, the fire flares"),
 S("8", "大远景,固定", "很晚,河面上远远出现一点灯光,越来越近", "橹声由远而近", 9,
   "extreme long shot down the black river at night, a single tiny light appearing far downstream and slowly growing closer", "static camera, the light approaches", key=True),
 S("9", "中景", "小舢板靠岸,一个人背着包袱跳下来,站在扫干净的台阶下", "周大:“阿禾。”", 6,
   "medium shot, a small skiff bumping against the steps, ZHOU DA, AGE 34: [锚点], thinner, a bundle on his back, jumping onto the bottom swept step and looking up", "static camera, he jumps ashore and calls"),
 S("10", "全景", "阿禾从茶亭冲出来,冲下台阶,一头扎进他怀里", "脚步声", 6,
   "wide shot, A HE, AGE 8: [锚点], bursting out of the tea pavilion and running down the swept steps into her father's arms, the lantern swinging", "static camera, she runs and collides into him", key=True),
 S("11", "近景", "她抬起头仔细看他的脸", "阿禾:“婆婆说,要看看你胖了还是瘦了。”", 6,
   "close shot, A HE, AGE 8: [锚点], pulling back to study her father's face in the lantern light", "static camera, she studies him"),
 S("12", "近景", "周大", "周大:“……瘦了。”阿禾:“信上说你胖了。”周大:“骗你的。”", 7,
   "close shot, ZHOU DA, AGE 34: [锚点], gaunt and weathered, smiling awkwardly", "static camera, he answers"),
 S("13", "近景,极缓推", "阿禾哭了,这一年第一次哭", "哭声", 6,
   "close shot, A HE, AGE 8: [锚点], her face crumpling, crying for the first time, clutching his jacket", "extremely slow push in, she cries", key=True),
]),
dict(head="内景 周家 冬至夜", short="周家 夜", era="冬", env="the ferryman's small house at night, a lantern hung at the door, a low table with bowls of rice balls and pickled greens, the old door frame with notches",
     tone="reunion",
script="""
周家门口挂起了灯。屋里,三个人围着矮桌,吃汤圆,吃新开缸的腌菜。桑娘、石生、陈先生、许秀才挤在门口,端着碗。
周大把怀里的东西掏出来,放在桌上:一小块干硬的泥,上面还有一点红漆。是立春那天的泥牛角。
周大:没舍得撒。
阿禾拿起来,攥在手心里。
阿禾(旁白):冬至。爹回来了。我不数了。
""",
shots=[
 S("14", "全景", "周家门口挂起灯,屋里三人围桌吃汤圆,门口挤着邻居", "说笑", 7,
   "wide shot of the ferryman's house at night, a lantern at the door, ZHOU DA, AGE 34: [锚点], A HE, AGE 8: [锚点], and ZHOU THE FERRYMAN, AGE 68: [锚点], around a low table with bowls, SANG NIANG, SHI SHENG, MR CHEN and XU XIUCAI crowding in the doorway with bowls", "static camera, everyone eats and laughs"),
 S("15", "特写", "周大掏出一小块干硬的泥,上面一点红漆——立春的泥牛角", "周大:“没舍得撒。”", 6,
   "close-up, a big calloused hand setting a small dry chip of clay with a trace of red paint on the table between the bowls", "static camera, the clay chip is set down", key=True),
 S("16", "近景", "阿禾拿起来,攥在手心里", "—", 5,
   "close shot, A HE, AGE 8: [锚点], picking up the clay chip and closing her fist around it, eyes still wet, smiling", "static camera, she holds it tight"),
 S("17", "大远景,固定", "冬至夜的村子,一家门口挂着灯", "阿禾(旁白):“冬至。爹回来了。我不数了。”", 9,
   "extreme long shot of the snowy village on the longest night, one lantern hanging at a doorway by the river, warm light inside, stars above", "static camera, still", key=True,
   out="hold; end of episode."),
]),
])

EPS["23"] = dict(cn="二十三", jq="小寒", title="消寒图",
summary="小寒,数九。陈先生给阿禾画了一张九九消寒图:一枝梅花,八十一个花瓣,一天涂一瓣,涂满了,春天就到了。阿禾问爹:涂满了你还走吗?周大说不走了,开春跟石生学造船。阿禾不信,要他写下来。周大不会写字,就在消寒图的角上按了一个手印。",
info=[("物候", "雁北乡,鹊始巢,雉始雊"), ("人物", "阿禾、周大、陈先生、石生、周老篙"),
      ("风俗", "九九消寒图:冬至起画素梅一枝,八十一瓣,日染一瓣,瓣尽而九九出,则春深矣。"),
      ("回收", "石生的手艺(第 13 集摇篮);阿禾每集数日子的习惯,换成了涂梅花。")],
curve="新(消寒图)→ 怕(还走吗)→ 诺(不走了)→ 定(一个手印)。",
scenes=[
dict(head="内景 私塾 午", short="私塾 午", era="冬", env="the village schoolroom in winter, a brazier, a sheet of paper on the desk with an ink outline of a plum branch",
     tone="playful gift",
script="""
字幕:小寒。雁北乡,鹊始巢,雉始雊。
私塾里生着火盆。陈先生在一张纸上画了一枝梅,一笔一笔,画出八十一个空心的花瓣。
陈先生:九九消寒图。从冬至起,一天涂一瓣。八十一瓣涂满,春天就来了。
他把图递给阿禾,又递给她一小碟胭脂。
阿禾:先生,你不是说我不数了吗?
陈先生:这不是数。这是画。
""",
shots=[
 S("1", "大远景,固定", "小寒的村子,河边结了薄冰,喜鹊在老樟树上筑巢", "鹊叫;字幕“小寒”与三候", 8,
   "extreme long shot of the village in deep winter, thin ice along the river edges, magpies building a nest in the bare upper branches of the camphor tree", "static camera, a magpie flies in with a twig", key=True),
 S("2", "特写", "笔在纸上画出一枝梅,八十一个空心花瓣", "—", 7,
   "close-up, a brush drawing a single plum branch in ink on paper, adding small empty circular petals one after another", "static camera, petals appear one by one", key=True),
 S("3", "近景", "陈先生", "陈先生:“九九消寒图。从冬至起,一天涂一瓣。八十一瓣涂满,春天就来了。”", 8,
   "close shot, MR CHEN, AGE 46: [锚点], by the brazier, holding up the drawing", "static camera, he explains"),
 S("4", "双人", "他递给阿禾图和一碟胭脂", "阿禾:“先生,你不是说我不数了吗?”陈先生:“这不是数。这是画。”", 7,
   "two-shot, MR CHEN, AGE 46: [锚点], handing the drawing and a small dish of rouge to A HE, AGE 8: [锚点]", "static camera, she takes them and asks"),
]),
dict(head="内景 周家 夜", short="周家 夜", era="冬", env="the ferryman's house at night, the plum drawing pinned to the wall beside the door frame with the height notches, a lamp",
     tone="a promise made without writing",
script="""
夜里。消寒图钉在门框旁边的墙上,已经涂红了三瓣。
阿禾用手指蘸胭脂,涂第四瓣。
阿禾:爹,八十一瓣涂满了,你还走吗?
周大在补渔网,手停了。
周大:不走了。开春,跟石生学造船。
阿禾:你写下来。
周大:我不会写字。
阿禾把胭脂碟推过去。
周大看了看,把大拇指在胭脂里按了按,在消寒图的角上按了一个红手印。
阿禾(旁白):小寒。爹按了一个手印。还有七十七瓣。
""",
shots=[
 S("5", "特写", "门框旁墙上的消寒图,已涂红三瓣;小手指蘸胭脂涂第四瓣", "—", 6,
   "close-up, the plum-branch drawing pinned beside the notched door frame, three petals coloured red, a small fingertip dipped in rouge filling in the fourth", "static camera, the fourth petal turns red", key=True),
 S("6", "双人", "阿禾问;周大补渔网,手停了", "阿禾:“爹,八十一瓣涂满了,你还走吗?”", 6,
   "two-shot by lamp light, A HE, AGE 8: [锚点], at the wall, ZHOU DA, AGE 34: [锚点], mending a net, his hands stopping", "static camera, his hands stop"),
 S("7", "近景", "周大", "周大:“不走了。开春,跟石生学造船。”", 5,
   "close shot, ZHOU DA, AGE 34: [锚点], looking up from the net at his daughter", "static camera, he says it"),
 S("8", "双人", "阿禾不信", "阿禾:“你写下来。”周大:“我不会写字。”", 5,
   "two-shot, A HE, AGE 8: [锚点], arms folded, ZHOU DA, AGE 34: [锚点], embarrassed", "static camera, she demands, he admits"),
 S("9", "特写", "大拇指在胭脂里按一按,在消寒图角上按了一个红手印", "—", 7,
   "close-up, a big rough thumb pressed into a dish of rouge and then firmly onto the corner of the plum drawing, leaving a red thumbprint", "static camera, the thumb presses and lifts", key=True),
 S("10", "大远景,固定", "夜里的周家,窗里一盏灯", "阿禾(旁白):“小寒。爹按了一个手印。还有七十七瓣。”", 8,
   "extreme long shot of the ferryman's house at night by the frozen river, one lit window, magpie nest dark in the camphor tree", "static camera, still", key=True,
   out="hold; end of episode."),
]),
])

EPS["24"] = dict(cn="二十四", jq="大寒", title="新生",
summary="大寒,一年最冷的一夜。桑娘要生了,稳婆住在河对岸。河上结了冰碴,周老篙和周大一个撑篙一个破冰,把稳婆接过河。天快亮的时候,孩子哭了。石生抱着孩子放进立秋做的樟木摇篮。大家让阿禾给孩子起个小名。阿禾说:叫阿春吧,过几天就立春了。她回家,在消寒图上涂了一瓣。",
info=[("物候", "鸡始乳,征鸟厉疾,水泽腹坚"), ("人物", "桑娘、石生、阿禾、周老篙、周大、稳婆、陈先生、许秀才"),
      ("回收", "小满有孕(第 8 集);立秋的樟木摇篮(第 13 集);小寒的消寒图(第 23 集);第 1 集第一个镜头的机位。"),
      ("结尾", "二十四集首尾相接:最后一个镜头与第 1 集第 1 镜同机位,大寒之后又是立春。")],
curve="冷(最冷的一夜)→ 急(过河接稳婆)→ 熬(等)→ 亮(啼哭)→ 名(阿春)→ 续(又一瓣)。",
scenes=[
dict(head="外景 渡口 大寒夜", short="渡口 夜", era="冬", env=ENV_FERRY + ", the coldest night, ice crusting the river edges and floating in slabs, snow, two lanterns",
     tone="urgent and cold",
script="""
字幕:大寒。鸡始乳,征鸟厉疾,水泽腹坚。
半夜。石生提着灯笼,一路跑到渡口,拍周家的门。
石生:周伯!桑娘要生了!稳婆在对岸!
周老篙披上衣服就出来了。周大跟在后面。
河上结了冰碴,一块一块地浮着。周老篙撑篙,周大拿着一根木杠站在船头,一下一下砸开前面的冰。
船慢慢地往对岸挤。
""",
shots=[
 S("1", "大远景,固定", "大寒夜,河上浮着冰,渡口两盏灯", "冰碴碰撞声;字幕“大寒”与三候", 8,
   "extreme long shot on the coldest night, the river crusted with ice and floating slabs, snow on the banks, two lanterns at the ferry landing", "static camera, ice slabs drift and knock", key=True),
 S("2", "中景", "石生提灯笼一路跑来,拍周家的门", "石生:“周伯!桑娘要生了!稳婆在对岸!”", 6,
   "medium shot, SHI SHENG, AGE 22: [锚点], running through the snow with a lantern and pounding on the ferryman's door", "static camera, he pounds and shouts"),
 S("3", "中景", "周老篙披上衣服出来,周大跟在后面", "—", 4,
   "medium shot, ZHOU THE FERRYMAN, AGE 68: [锚点], throwing on a padded jacket and coming out, ZHOU DA, AGE 34: [锚点], right behind him", "static camera, they come out"),
 S("4", "中景", "周大站在船头用木杠砸冰,周老篙撑篙", "砸冰声", 7,
   "medium shot of the FERRY BOAT pushing into the icy river at night, ZHOU DA, AGE 34: [锚点], standing in the bow smashing the ice ahead with a wooden pole, ZHOU THE FERRYMAN, AGE 68: [锚点], poling hard in the stern, lantern light", "camera moves with the boat as it forces through", key=True),
 S("5", "大远景,固定", "船在冰碴里慢慢往对岸挤", "—", 6,
   "extreme long shot, a tiny lantern-lit boat pushing slowly through broken ice toward the far bank in the dark", "static camera, the boat inches across"),
]),
dict(head="内景 石生家 大寒夜到黎明", short="石生家 夜到黎明", era="冬", env="the carpenter's house at night, a closed inner door with lamp light under it, the camphor-wood cradle hanging from the beam, a brazier",
     tone="waiting, then dawn",
script="""
石生家。稳婆进了里屋,门关上了。
外屋,石生走来走去。陈先生和许秀才坐着,谁也不说话。阿禾靠在爹的怀里,盯着那只空摇篮。
窗纸慢慢发白。
里屋传出一声啼哭。
所有人都站了起来。
门开了。稳婆抱出一个小小的襁褓,交到石生手里。石生抱着,手在抖。
他把孩子放进樟木摇篮。摇篮轻轻晃。
石生:先生,起个名字吧。
陈先生摆摆手,看向阿禾。
陈先生:让阿禾起。
阿禾凑到摇篮边看了很久。
阿禾:叫阿春吧。过几天,就立春了。
""",
shots=[
 S("6", "全景", "稳婆进了里屋,门关上;外屋石生走来走去,大家坐着不说话,阿禾靠在爹怀里盯着空摇篮", "—", 8,
   "wide shot of the carpenter's outer room at night, a closed inner door with lamp light beneath it, SHI SHENG, AGE 22: [锚点], pacing, MR CHEN, AGE 46: [锚点], and XU XIUCAI, AGE 20: [锚点], seated silent, A HE, AGE 8: [锚点], leaning against ZHOU DA, AGE 34: [锚点], staring at the empty cradle", "static camera, the man paces"),
 S("7", "中景,固定", "窗纸慢慢发白", "—", 6,
   "medium shot of a paper window slowly turning from black to pale blue-white with dawn", "static camera, the window brightens"),
 S("8", "特写", "空摇篮;里屋传出一声啼哭", "婴儿啼哭", 4,
   "close-up of the empty camphor-wood cradle hanging still, at the sound of a cry it trembles very slightly", "static camera, the cradle trembles", key=True),
 S("9", "全景", "所有人都站了起来", "—", 4,
   "wide shot, everyone in the outer room rising to their feet at once", "static camera, they stand"),
 S("10", "中景", "门开了,稳婆抱出襁褓交给石生,石生的手在抖", "—", 6,
   "medium shot, the inner door opening, a midwife handing a tiny swaddled baby to SHI SHENG, AGE 22: [锚点], whose hands shake", "static camera, the baby passes into his hands"),
 S("11", "特写", "孩子放进樟木摇篮,摇篮轻轻晃", "吱呀", 6,
   "close-up, a tiny swaddled baby laid into the pale camphor-wood cradle, the cradle swinging gently", "static camera, the cradle sways", key=True),
 S("12", "双人", "石生请陈先生起名,陈先生看向阿禾", "石生:“先生,起个名字吧。”陈先生:“让阿禾起。”", 6,
   "two-shot, SHI SHENG, AGE 22: [锚点], turning to MR CHEN, AGE 46: [锚点], who waves his hand and nods toward the girl", "static camera, he defers to her"),
 S("13", "近景,极缓推", "阿禾凑到摇篮边看了很久", "阿禾:“叫阿春吧。过几天,就立春了。”", 8,
   "close shot, A HE, AGE 8: [锚点], leaning over the cradle looking at the baby in the dawn light, the silver pin in her hair", "extremely slow push in, she looks, then speaks", key=True),
]),
dict(head="内景 周家 / 外景 鹭浦 黎明", short="周家 · 鹭浦 黎明", era="冬", env="the ferryman's house at dawn with the plum drawing on the wall, then LU PU VILLAGE seen from the same position as the very first shot of the series",
     tone="the circle closes",
script="""
黎明。阿禾回到家,蘸了胭脂,在消寒图上涂了一瓣。墙角那个红手印还在。
门框上的刻痕,门外的河,河上的冰开始化了。
阿禾(旁白):大寒。阿春出来了。再过几天,又是立春。
""",
shots=[
 S("14", "特写", "阿禾蘸胭脂,在消寒图上涂了一瓣;墙角的红手印还在", "—", 6,
   "close-up, a small finger with rouge filling one more petal on the plum drawing, the red thumbprint in the corner, the notched door frame beside it", "static camera, the petal turns red"),
 S("15", "大远景,固定", "与第 1 集第 1 镜同机位:黎明的鹭浦,河冰在化,老樟树上喜鹊窝", "阿禾(旁白):“大寒。阿春出来了。再过几天,又是立春。”", 12,
   "extreme long shot at dawn of LU PU VILLAGE from exactly the same position as the first shot of the series, white walls and dark roofs, the stone bridge, the camphor tree with a magpie nest, the river ice starting to melt, thin mist", "static camera, the mist drifts as on the first morning", key=True,
   out="hold until the mist thins; fade out; end of the series."),
]),
])
