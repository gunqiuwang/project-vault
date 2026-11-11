# 《高处》分镜脚本与生成提示词生成器
# 输出: md/40-shots.md(视觉总纲 + 第 1–6 集), md/41-shots2.md(第 7–12 集)

STYLE = ("cinematic realism, 35mm film look, natural practical light, restrained composition, "
         "shallow depth of field, 2:1 widescreen, 24fps, no text, no watermark")

GRADE = {
    "95": ("1990s 回忆 · 褪色暖调", "1990s rural memory, faded warm colors, soft vignette, gentle grain"),
    "08": ("2008 · 湿热黄绿", "humid summer 2008 Shenzhen, warm green-yellow grade, heavy film grain, sodium streetlights"),
    "10": ("2009–2012 · 钠灯橙", "early-2010s Shenzhen, saturated sodium-orange nights, warm tungsten interiors, light grain"),
    "14": ("2013–2016 · 玻璃青", "mid-2010s Shenzhen, cleaner digital look, cool teal reflections from glass towers"),
    "18": ("2017–2019 · 阴天中性", "late-2010s Shenzhen, neutral soft overcast light, muted colors"),
    "21": ("2020–2022 · 冷灰", "2020-2022, desaturated cold grey, fluorescent interiors, masks visible on people"),
    "23": ("2023 台风夜 · 蓝黑", "typhoon night 2023, near-monochrome blue-black, horizontal rain, red-blue emergency lights, searchlights"),
    "27": ("2024–2027 · 晨雾", "2024-2027, pale morning light, soft haze, low contrast, quiet"),
}

C = {
 "shen08": "Shen Jibai, 28, tall lean Chinese man, sharp cheekbones, short neat hair, crisp white shirt, tired intelligent eyes",
 "shen12": "Shen Jibai, 32, tall lean Chinese executive, dark suit, slight Jiangxi reserve, faint shadows under eyes",
 "shen18": "Shen Jibai, 38, tall lean Chinese chairman, graying temples, deep lines under eyes, dark suit",
 "shen22": "Shen Jibai, 42, gaunt tall Chinese man, short hair with gray, dark jacket, pale face",
 "shen23": "Shen Jibai, 43, gaunt tall Chinese man, soaked dark wool overcoat over an old worn sweater with frayed cuffs",
 "he08": "He Jun, 23, short stocky Chinese man from Sichuan, crew cut, thick eyebrows, mud-soaked clothes",
 "he12": "He Jun, 27, short stocky Chinese man, crew cut, thick eyebrows, white shirt buttoned to the top, small scar on the web of his hand",
 "he15": "He Jun, 30, stocky Chinese site foreman, crew cut, thick eyebrows, dark jacket, calm flat expression",
 "he18": "He Jun, 33, stocky Chinese man, crew cut, thick eyebrows, black suit, composed face like river-worn stone",
 "he22": "He Jun, 37, stocky Chinese man, crew cut streaked with gray, thick eyebrows, faded work jacket",
 "he23": "He Jun, 38, stocky Chinese man, gray-streaked crew cut, thick eyebrows, soaked faded work jacket, slightly stooped",
 "lin08": "Lin Wan, 25, slim Chinese woman from Hunan, long hair tied back, real-estate sales uniform, still watchful eyes",
 "lin10": "Lin Wan, 27, slim Chinese woman, short bob haircut, crisp white shirt buttoned high, red pen in hand",
 "lin17": "Lin Wan, 34, slim Chinese executive woman, short bob, white shirt, calm unreadable face",
 "lin21": "Lin Wan, 38, very thin Chinese woman, short hair grown out, no makeup, sunken cheeks, old grey sweater",
 "lin27": "Lin Wan, 44, thin pale Chinese woman, hair in a low ponytail, plain grey coat, small cloth bag",
 "zhou08": "Zhou Yu, 27, thin Chinese architect, glasses, rolled shirt sleeves, mechanical pencil behind ear",
 "zhou13": "Zhou Yu, 32, thin Chinese man, glasses, longish hair, old T-shirt",
 "zhou20": "Zhou Yu, 39, thin Chinese man, glasses, long uncut hair, stubble, blue surgical mask",
 "zhou27": "Zhou Yu, 46, thin Chinese man, glasses, short hair, old jacket, empty hands",
 "chen08": "Chen Mo, 28, Chinese newspaper reporter, ponytail, rain jacket, notebook in hand",
 "chen15": "Chen Mo, 35, Chinese woman journalist, ponytail, plain cardigan, tired determined eyes",
 "chen20": "Chen Mo, 40, Chinese freelance journalist, ponytail with some gray, plain clothes, mask pulled down",
 "chen27": "Chen Mo, 47, Chinese woman, gray-streaked ponytail, plain coat, bottle of water in hand",
 "xu08": "Xu Zhiyi, 29, elegant Chinese heiress, silk robe, hair down, composed face",
 "xu18": "Xu Zhiyi, 39, elegant Chinese businesswoman, black dress, controlled grief, fine chain necklace",
 "xu25": "Xu Zhiyi, 46, elegant Chinese chairwoman, tailored navy suit, fine chain necklace with a tiny old key",
 "chuan": "He Xiaochuan, 19, skinny Chinese construction worker from Sichuan, sunburnt, gap in his front teeth, bright grin, hard hat",
 "zheng": "Zheng Jianguo, 51, weathered Chinese site supervisor, white safety helmet, rain cape, old Nokia phone",
 "ayong": "A-Yong, 19, Chinese construction worker, round face, single eyelids, wet hair stuck to forehead, cheap raincoat",
 "liu": "Liu Jianbo, 40, Chinese firefighter, helmet and reflective turnout gear, rain streaming down",
 "tang": "Tang Siqi, 26, cheerful Chinese saleswoman from Jiangxi, round face, ponytail, sales blazer",
 "qian": "Qian Guodong, 50, precise Chinese factory quality manager, glasses, short-sleeved shirt, pen in pocket",
 "liujie": "Liu Guifang, 45, Chinese housekeeper from Sichuan, apron, kind practical face",
 "xuzhen": "Xu Zhen, 38, sleek Chinese businessman, slicked hair, expensive casual shirt",
 "gao": "Gao Min, 41, severe elegant Chinese bank risk officer, short hair, reading glasses, grey suit",
 "gu": "Gu Yuan, 45, tall thin Chinese photographer, half-gray hair, old linen shirt, camera calluses",
 "xiaoyu": "Zheng Xiaoyu, 24, earnest young Chinese woman, plain office clothes, small backpack",
 "chunmei": "Wang Chunmei, 32, sturdy Chinese woman from rural Sichuan, hair in a bun, simple floral blouse",
 "linqiang": "Lin Qiang, 34, soft-faced Chinese man from a small town, cheap polo shirt, face mask",
 "li": "Li Guoqiang, 36, Chinese chauffeur, ex-soldier posture, buzz cut, black suit, white gloves",
 "xuhs": "Xu Huaishan, 75, frail Chinese tycoon in a hospital bed, sharp calculating eyes",
 "shenfu": "Shen's father, 70s, frail Chinese villager in a wheelchair, white hair, blanket over legs",
}

