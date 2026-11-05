ENV_FERRY = "LU PU VILLAGE ferry landing under the enormous old camphor tree, the stone steps, the FERRY BOAT, the thatched tea pavilion, the slow green river"

EPS = {}

EPS["07"] = dict(cn="七", jq="立夏", title="称人",
summary="立夏这天,村里在老樟树下挂起大秤,挨个称人,图一年平安。阿禾挂在秤钩上的竹篮里,轻得秤砣都压不住。回到家,爷爷照老规矩在门框上刻今年的高度。门框上还有另一排刻痕,是她娘小时候的。今年,阿禾第一次超过了娘八岁那一刀。",
info=[("物候", "蝼蝈鸣,蚯蚓出,王瓜生"), ("人物", "阿禾、周老篙、王婆、桑娘、石生、村民"),
      ("风俗", "立夏称人:在大树下悬大秤称体重,说吉利话;孩子胸前挂立夏蛋,互相斗蛋。"),
      ("揭示", "门框上并排两列刻痕:一列是阿禾娘,一列是阿禾。")],
curve="闹(称人、斗蛋)→ 轻(秤砣压不住)→ 静(门框)→ 暖(超过娘的那一刀)。",
scenes=[
dict(head="外景 渡口老樟树下 晨", short="老樟树下 晨", era="夏", env=ENV_FERRY + ", a huge wooden steelyard hanging from a low camphor branch with a bamboo basket on the hook",
     tone="noisy, good-humoured", crowd="villagers queuing to be weighed, children with egg nets on their chests",
script="""
字幕:立夏。蝼蝈鸣,蚯蚓出,王瓜生。
老樟树的横枝上吊着一杆大秤,秤钩上挂着一只竹篮。全村排着队称人。
石生拉着秤绳。王婆拿着扇子坐在一边,每称一个就念一句吉利话。
石生:桑娘,九十二斤!
王婆:九十二,有吃有余!
孩子们胸前都挂着一只彩线网兜,兜里装着煮鸡蛋,两两对着撞。“咔”一声,谁的蛋碎了谁输。
""",
shots=[
 S("1", "大远景,固定", "初夏的渡口,老樟树新叶浓绿,横枝上吊着一杆大秤", "蝉初鸣;字幕“立夏”与三候", 9,
   "extreme long shot of the ferry landing in early summer, the old camphor tree in dense fresh leaves, a huge wooden steelyard hanging from a low branch, VILLAGERS gathered", "static camera, leaves stir", key=True),
 S("2", "中景", "全村排队称人,石生拉秤绳", "笑声", 6,
   "medium shot, SHI SHENG, AGE 22: [锚点], hauling on the steelyard rope, SANG NIANG, AGE 19: [锚点], sitting in the bamboo basket on the hook laughing, VILLAGERS queuing", "static camera, the basket lifts off the ground"),
 S("3", "近景", "石生读秤,王婆念吉利话", "石生:“桑娘,九十二斤!”王婆:“九十二,有吃有余!”", 6,
   "close shot, GRANNY WANG, AGE 80: [锚点], seated with her fan, calling out a blessing with a grin", "static camera, she calls out"),
 S("4", "特写", "孩子胸前的彩线网兜,两只蛋对撞,一只碎了", "“咔”,欢叫", 5,
   "close-up, two boiled eggs in coloured string nets hanging from children's necks knocked together, one shell cracking", "static camera, the eggs clack, one cracks"),
]),
dict(head="外景 老樟树下 晨(续)", short="老樟树下 续", era="夏", env=ENV_FERRY + ", the steelyard with the bamboo basket",
     tone="a small girl very light in a big world",
script="""
轮到阿禾。她坐进竹篮,石生一拉,篮子飞了起来。秤砣怎么挪都压不平,大家笑。
石生:四十一斤!秤砣比你还沉!
王婆:四十一,长得快!等你爹回来,抱不动你!
阿禾在篮子里晃着,也笑了。
""",
shots=[
 S("5", "中景", "阿禾坐进竹篮,篮子一下飞了起来", "笑声", 5,
   "medium shot, A HE, AGE 8: [锚点], climbing into the bamboo basket on the hook, SHI SHENG, AGE 22: [锚点], pulling, the basket shooting up too easily", "static camera, the basket swings up"),
 S("6", "特写", "秤砣在秤杆上挪来挪去压不平", "—", 4,
   "close-up, a big hand sliding the iron weight back and forth along the wooden beam, the beam tipping", "static camera, the weight slides"),
 S("7", "近景", "石生", "石生:“四十一斤!秤砣比你还沉!”", 4,
   "close shot, SHI SHENG, AGE 22: [锚点], laughing as he reads the beam", "static camera, he laughs and calls"),
 S("8", "近景", "王婆", "王婆:“四十一,长得快!等你爹回来,抱不动你!”", 6,
   "close shot, GRANNY WANG, AGE 80: [锚点], pointing her fan at the girl", "static camera, she calls the blessing"),
 S("9", "中景", "阿禾在篮子里晃着,笑了", "—", 5,
   "medium shot, A HE, AGE 8: [锚点], swinging in the basket under the camphor leaves, laughing", "static camera, the basket swings, she laughs", key=True),
]),
dict(head="内景 周家 门口 黄昏", short="周家门口 黄昏", era="夏", env="the doorway of the ferryman's small house, an old wooden door frame with rows of carved notches and small characters, warm evening light",
     tone="a quiet revelation",
script="""
黄昏。周家门口。阿禾背靠门框站得笔直。周老篙用小刀在她头顶的门框上刻了一道。
门框上有两排刻痕。左边一排是新的,是阿禾的。右边一排旧得发黑,每道旁边刻着一个小小的“秀”字。
阿禾:爷爷,这个“秀”是谁?
周老篙:你娘。她小时候,每年立夏也站在这儿。
阿禾转过身,踮起脚,用手指找右边那排里刻着“八岁”的那一刀。新刻的那道,比它高出一点。
阿禾:我比娘八岁的时候高!
周老篙:嗯。比她高。
阿禾(旁白):立夏。我比娘高了一点点。还有十五个节气。
""",
shots=[
 S("10", "中景", "阿禾背靠门框站得笔直,周老篙在她头顶刻一道", "刻木声", 7,
   "medium shot at dusk, A HE, AGE 8: [锚点], standing very straight with her back to an old door frame, ZHOU THE FERRYMAN, AGE 68: [锚点], carving a notch above her head with a small knife", "static camera, he carves"),
 S("11", "特写,缓摇", "门框上两排刻痕:左边新,右边旧得发黑,每道旁刻一个小“秀”字", "—", 7,
   "close-up slow tilt along an old wooden door frame, two columns of carved notches, the left fresh and pale, the right old and dark, each old notch with a tiny carved character beside it", "slow tilt up along the frame", key=True),
 S("12", "双人", "阿禾问", "阿禾:“爷爷,这个‘秀’是谁?”", 4,
   "two-shot at the doorway, A HE, AGE 8: [锚点], touching a dark notch, looking up at ZHOU THE FERRYMAN, AGE 68: [锚点]", "static camera, she asks"),
 S("13", "近景", "周老篙", "周老篙:“你娘。她小时候,每年立夏也站在这儿。”", 6,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], looking at the old notches, warm evening light", "static camera, he answers softly"),
 S("14", "特写", "阿禾踮脚,手指找到刻着“八岁”的那一刀,新刻的一道比它高出一点", "—", 7,
   "close-up, a child's finger resting on an old dark notch, a fresh pale notch carved just slightly above it in the neighbouring column", "static camera, the finger moves from the old notch up to the new one", key=True),
 S("15", "近景", "阿禾转身,眼睛发亮", "阿禾:“我比娘八岁的时候高!”周老篙:“嗯。比她高。”", 6,
   "close shot, A HE, AGE 8: [锚点], turning around with shining eyes", "static camera, she turns and beams"),
 S("16", "大远景,固定", "黄昏的村子,一扇门里两个人影", "阿禾(旁白):“立夏。我比娘高了一点点。还有十五个节气。”", 8,
   "extreme long shot at dusk, the small ferryman's house by the river, two figures in the lit doorway, the camphor tree dark against the sky", "static camera, the light fades", key=True,
   out="hold; end of episode."),
]),
])

