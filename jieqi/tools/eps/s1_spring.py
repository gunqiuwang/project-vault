ENV_FERRY = "LU PU VILLAGE ferry landing under the enormous old camphor tree, the stone steps, the FERRY BOAT, the thatched tea pavilion, the slow green river"

EPS = {}

EPS["01"] = dict(cn="一", jq="立春", title="春牛",
summary="一年从立春开始。村里打春牛,孩子们抢泥牛的碎块;阿禾的爹周大要跟漕船去临安,一走就是一年。阿禾不哭,揣着一块春牛的泥,沿着河岸追船。爷爷周老篙告诉她:冬至就回来。全剧二十四集由此开始数日子。",
info=[("物候", "东风解冻,蛰虫始振,鱼陟负冰"), ("人物", "阿禾、周老篙、周大、陈先生、村民"),
      ("风俗", "鞭春牛:立春日用彩鞭打泥塑春牛,打碎后众人抢碎土,带回家撒在田里求丰年。"),
      ("贯穿线", "周大跟漕船出门,冬至(第 22 集)回来。阿禾每集结尾数一次日子。")],
curve="热闹(打春牛)→ 别(漕船)→ 倔(不哭,追船)→ 定(冬至就回来)。",
scenes=[
dict(head="外景 祠堂前空地 晨", short="祠堂前 晨", era="春", env="the open ground before the village ancestral hall, a clay spring ox painted red and green on a wooden frame, villagers gathered, thin morning mist",
     tone="festive and noisy, cold air", crowd="thirty villagers and children",
script="""
字幕:淳熙十二年 立春。东风解冻,蛰虫始振,鱼陟负冰。
祠堂前,一头泥塑的春牛立在木架上,涂得红红绿绿。全村的人围着。
陈先生拿着一根缠了彩纸的鞭子,清了清嗓子。
陈先生:一打风调雨顺!
他抽了一鞭。泥牛掉下一块。
陈先生:二打五谷丰登!
孩子们挤在最前面,阿禾挤得最凶。
陈先生:三打——
泥牛碎了。孩子们一拥而上抢碎块。阿禾抢到一块牛角,攥在手里,回头找人。
她爹周大站在人群外面,肩上已经背好了包袱。
""",
shots=[
 S("1", "大远景,固定", "薄雾里的鹭浦村:白墙黑瓦、石拱桥、渡口老樟树", "鸡鸣、远处锣鼓;字幕“淳熙十二年 立春”与三候", 9,
   "extreme long shot at dawn of LU PU VILLAGE in thin mist, whitewashed walls and dark roofs along the river, the hump-backed stone bridge, the old camphor tree at the ferry", "static camera, mist drifts slowly, smoke rises from a few chimneys", key=True),
 S("2", "全景", "祠堂前,彩绘泥牛立在木架上,全村围着", "人声", 6,
   "wide shot of the open ground before the ancestral hall, a clay spring ox painted red and green on a wooden frame, VILLAGERS crowding around, children in front", "static camera, the crowd jostles"),
 S("3", "中景", "陈先生举彩鞭,抽第一鞭", "陈先生:“一打风调雨顺!”", 5,
   "medium shot, MR CHEN, AGE 46: [锚点], raising a whip wrapped in coloured paper and striking the clay ox, a chunk falling", "static camera, he strikes once"),
 S("4", "中景", "第二鞭;孩子们挤在最前面,阿禾挤得最凶", "陈先生:“二打五谷丰登!”", 5,
   "medium shot, children pushing at the front of the crowd, A HE, AGE 8: [锚点], squeezing to the very front with fierce concentration", "static camera, she elbows forward"),
 S("5", "特写", "第三鞭,泥牛碎裂", "陈先生:“三打——”碎裂声、欢呼", 4,
   "close-up, the painted clay ox cracking apart under a paper-wrapped whip, pieces falling", "static camera, the ox breaks apart", key=True),
 S("6", "中景", "孩子们一拥而上抢碎块,阿禾抢到一块牛角", "欢叫", 6,
   "medium shot, children diving for the clay pieces, A HE, AGE 8: [锚点], coming up with a painted clay ox horn held high", "static camera, she rises with the horn"),
 S("7", "近景", "阿禾攥着牛角回头找人", "—", 4,
   "close shot, A HE, AGE 8: [锚点], clutching the clay horn, turning to search the crowd", "static camera, she turns and searches"),
 S("8", "中景", "人群外,周大肩上已背好包袱", "—", 5,
   "medium shot, ZHOU DA, AGE 34: [锚点], standing apart from the crowd with a cloth bundle tied on his back, watching his daughter", "static camera, he stands and watches"),
]),
dict(head="外景 渡口 晨", short="渡口 晨", era="春", env=ENV_FERRY + ", a long grain barge waiting midstream",
     tone="a goodbye neither of them is good at",
script="""
渡口。一条长长的漕船停在河心。
周大蹲下来,和阿禾一样高。
周大:在家听爷爷的话。
阿禾不说话,把手里那块泥牛角塞进爹的手里。
阿禾:撒在船上。船也要丰年。
周大笑了,把泥块揣进怀里。周老篙撑着渡船,送他到漕船边。
""",
shots=[
 S("9", "全景", "渡口,一条长长的漕船停在河心", "水声", 6,
   "wide shot of the ferry landing in morning light, a long grain barge waiting in midstream, ZHOU THE FERRYMAN, AGE 68: [锚点], holding the FERRY BOAT at the steps", "static camera, the barge rocks gently"),
 S("10", "双人", "周大蹲下来,和阿禾一样高", "周大:“在家听爷爷的话。”", 5,
   "two-shot on the stone steps, ZHOU DA, AGE 34: [锚点], crouching to his daughter's height, A HE, AGE 8: [锚点], silent, lips pressed tight", "static camera, he crouches and speaks"),
 S("11", "特写", "阿禾把泥牛角塞进爹手里", "阿禾:“撒在船上。船也要丰年。”", 6,
   "close-up, a child's small hand pressing a painted clay ox horn into a big calloused palm", "static camera, she presses it in"),
 S("12", "近景", "周大笑了,把泥块揣进怀里", "—", 4,
   "close shot, ZHOU DA, AGE 34: [锚点], laughing softly and tucking the clay piece inside his jacket", "static camera, he tucks it away"),
 S("13", "远景", "周老篙撑渡船,送周大到漕船边", "撑篙声", 7,
   "long shot, the small FERRY BOAT crossing to the grain barge, ZHOU THE FERRYMAN, AGE 68: [锚点], poling, ZHOU DA, AGE 34: [锚点], standing in the bow", "static camera, the ferry slides across"),
]),
dict(head="外景 河岸 晨", short="河岸 晨", era="春", env="the river bank path beside LU PU VILLAGE, bare willows with the first green, mulberry fields, the grain barge moving downstream",
     tone="a child running against a whole year",
script="""
漕船起锚,顺流往东。
阿禾沿着河岸跑。跑过石拱桥,跑过桑园,跑过最后一户人家。路到头了。
她站住。船越来越小。
周老篙撑着空渡船回来,停在她身边的岸下。
周老篙:冬至就回来。
阿禾:冬至是哪天?
周老篙:从今天数,二十二个节气。
阿禾伸出手指头数了数,不够。
阿禾(旁白):立春。爹走了。还有二十一个节气。
""",
shots=[
 S("14", "大远景,固定", "漕船起锚,顺流往东(画左)", "号子声", 7,
   "extreme long shot, the long grain barge raising its sail and drifting downstream toward frame left, the village on the right, morning mist", "static camera, the barge moves left"),
 S("15", "中景,跟", "阿禾沿着河岸跑,跑过石拱桥", "脚步、喘气", 6,
   "medium tracking shot, A HE, AGE 8: [锚点], running along the river bank path and over the hump-backed stone bridge", "camera tracks with her as she runs"),
 S("16", "全景", "跑过桑园,跑过最后一户人家,路到头了", "—", 6,
   "wide shot, a small girl running past bare mulberry fields and the last house to where the bank path ends in reeds", "static camera, she runs in and stops"),
 S("17", "近景", "她站住,看着船越来越小", "风声", 5,
   "close shot, A HE, AGE 8: [锚点], standing at the end of the path, breathing hard, eyes fixed downstream, not crying", "static camera, she stares"),
 S("18", "大远景,固定", "船变成一个小点", "—", 5,
   "extreme long shot down the river, the grain barge now a tiny dark shape in the mist", "static camera, the shape fades"),
 S("19", "中景", "周老篙撑空渡船停在她身边的岸下", "周老篙:“冬至就回来。”", 5,
   "medium shot, ZHOU THE FERRYMAN, AGE 68: [锚点], drifting the empty FERRY BOAT to the bank below the girl, leaning on his pole", "static camera, the boat drifts in"),
 S("20", "双人", "阿禾问", "阿禾:“冬至是哪天?”周老篙:“从今天数,二十二个节气。”", 6,
   "two-shot, A HE, AGE 8: [锚点], on the bank looking down at ZHOU THE FERRYMAN, AGE 68: [锚点], in the boat", "static camera, she asks, he answers"),
 S("21", "特写", "阿禾伸出手指头数,不够", "—", 5,
   "close-up, a child's two hands counting on all ten fingers, then starting again", "static camera, the fingers count and run out"),
 S("22", "大远景,固定", "河岸尽头,一老一小,一条空船", "阿禾(旁白):“立春。爹走了。还有二十一个节气。”", 8,
   "extreme long shot, a small girl on the bank and an old man in a boat at the end of the river path, the misty river running east", "static camera, still", key=True,
   out="hold the image, mist drifts; end of episode."),
]),
])