SIZE = {"大远景":"extreme wide shot","远景":"wide shot","全景":"full shot","中景":"medium shot",
        "近景":"medium close-up","特写":"close-up","大特写":"extreme close-up","主观":"POV shot",
        "俯拍":"high-angle shot","仰拍":"low-angle shot","长焦":"long-lens telephoto shot"}
MOVE = {"固定":"locked-off camera","缓推":"slow push-in","缓拉":"slow pull-back","摇":"slow pan",
        "手持":"handheld camera","跟":"tracking shot following the subject","升":"slow crane up",
        "降":"slow crane down","慢放":"slow motion"}

EPS = {}
def ep(n, title, shots): EPS[n] = (title, shots)
# 镜头: (编号, 场, 景别, 运动, 中文画面, 英文动作, [人物], 年代色调)

ep(1, "网 · 2008 · 老郑", [
 ("1-01","1","大远景","升","台风夜,四十二层没有墙的烂尾楼,探照灯打在东南角一个很小的人影上",
  "an unfinished 42-storey concrete skyscraper with no walls in a typhoon, a searchlight finds a tiny human figure at the top south-east corner", [], "23"),
 ("1-02","2","中景","手持","警戒线前,一个浑身湿透的男人钻过警戒带,跑进漆黑的楼梯间",
  "a soaked man ducks under police tape and runs into a pitch-black stairwell", ["he23"], "23"),
 ("1-03","2","中景","固定","无牌黑车,司机撑伞,穿大衣的男人不要伞,递出身份证;风掀开大衣露出旧毛衣",
  "an unplated black sedan, a driver holds a large umbrella, a man in an overcoat refuses it and hands his ID to police; wind lifts the coat revealing an old sweater", ["shen23"], "23"),
 ("1-04","3","近景","缓推","板房里,老郑在烟盒纸上算钱,存折上 14600,电视里放奥运女排",
  "inside a site cabin, a supervisor writes numbers on a cigarette pack beside an open bankbook, Olympic volleyball on a small TV", ["zheng"], "08"),
 ("1-05","5","全景","固定","正午三十一层楼板边,小川捧本子画画,周屿递给他一支自动铅笔,远处是海",
  "noon on an open 31st-floor slab, a young worker sketches in a notebook while an architect hands him a mechanical pencil, the sea in the distance", ["chuan","zhou08"], "08"),
 ("1-06","7","中景","手持","工人用刀割断安全网的尼龙绳,绿色的网一片片垮下来,露出黑天",
  "workers cut nylon ropes with knives, green safety nets collapse panel by panel exposing the black night sky", ["chuan"], "08"),
 ("1-07","7","特写","固定","诺基亚屏幕,拍下楼板上一大堆湿漉漉的网",
  "an old Nokia phone screen photographing a wet heap of green safety netting on a concrete slab", ["zheng"], "08"),
 ("1-08","9","全景","手持","一块两米高的幕墙玻璃悬在半空像帆;小川回头笑,举手机录海",
  "a two-metre glass curtain-wall panel swings in mid-air like a sail; the young worker turns back grinning, filming the sea with his phone", ["chuan"], "08"),
 ("1-09","10","近景","缓推","东南角空了,一根临时钢丝绳的一头垂在楼外轻轻晃",
  "an empty south-east corner, the loose end of a temporary steel cable dangles outside the slab swaying in the wind (no person, no fall shown)", ["zheng"], "08"),
 ("1-10","13","全景","固定","工地门口,年轻人跪在雨里;售楼处的女人撑开伞,遮在他头顶",
  "at a construction gate a young man kneels in the downpour; a saleswoman steps out and holds an umbrella over his head", ["he08","lin08"], "08"),
 ("1-11","19","仰拍","缓推","三十一层东南角的玻璃在太阳下亮得晃眼,绿色安全网在风里鼓起又落下",
  "low angle up a finished tower, the 31st-floor corner glass blazing in the sun, green safety nets billowing and falling", [], "08"),
 ("1-12","20","中景","固定","卧室门口,浑身湿透的丈夫看着镜前的妻子",
  "a soaked husband stands in a bedroom doorway looking at his wife at her vanity mirror", ["shen08","xu08"], "08"),
])