EPS["08"] = dict(cn="八", jq="小满", title="蚕",
summary="小满前后,蚕要上山结茧。桑娘一连几夜守在蚕室里添叶,累得直吐。王婆来看,摸了摸她的脉,笑了:“不是累的。有了。”石生正扛着一捆蚕簇进门,一下全掉在地上。",
info=[("物候", "苦菜秀,靡草死,麦秋至"), ("人物", "桑娘、石生、王婆、阿禾"),
      ("风俗", "小满前后蚕上山结茧;江南蚕农有祭蚕神、小满“抢水”之俗。"),
      ("贯穿线", "桑娘有孕,大寒生产(第 24 集)。")],
curve="累(守夜添叶)→ 担心(吐)→ 意外(“有了”)→ 乱(蚕簇落地)→ 喜。",
scenes=[
dict(head="内景 蚕室 夜", short="蚕室 夜", era="夏", env="SILKWORM ROOM at night lit by one oil lamp, tiers of round bamboo trays crowded with fat white silkworms eating mulberry leaves, the sound of munching",
     tone="close, warm, tired",
script="""
字幕:小满。苦菜秀,靡草死,麦秋至。
夜。蚕室里沙沙一片,像下雨,是几万条蚕在吃桑叶。
桑娘提着灯,一层层地撒叶。阿禾帮她抱叶子,眼皮在打架。
桑娘:再熬两夜,就上山了。
她直起腰,忽然捂住嘴,冲出门去。
""",
shots=[
 S("1", "大远景,固定", "麦黄的田边,村子里一扇窗亮着灯", "蛙声;字幕“小满”与三候", 8,
   "extreme long shot at night of LU PU VILLAGE beside fields of yellowing wheat, one paper window glowing among dark houses", "static camera, the window glows", key=True),
 S("2", "特写", "竹匾里满满的白蚕,啃着桑叶,沙沙如雨", "沙沙声", 5,
   "close-up, a round bamboo tray crowded with fat white silkworms devouring mulberry leaves, lamp light", "static camera, the silkworms munch"),
 S("3", "中景", "桑娘提灯一层层撒叶,阿禾抱着叶子打瞌睡", "桑娘:“再熬两夜,就上山了。”", 7,
   "medium shot of the SILKWORM ROOM, SANG NIANG, AGE 19: [锚点], scattering mulberry leaves over tier after tier of trays by lamp light, A HE, AGE 8: [锚点], holding an armful of leaves and nodding off", "static camera, she works, the child dozes"),
 S("4", "近景", "桑娘直起腰,忽然捂住嘴,冲出门", "—", 5,
   "close shot, SANG NIANG, AGE 19: [锚点], straightening her back, suddenly covering her mouth and rushing out", "static camera, she turns and rushes out"),
]),
dict(head="内景 蚕室 晨", short="蚕室 晨", era="夏", env="SILKWORM ROOM in early morning light through paper windows, bundles of straw cocooning frames, the first white cocoons",
     tone="worry turned to joy",
script="""
清晨。王婆拄着拐杖进了蚕室,看了看第一批结了白茧的蚕簇,点点头。
她拉过桑娘的手腕,摸了一会儿脉,笑了。
王婆:你这几夜吐,不是累的。
桑娘:那是……
王婆:有了。
桑娘愣住。门口,石生正扛着一大捆蚕簇进门。蚕簇“哗啦”全掉在了地上。
石生:……有了?
桑娘看着他,先笑出了声。
阿禾凑到竹匾边,看见一颗刚结好的白茧,用手指轻轻碰了碰。
阿禾(旁白):小满。桑娘姐姐肚子里有了一个小人。还有十四个节气。
""",
shots=[
 S("5", "特写", "稻草蚕簇上结出了第一批雪白的茧", "—", 5,
   "close-up, bundles of straw cocooning frames with the first pure white cocoons spun among them, soft morning light", "static camera, a silkworm spins its last threads", key=True),
 S("6", "中景", "王婆拄拐进门,看看蚕簇,点点头", "—", 5,
   "medium shot, GRANNY WANG, AGE 80: [锚点], stepping into the SILKWORM ROOM with a cane, inspecting the cocoons and nodding", "static camera, she enters and nods"),
 S("7", "双人", "王婆拉过桑娘的手腕摸脉,笑了", "王婆:“你这几夜吐,不是累的。”", 7,
   "two-shot, GRANNY WANG, AGE 80: [锚点], holding the wrist of a pale SANG NIANG, AGE 19: [锚点], feeling the pulse, then smiling", "static camera, she feels the pulse and smiles"),
 S("8", "近景", "桑娘;王婆", "桑娘:“那是……”王婆:“有了。”", 5,
   "close shot, SANG NIANG, AGE 19: [锚点], blinking, not understanding, then understanding", "static camera, her face changes"),
 S("9", "中景,门框构图", "门口石生扛着一大捆蚕簇,哗啦全掉在地上", "“哗啦”", 5,
   "medium shot framed by the doorway, SHI SHENG, AGE 22: [锚点], carrying a big bundle of straw frames on his shoulder, the whole bundle sliding off and crashing down", "static camera, the bundle falls"),
 S("10", "近景", "石生", "石生:“……有了?”", 3,
   "close shot, SHI SHENG, AGE 22: [锚点], frozen in the doorway with empty arms", "static camera, he stares"),
 S("11", "近景", "桑娘看着他,先笑出了声", "笑声", 5,
   "close shot, SANG NIANG, AGE 19: [锚点], looking at her husband and bursting into laughter", "static camera, she laughs"),
 S("12", "特写", "阿禾用手指轻轻碰了碰一颗新茧", "阿禾(旁白):“小满。桑娘姐姐肚子里有了一个小人。还有十四个节气。”", 8,
   "close-up, a child's fingertip gently touching a freshly spun white cocoon on the straw frame", "static camera, the finger touches the cocoon and stays", key=True,
   out="hold on the cocoon; end of episode."),
]),
])