EPS["02"] = dict(cn="二", jq="雨水", title="伞",
summary="许秀才要去临安赴春闱。下了一整天的雨,陈先生追到渡口,把一把旧油纸伞塞给他。这把伞跟着陈先生考过三次,一次也没中。“伞是好伞,只是我不中用。”",
info=[("物候", "獭祭鱼,候雁北,草木萌动"), ("人物", "许秀才、陈先生、阿禾、周老篙"),
      ("背景", "南宋省试(春闱)在临安举行,时间在早春二月前后。"),
      ("贯穿线", "许秀才谷雨落第回村(第 6 集);陈先生大雪时为他题字(第 21 集)。")],
curve="湿(一天的雨)→ 急(追到渡口)→ 自嘲(三次不中)→ 托付(伞)。",
scenes=[
dict(head="外景 村巷 雨 午后", short="村巷 雨", era="春", env="a narrow wet stone lane of LU PU VILLAGE between whitewashed walls, rain, green moss, water dripping from tiled eaves",
     tone="soft rain, quiet hurry",
script="""
字幕:雨水。獭祭鱼,候雁北,草木萌动。
雨下了一整天。许秀才背着书箱,戴着斗笠,从巷子里走出来。邻居们站在门口送他。
私塾里,陈先生正在教孩子念书,听见外面的声音,停住了。
他放下书,走到墙角,拿起一把旧油纸伞。伞面补过两处。
""",
shots=[
 S("1", "大远景,固定", "雨中的鹭浦,河面满是雨点", "雨声;字幕“雨水”与三候", 8,
   "extreme long shot of LU PU VILLAGE in steady spring rain, the river surface pocked with raindrops, the stone bridge grey, willows faintly green", "static camera, rain falls", key=True),
 S("2", "中景", "许秀才背书箱戴斗笠从巷子走出,邻居在门口送", "雨声、人声", 7,
   "medium shot, XU XIUCAI, AGE 20: [锚点], walking down the wet stone lane with a book box on his back and a straw rain hat, VILLAGERS at their doors waving", "static camera, he walks toward camera"),
 S("3", "全景", "私塾里,陈先生教孩子念书,听见外面停住", "童声念书,停", 6,
   "wide shot of a small village schoolroom, children at low desks, MR CHEN, AGE 46: [锚点], holding a book, stopping mid-line to listen to the lane", "static camera, the reading stops"),
 S("4", "特写", "墙角一把旧油纸伞,补过两处", "—", 5,
   "close-up, an old oil-paper umbrella leaning in a corner, its yellowed paper patched in two places", "static camera, a hand reaches in and takes it", key=True),
]),
dict(head="外景 渡口 雨 傍晚", short="渡口 雨", era="春", env=ENV_FERRY + ", rain, the river grey and dimpled",
     tone="a teacher pretending not to care",
script="""
渡口。周老篙撑着渡船等在台阶下。阿禾坐在船头,头上顶着一片荷叶。
许秀才刚要上船,身后有人喊。
陈先生:等一等!
陈先生一路小跑过来,身上湿透了,手里的伞却是合着的。
他把伞塞给许秀才。
许秀才:先生,这是您的伞。
陈先生:这把伞跟我去过三次临安。
陈先生:伞是好伞,只是我不中用。
许秀才看着他。
陈先生:去吧。考不考得中,都回来。鹭浦的雨,还等你回来听。
许秀才撑开伞,上了船。阿禾挪到一边,给他让地方。
渡船离岸。陈先生站在雨里,没有伞。
阿禾回头看他,把头上的荷叶举了起来,冲他晃了晃。
阿禾(旁白):雨水。许哥哥去考状元了。还有二十个节气。
""",
shots=[
 S("5", "全景", "渡船等在台阶下,阿禾坐在船头,头顶荷叶", "雨打荷叶", 6,
   "wide shot of the ferry landing in rain, ZHOU THE FERRYMAN, AGE 68: [锚点], waiting at the stone steps with the FERRY BOAT, A HE, AGE 8: [锚点], sitting in the bow holding a big dried lotus leaf over her head", "static camera, rain drums on the leaf"),
 S("6", "中景", "许秀才刚要上船,身后有人喊", "陈先生(画外):“等一等!”", 4,
   "medium shot, XU XIUCAI, AGE 20: [锚点], one foot on the boat, turning back at a shout", "static camera, he turns"),
 S("7", "全景", "陈先生一路小跑过来,浑身湿透,伞却合着", "脚步溅水", 6,
   "wide shot, MR CHEN, AGE 46: [锚点], hurrying down the wet path to the landing, soaked through, a closed old umbrella in his hand", "static camera, he runs in"),
 S("8", "双人", "他把伞塞给许秀才", "许秀才:“先生,这是您的伞。”", 5,
   "two-shot on the steps, MR CHEN, AGE 46: [锚点], pushing the patched umbrella into the hands of XU XIUCAI, AGE 20: [锚点]", "static camera, the umbrella changes hands"),
 S("9", "近景", "陈先生", "陈先生:“这把伞跟我去过三次临安。伞是好伞,只是我不中用。”", 8,
   "close shot, MR CHEN, AGE 46: [锚点], rain running down his face, a small crooked smile", "extremely slow push in, he says it lightly", key=True),
 S("10", "近景", "许秀才看着他", "—", 3,
   "close shot, XU XIUCAI, AGE 20: [锚点], holding the umbrella, looking at his teacher", "static camera, he looks"),
 S("11", "近景", "陈先生", "陈先生:“去吧。考不考得中,都回来。鹭浦的雨,还等你回来听。”", 8,
   "close shot, MR CHEN, AGE 46: [锚点], waving him toward the boat", "static camera, he speaks and waves"),
 S("12", "中景", "许秀才撑开伞上船,阿禾挪到一边让地方", "撑伞声", 5,
   "medium shot, XU XIUCAI, AGE 20: [锚点], opening the yellow patched umbrella and stepping into the boat, A HE, AGE 8: [锚点], shifting aside", "static camera, the umbrella blooms open"),
 S("13", "远景", "渡船离岸,陈先生站在雨里,没有伞", "雨声", 7,
   "long shot, the FERRY BOAT pulling away into the grey river with one yellow umbrella in it, MR CHEN, AGE 46: [锚点], left standing on the steps in the rain", "static camera, the boat pulls away"),
 S("14", "近景", "阿禾回头,把荷叶举起来冲他晃了晃", "—", 4,
   "close shot, A HE, AGE 8: [锚点], in the moving boat, turning back and waving her lotus leaf high", "static camera, she waves the leaf"),
 S("15", "大远景,固定", "雨里的河,一把黄伞越来越远,岸上一个湿透的人", "阿禾(旁白):“雨水。许哥哥去考状元了。还有二十个节气。”", 8,
   "extreme long shot of the rainy river, a small yellow umbrella moving away on the water, a soaked figure on the stone steps under the camphor tree", "static camera, rain falls", key=True,
   out="hold the image in the rain; end of episode."),
]),
])