ep(2, "河 / 样板间 · 2009–2010 · 陈默、唐思琪", [
 ("2-01","1","主观","手持","没有灯的楼梯井,手电光往上晃,红漆 28F 一闪而过",
  "climbing a dark stairwell, a flashlight beam shakes upward, a red spray-painted '28F' flashes past", [], "23"),
 ("2-02","3","全景","固定","城中村水泥明渠,警戒线,白布盖着尸体,一只脚有鞋一只没有",
  "a concrete canal between dense urban-village buildings, police tape, a body under a white sheet, one shoe missing", ["chen08"], "10"),
 ("2-03","5","远景","固定","最小的告别厅,最后一排角落站着一个年轻男人,没有拿香",
  "the smallest funeral hall, a young man stands alone in the back corner without incense", ["he08","chen08"], "10"),
 ("2-04","7","中景","摇","河边大排档老板的锅铲指向下游那一段坏掉的栏杆,警戒带在风里飘",
  "a riverside food-stall owner points his spatula down the canal to a broken railing with fluttering tape", ["chen08"], "10"),
 ("2-05","10","特写","固定","冰箱门上三张便签:何峻、郑建国、沈?",
  "three sticky notes on a fridge door handwritten in Chinese", [], "10"),
 ("2-06","11","中景","固定","板房售楼处沙盘后,两个女孩坐在地上吃盒饭,林晚把肉拨到一边",
  "behind a sales-office scale model, two young women eat boxed lunches on the floor, one pushes the meat aside to save it", ["lin08","tang"], "08"),
 ("2-07","12","中景","缓推","年会喧闹里,林晚望向最后一桌——唯一一个不喝酒、端着可乐的人",
  "at a noisy corporate banquet a woman looks toward the back table at the only man holding a cola instead of liquor", ["lin10","he08"], "10"),
 ("2-08","15","中景","固定","样板间淡蓝色的客厅,唐思琪站在门口,走廊尽头主卧的门缝一片黑",
  "a show-flat living room in pale blue city light, a young woman frozen at the door, a dark sliver of a half-open bedroom door at the end of the hall", ["tang"], "10"),
 ("2-09","17","特写","固定","折叠桌上的笔筒插满同一个牌子的自动铅笔;她没有装走",
  "a pencil cup crammed with identical mechanical pencils on a folding table in an emptied tiny room", ["lin10"], "10"),
 ("2-10","20","中景","固定","台阶上的林晚,塔吊的影子从她脸上扫过去",
  "a woman in a white shirt on steps, the shadow of a turning tower crane sweeps across her face", ["lin10"], "10"),
])

ep(3, "渗水 / 兄弟 · 2011–2012 · 钱国栋、刘姐", [
 ("3-01","2","特写","缓推","一滴水落在手背上;吊顶接缝洇出一条像地图的黄色水印",
  "a drop of water lands on a man's hand; a yellow leak stain like a map spreads across a ceiling seam", ["qian"], "10"),
 ("3-02","4","中景","固定","总部大堂,年轻的总经理一个人走出电梯,向二十几个业主鞠躬",
  "in a corporate lobby a young executive steps out of the elevator alone and bows to a crowd of angry homeowners", ["shen12","qian"], "10"),
 ("3-03","5","中景","固定","工程部的人进门换鞋套,看墙上澳门大三巴前的旧合影",
  "a site engineer in shoe covers studies an old couple's photo in front of the Ruins of St. Paul's, Macau", ["he12"], "10"),
 ("3-04","8","全景","缓推","澳门贵宾厅,厚地毯,荷官翻开红心 K,筹码推出去又推回来",
  "a private Macau baccarat room, thick carpet, the dealer flips a king of hearts, chips slide across the felt", ["qian"], "10"),
 ("3-05","9","远景","固定","暗红走廊尽头,一个短发结实的背影喝着可乐起身离开",
  "at the end of a dark red hotel corridor, a stocky short-haired man with a cola can rises and walks away", ["he12"], "10"),
 ("3-06","13","中景","固定","淡黄色婴儿房没开灯,许知意靠墙坐在婴儿床边的地上,木头小鸟挂饰",
  "an unlit pale-yellow nursery, a woman sits on the floor against the wall beside an empty crib with hanging wooden birds", ["xu08"], "10"),
 ("3-07","15","中景","固定","门垫上擦鞋底擦了很久的年轻人,白衬衫扣到最上面一颗,拎着水果",
  "a young man in a white shirt buttoned to the top wipes his shoes on a doormat for a long time, holding a bag of fruit", ["he12","liujie"], "10"),
 ("3-08","16","近景","固定","厨房灯下,何峻擦碗,每一个对着灯看一下;虎口的疤",
  "under a kitchen light a man dries bowls, holding each one up to the light; a scar on the web of his hand", ["he12","liujie"], "10"),
 ("3-09","17","近景","固定","书房门缝里两个人的声音,刘姐在走廊关灯",
  "a housekeeper switches off a hallway light beside a study door left ajar, warm light spilling out", ["liujie"], "10"),
 ("3-10","19","中景","固定","红灯,路边白色皮卡里的人抽着烟望向许家",
  "at a red light, a man in a white pickup truck smokes and stares toward a lakeside mansion", ["he12"], "10"),
])