EPS["09"] = dict(cn="九", jq="芒种", title="插秧",
summary="芒种,全村下田插秧。男女老少一字排开,唱着秧歌往后退。陈先生和许秀才也挽起裤腿下了田,陈先生一脚踩空,坐进了泥里,满田的人笑弯了腰。阿禾插的那一行歪歪扭扭,她急得要拔了重插。爷爷说:歪的也长。",
info=[("物候", "螳螂生,鵙始鸣,反舌无声"), ("人物", "阿禾、周老篙、陈先生、许秀才、桑娘、石生、村民"),
      ("风俗", "芒种插秧,江南有唱秧歌、送花神之俗。"),
      ("秧歌", "五代契此(布袋和尚)《插秧诗》:手把青秧插满田,低头便见水中天。心地清净方为道,退步原来是向前。南宋江南已广为流传,剧中由村民唱成秧歌。")],
curve="齐(一字排开)→ 乐(秧歌)→ 笑(先生坐进泥里)→ 急(歪了)→ 宽(歪的也长)。",
scenes=[
dict(head="外景 水田 晨", short="水田 晨", era="夏", env="flooded rice paddies outside LU PU VILLAGE mirroring the sky, bundles of green seedlings, low hills, white egrets",
     tone="communal rhythm and laughter", crowd="twenty villagers planting rice in a line",
script="""
字幕:芒种。螳螂生,鵙始鸣,反舌无声。
水田像一面面镜子,照着天。全村的人一字排开,弯着腰,一边插秧一边往后退。
有人起了个头,大家接着唱。
村民(唱):手把青秧插满田,低头便见水中天——
陈先生和许秀才挽着裤腿下了田,陈先生小心翼翼,一步一步。
陈先生(唱):退步原来是向前……
他往后一退,一脚踩空,坐进了泥里。
满田的人笑弯了腰。许秀才去拉他,自己也滑倒了。
""",
shots=[
 S("1", "大远景,固定", "水田像镜子照着天,白鹭飞过", "鸟鸣;字幕“芒种”与三候", 9,
   "extreme long shot of flooded rice paddies outside the village mirroring the sky and low hills, white egrets lifting off", "static camera, egrets cross the sky", key=True),
 S("2", "全景", "全村一字排开,弯腰插秧,往后退", "秧歌起", 7,
   "wide shot, a long line of VILLAGERS bent over in the water planting seedlings and stepping backward in rhythm", "static camera, the line moves back step by step"),
 S("3", "特写", "手把青秧插进水里,水面映着天", "村民(唱):“手把青秧插满田,低头便见水中天——”", 7,
   "close-up, hands pushing green rice seedlings into the muddy water, the sky and clouds reflected around them", "static camera, seedling after seedling goes in", key=True),
 S("4", "中景", "陈先生和许秀才挽着裤腿下田,陈先生小心翼翼", "—", 5,
   "medium shot, MR CHEN, AGE 46: [锚点], and XU XIUCAI, AGE 20: [锚点], trousers rolled up, stepping gingerly into the paddy with seedlings in hand", "static camera, they step in carefully"),
 S("5", "近景", "陈先生唱着往后退", "陈先生(唱):“退步原来是向前……”", 4,
   "close shot, MR CHEN, AGE 46: [锚点], singing earnestly and stepping backward", "static camera, he sings and steps"),
 S("6", "中景", "一脚踩空,坐进泥里", "扑通", 4,
   "medium shot, MR CHEN, AGE 46: [锚点], losing his footing and sitting down hard in the muddy water", "static camera, he sits down with a splash"),
 S("7", "全景", "满田的人笑弯了腰;许秀才去拉他,自己也滑倒了", "哄笑", 6,
   "wide shot, the whole line of VILLAGERS doubled over laughing, XU XIUCAI, AGE 20: [锚点], reaching to help and slipping into the mud too", "static camera, laughter, a second splash"),
]),
dict(head="外景 水田 午", short="水田 午", era="夏", env="the same paddies at noon, neat rows of seedlings, one crooked row, the ferryman resting on the bank",
     tone="gentle acceptance",
script="""
中午。大家坐在田埂上吃饭。
阿禾看着自己插的那一行,歪歪扭扭,像一条蛇。别人的都笔直。
她跳进田里,要把秧拔了重插。
周老篙:别拔。
阿禾:它是歪的。
周老篙:歪的也长。秋天你再来看,分不出哪行是歪的。
阿禾站在水里,看了一会儿,爬回田埂上。
阿禾(旁白):芒种。我插了一行歪的。还有十三个节气。
""",
shots=[
 S("8", "全景", "中午,大家坐在田埂上吃饭", "说笑", 6,
   "wide shot at noon, VILLAGERS sitting along the earth bank eating rice from bowls, the planted paddies before them", "static camera, they eat and chat"),
 S("9", "主观,俯拍", "一片笔直的秧苗里,一行歪歪扭扭像一条蛇", "—", 5,
   "high-angle point-of-view shot over the paddy, neat straight rows of seedlings and one crooked wobbling row among them", "static camera, still"),
 S("10", "中景", "阿禾跳进田里要拔秧", "—", 4,
   "medium shot, A HE, AGE 8: [锚点], jumping into the paddy and grabbing at her crooked row of seedlings", "static camera, she jumps in"),
 S("11", "双人", "周老篙叫住她", "周老篙:“别拔。”阿禾:“它是歪的。”", 5,
   "two-shot, ZHOU THE FERRYMAN, AGE 68: [锚点], on the bank with a rice bowl, A HE, AGE 8: [锚点], in the water holding a seedling", "static camera, he calls, she answers"),
 S("12", "近景", "周老篙", "周老篙:“歪的也长。秋天你再来看,分不出哪行是歪的。”", 7,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], chewing, unbothered, squinting at the field", "static camera, he speaks", key=True),
 S("13", "大远景,固定", "阿禾站在水里看了一会儿,爬回田埂;满田秧苗", "阿禾(旁白):“芒种。我插了一行歪的。还有十三个节气。”", 9,
   "extreme long shot of the green-dotted paddies at noon, a small girl standing in the water, then climbing back onto the bank beside her grandfather", "static camera, she climbs out", key=True,
   out="hold on the field; end of episode."),
]),
])