EPS["03"] = dict(cn="三", jq="惊蛰", title="春雷",
summary="桑娘和石生成亲。拜堂拜到一半,天上响了今年第一声雷。老人们说惊蛰的雷是好兆头,虫醒了,桑叶要发了。新娘子在红盖头底下笑出了声。",
info=[("物候", "桃始华,仓庚鸣,鹰化为鸠"), ("人物", "桑娘、石生、王婆、阿禾、周老篙、陈先生、村民"),
      ("风俗", "惊蛰春雷,民间以为“春雷响,万物长”;蚕农盼桑叶早发。"),
      ("贯穿线", "桑娘小满时有孕(第 8 集),大寒生产(第 24 集)。")],
curve="喜(迎亲船)→ 紧(拜堂)→ 惊(第一声雷)→ 笑(盖头下的笑)→ 甜(桃花)。",
scenes=[
dict(head="外景 河道 午", short="河道 午", era="春", env="the green river of LU PU VILLAGE with peach trees in first bloom on the banks, a small wedding boat hung with red cloth",
     tone="bright, shy, cheerful", crowd="villagers on the bank and children running",
script="""
字幕:惊蛰。桃始华,仓庚鸣,鹰化为鸠。
河边的桃树开了第一批花。一条挂着红布的小船慢慢划过来,船头坐着穿红衣、蒙着盖头的新娘。
撑船的是周老篙。阿禾站在船尾,手里抱着一只装满花生红枣的篮子,一路往岸上撒。
岸上的孩子们追着船抢。
""",
shots=[
 S("1", "大远景,固定", "河边桃树开了第一批花,一条挂红布的小船划来", "唢呐;字幕“惊蛰”与三候", 9,
   "extreme long shot of the green river with peach trees in first pink bloom on the banks, a small boat hung with red cloth gliding toward the village", "static camera, the red boat glides in", key=True),
 S("2", "中景", "船头坐着红衣盖头的新娘,周老篙撑船", "唢呐", 6,
   "medium shot, SANG NIANG, AGE 19: [锚点], in a red wedding jacket with a red veil over her head sitting in the bow, ZHOU THE FERRYMAN, AGE 68: [锚点], poling in a clean jacket", "camera drifts alongside the boat"),
 S("3", "中景", "阿禾站在船尾往岸上撒花生红枣", "孩子们的叫声", 5,
   "medium shot, A HE, AGE 8: [锚点], standing in the stern throwing handfuls of peanuts and red dates from a basket toward the bank", "static camera, she throws handful after handful"),
 S("4", "全景", "岸上的孩子们追着船抢", "笑闹", 5,
   "wide shot, village children running along the bank under peach blossoms scrambling for the peanuts and dates", "static camera, the children run past"),
]),
dict(head="内景 石生家堂屋 午", short="堂屋 午", era="春", env="a modest tiled village hall with red paper on the doors, a small altar table with candles, guests packed along the walls, the open door showing a darkening sky",
     tone="solemn ceremony, then a burst of laughter", crowd="twenty wedding guests",
script="""
堂屋里挤满了人。王婆坐在上首,当证婚的长辈。陈先生扯着嗓子唱礼。
陈先生:一拜天地——
新郎新娘对着门外跪下去。门外的天,忽然暗了。
陈先生:二拜——
“轰隆——”
今年第一声春雷。满屋子人都愣住了。
新娘子在盖头底下笑出了声。
王婆一拍大腿。
王婆:好!惊蛰雷,一声响,虫醒了,桑也要发了!这是天也来喝喜酒!
满屋大笑。石生红着脸,伸手去扶新娘,扶了两次才扶起来。
""",
shots=[
 S("5", "全景", "挤满人的堂屋,王婆坐上首,陈先生唱礼", "陈先生:“一拜天地——”", 7,
   "wide shot of the crowded village hall, GRANNY WANG, AGE 80: [锚点], seated in the place of honour, MR CHEN, AGE 46: [锚点], calling the rites, SHI SHENG, AGE 22: [锚点], and SANG NIANG, AGE 19: [锚点], kneeling toward the open door", "static camera, the couple kneels"),
 S("6", "全景,门框构图", "门外的天忽然暗了", "风起", 4,
   "wide shot through the open door from inside, the sky over the village suddenly darkening with heavy spring cloud", "static camera, the light drops"),
 S("7", "近景", "陈先生", "陈先生:“二拜——”", 3,
   "close shot, MR CHEN, AGE 46: [锚点], drawing breath to call the second bow", "static camera, he calls"),
 S("8", "大远景,固定", "村子上空一道闪,第一声春雷", "“轰隆——”", 4,
   "extreme long shot of the village roofs under dark cloud, a flash lighting the sky", "static camera, the sky flashes", key=True),
 S("9", "全景", "满屋子人都愣住了", "—", 4,
   "wide shot, every guest in the hall frozen and looking up at the roof", "static camera, everyone freezes"),
 S("10", "特写", "红盖头底下,新娘子笑出了声,盖头在抖", "笑声", 4,
   "close-up, a red wedding veil trembling as the bride beneath it laughs", "static camera, the veil shakes with laughter"),
 S("11", "近景", "王婆一拍大腿", "王婆:“好!惊蛰雷,一声响,虫醒了,桑也要发了!这是天也来喝喜酒!”", 8,
   "close shot, GRANNY WANG, AGE 80: [锚点], slapping her knee and laughing, pointing her fan at the sky", "static camera, she slaps her knee and declares"),
 S("12", "全景", "满屋大笑", "哄笑", 4,
   "wide shot, the whole hall bursting into laughter", "static camera, everyone laughs"),
 S("13", "中景", "石生红着脸去扶新娘,扶了两次才扶起来", "—", 6,
   "medium shot, SHI SHENG, AGE 22: [锚点], red-faced, reaching to help the veiled bride up, fumbling once, then lifting her by both hands", "static camera, he fumbles, then helps her up"),
]),
dict(head="外景 桃树下 傍晚", short="桃树下 傍晚", era="春", env="peach trees in bloom by the river after the rain, wet petals on the ground, the sky clearing",
     tone="sweet and quiet after the noise",
script="""
雨过了。桃树下落了一地花瓣。
阿禾和周老篙坐在渡口的台阶上,看着新人那家的窗户亮了灯。
阿禾:爷爷,虫真的醒了吗?
周老篙抬起一块石头。底下一只小虫慢慢爬了出来。
阿禾(旁白):惊蛰。桑娘姐姐嫁人了。还有十九个节气。
""",
shots=[
 S("14", "大远景,固定", "雨过天晴,桃树下落了一地花瓣,新人家的窗亮了灯", "滴水声", 8,
   "extreme long shot at dusk after rain, peach trees by the river dropping wet petals, one window glowing warm in the village", "static camera, petals drift down", key=True),
 S("15", "双人", "阿禾和周老篙坐在渡口台阶上", "阿禾:“爷爷,虫真的醒了吗?”", 5,
   "two-shot, A HE, AGE 8: [锚点], and ZHOU THE FERRYMAN, AGE 68: [锚点], sitting on the wet stone steps of the ferry landing at dusk", "static camera, she asks"),
 S("16", "特写", "爷爷抬起一块石头,底下一只小虫慢慢爬出来", "—", 6,
   "close-up, an old hand lifting a flat wet stone, a small beetle slowly crawling out into the light", "static camera, the beetle crawls out", key=True),
 S("17", "近景", "阿禾看着,笑了", "阿禾(旁白):“惊蛰。桑娘姐姐嫁人了。还有十九个节气。”", 7,
   "close shot, A HE, AGE 8: [锚点], leaning down to watch the beetle, smiling", "static camera, she watches and smiles",
   out="hold the smile; end of episode."),
]),
])