ep(4, "天兔 · 2013 · 周屿", [
 ("4-01","2","全景","摇","城中村小屋墙上钉满楼梯画,螺旋的、悬挑的",
  "a tiny urban-village room, every wall covered with drawings of staircases, spiral and cantilevered", ["zhou13"], "14"),
 ("4-02","5","中景","固定","守灵夜,堂屋只剩她一人,从供桌那碗红烧肉里夹一块慢慢嚼",
  "a funeral vigil at night, a woman alone takes a piece of braised pork from the offering bowl before her father's portrait and chews slowly", ["lin10"], "14"),
 ("4-03","7","中景","固定","高铁车厢,窗外黄了的稻田往后退,她闭着眼",
  "a high-speed train carriage, golden rice fields sliding past the window, a woman with eyes closed beside a man by the window", ["lin10","zhou13"], "14"),
 ("4-04","8","全景","手持","深圳北站玻璃门外,雨横着走,一块广告牌翻滚过广场",
  "outside a station's glass doors the rain flies sideways and a billboard tumbles across the plaza", ["lin10","zhou13"], "14"),
 ("4-05","9","全景","跟","停电的街道积水到小腿,她拎着高跟鞋光脚走,头发贴在脸上,在笑",
  "on a blacked-out street flooded to the shins, a woman walks barefoot carrying her heels, hair plastered to her face, laughing", ["lin10","zhou13"], "14"),
 ("4-06","10","中景","固定","蜡烛光里,她穿着太大的旧 T 恤坐在床边小口喝水,墙上楼梯的影子在晃",
  "by candlelight a woman in an oversized old T-shirt sits on a bed sipping water, staircase drawings' shadows trembling on the wall", ["lin10","zhou13"], "14"),
 ("4-07","11","特写","固定","被门缝的风吹倒向一边的烛火;剪影(亲密戏只拍到这里)",
  "a candle flame bent sideways by a draft, two silhouettes blurred behind it, tasteful and non-explicit", [], "14"),
 ("4-08","13","大特写","固定","静音的手机亮起,来电显示只有一个字:川",
  "a silent phone lighting up on a dark floor, caller ID shows a single Chinese character", [], "14"),
 ("4-09","15","俯拍","固定","晨光里满是断枝的巷子,她光着脚拎着鞋走出去,一次也没回头",
  "high angle from a window: a debris-filled alley at dawn, a barefoot woman carrying her shoes walks away without looking back", ["lin10"], "14"),
 ("4-10","16","特写","缓推","效果图三十一层阳台上一个很小的人;废纸上铅笔写的'川'",
  "a rendering on a monitor zoomed to a tiny figure on a 31st-floor balcony, then a scrap of paper with one pencilled character", ["zhou13"], "14"),
])

ep(5, "局 / 墙 · 2014–2015 · 许振、陈默", [
 ("5-01","1","特写","固定","楼板积水里漂着湿透的效果图'深圳的新高度',一只脚踩过",
  "a soaked marketing rendering floats in a puddle on a concrete slab, a boot steps through it", [], "23"),
 ("5-02","3","中景","固定","茶楼包间,何峻用两根手指在桌上轻敲两下,信封推过去",
  "in a private tea room a man taps the table twice with two fingers as an envelope is slid toward him", ["he15","xuzhen"], "14"),
 ("5-03","5","主观","慢放","KTV 包间灯光开始晃,声音变远;门被撞开,灯全亮",
  "POV in a karaoke room, lights begin to smear and swim, then the door bursts open and harsh lights flood on", ["xuzhen"], "14"),
 ("5-04","7","中景","固定","走廊尽头楼梯口站着短发白衬衫的女人,对他点头",
  "at the end of a mansion corridor a short-haired woman in a white shirt nods at a shaken man", ["lin10","xuzhen"], "14"),
 ("5-05","8","全景","固定","塔吊吊着钢筋从两人头顶移过,影子扫过地面;'太早了'",
  "a tower crane carries a bundle of rebar overhead, its shadow sweeping across a man at a car window", ["he15","xuzhen"], "14"),
 ("5-06","10","中景","跟","抱着纸箱走出报社大楼的女记者",
  "a laid-off woman journalist walks out of a newspaper building carrying a cardboard box", ["chen15"], "14"),
 ("5-07","12","全景","缓推","出租屋整面墙的剪报和便签,红毛线全部系向中间一个名字",
  "a whole wall of clippings and sticky notes, red yarn strung from every item to one central name", ["chen15"], "14"),
 ("5-08","16","中景","固定","黄昏工地门口,逆光里他教年轻工人系安全带",
  "at a construction gate at dusk, a backlit foreman patiently shows a young worker how to clip a safety harness", ["he15","chen15"], "14"),
 ("5-09","17","全景","固定","关了灯,窗外光照着那面墙",
  "a dark room, only streetlight through the window falling on the yarn wall, a woman sitting in shadow", ["chen15"], "14"),
])