EPS["10"] = dict(cn="十", jq="夏至", title="荷",
summary="夏至,一年里白天最长。陈先生带孩子们到荷塘边上课,念一首新诗:“小荷才露尖尖角,早有蜻蜓立上头。”话音没落,一只蜻蜓真的落在了荷尖上。孩子们屏住呼吸。阿禾问先生自己写过诗没有。先生说写过很多,一首也没留下。阿禾说:那你写一首给我。",
info=[("物候", "鹿角解,蝉始鸣,半夏生"), ("人物", "陈先生、阿禾、许秀才、村里孩子"),
      ("诗", "杨万里《小池》:泉眼无声惜细流,树阴照水爱晴柔。小荷才露尖尖角,早有蜻蜓立上头。杨万里与剧中同时代,这首诗当时是“新诗”。"),
      ("陈先生的诗(原创)", "日长不肯暮,童子问归期。荷上蜻蜓立,还如未到时。")],
curve="慢(最长的一天)→ 奇(蜻蜓真的来了)→ 问(你写过诗吗)→ 赠(一首给阿禾的诗)。",
scenes=[
dict(head="外景 荷塘边 午后", short="荷塘 午后", era="夏", env="a lotus pond behind LU PU VILLAGE at the height of summer, broad green leaves, pink lotus buds, a willow giving shade, cicadas",
     tone="drowsy, wondering", crowd="six village children sitting on the bank",
script="""
字幕:夏至。鹿角解,蝉始鸣,半夏生。
荷塘边柳荫下,陈先生带着孩子们上课。蝉叫得震耳朵。
陈先生:今天念一首新诗,临安杨大人写的。
陈先生:泉眼无声惜细流,树阴照水爱晴柔。小荷才露尖尖角——
一只蜻蜓飞过来,轻轻落在一枝荷花的尖角上。
孩子们一齐屏住呼吸。
陈先生看见了,压低声音念完。
陈先生:……早有蜻蜓立上头。
孩子们捂着嘴笑。蜻蜓不动。
""",
shots=[
 S("1", "大远景,固定", "盛夏荷塘,柳荫,蝉鸣震耳", "蝉鸣;字幕“夏至”与三候", 9,
   "extreme long shot of a lotus pond behind the village at the height of summer, broad green leaves and pink buds, a willow casting deep shade, heat haze", "static camera, the leaves sway slightly", key=True),
 S("2", "全景", "柳荫下陈先生带孩子们上课", "陈先生:“今天念一首新诗,临安杨大人写的。”", 7,
   "wide shot in willow shade, MR CHEN, AGE 46: [锚点], sitting on a stone with a book, A HE, AGE 8: [锚点], and other children on the grass facing the pond", "static camera, he opens the book"),
 S("3", "近景", "陈先生念诗", "陈先生:“泉眼无声惜细流,树阴照水爱晴柔。小荷才露尖尖角——”", 8,
   "close shot, MR CHEN, AGE 46: [锚点], reciting with his eyes half closed, dappled light", "static camera, he recites"),
 S("4", "特写", "一只蜻蜓飞来,落在荷花尖角上", "—", 6,
   "close-up, a red dragonfly hovering and alighting on the very tip of a closed pink lotus bud", "static camera, the dragonfly lands and folds its wings", key=True),
 S("5", "全景", "孩子们一齐屏住呼吸", "蝉声忽远", 4,
   "wide shot, all the children frozen, staring at the pond with held breath", "static camera, nobody moves"),
 S("6", "近景", "陈先生看见了,压低声音念完", "陈先生:“……早有蜻蜓立上头。”", 5,
   "close shot, MR CHEN, AGE 46: [锚点], seeing the dragonfly and whispering the last line, delighted", "static camera, he whispers"),
 S("7", "中景", "孩子们捂着嘴笑,蜻蜓不动", "闷笑", 5,
   "medium shot, children with hands over their mouths giggling, the dragonfly on the lotus tip behind them", "static camera, they giggle"),
]),
dict(head="外景 荷塘边 傍晚", short="荷塘 傍晚", era="夏", env="the lotus pond at a long late dusk, the sun still up, the sky gold, the water still",
     tone="a gift between a failed scholar and a child",
script="""
傍晚,太阳还不肯落。孩子们都回家了,阿禾没走。
阿禾:先生,你写过诗吗?
陈先生:写过很多。
阿禾:在哪儿?
陈先生:烧了,丢了,忘了。一首也没留下。
阿禾想了想。
阿禾:那你写一首给我。我留着。
陈先生看了她很久,折了一根柳枝,在塘边的湿泥上写字。
陈先生:日长不肯暮,童子问归期。荷上蜻蜓立,还如未到时。
阿禾:什么意思?
陈先生:意思是,日子长,等的人还没到。可是蜻蜓也没走。
阿禾一个字一个字地记。
阿禾(旁白):夏至。先生给我写了一首诗。还有十二个节气。
""",
shots=[
 S("8", "大远景,固定", "傍晚,太阳还不肯落,荷塘边只剩两个人", "蛙声", 7,
   "extreme long shot at a long golden dusk, the sun still above the hills, the lotus pond still, a man and a child alone on the bank", "static camera, the light lingers"),
 S("9", "双人", "阿禾问", "阿禾:“先生,你写过诗吗?”陈先生:“写过很多。”", 5,
   "two-shot, A HE, AGE 8: [锚点], sitting beside MR CHEN, AGE 46: [锚点], on the bank", "static camera, she asks"),
 S("10", "近景", "陈先生", "阿禾:“在哪儿?”陈先生:“烧了,丢了,忘了。一首也没留下。”", 7,
   "close shot, MR CHEN, AGE 46: [锚点], smiling lightly at the water", "static camera, he answers easily"),
 S("11", "近景", "阿禾想了想", "阿禾:“那你写一首给我。我留着。”", 5,
   "close shot, A HE, AGE 8: [锚点], serious, looking up at him", "static camera, she asks"),
 S("12", "近景", "陈先生看了她很久", "—", 4,
   "close shot, MR CHEN, AGE 46: [锚点], looking at the child for a long moment, the smile fading", "extremely slow push in, he looks at her"),
 S("13", "特写", "柳枝在塘边湿泥上写字", "陈先生:“日长不肯暮,童子问归期。荷上蜻蜓立,还如未到时。”", 10,
   "close-up, a willow twig writing lines of characters in the wet mud at the edge of the pond, golden light", "static camera, the twig writes slowly", key=True),
 S("14", "双人", "阿禾问意思", "阿禾:“什么意思?”陈先生:“意思是,日子长,等的人还没到。可是蜻蜓也没走。”", 9,
   "two-shot, A HE, AGE 8: [锚点], and MR CHEN, AGE 46: [锚点], looking at the words in the mud", "static camera, she asks, he explains"),
 S("15", "大远景,固定", "荷塘边一大一小,泥上一首诗,蜻蜓还立在荷尖上", "阿禾(旁白):“夏至。先生给我写了一首诗。还有十二个节气。”", 9,
   "extreme long shot at the last light, the pond, a man and a child bent over the mud by the water, a dragonfly still on a lotus tip", "static camera, the sun finally sets", key=True,
   out="hold as the light goes; end of episode."),
]),
])