EPS["04"] = dict(cn="四", jq="春分", title="竖蛋",
summary="春分这天,孩子们比赛把鸡蛋竖在地上。别的孩子都竖起来了,阿禾的蛋一次也立不住。她在茶亭的桌上试了一整天,王婆在旁边喝茶看着。太阳落山前,蛋立住了。王婆说:昼夜一样长,心定了,蛋就站住了。",
info=[("物候", "玄鸟至,雷乃发声,始电"), ("人物", "阿禾、王婆、村里孩子、周老篙"),
      ("风俗", "春分竖蛋:春分日昼夜等长,民间有在这天把鸡蛋竖立的游戏。"),
      ("这一集的意思", "急不来的事。阿禾在等一个人,这一集学的是怎么等。")],
curve="热闹(别人都成了)→ 急(只有她不行)→ 赌气 → 静(王婆的茶)→ 成(太阳落山前)。",
scenes=[
dict(head="外景 晒谷场 晨", short="晒谷场 晨", era="春", env="a flat earthen threshing ground at the edge of LU PU VILLAGE in spring morning light, children crouching over eggs, swallows overhead",
     tone="playful competition", crowd="eight village children",
script="""
字幕:春分。玄鸟至,雷乃发声,始电。
晒谷场上,孩子们蹲成一圈,每人手里一个鸡蛋。
一个、两个、三个——蛋一个个立在了地上。孩子们欢呼。
阿禾的蛋倒了。她扶起来,又倒了。
孩子:阿禾立不起来!
孩子们哄笑着跑开。阿禾攥着蛋,咬着嘴唇。
""",
shots=[
 S("1", "大远景,固定", "春分晨光,燕子掠过村子", "燕子叫;字幕“春分”与三候", 8,
   "extreme long shot of LU PU VILLAGE in clear spring morning light, swallows skimming low over the river and roofs", "static camera, swallows dart across", key=True),
 S("2", "全景,俯拍", "晒谷场上孩子们蹲成一圈,每人一个鸡蛋", "笑闹", 5,
   "high-angle wide shot of village children crouching in a circle on the threshing ground, each holding an egg upright on the packed earth", "static camera, they concentrate"),
 S("3", "特写", "一个、两个、三个——蛋一个个立住了", "欢呼", 6,
   "close-up at ground level, eggs standing upright one after another on the earth as small hands let go", "static camera, egg after egg stands"),
 S("4", "特写", "阿禾的蛋倒了,扶起来,又倒了", "—", 5,
   "close-up, a child's hand letting go of an egg that rolls over, setting it up again, it rolls again", "static camera, it falls twice"),
 S("5", "中景", "孩子们哄笑着跑开,阿禾攥着蛋咬着嘴唇", "孩子:“阿禾立不起来!”", 6,
   "medium shot, children running off laughing, A HE, AGE 8: [锚点], left crouching alone with an egg in her fist, biting her lip", "static camera, they run off, she stays"),
]),
dict(head="外景 茶亭 日", short="茶亭 日", era="春", env="the thatched tea pavilion beside the ferry landing, a low wooden table, a clay kettle on a small stove, the old camphor tree, the river",
     tone="patience taught without a lesson",
script="""
茶亭。阿禾把蛋放在桌上,一次又一次地试。王婆坐在对面,慢慢喝茶。
阿禾:王婆婆,它为什么不站?
王婆:你手抖。
阿禾:我手不抖!
王婆不说话,给她倒了一碗茶。
阿禾赌气不喝。日头从东挪到头顶,又往西斜。茶亭外,过河的人来来去去,周老篙撑了一趟又一趟。
阿禾终于端起茶碗,喝了一口,长长地出了口气。
她把蛋放下。手松开。
蛋站住了。
阿禾不敢出声,看向王婆。
王婆:今天昼夜一样长。心定了,蛋就站住了。
阿禾(旁白):春分。蛋站住了。还有十八个节气。
""",
shots=[
 S("6", "全景,固定", "茶亭,阿禾一次又一次地试,王婆在对面喝茶", "茶壶咕嘟", 7,
   "wide shot of the thatched tea pavilion by the ferry, A HE, AGE 8: [锚点], trying again and again to stand an egg on the low table, GRANNY WANG, AGE 80: [锚点], sipping tea opposite", "static camera, the girl tries, the old woman sips"),
 S("7", "双人", "阿禾问", "阿禾:“王婆婆,它为什么不站?”王婆:“你手抖。”", 5,
   "two-shot across the tea table, A HE, AGE 8: [锚点], frustrated, GRANNY WANG, AGE 80: [锚点], calm, fanning herself", "static camera, she asks, the old woman answers"),
 S("8", "近景", "阿禾", "阿禾:“我手不抖!”", 3,
   "close shot, A HE, AGE 8: [锚点], indignant, holding the egg", "static camera, she protests"),
 S("9", "特写", "王婆给她倒了一碗茶", "倒茶声", 4,
   "close-up, a wrinkled hand pouring pale green tea from a clay kettle into a small bowl in front of the girl", "static camera, tea pours"),
 S("10", "中景,固定,叠化", "日头挪动,茶亭外过河的人来来去去,周老篙撑了一趟又一趟", "渡船来去", 9,
   "medium shot of the ferry seen from the tea pavilion, the light moving from morning to afternoon, ZHOU THE FERRYMAN, AGE 68: [锚点], ferrying VILLAGERS across again and again", "static camera, time-lapse dissolves as shadows move"),
 S("11", "近景", "阿禾终于端起茶碗,喝了一口,长长出了口气", "—", 6,
   "close shot, A HE, AGE 8: [锚点], in late afternoon light, finally lifting the tea bowl, drinking, letting out a long breath", "static camera, she drinks and breathes out", key=True),
 S("12", "特写", "她把蛋放下,手松开,蛋站住了", "—", 6,
   "close-up, a small hand slowly letting go of an egg on the wooden table, the egg standing perfectly upright in low golden light", "static camera, the hand opens, the egg stands", key=True),
 S("13", "近景", "阿禾不敢出声,看向王婆", "—", 3,
   "close shot, A HE, AGE 8: [锚点], holding her breath, eyes sliding toward the old woman", "static camera, she looks up"),
 S("14", "近景", "王婆", "王婆:“今天昼夜一样长。心定了,蛋就站住了。”", 7,
   "close shot, GRANNY WANG, AGE 80: [锚点], smiling into her tea bowl, sunset light", "static camera, she speaks without looking up"),
 S("15", "大远景,固定", "夕阳下的茶亭,桌上一枚立着的蛋", "阿禾(旁白):“春分。蛋站住了。还有十八个节气。”", 8,
   "extreme long shot at sunset, the tea pavilion and camphor tree by the river, two small figures at the table, the light even and golden", "static camera, the sun sets", key=True,
   out="hold; end of episode."),
]),
])