ep(6, "授信 · 2016 · 高敏", [
 ("6-01","1","特写","固定","被风撞开又撞上的铁门,印着褪色的监管账户字样",
  "a temporary steel gate banging open and shut in the storm, faded bank lettering on it", [], "23"),
 ("6-02","3","特写","固定","八页纸,最后一段被荧光笔划出",
  "eight typed pages on a desk, the last paragraph highlighted in yellow", ["gao"], "14"),
 ("6-03","5","中景","固定","展厅黑白照片:钢筋像肋骨;林晚介绍高瘦的摄影师,然后不见了",
  "in a gallery of black-and-white construction photos, a woman introduces a tall thin photographer, then slips out of frame", ["gao","gu","lin17"], "14"),
 ("6-04","7","大远景","固定","凌晨四点没有墙的楼板,她抓着他的胳膊,太阳从海湾升起",
  "4am on a wall-less floor slab of a new tower, a woman holds a man's arm in the wind as the sun rises over the bay", ["gao","gu"], "14"),
 ("6-05","8","特写","固定","阳台雨夜,他的手,拿相机磨出的茧;镜头转向栏杆上的雨",
  "a rainy hotel balcony at night, close on a man's calloused hand, then the camera drifts to rain on the railing (non-explicit)", ["gu"], "14"),
 ("6-06","9","长焦","固定","从很远的地方拍过来的一个镜头:阳台上一个女人的身影,边缘发虚",
  "an extreme telephoto surveillance-like shot from far away, a woman alone on a hotel balcony at dawn, soft edges", ["gao"], "14"),
 ("6-07","11","特写","固定","茶几上拆开的牛皮纸信封,十几张偷拍照片",
  "a torn kraft envelope on a coffee table spilling covert photographs", [], "14"),
 ("6-08","15","中景","固定","电梯门关上之前,林晚抬手按了一下眼角",
  "as elevator doors close, a composed businesswoman briefly presses the corner of her eye", ["lin17"], "14"),
 ("6-09","16","特写","缓推","一张黑白照片:分不清哪里是海哪里是天;背面潦草的钢笔字",
  "a black-and-white photo of grey sea and grey sky with no horizon, scrawled ink on the back", ["gao"], "18"),
])

LEFT = [1,2,3,4,5,6]

ep(7, "面试 / 磁带 · 2017–2018 · 郑小雨、许知意", [
 ("7-01","1","特写","固定","香港公寓没开灯,女人的手捏住链子上的小钥匙,手机里是直播",
  "a dark Hong Kong apartment during a No.10 typhoon signal, a woman's fingers grip a tiny old key on a neck chain, a livestream glowing on a phone", [], "23"),
 ("7-02","4","中景","固定","小会议室,面试官合上简历",
  "a small meeting room, a short-haired interviewer closes a resume across from a nervous young woman", ["lin17","xiaoyu"], "18"),
 ("7-03","6","近景","固定","潮汕牛肉火锅店,一片牛肉被夹进对面的碗里",
  "a humble beef hotpot restaurant, a woman places a slice of beef into the young woman's bowl", ["lin17","xiaoyu"], "18"),
 ("7-04","9","特写","固定","手机里的庆典合影,第三排边上半张往画面外走的脸;盘子摔在地上",
  "a phone showing a group photo, a half-face at the edge walking out of frame; a plate shatters on the floor", ["xiaoyu"], "18"),
 ("7-05","13","特写","固定","小牛皮纸袋里的黑色移动硬盘,贴着写密码的便签",
  "a small black external hard drive with a password sticky note inside a kraft paper bag on a restaurant table", ["xiaoyu"], "18"),
 ("7-06","18","特写","固定","病床上的老人从枕头下摸出一把小钥匙塞进女儿手心",
  "a dying old man pulls a small key from under his pillow and presses it into his daughter's palm", ["xuhs","xu18"], "18"),
 ("7-07","19","中景","固定","殡仪馆走廊,他把那张纸对折再对折,放进内袋",
  "in a funeral-home corridor a man folds a schedule sheet twice and tucks it into his suit pocket facing a woman in black", ["he18","xu18"], "18"),
 ("7-08","20","全景","缓推","董事会长桌末端,林晚一笔签下任命书",
  "at the far end of a long boardroom table, a woman signs an appointment document in one firm stroke", ["lin17","xu18","shen18"], "18"),
 ("7-09","24","特写","缓推","台风停电的书房,蜡烛,转动的磁带,标签 8.22",
  "a study during a typhoon blackout, candlelight, a cassette turning in an old recorder, label reading 8.22", ["xu18"], "18"),
 ("7-10","28","特写","固定","天亮,她把钥匙穿上细链子,挂在自己脖子上",
  "at dawn a woman threads a tiny key onto a fine chain and fastens it around her neck", ["xu18"], "18"),
])

