# 《驿》全剧本 · 总览

这里收着《驿》十集加尾声的全部剧本材料:分场剧本、台词、分镜表、每个镜头的首帧与动态提示词,以及动画版的分段提示词。世界观、人物小传和第八节的提示词规范仍以设定集文档为准:https://claude.ai/artifact/4tX3MbUpzQGkGqia9DccS1

每一集的页面结构都一样:

1. **本集概要**:这一集做什么、人物、钥匙物件、情绪曲线。
2. **本集新增锚点**:这一集第一次出现的人物、年龄段和场景的英文描述,生成时原样复制。
3. **分场剧本**:场景、动作和全部台词。
4. **分镜表**:镜号、景别与运镜、画面、声音与台词、剪辑后秒数。
5. **生成提示词**:每个镜头一组“图”(首帧)和“动”(图生视频动作)。
6. **动画版分段提示词**:按 MiniMax H3 工作流,每段 10–13 秒一次生成,段内按时间轴排镜头。

## 分集一览

| 集 | 镜头合计 | 镜头数 | 动画段数 | 概要 |
|---|---|---|---|---|
{{EP_TABLE}}

镜头合计不含片头片尾。设定集写的是每集 8–12 分钟;目前第 1 集 7 分 23 秒,其余各集 4 分 40 秒到 6 分 50 秒,比设定短。原因是台词写得克制,每镜平均 5–6 秒。要拉长时,优先加空镜、风声段落和停顿,不加台词;也可以把关键帧镜头放到 8–10 秒。

## 修订说明(与设定集不一致的地方)

- **灞桥,不是“灶桥”。** 设定集第四节和第 2 集大纲写的是“长安灶桥”,应为灞桥(长安城东,唐人折柳送别之地)。剧本里已改。
- **铜铃的位置。** 第 1 集第 3 场里,诺桑在驿厅门框上碰响了铜铃,但第 4 场(736)卢父把铃挂在门楼上。两处必须是同一只铃,所以这样处理:
  - 736 至 763 年,铃挂在门楼外侧,有客就响。
  - 第 8 集补一场:764 年最后一个驿卒走后,卢七把铃从门楼摘下,挂到驿厅门内。一个人守驿,夜里在厅里要听得见。
  - 因此 787 年门楼上只剩一截铃绳,铃在驿厅门内。第 1 集镜 6 的画面改为“门楼下空着的铃钩”。
- **红绳的规则。** 第一根是和义公主系的(744),此后每年她离开的那天卢七系一根,到 787 年是第四十三根。
- **柳娘的炭画马。** 第 3 集里 8 岁的柳娘攥着炭从门后探头,只露一眼,不交代;第 7 集揭晓墙脚那匹马是她九岁时画的,画的是大军征马后唯一留下的小灰驹。
- **老马“灰”的来历。** 第 6 集军官嫌小、没有征走的那匹小灰驹,就是“灰”。787 年它三十多岁,是匹极老的马。
- **康萨保改的姓。** 设定集写“改姓为安”。安禄山起兵后,“安”正是最犯忌的姓,史上姓安的胡人多改了姓(如安重璋改名李抱玉)。剧本改为把“康”改成发音相近的“姜”。
- **家书没寄出的原因。** 大纲写“寄信的驿骑一直没有等到”。第 4 集改为:败报传来后,东去的驿骑到了,卢七却没把信交出去——他不知道该不该让母亲读一封可能已经死去的儿子写的信。第 9 集赵小满把信揣在怀里,自己送回去。
- **家书里的“扣一匹绢”。** 疑为“扯一匹绢”(买布论“扯”),剧本按“扯”写,请确认。
- **张归往西走。** 张归回沙州(敦煌),在苦泉驿以西,所以第 10 集他向西离开,长卷因此到了敦煌,接上尾声的藏经洞。

## 提示词通用块

以下几段在每个镜头里原样替换,出自设定集第八节。

**[风格前缀]**

```
cinematic film still, Tang dynasty China, 8th century, remote desert post station on the Silk Road near Dunhuang, natural light, muted film grain, historically accurate costumes and architecture, restrained and poetic mood, vast negative space
```

**年代色调后缀(五选一)**

```
[开元] warm golden sunlight, clean blue sky, bright ochre sand, youthful and hopeful
[天宝] rich Dunhuang mural palette, cinnabar red, mineral azurite blue and malachite green, warm dusk light, bonfires, bustling
[乱后] desaturated earth tones, grey-brown, overcast diffuse light, single oil lamp, cold wind, lonely
[现实线 787] cold blue-grey dusk, desaturated, one touch of willow green, quiet and austere
[尾声 1900] dim cave interior, single shaft of light, aged paper tones, archival photo grain
```

**反向提示词**

```
anime, cartoon, fantasy armor, modern clothing, Qing dynasty or Ming dynasty costume, wuxia exaggeration, glossy skin, heavy makeup, plastic look, oversaturated, lens flare, text watermark, deformed hands, extra fingers
```

**设定集原有的角色锚点**