EPS["11"] = dict(cn="十一", jq="小暑", title="晒书",
summary="六月六,家家晒书晒衣。陈先生把一箱旧书摊满了私塾的院子。一阵风过,书页乱飞,许秀才去追,捡回来一张发黄的考卷,上面有考官的朱批:“不取”。是陈先生二十年前的卷子。许秀才读完,说:写得好。陈先生说:好文章不一定中。他把考卷折成一只纸船,给了阿禾。",
info=[("物候", "温风至,蟋蟀居宇,鹰始挚"), ("人物", "陈先生、许秀才、阿禾"),
      ("风俗", "六月初六晒书晒衣(晒伏),防霉防蛀。"),
      ("回收", "陈先生三次不中(第 2 集);第 21 集陈先生为许秀才题字。")],
curve="满(一院子书)→ 乱(风)→ 刺(“不取”)→ 认(写得好)→ 放(纸船)。",
scenes=[
dict(head="外景 私塾院子 午", short="私塾院子 午", era="夏", env="the small courtyard of the village school in blazing summer sun, open books and scrolls spread on mats, bamboo poles hung with robes, a well",
     tone="hot, bright, a little sad",
script="""
字幕:小暑。温风至,蟋蟀居宇,鹰始挚。
六月六。私塾的院子里铺满了竹席,竹席上摊满了书。竹竿上晾着陈先生仅有的两件长衫。
陈先生一本一本地翻开,让太阳晒。许秀才帮他搬箱子,阿禾在书和书中间跳来跳去。
一阵热风卷过院子。书页“哗啦啦”翻飞,几张散页飞上了墙头。
许秀才追过去,爬上墙头捡。
""",
shots=[
 S("1", "大远景,固定", "烈日下的村子,家家门口晾着衣被、书本", "蝉鸣;字幕“小暑”与三候", 8,
   "extreme long shot of LU PU VILLAGE under blazing summer sun, quilts, clothes and books spread out to dry before every house", "static camera, heat shimmer", key=True),
 S("2", "全景,俯拍", "私塾院子铺满竹席,竹席上摊满了书", "—", 6,
   "high-angle wide shot of the village school courtyard covered in bamboo mats with open books and scrolls drying in the sun, two robes on a bamboo pole", "static camera, pages flutter slightly"),
 S("3", "中景", "陈先生一本本翻开晒,许秀才搬箱子,阿禾在书间跳", "—", 6,
   "medium shot, MR CHEN, AGE 46: [锚点], opening books one by one, XU XIUCAI, AGE 20: [锚点], carrying a book chest, A HE, AGE 8: [锚点], hopping between the mats", "static camera, they work"),
 S("4", "全景", "一阵热风卷过,书页翻飞,几张散页飞上墙头", "“哗啦啦”", 5,
   "wide shot, a gust of hot wind sweeping the courtyard, pages flipping wildly, loose sheets flying up onto the wall top", "static camera, the pages fly"),
 S("5", "中景", "许秀才爬上墙头去捡", "—", 4,
   "medium shot, XU XIUCAI, AGE 20: [锚点], scrambling up onto the low courtyard wall to grab a loose yellowed sheet", "static camera, he climbs and grabs"),
]),
dict(head="外景 私塾院子 午后", short="私塾院子 午后", era="夏", env="the same school courtyard in the afternoon, the shade of the eaves",
     tone="a verdict reversed by one reader",
script="""
许秀才拿着那张纸,站在墙头上不动了。纸已经发黄,上面密密麻麻的小楷,卷尾一行朱批:不取。
他跳下来,拿给陈先生。
许秀才:先生,这是……
陈先生:二十年前的。头一回。
许秀才低头看完,又看了一遍。
许秀才:写得好。
陈先生:好文章不一定中。
他接过考卷,看了一眼朱批,笑了笑,一折、两折,折成了一只纸船,递给阿禾。
陈先生:拿去,放到河里。让它自己去临安。
阿禾捧着纸船,跑出了院子。
阿禾(旁白):小暑。先生的卷子变成了一只船。还有十一个节气。
""",
shots=[
 S("6", "近景,仰拍", "许秀才站在墙头,拿着那张纸不动了", "—", 4,
   "low-angle close shot, XU XIUCAI, AGE 20: [锚点], standing on the wall top reading a yellowed sheet, frozen", "static camera, he reads"),
 S("7", "特写", "发黄的考卷,密密麻麻的小楷,卷尾一行朱批(文字后期合成)", "—", 6,
   "close-up, a yellowed exam paper covered in tiny neat regular-script characters, a line of red ink at the end", "slow push in toward the red line", key=True),
 S("8", "双人", "他跳下来拿给陈先生", "许秀才:“先生,这是……”陈先生:“二十年前的。头一回。”", 7,
   "two-shot in the eaves' shade, XU XIUCAI, AGE 20: [锚点], holding out the paper, MR CHEN, AGE 46: [锚点], glancing at it calmly", "static camera, he holds it out"),
 S("9", "近景", "许秀才低头看完,又看一遍", "许秀才:“写得好。”", 6,
   "close shot, XU XIUCAI, AGE 20: [锚点], reading the paper through again, then looking up", "static camera, he reads and looks up"),
 S("10", "近景", "陈先生", "陈先生:“好文章不一定中。”", 4,
   "close shot, MR CHEN, AGE 46: [锚点], a calm small smile", "static camera, he says it simply", key=True),
 S("11", "特写", "他看一眼朱批,一折两折,折成一只纸船", "纸声", 7,
   "close-up, a scholar's ink-stained hands folding the old exam paper with its red verdict into a small paper boat", "static camera, the hands fold"),
 S("12", "双人", "纸船递给阿禾", "陈先生:“拿去,放到河里。让它自己去临安。”", 6,
   "two-shot, MR CHEN, AGE 46: [锚点], handing the paper boat to A HE, AGE 8: [锚点]", "static camera, the boat changes hands"),
 S("13", "大远景,固定", "河面上一只纸船顺流漂向东", "阿禾(旁白):“小暑。先生的卷子变成了一只船。还有十一个节气。”", 9,
   "extreme long shot of the bright river, a tiny paper boat floating downstream toward frame left, a small girl on the stone steps watching", "static camera, the paper boat drifts away", key=True,
   out="hold; end of episode."),
]),
])