ep(8, "第二部手机 · 2019 · 春梅", [
 ("8-01","1","中景","固定","台风夜城中村饭桌,一碗卧了两个鸡蛋的面,对面空椅子",
  "a typhoon night in an urban-village flat, a bowl of noodles with two eggs on the table, an empty chair opposite", ["chunmei"], "23"),
 ("8-02","2","全景","固定","刚铺好的水泥路上的流水席,他敬酒用的是可乐",
  "a rural Sichuan wedding banquet on a freshly paved concrete road, the groom toasts guests with cola", ["he08","chunmei"], "10"),
 ("8-03","9","中景","固定","清明坟前一罐拉开的可乐冒着气泡",
  "at a hillside grave during Qingming, an opened cola can fizzes in front of the headstone, a man crouching", ["he22"], "18"),
 ("8-04","14","特写","缓推","铁皮饼干盒:碎屏诺基亚、贴着发白卡通贴纸的山寨机、一张银行卡",
  "a tin biscuit box holding a shattered Nokia wrapped in tape, a cheap phone with a faded cartoon sticker, and a bank card", ["chunmei"], "18"),
 ("8-05","18","中景","固定","阳台上他抽烟,楼下烧烤摊的烟一缕一缕往上飘",
  "a man smokes on a balcony, barbecue smoke from the alley below drifting upward", ["he22","chunmei"], "18"),
 ("8-06","19","中景","固定","出门前,白衬衫扣到最上面一颗",
  "a man leaving home in a white shirt buttoned to the very top, his wife watching from the kitchen", ["he22","chunmei"], "18"),
 ("8-07","22","长焦","固定","隔着高档小区的铁栅栏,花坛边一个人一根接一根抽烟,仰头看楼",
  "through the iron fence of an upscale compound, a man on a planter edge chain-smokes, staring up at a high floor", ["he22"], "18"),
 ("8-08","23","中景","固定","他低下头,两只手撑在膝盖上,肩膀在动;栅栏外她攥紧铁杆",
  "the man bows his head, hands on knees, shoulders shaking; outside the fence a woman's knuckles whiten on the bars", ["he22","chunmei"], "18"),
 ("8-09","27","中景","固定","她从后面抱住他,他的手覆在她手上",
  "in a dark bedroom a woman embraces her husband from behind and his hand covers hers", ["he22","chunmei"], "18"),
])

ep(9, "反向 · 2020 · 陈默", [
 ("9-01","2","全景","固定","空荡的街,红马甲大妈坐在铁栅栏后的折叠桌前",
  "an empty street in early 2020, a volunteer in a red vest sits at a folding table behind a metal barrier with a thermometer gun", ["chen20"], "21"),
 ("9-02","7","中景","固定","六楼门开,戴口罩的长发男人,身后墙上全是楼梯",
  "a sixth-floor door opens on a long-haired masked man, staircase drawings covering the wall behind him", ["zhou20","chen20"], "21"),
 ("9-03","8","近景","固定","桌上那支自动铅笔被手指拨过来,拨过去;录音笔红灯",
  "a finger nudges a mechanical pencil back and forth on a table beside a recording pen's red light", ["zhou20"], "21"),
 ("9-04","16","全景","固定","最后一班公交,空荡荡的深南大道,亮灯却没有人的写字楼",
  "the last bus, a lone passenger by the window, an empty eight-lane boulevard and lit, deserted office towers", ["chen20"], "21"),
 ("9-05","18","特写","固定","红毛线一根一根从图钉上脱下来,垂在墙上像断了的网",
  "red yarn pulled off pushpins one by one, hanging slack on the wall like a torn net", ["chen20"], "21"),
 ("9-06","20","全景","缓拉","重新系好的毛线全部往上走,最上面是效果图'深圳的新高度'",
  "the re-strung yarn wall, every line now leading upward to a skyscraper rendering pinned at the top", ["chen20"], "21"),
 ("9-07","21","近景","固定","她坐下,两只手夹在膝盖中间止住发抖",
  "a woman sits down and clamps her trembling hands between her knees", ["chen20"], "21"),
 ("9-08","25","特写","固定","电脑文档第一行:这是一个关于等待的故事",
  "a laptop screen with a single line of Chinese text and a blinking cursor in a dark room", [], "21"),
 ("9-09","26","远景","固定","窗外很远的前海,塔吊顶上的红色航标灯一闪一闪",
  "through a window, far-off tower cranes blink red aviation lights over the harbor district", ["chen20"], "21"),
])