```
LU QI, AGE 14: thin Han Chinese boy, sun-darkened skin, short topknot tied with a hemp cord, coarse undyed hemp short jacket and leg wraps, bright curious eyes, chapped cheeks

LU QI, AGE 33: lean Han Chinese man, weathered tanned face, short beard, black futou cap, faded dark green round-collar robe with leather belt, calm steady eyes, calloused hands

LU QI, AGE 65: old Han Chinese man, deeply lined face, thin white beard, white hair in a small topknot, very worn and patched round-collar robe washed almost grey but neatly kept, slightly stooped, quiet dignified gaze

ZHANG GUI, AGE 18: slender young Han Chinese man, Tibetan-style braided hair, left-lapel sheepskin robe, a folded Tang round-collar robe tucked at his waist, ink-stained fingers, guarded and earnest expression

A HENG, AGE 20-37: Han Chinese peasant woman from Guazhou, round warm face, quick smile, hair in a simple bun with a wooden pin, plain indigo jacket and skirt, sleeves rolled up, flour on her hands

PRINCESS HEYI, AGE 17: young Tang princess, high Tang court dress under a travelling hu-style riding coat, veiled weimao hat, delicate face, holding a single willow branch

KANG SABAO: Sogdian merchant, curly reddish beard, pointed felt hat, turned-down-collar kaftan, prominent nose, laughing eyes

ZHAO XIAOMAN, AGE 15 / AGE 51: (15) skinny Guanzhong peasant boy in an oversized cloth armour, bamboo hat, nervous grin; (51) white-haired gaunt veteran in battered patched armour, same eyes, carrying a cloth bundle
```

第 1 集“本集新增锚点”里另有 FATHER LU, AGE 50、KANG SABAO, AGE 30、SCHOLAR、TIBETAN SOLDIERS、HUI、POST STATION 787 / 736、POEM WALL 787 / 736,见设定集文档第一集标签。

## 各集新增锚点汇总

{{ANCHORS}}

## 动画版通用块

动画版的分段提示词里用到下面这些块,生成时原样替换。画风的理由见设定集文档“动画版”标签:现实线像褪色的墙,回忆线像墙上的画。

**[STYLE 787] 现实线:淡彩手绘**

```
hand-painted 2D animated film, gouache and transparent watercolor on textured paper, soft dry-brush edges, no black outlines, muted palette of cold blue-grey, pale ochre and faded earth, large areas of empty sky, visible paper grain, painterly texture that gently shifts from frame to frame, restrained limited animation, the only saturated color allowed is the faded red of the willow cords, quiet and austere, Tang dynasty Hexi corridor, 787 AD
```

**[STYLE 盛唐] 开元、天宝回忆(736–755):敦煌壁画式重彩**

```
hand-painted 2D animated film in the manner of High Tang Dunhuang cave murals, mineral pigments of azurite blue, malachite green, cinnabar red and ochre on warm plastered ground, fine even iron-wire line drawing, flat decorative color areas with soft mineral grain, warm lamplight glow, lively and abundant, Tang dynasty
```

**[STYLE 乱后] 乱后回忆(755 年冬至 786):褐变的壁画**

```
hand-painted 2D animated film in the manner of Middle Tang Dunhuang murals after the pigments have browned, oxidised reds turned dark brown, faded greens, ochre and grey-brown on cracked plaster, sparse iron-wire line drawing, large empty areas of bare wall, single warm lamp against cold surroundings, lonely and spare, Tang dynasty after 755 AD
```

**[STYLE 1900] 尾声:旧照片里的画**

```
hand-painted 2D animated film imitating an aged sepia photograph, warm paper tones, soft grain and faint scratches, a single shaft of light in darkness, minimal movement, Dunhuang 1900 AD
```

**[通用法则]**

```
ENVIRONMENT LOCK: stay inside the reference environment; add no props, buildings or plants that are not in the references; no text, no subtitles, no film crew, no modern objects.
CAMERA LAW: every camera is a real physical position at a stated height and distance; moves are only slow push-ins, slow pans, slow tilts and side tracking at the subject's own speed; locked-off shots stay perfectly still; no handheld shake, no digital zoom or crop, no whip pans; frame each shot before its action accent.
PERFORMANCE LAW: act with small concrete body chains (weight shift, torso, shoulder, wrist, fingers); one action per shot, finished in the first half of the shot, then hold; mouths move only on on-screen lines; forbidden: looking at camera, exaggerated gestures, repeated identical loops, frozen statue poses, sudden fast motion.
```

**[通用禁止项]**

```
no photorealism, no live-action look, no 3D render, no CGI shading, no anime cel shading, no thick black outlines, no lens flare, no text, no subtitles, no watermark
```

## 配音声线(Qwen3-TTS VoiceDesign)

全部普通话,不带台湾腔;西北人物可略带西北口音,但字音要标准。吐蕃语台词不做 TTS,请会藏语的人录,或只保留语气声、后期加字幕。

| 人物 | 声线描述 |
|---|---|
| 卢七(65) | 老年男声,低沉沙哑,气息短,语速很慢,句尾往下落,平静克制,不带哭腔 |
| 卢七(22–41) | 青壮年男声,嗓音偏干,话少,句子短,带一点西北口音 |
| 少年卢七(14) | 少年男声,清亮,略带怯,好奇 |
| 张归(18) | 青年男声,清但有点干涩,读令时端正生硬,私下说话放低、迟疑;旁白像抄写时的自言自语 |
| 卢老驿长 | 中年男声,嗓门大,干脆利落,老兵口气;病中气弱但不乱 |
| 康萨保 | 中年男声,洪亮爱笑,汉话带外国口音(元音拖长、声调偏平),但字要听得清 |
| 和义公主(17) | 少女声,轻、慢、稳,有教养,不娇 |
| 韦幼安 | 25 岁:明亮张扬,带酒气;31 岁:同一个人,沙哑、疲惫、自嘲 |
| 阿蘅 | 年轻女声,爽朗爱笑,瓜州乡音;唱曲时清亮质朴 |
| 柳娘 | 孩童女声,脆 |
| 赵小满 | 15 岁:变声期少年,紧张时说话快;51 岁:苍老男声,关中口音,说话慢 |
| 王进 | 青年军汉,粗声大嗓,爽快 |
| 李承知 | 中年男声,冻得发抖,话很少,每句都很急 |
| 节儿 | 中年男声,说吐蕃语,语速平稳,有官气 |