EPS["05"] = dict(cn="五", jq="清明", title="纸鸢",
summary="清明上坟。周老篙带阿禾去山坡上扫墓:奶奶的坟,和阿禾娘的坟。回来路上,孩子们在放纸鸢,按老规矩,放高了就剪断线,让它把晦气带走。阿禾的纸鸢是爹走前给她扎的。她犹豫了很久,把线剪了:“给娘送去。”",
info=[("物候", "桐始华,田鼠化为鴽,虹始见"), ("人物", "阿禾、周老篙、村里孩子"),
      ("风俗", "清明扫墓;放断鹞:纸鸢放高后剪断线,任其飘走,俗称放走晦气。"),
      ("揭示", "阿禾的娘在她三岁时病故。这是全剧第一次提到。")],
curve="静(扫墓)→ 问(娘长什么样)→ 闹(满天纸鸢)→ 舍(剪线)。",
scenes=[
dict(head="外景 山坡坟地 晨", short="山坡 晨", era="春", env="a gentle hillside above LU PU VILLAGE with two small grass-covered graves among tea bushes, fine rain clearing, the village and river below",
     tone="quiet, plain grief",
script="""
字幕:清明。桐始华,田鼠化为鴽,虹始见。
山坡上两座小坟。周老篙拔着坟头的草。阿禾在一旁摆上青团。
周老篙对着一座坟。
周老篙:老婆子,阿禾长高了。
他转向另一座坟,没说话,摸了摸墓碑。
阿禾:爷爷,娘长什么样?
周老篙想了想。
周老篙:跟你一样,不爱哭。
""",
shots=[
 S("1", "大远景,固定", "细雨初停的山坡,两座小坟,山下是村子和河", "鸟鸣;字幕“清明”与三候", 9,
   "extreme long shot of a hillside above the village after fine rain, two small grass-covered graves among tea bushes, LU PU VILLAGE and the river below in mist", "static camera, mist lifts slowly", key=True),
 S("2", "中景", "周老篙拔坟头的草,阿禾摆上青团", "—", 6,
   "medium shot, ZHOU THE FERRYMAN, AGE 68: [锚点], kneeling and pulling weeds from a grave, A HE, AGE 8: [锚点], setting green rice cakes on a leaf before it", "static camera, they work in silence"),
 S("3", "近景", "周老篙对着一座坟", "周老篙:“老婆子,阿禾长高了。”", 5,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], speaking softly to the grave", "static camera, he speaks"),
 S("4", "特写", "他转向另一座坟,没说话,摸了摸墓碑", "—", 5,
   "close-up, an old hand resting on a small plain gravestone, rubbing moss from its edge", "static camera, the hand rests and rubs"),
 S("5", "近景", "阿禾", "阿禾:“爷爷,娘长什么样?”", 3,
   "close shot, A HE, AGE 8: [锚点], looking at the second grave", "static camera, she asks"),
 S("6", "近景", "周老篙想了想", "周老篙:“跟你一样,不爱哭。”", 6,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], thinking, then looking at the girl", "static camera, he thinks, then answers", key=True),
]),
dict(head="外景 河滩 午后", short="河滩 午后", era="春", env="a wide grassy river flat below the village, many paper kites in the sky, a faint rainbow",
     tone="open sky, one small sacrifice", crowd="village children flying kites",
script="""
河滩上满天纸鸢。孩子们放高了,就“咔嚓”一剪,看着纸鸢飘走,拍手大叫。
孩子:晦气飞喽!
阿禾的纸鸢是一只燕子,是爹走前给她扎的。飞得最高。
阿禾拿着剪子,看看线,又看看天。
阿禾:爷爷,剪了,它飞到哪儿去?
周老篙:风往哪吹,就到哪。
阿禾:能飞到娘那儿吗?
周老篙没回答。
阿禾剪断了线。燕子纸鸢晃了晃,越飞越高,飞进了天边一道淡淡的虹里。
阿禾(旁白):清明。我给娘送了一只燕子。还有十七个节气。
""",
shots=[
 S("7", "大远景,固定", "河滩上满天纸鸢,天边一道淡虹", "风声、笑闹", 8,
   "extreme long shot of a grassy river flat, many paper kites high in a clearing sky, a faint rainbow over the hills", "static camera, kites sway", key=True),
 S("8", "中景", "孩子们“咔嚓”一剪,看纸鸢飘走,拍手大叫", "孩子:“晦气飞喽!”", 5,
   "medium shot, children cutting a kite string with scissors and cheering as the kite drifts free", "static camera, snip, the kite floats away"),
 S("9", "近景,仰拍", "阿禾的燕子纸鸢飞得最高", "—", 5,
   "low-angle close shot, a paper swallow kite painted black and white flying highest of all against the bright sky", "static camera, the kite climbs"),
 S("10", "近景", "阿禾拿着剪子,看看线,又看看天", "阿禾:“爷爷,剪了,它飞到哪儿去?”", 6,
   "close shot, A HE, AGE 8: [锚点], holding the kite line in one hand and scissors in the other, looking up", "static camera, she hesitates"),
 S("11", "双人", "周老篙", "周老篙:“风往哪吹,就到哪。”阿禾:“能飞到娘那儿吗?”", 7,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], standing behind A HE, AGE 8: [锚点], both looking at the sky", "static camera, they talk without looking at each other"),
 S("12", "近景", "周老篙没回答", "—", 3,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], looking at the sky, saying nothing", "static camera, silence"),
 S("13", "特写", "阿禾剪断了线", "“咔嚓”", 3,
   "close-up, small hands closing scissors on a taut kite string", "static camera, the string parts"),
 S("14", "大远景,固定", "燕子纸鸢晃了晃,越飞越高,飞进那道淡淡的虹里", "阿禾(旁白):“清明。我给娘送了一只燕子。还有十七个节气。”羌笛", 10,
   "extreme long shot, a small swallow kite wobbling free and drifting higher and higher toward a faint rainbow over the blue hills", "static camera, the kite shrinks into the sky", key=True,
   out="the kite disappears into the light; end of episode."),
]),
])