EPS["12"] = dict(cn="十二", jq="大暑", title="萤",
summary="大暑,热得屋里待不住。全村的人把竹床搬到河边纳凉。萤火虫从草里飞起来。阿禾用纱袋装了一袋萤火虫,跑去送给许秀才“夜读”,惹得陈先生大笑。爷爷说,你娘小时候也干过一模一样的事。阿禾想了想,把纱袋打开,萤火虫飞散在河面上。",
info=[("物候", "腐草为萤,土润溽暑,大雨时行"), ("人物", "阿禾、周老篙、许秀才、陈先生、王婆、村民"),
      ("典故", "囊萤夜读:晋人车胤家贫,夏夜以练囊盛萤火照书。"),
      ("贯穿线", "全剧过半,阿禾第一次主动“放手”。")],
curve="闷(热)→ 凉(河边竹床)→ 亮(萤火)→ 笑(囊萤夜读)→ 想(娘也这样)→ 放。",
scenes=[
dict(head="外景 河边 夜", short="河边 夜", era="夏", env="the river bank by the ferry on a hot summer night, bamboo beds and stools set out under the camphor tree, fans, a half moon, fireflies rising from the grass",
     tone="languid, glowing", crowd="villagers lying on bamboo beds fanning themselves",
script="""
字幕:大暑。腐草为萤,土润溽暑,大雨时行。
夜里还是热。全村人把竹床搬到了河边,摇着扇子,说着闲话。
王婆躺在竹榻上,扇子越摇越慢。
草丛里,一点、两点,萤火虫飞起来了。越来越多。
孩子们跳起来去扑。阿禾拿着一只纱袋,扑得最准。
""",
shots=[
 S("1", "大远景,固定", "热夜的河边,竹床一排排,老樟树下扇影摇动", "蛙声、扇声;字幕“大暑”与三候", 9,
   "extreme long shot of the river bank on a hot summer night, rows of bamboo beds under the camphor tree, VILLAGERS fanning themselves, a half moon", "static camera, fans move slowly", key=True),
 S("2", "近景", "王婆躺在竹榻上,扇子越摇越慢", "—", 5,
   "close shot, GRANNY WANG, AGE 80: [锚点], lying on a bamboo couch, her fan slowing as she dozes", "static camera, the fan slows"),
 S("3", "特写", "草丛里一点、两点,萤火虫飞起来", "—", 6,
   "close-up of dark riverside grass, one, then two, then many fireflies lifting off and glowing", "static camera, the lights multiply", key=True),
 S("4", "中景", "孩子们跳起来扑,阿禾拿着纱袋扑得最准", "笑叫", 6,
   "medium shot, children leaping after fireflies in the dark, A HE, AGE 8: [锚点], sweeping a small gauze bag through the air and catching them", "static camera, they chase the lights"),
]),
dict(head="外景 河边 夜(续)", short="河边 夜 续", era="夏", env="the same river bank at night, a small table where the young scholar reads by a dim lamp, fireflies over the water",
     tone="laughter, then a memory",
script="""
许秀才在竹床边就着一盏小油灯看书,热得满头汗。
阿禾跑过来,把一袋亮闪闪的萤火虫挂在他的书上方。
阿禾:许哥哥,给你夜读!省灯油!
许秀才愣住。旁边的陈先生大笑起来,笑得咳嗽。
陈先生:车胤再世!
阿禾跑回爷爷身边,得意地坐下。
周老篙:你娘小时候,也干过一模一样的事。
阿禾:真的?
周老篙:装了一袋,挂在我的船篷上。说这样夜里撑船就不怕黑了。
阿禾看着河面,想了一会儿。她跑回许秀才那里,把纱袋取下来,解开了口子。
萤火虫一点点飞出去,飞散在黑黑的河面上。
阿禾(旁白):大暑。我把萤火虫放了。还有十个节气。
""",
shots=[
 S("5", "中景", "许秀才就着小油灯看书,满头汗", "—", 5,
   "medium shot, XU XIUCAI, AGE 20: [锚点], reading beside a bamboo bed by a tiny oil lamp, sweating", "static camera, he wipes his brow and reads"),
 S("6", "中景", "阿禾把一袋萤火虫挂在他书上方", "阿禾:“许哥哥,给你夜读!省灯油!”", 6,
   "medium shot, A HE, AGE 8: [锚点], hanging a glowing gauze bag of fireflies on a stick above the young man's book", "static camera, she hangs it proudly"),
 S("7", "近景", "许秀才愣住,陈先生在旁大笑", "陈先生:“车胤再世!”", 5,
   "close shot, XU XIUCAI, AGE 20: [锚点], blinking up at the glowing bag, MR CHEN, AGE 46: [锚点], beside him laughing and coughing", "static camera, the teacher laughs"),
 S("8", "双人", "阿禾坐回爷爷身边", "周老篙:“你娘小时候,也干过一模一样的事。”阿禾:“真的?”", 7,
   "two-shot on a bamboo bed, A HE, AGE 8: [锚点], sitting down proudly beside ZHOU THE FERRYMAN, AGE 68: [锚点], who fans her", "static camera, he fans and speaks"),
 S("9", "近景", "周老篙", "周老篙:“装了一袋,挂在我的船篷上。说这样夜里撑船就不怕黑了。”", 8,
   "close shot, ZHOU THE FERRYMAN, AGE 68: [锚点], looking at the FERRY BOAT moored in the dark", "static camera, he remembers", key=True),
 S("10", "近景", "阿禾看着河面,想了一会儿", "—", 4,
   "close shot, A HE, AGE 8: [锚点], looking at the dark river, thinking", "static camera, she thinks"),
 S("11", "特写", "她解开纱袋口子", "—", 4,
   "close-up, small fingers untying the mouth of a glowing gauze bag", "static camera, the knot comes loose"),
 S("12", "大远景,固定", "萤火虫飞出去,散在黑黑的河面上", "阿禾(旁白):“大暑。我把萤火虫放了。还有十个节气。”羌笛", 10,
   "extreme long shot of the dark river at night, a cloud of fireflies drifting out from the bank and spreading over the water, the moored ferry boat", "static camera, the lights spread and fade", key=True,
   out="hold as the fireflies scatter; end of episode."),
]),
])