ep(10, "面 · 2021 · 林强", [
 ("10-01","2","中景","固定","1995 年乡下老屋,一碗红烧肉,女孩把自己那块拨到碗边",
  "a poor rural home in 1995, a bowl of braised pork, a 12-year-old girl pushes her one piece to the edge of her bowl while her brother grabs more", [], "95"),
 ("10-02","10","全景","手持","写字楼下几百个投资人,横幅上印着她笑着演讲的照片",
  "hundreds of protesting investors below an office tower, a banner printed with a smiling woman giving a speech", ["linqiang"], "21"),
 ("10-03","13","中景","固定","老小区五楼门开,穿旧毛衣、瘦脱了形的姐姐",
  "a fifth-floor door in an old walk-up opens on a gaunt woman in an old grey sweater", ["lin21","linqiang"], "21"),
 ("10-04","14","特写","固定","一张银行卡推过桌面,旁边一碗吃了一半的泡面",
  "a bank card slid across a bare table next to a half-eaten cup of instant noodles", ["lin21"], "21"),
 ("10-05","16","全景","跟","深夜握手楼窄巷,只有一家面馆亮着,门口大锅冒白气",
  "late night in a narrow urban-village alley, a single noodle shop lit, steam pouring from a big stockpot at the door", ["lin21"], "21"),
 ("10-06","17","远景","固定","隔着白气:她和一个背对镜头的男人对坐吃面,一句话不说",
  "seen through steam from across the alley: a woman and a man with his back to camera eat noodles in silence", ["lin21","he22"], "21"),
 ("10-07","19","特写","固定","她把碗里最后一块牛肉夹进他的碗里",
  "close on chopsticks: a woman moves the last piece of beef from her bowl into the man's bowl", ["lin21"], "21"),
 ("10-08","21","主观","固定","手机取景框里的面馆,大拇指悬在快门上,然后离开",
  "POV through a phone camera framing the noodle shop, a thumb hovers over the shutter, then lifts away", ["linqiang"], "21"),
 ("10-09","27","特写","固定","手机推送:法定代表人林某投案自首",
  "a phone notification about a company's legal representative surrendering to police, on a small-town balcony at night", ["linqiang"], "21"),
])

ep(11, "后视镜 · 2022 · 小李", [
 ("11-01","1","中景","固定","暴雨里的网约车,后视镜里空的后座,远处四十二层的楼",
  "a ride-hailing car in torrential rain, the rear-view mirror shows an empty back seat, a 42-storey shell in the distance", ["li"], "23"),
 ("11-02","3","特写","固定","后视镜里:后座两个男人并排坐着,一路不说话",
  "rear-view mirror shot: two men sit side by side in the back of a luxury car, silent", ["shen18","he18"], "18"),
 ("11-03","7","特写","固定","后视镜里那张很白的脸:'限制出境'",
  "rear-view mirror shot of a pale executive with eyes closed after being stopped at the border", ["shen22","li"], "21"),
 ("11-04","10","中景","手持","人群里矿泉水瓶砸在他额头上,他没有躲",
  "in a crowd of angry creditors a plastic water bottle hits a man's forehead and he does not flinch", ["shen22"], "21"),
 ("11-05","11","特写","缓推","后视镜里,他用纸巾按住沈的伤口,低头看着那张脸",
  "rear-view mirror: one man presses a tissue to the other's bleeding forehead and studies his face", ["he22","shen22"], "21"),
 ("11-06","14","特写","固定","同一块后视镜里,一张睡着的脸,镜子边缘半只醒着的眼睛",
  "a single rear-view mirror holding a sleeping face and, at its edge, half of another man's wakeful eye", ["shen22","he22"], "21"),
 ("11-07","15","特写","固定","膝盖上的手:攥紧,松开,攥紧",
  "close on a man's hand on his knee in a moving car: clenching, relaxing, clenching", ["he22"], "21"),
 ("11-08","19","中景","固定","山村院子的灯下,轮椅上的父亲递出一个旧蓝布包",
  "under a bare bulb in a mountain village courtyard, a father in a wheelchair hands his son an old blue cloth bundle of cash", ["shenfu","shen22"], "21"),
 ("11-09","24","全景","固定","贴满法院封条的车中间,他一个人站着,很小",
  "in an underground garage full of court-sealed cars, one man stands alone, small", ["shen22"], "21"),
])