EPS["06"] = dict(cn="六", jq="谷雨", title="采茶",
summary="谷雨前后,村后山上采茶。许秀才落第回来了,一路低着头,不敢进村,躲进了王婆的茶亭。王婆不问考得怎样,只给他泡了一碗新茶:“谷雨的茶,先苦后甜。”陈先生来了,看见那把旧伞,什么都没说,接过伞,撑开,和他一起淋着雨回村。",
info=[("物候", "萍始生,鸣鸠拂其羽,戴胜降于桑"), ("人物", "许秀才、王婆、陈先生、桑娘、阿禾、采茶的村妇"),
      ("风俗", "谷雨采茶,俗称“雨前茶”;江南有谷雨饮新茶之俗。"),
      ("回收", "第 2 集的旧油纸伞。")],
curve="满(采茶的山坡)→ 羞(落第归来)→ 暖(一碗新茶)→ 宽(一把伞两个人)。",
scenes=[
dict(head="外景 茶山 晨", short="茶山 晨", era="春", env="terraced tea bushes on the low hill behind LU PU VILLAGE in fine morning rain, women picking with bamboo baskets",
     tone="busy, green, singing", crowd="eight village women picking tea",
script="""
字幕:谷雨。萍始生,鸣鸠拂其羽,戴胜降于桑。
细雨里,茶山上一片青绿。村妇们背着竹篓采茶,一边采一边唱。桑娘也在,手快得看不清。
阿禾跟在后面捡掉下的茶芽。
她直起腰,看见山下的河边小路上,一个人背着书箱,打着一把黄伞,走得很慢。
阿禾:是许哥哥!
""",
shots=[
 S("1", "大远景,固定", "细雨里青绿的茶山,村妇背竹篓采茶", "采茶歌;字幕“谷雨”与三候", 9,
   "extreme long shot of terraced tea bushes on the hill behind the village in fine morning rain, women with bamboo baskets picking", "static camera, rain drifts, the women move slowly", key=True),
 S("2", "特写", "手指飞快地掐下嫩芽", "—", 4,
   "close-up, quick fingers pinching the tender top two leaves from tea bushes and tossing them into a basket", "static camera, the fingers pick rapidly"),
 S("3", "中景", "桑娘采得最快,阿禾跟在后面捡掉下的茶芽", "采茶歌", 5,
   "medium shot, SANG NIANG, AGE 19: [锚点], picking fast and singing, A HE, AGE 8: [锚点], behind her gathering fallen tea buds", "static camera, they work along the row"),
 S("4", "主观,远景", "山下河边小路上,一个人背书箱打黄伞,走得很慢", "阿禾:“是许哥哥!”", 7,
   "point-of-view long shot down the hill, a lone figure with a book box on his back under a yellow patched umbrella walking slowly along the river path", "static camera, the figure trudges"),
]),
dict(head="外景 茶亭 午", short="茶亭 午", era="春", env="the thatched tea pavilion by the ferry in rain, a small stove with a kettle, a basket of fresh tea leaves, the river",
     tone="shame dissolved without a word about it",
script="""
许秀才没有进村,拐进了渡口的茶亭,收了伞,坐在最角落里。
王婆在炉子上烘着新茶,看了他一眼,什么也没问。
她泡了一碗茶,推到他面前。
王婆:谷雨的茶。先苦,后甜。
许秀才捧着碗,喝了一口,眼圈红了。
许秀才:婆婆,我没中。
王婆:我又没问你。喝茶。
外面的雨里,陈先生站在茶亭门口,浑身湿透。他看见了靠在墙角的那把旧伞。
许秀才站起来,不敢看他。
许秀才:先生,我……
陈先生拿起那把伞,撑开。
陈先生:回来就好。走,回村。
两个人挤在一把伞下,走进雨里。伞太小,两个人的肩膀都淋湿了。
阿禾(旁白):谷雨。许哥哥回来了,伞也回来了。还有十六个节气。
""",
shots=[
 S("5", "全景", "许秀才拐进茶亭,收了伞,坐在最角落", "雨声", 7,
   "wide shot of the tea pavilion in the rain, XU XIUCAI, AGE 20: [锚点], ducking in, closing the patched yellow umbrella and sitting in the farthest corner, GRANNY WANG, AGE 80: [锚点], at the stove", "static camera, he sits down heavily"),
 S("6", "特写", "王婆在炉上烘新茶", "炒茶沙沙", 5,
   "close-up, wrinkled hands turning fresh green tea leaves in a shallow iron pan over a small stove, steam rising", "static camera, the leaves are turned"),
 S("7", "中景", "王婆泡了一碗茶,推到他面前", "王婆:“谷雨的茶。先苦,后甜。”", 6,
   "medium shot, GRANNY WANG, AGE 80: [锚点], setting a bowl of new tea before XU XIUCAI, AGE 20: [锚点]", "static camera, she sets it down"),
 S("8", "近景", "许秀才捧碗喝了一口,眼圈红了", "许秀才:“婆婆,我没中。”", 6,
   "close shot, XU XIUCAI, AGE 20: [锚点], holding the bowl in both hands, drinking, eyes reddening", "static camera, he drinks and speaks"),
 S("9", "近景", "王婆", "王婆:“我又没问你。喝茶。”", 4,
   "close shot, GRANNY WANG, AGE 80: [锚点], turning back to her pan, unbothered", "static camera, she answers and turns away", key=True),
 S("10", "中景,门框构图", "陈先生站在茶亭门口,浑身湿透,看见墙角的旧伞", "雨声", 6,
   "medium shot framed by the pavilion entrance, MR CHEN, AGE 46: [锚点], soaked, standing in the rain, looking at the old umbrella leaning in the corner", "static camera, he stands and looks"),
 S("11", "近景", "许秀才站起来,不敢看他", "许秀才:“先生,我……”", 4,
   "close shot, XU XIUCAI, AGE 20: [锚点], standing up, eyes on the floor", "static camera, he stands"),
 S("12", "中景", "陈先生拿起伞,撑开", "陈先生:“回来就好。走,回村。”", 6,
   "medium shot, MR CHEN, AGE 46: [锚点], picking up the patched umbrella and opening it with a soft smile", "static camera, the umbrella opens"),
 S("13", "大远景,固定", "两个人挤在一把伞下走进雨里,肩膀都淋湿了", "阿禾(旁白):“谷雨。许哥哥回来了,伞也回来了。还有十六个节气。”", 10,
   "extreme long shot, two men sharing one small yellow umbrella walking along the rainy river path toward the village, both shoulders wet, the tea pavilion behind", "static camera, they walk slowly away", key=True,
   out="hold on the umbrella in the rain; end of episode."),
]),
])