ep(12, "四十二层 / 伸手 · 2023–2027 · 阿勇、陈默", [
 ("12-01","1","中景","固定","铁皮宿舍里十几部手机同时亮起尖叫",
  "inside a tin-roofed workers' dormitory a dozen phones light up at once with emergency alerts", ["ayong"], "23"),
 ("12-02","4","中景","固定","开工前,楼梯口一个一个检查安全带挂钩",
  "before a shift, a foreman at a stairwell checks every worker's harness hook one by one", ["he22","ayong"], "21"),
 ("12-03","13","全景","手持","四十二层东南角,他举着手机直播,身后是对岸香港的灯",
  "on the open 42nd floor in the typhoon a young worker livestreams on his phone, Hong Kong lights across the bay behind him", ["ayong"], "23"),
 ("12-04","16","中景","固定","湿透的大衣男人把缠满胶带的牛皮纸袋塞进少年手里",
  "a man in a soaked overcoat presses a taped kraft-paper parcel into a young worker's hands", ["shen23","ayong","he23"], "23"),
 ("12-05","20","长焦","慢放","【三秒钟】三十层转角回望:四十二层楼板边两个人影,一前一后,像两根钢筋",
  "telephoto from a stair landing far below: two silhouettes at the slab edge, one in front near the drop, one a step behind, rain blurring everything", [], "23"),
 ("12-06","22","特写","固定","救护车里拆开的纸袋:一沓发灰的旧钞",
  "inside an ambulance, a parcel opened: bundles of cash with rubber bands, one stack of old faded grey banknotes", ["ayong"], "23"),
 ("12-07","23","中景","固定","楼梯间出口,一个人架着另一个人的胳膊走出来",
  "at the stairwell exit one man supports another by the arm as they emerge into the rain", ["he23","shen23"], "23"),
 ("12-08","25","远景","跟","他没打伞,沿着围挡一直往前走,一次也没回头",
  "a man walks away in the rain along a construction hoarding without an umbrella, never looking back", ["he23"], "23"),
 ("12-09","31","全景","升","复工的楼,每一层外侧挂上绿色安全网",
  "the resumed tower, workers hang neat green safety nets on every floor", ["xu25","chen27"], "27"),
 ("12-10","34","大远景","固定","山坡两座坟,一间小砖房,坟前一罐可乐、一支铅笔",
  "a hillside with two graves and a small brick hut, a cola can and a mechanical pencil at a headstone, a man's back in the doorway", [], "27"),
 ("12-11","36","全景","固定","监狱侧门,她出来,隔着马路看着站牌下的他(不剪)",
  "a woman steps out of a prison side gate and looks across the road at a man by a bus stop, held in one long take", ["lin27","zhou27"], "27"),
 ("12-12","37","近景","固定","公交车门口,硬币落进投币箱;'他没伸手'",
  "at a bus door a woman drops a coin into the fare box and speaks to a breathless woman outside", ["lin27","chen27"], "27"),
 ("12-13","39","长焦","慢放","【三秒钟·第二次】慢放,后面那个人影的胳膊往前动了一下,定格",
  "the same telephoto silhouettes in slow motion, the rear figure's arm moves forward, freeze-frame, ambiguous: a reaching hand or a sleeve in the wind", [], "23"),
 ("12-14","41","大远景","缓拉","雾散了,他还站在那里;远处一栋楼外挂着绿网",
  "the morning haze lifts, a man still waiting at a bus stop, far away a building under construction wrapped in green safety nets", ["zhou27"], "27"),
])

def prompt(s):
    sid, sc, size, mv, zh, en, cast, era = s
    parts = [f"{SIZE[size]}, {MOVE[mv]}", en]
    if cast: parts.append("Characters: " + "; ".join(C[c] for c in cast))
    parts.append(GRADE[era][1]); parts.append(STYLE)
    return ". ".join(parts) + "."

def ep_md(n):
    title, shots = EPS[n]
    o = [f"## 第 {n} 集 · {title}", "", f"关键镜头 {len(shots)} 个,每个镜头生成一段 10 秒。", ""]
    o.append("| 镜头 | 场 | 景别 / 运动 | 色调 | 画面 |"); o.append("|---|---|---|---|---|")
    for s in shots:
        o.append(f"| {s[0]} | {s[1]} | {s[2]} / {s[3]} | {GRADE[s[7]][0]} | {s[4]} |")
    o.append("")
    for s in shots:
        o.append(f"**{s[0]}** · 场 {s[1]}"); o.append(""); o.append("```"); o.append(prompt(s)); o.append("```"); o.append("")
    return "\n".join(o)

bible = ["# 分镜脚本与生成提示词(一)","",
"本页是全剧的视觉总纲,以及第 1–6 集的关键镜头。第 7–12 集在“分镜(二)”。","",
"## 规格","",
"- 画幅 2:1(1280×640),24 fps;视频工具每段固定 10 秒,所以一个关键镜头对应一段。",
"- 每集挑 9–14 个关键镜头:决定这一集记忆点的画面。其余过场镜头按剧本现场拍,或用同一套人物和色调提示词补齐。",
"- 英文提示词结构:景别与运动 → 画面动作 → 人物描述 → 年代色调 → 统一风格。人物描述固定写法,保证同一个人在十五年里认得出来。","",
"## 铁律","",
"1. **何小川坠落不拍。** 只拍空了的东南角、垂下去的钢丝绳。",
"2. **四十二层的对话不拍。** 靠近沈既白和何峻,声音只留风;画面只有阿勇回头那三秒钟的长焦剪影,终集慢放一次。",
"3. **亲密戏只拍剪影、烛火、雨、手。** 不拍身体。",
"4. **核心三人没有旁白。** 镜头可以看他们,不进入他们。",
"5. **后视镜、门缝、栅栏、白气、长焦。** 讲述者永远隔着东西看别人,构图里要有这层“隔”。","",
"## 年代色调","",
"| 键 | 年代 | 英文色调词 |","|---|---|---|"]
for k,(zh,en) in GRADE.items(): bible.append(f"| {k} | {zh} | {en} |")
bible += ["","## 人物定妆(英文提示词)","","| 代号 | 描述 |","|---|---|"]
for k,v in C.items(): bible.append(f"| {k} | {v} |")
bible += ["","## 统一风格后缀","","```",STYLE,"```",""]

import os
os.makedirs("md", exist_ok=True)
open("md/40-shots.md","w").write("\n".join(bible) + "\n" + "\n".join(ep_md(n) for n in LEFT))
open("md/41-shots2.md","w").write("# 分镜脚本与生成提示词(二)\n\n第 7–12 集关键镜头。人物定妆、年代色调与统一风格见“分镜(一)”。\n\n" + "\n".join(ep_md(n) for n in range(7,13)))
print(sum(len(v[1]) for v in EPS.values()), "shots")
