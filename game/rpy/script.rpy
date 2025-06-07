define a = Character("胡永安")
define b = Character("小吏（王贵）")
define c = Character("德璀琳")
define d = Character("经验丰富的邮差")
define e = Character("路过的邮差")
define f = Character("佟在田")
define g = Character("李鸿章")
define h = Character("刘桂芳")
define i = Character("山东巡抚")

define  eye_open = ImageDissolve ("images/sence1tianjin.png",.5, ramplen =128, reverse = False )
define  eye_close = ImageDissolve ("images/sence1tianjin.png",.5, ramplen =128, reverse = True )
define  eye_open1 = ImageDissolve ("images/sence2dclwork.png",.5, ramplen =128, reverse = False )

label start:
   play music"audio/feet.mp3"
   scene black
   ".........."
   stop music
   play music"audio/BGM1.mp3"

   scene sence1tianjin with eye_open
   "站在这里，仿佛能够感受到邮政百年的历史在身边流淌，让人不由自主地沉浸其中。每一块砖瓦都透露着岁月的沧桑，但又流露出一股沉稳与庄重。"
   "这不仅是一座建筑，更是承载着时代记忆的宏伟史诗。"
   scene baiguang with eye_close


   scene sence new
   "光绪四年 1878年  华洋书信馆 门外……"
   "华洋书信馆： 清末海关试办邮政期间招商办理邮务的机构 ，运营时间是1878-1882年。"
   show huyongan at left
   a"奇怪？我刚刚不是推门进去了吗，这又是哪儿？（十分疑惑，再次推门进去。）"
   stop music

   scene black with eye_open

   scene black with eye_close
   play music"audio/BGM2.mp3"
   scene sence1youzheng
   show huyongan at left
   a"这是博物馆吗？现在的博物馆都搞沉浸式了？"

   scene sence3youzhengback

   show xiaoli at right
   b"（匆忙）总听差大人，您怎么现在才来啊？都已经巳时了！"
   hide xiaoli
   show huyongan at left
   a"（心里想：听差？）你们这博物馆这么新颖啊，还是剧情向的。"
   hide huyongan
   show xiaoli at right
   b"大人，您说的话我怎么听不懂啊。"
   hide xiaoli
   show huyongan at left
   a"大哥，你也入戏太深了，给我点提示，我这会儿脑子有点蒙。"
   hide huyongan
   show xiaoli at right
   b"大人，我不知道您什么意思，就别拿小的逗乐了。"
   hide xiaoli
   show huyongan at left
   a"（回想起刚刚闪过的白光以及诡异的眩晕感，心想：我难不成真的是穿越了？）我是谁？这是什么年代？"
   hide huyongan
   show xiaoli at right
   b"（心里觉得奇怪：难道大人睡了一觉糊涂了不成？但还是恭敬回答）回禀大人，如今乃是光绪四年。您叫胡永安。"
   hide xiaoli
   show huyongan at left
   a"（心里想：光绪四年，这不就是清代邮政创办之初的年份吗？刚要参观邮政博物馆，就给我穿越到这里。这下真成沉浸式体验了。）"
   a"你刚刚说我怎么才来，是什么意思？"
   hide huyongan
   show xiaoli at right
   b"大人，您这会儿已经迟到了，您不会忘记了什么时辰上值了吧。"
   hide xiaoli
   show huyongan at left
   a"（心虚）没有没有，我当然记得了。（四处打量，瞥见钉在墙上的时间表）"
   hide huyongan
   show xiaoli at right
   b"大人，咱先别聊这些了。德璀琳大人说有件急事，需要您找他一下。"
   hide xiaoli
   show huyongan at left
   a"（心里想：可能完成任务我就能回归我的时代了）我这就去。"
   stop music


   scene black with eye_open1
   scene sence2dclwork
   "德璀琳办公室"
   play music"audio/bgm4.mp3"
   show huyongan at left
   a"（强装镇定）大人，您找我。"
   hide huyongan
   show decuilin at right
   c"胡先生，有个很重要的事需要委托给你。"
   hide decuilin
   call screen ck
   label end:
   "德璀琳:清代海关外籍官员。德国人。1864年进入中国海关，长期任天津海关税务司。1878年3月23日，受中国海关总税务司赫德指派，以天津为中心，在北京、天津、烟台、牛庄(后改营口)、上海五处，依照欧洲办法，开始试办新式邮政，中国近代邮政由此发端."
   "为了简化操作手续和账务处理，委托海关上海造册处印制邮票，于1878年7月下旬开始在天津发行了大龙邮票。1913年病死于天津，所遗大量中国早期邮集陆续在天津售出。"
   show huyongan at left
   a"大人您尽管吩咐。"
   hide huyongan
   show decuilin at right
   c"天津海关开办了一条骑差邮路，在天津和北京间开展定期邮递业务。现如今邮路虽已建成，但缺少负责人进行看护。我这几日思来想去，觉得交给你，我是最放心的。你意下如何呢？"

   call demo from _call_demo

   scene sence1youzheng
   play music"audio/bgm5.mp3"
   show huyongan at left
   a"创办京津之间的骑差邮路需要大量的人手和马匹，我这初来乍到，上哪儿召集人手呢？（苦恼）"
   hide huyongan
   show xiaoli at right
   b"大人，您这是怎么了？愁眉苦脸的，被德璀琳大人批评了？"
   hide xiaoli
   show huyongan at left
   a"（摇头苦笑）批评倒是没批评，只是给了我一项重任，要创办京津之间的骑差邮路，还得负责招募人手和马匹。我这心里头，真是七上八下的。"
   hide huyongan
   show xiaoli at right
   b"哎呀，大人，这可是个美差事啊！恭喜大人，得到德璀琳大人的重用。大人在工作上有用得到在下的地方，在下必不遗余力地配合。"
   hide xiaoli
   show huyongan at left
   a"现在我正为人手问题发愁呢，不知您有何见教？"
   hide huyongan
   show xiaoli at right
   b"这个好办，咱邮局里多的是身体健壮、责任心强的小伙子。大人可能忘了，您那里应该有信差档案的。"
   hide xiaoli
   show huyongan at left
   a"噢，哈哈哈哈哈，没错没错，瞧我这脑子，我给忘了。多谢提醒。（尴尬的笑）不过，这马匹的准备，肯定是需要重新购买了。"
   hide huyongan
   show xiaoli at right
   b"马匹的事情，大人尽管放心。我这就联系马行，挑几匹脚力好、性情稳、适合长途奔袭的马。"
   hide xiaoli
   show huyongan at left
   a"多谢相助，你真是帮我解决了一大难题啊。"
   hide huyongan
   show xiaoli at right
   b"大人言重了，这都是在下应该做的。（匆匆离去）"
   hide xiaoli

   scene black with eye_open1
   scene sence2hyawork
   "胡永安办公室"
   play music"audio/bgm4.mp3"
   show huyongan at left
   a"(自言自语）看来，这穿越也不全然是坏事，至少能让我亲身体验一番清代邮政的创办过程。既然来了，就得把事情办好，说不定还能在这过程中找到回到现实世界的线索呢。"
   a"（拿出纸笔，在纸上规划线路及安排）京津之间线路可以参考之前的邮驿安排，设置中继站，邮差接力运送信件，这样可以提升运送的效率。"
   a"（在桌子抽屉里翻找到信差档案）我当时怎么没想到，我是个总听差，手底下肯定有不少信差。"
   a"（细细翻看档案，挑选合适的信差）嗯，这个不错，体格强、耐力好。这个也不错，经验丰富。暂时就这八个吧。"
   "(胡永安放下档案，环视办公室周围，墙上挂着邮袋、斗笠和号衣，窗边桌子上放着提灯、铃铛，墙角处斜靠着几根扁担和一根稍短的木棍)"
   hide huyongan
   call screen to
   label ld:
   "铃铛：警示作用,在邮差骑马或步行传递邮件的过程中，铃铛的声响可以起到警示作用，提醒行人和其他交通参与者注意避让。同时，铃铛的响声也提醒人们“送信的来了”。 "
   call screen to
   label yd:
   "邮袋：邮袋是邮件容器的一种，一般用帆布制作，是邮件在分拣封发和运输中最常使用的一种邮件容器。由于邮件大小不一，邮袋分许多种型号，型号和生产年份印在袋身上。邮袋为邮政部门专用，严禁挪作他用。 "
   call screen to
   label mz:
   "一、实用功能:①遮阳避雨：斗笠作为一种传统的遮阳避雨工具，在清朝时期被广泛使用。邮差在户外长时间工作，经常会遇到日晒雨淋的情况。携带斗笠可以有效地遮挡阳光和雨水，保护邮差免受自然环境的侵扰，确保他们能够顺利完成邮递任务。"
   "②防风防尘：在风沙较大的地区，斗笠还能起到防风防尘的作用。邮差在行走或骑马时，斗笠可以阻挡风沙对眼睛和面部的侵袭，保持视线清晰，减少不适感。"
   " 二、身份标识:虽然斗笠本身并不直接作为邮差的身份标识，但在一些特定的情境下，它可能与其他装备（如邮差服、邮袋等）一起构成邮差的形象特征。这种形象特征有助于在人群中迅速识别邮差，提高邮递工作的效率和安全性。"

   call screen to
   label bd:
   "扁担：对于步差（即主要依靠步行传递邮件的邮差），他们常常使用扁担挑着装有邮件的邮包进行长途跋涉，这是他们重要的负重工具。"
   "木棍：自卫工具，在长途跋涉或穿越荒野时，邮差可能会遇到各种危险，如野兽袭击、盗匪抢劫等。棍子作为一种简单的自卫工具，可以在紧急情况下为邮差提供一定程度的保护。"
   call screen to
   label hy:
   "号坎（号衣）：在清朝末年，邮差在执行任务时，通常会穿着一种无领无袖、带有红绿色调的号坎（当时称为号衣）。这种号坎上饰有黄色字样或图案，用以标明邮差的身份。这种装备虽然简单，但在当时却起到了很好的识别作用。"
   call screen to
   label tg:
   "跳过物品介绍。"
   stop music
   show xiaoli at right
   play music"audio/BGM2.mp3"
   b"（跑的上气不接下气）大人，马匹已经订好了，一共是十匹。"
   hide xiaoli
   show huyongan at left
   a"不错，效率真高。（递出一张名单）我这里选了八个邮差，你看他们如何呢？"
   hide huyongan
   show xiaoli at right
   b"（接过名单查看）大人好眼光，这有好几个都是出了名的送邮的好手，工作能力强。"
   hide xiaoli
   show huyongan at left
   a"那就好，麻烦你通知这几人明天早上到我办公室集合。"
   hide huyongan
   show xiaoli at right
   b"得嘞，我这就传达给他们。"
   hide xiaoli
   show huyongan at left
   a"稍等，内个。怪不好意思的，跟着我忙活这么长时间，我还不大记得你的名字。"
   hide huyongan
   show xiaoli at right
   b"大人日理万机，在下微名，何足挂齿。"
   hide xiaoli
   show huyongan at left
   a"这个还是要的，帮了我这么大的忙，日后论功行赏怎么会忘了你。"
   hide huyongan
   show xiaoli at right
   b"在下名叫王贵，谢大人记挂。"
   hide xiaoli
   show huyongan at left
   a"你且去吧，我会牢牢记住你的。"
   hide huyongan
   show xiaoli at right
   b"大人重情重义，在下没齿难忘。（拱手，离开）"
   hide xiaoli
   show huyongan at left
   a"现在送邮线路和人手已经大致安排妥当，是时候跟德璀琳汇报一下工作进展了。"
   hide huyongan
   "胡永安整理好桌面上的文件和规划图，深吸一口气，显得既紧张又期待。他站起身，轻轻拍了拍衣袍上的灰尘，仿佛是在为即将到来的重要会面做最后的准备。随后，胡永安步伐稳健地走出办公室，向德璀琳的办公室方向走去。"
   stop music

   scene sence2dclwork
   play music"audio/bgm4.mp3"
   "德璀琳正埋头于一堆文件之中，眉头紧锁，显然也在为清代邮政的创办事宜操劳。听到脚步声，德璀琳抬头"
   show decuilin at right
   c"啊，你来了，正好我有事要与你商议。"
   hide decuilin
   show huyongan at left
   a"大人，我正有此意。关于京津之间的邮政线路安排，我已经初步规划完毕，并挑选了八位经验丰富的信差。"
   hide huyongan
   "德璀琳眼睛一亮，示意他继续。"
   show huyongan at left
   a"我计划沿用并优化过去的邮驿制度，设立多个中继站，确保信件能够高效、安全地传递。同时，考虑到马匹的重要性，我已经预订了十匹健壮的马匹，以应对长途跋涉的需求。"
   hide huyongan
   show decuilin at right
   c"（点头表示赞同）你的考虑很周全，这确实是我们目前最需要的。不过，除了硬件上的准备，我们还需要在制度上进行创新，比如如何确保邮件的保密性、如何建立有效的监督机制等。"
   hide decuilin
   show huyongan at left
   a"（从怀中掏出另一份文件，递给德璀琳）：大人，关于这些，我也做了一些思考。我提议建立一套严格的邮件封装与开封制度，使用特殊标记和封印来确保邮件在传递过程中不被私自拆阅。同时，设立监督岗位，定期对各个环节进行检查，确保制度的有效执行。"
   hide huyongan
   show decuilin at right
   c"（德璀琳仔细翻阅着文件，不时点头，眼中闪烁着赞许的光芒。）很好，你的想法非常具有前瞻性。看来，你不仅适合做一名总听差，更是一位能够引领我们邮政事业向前发展的栋梁之才。"
   hide decuilin
   show huyongan at left
   a"多谢大人夸奖，我定当竭尽全力，不负所望。（恭敬地回答）"
   hide huyongan
   show decuilin at right
   c"（站起身，拍了拍胡永安的肩膀）去吧，按照你的计划去执行，我相信你能够带领我们的团队，开创清代邮政的新篇章。"
   hide decuilin
   "胡永安点头，满怀信心地离开了德璀琳的办公室，心中已经勾勒出了一幅清代邮政蓬勃发展的蓝图。而他，也将在这段历史的长河中，留下自己不可磨灭的印记。"
   stop music

   scene sence1hyawork
   play music"audio/bgm6.mp3"
   show xiaoli at right
   b"大人，昨天您选出来的八名邮差已经在门外候着了，马匹也已经安置在了邮局马棚里。"
   hide xiaoli
   show huyongan at left
   a"干得不错，让他们都进来吧"
   scene sence8pwork
   "（走进来八位年轻力壮、目光炯炯有神的邮差）"
   a"诸位，召集大家到此是为了组班经营我们的京津骑差邮路。我们的任务艰巨而光荣，各位都是局里的佼佼者，相信在大家的齐心努力之下，我们的邮路一定会顺利开办。"
   "（众人齐声应和，气氛热烈）"
   hide huyongan
   show xiaoli at right
   b"大人，京津之间路程不短，他们虽然各个出类拔萃，但长途奔袭，他们会吃不消的。"
   hide xiaoli
   show huyongan at left
   a"各位不必担心，这样的情况我早就考虑到了。我会将你们八人安排在五个站点，分别是天津一人、杨村二人、河西务二人、张家湾二人、北京一人，你们接力送信。这样会极大减轻你们的负担。"
   a"王贵，将这些接力安排和邮差号衣分发下去。"
   hide huyongan
   show xiaoli at right
   b"是。"
   hide xiaoli
   show haoyi
   "展示号衣"
   hide haoyi
   stop music
   scene 路线
   "接力安排"
   "初始配置"
   call screen at
   label bj:
   "北京：1匹马，1名信差（E）"
   call screen at
   label zwj:
   "张家湾：2匹马，2名信差（D1, D2）"
   call screen at
   label hxw:
   "河西务：2匹马，2名信差（C1, C2）"
   call screen at
   label yc:
   "杨村：2匹马，2名信差（B1, B2）"
   call screen at
   label tj:
   "天津：1匹马，1名信差（A）"
   call screen at
   label tg2:
   "跳过介绍。"
   "运作流程去程（天津到北京）"
   $ renpy.movie_cutscene("images/路线.webm")
   "回程（北京到天津）回程需要另一套人马进行接力，原先在北京待命的信差E和其他地方的信差（B2, C2, D2）已经准备好进行回程的接力。"
   "信差E骑马携带回信件从北京出发，前往张家湾。到达张家湾后，E1将信件转交给待命的信差D2，留在张家湾备用。后续阶段类似地，信件通过D2到C2，C2到B2，B2最终回到天津。"

   scene sence8pwork
   play music"audio/bgm6.mp3"
   show xiaoli at right
   b"大人当真聪慧过人，这种来回送信的接力模式，确保信件能够高效、安全地在两地之间传递。"
   hide xiaoli
   "（众人纷纷夸赞）"
   show huyongan at left
   a"（心里暗爽）谢过各位。咳咳，提醒一下，大家不要大意，虽然是接力送邮，但路上会有各种突发状况，对大家的身心仍是一个不小的考验。"
   hide huyongan
   "大人放心，吾等定当竭尽全力。（情绪高亢）"
   show huyongan at left
   a"谢各位支持，现在大家回去准备好装备，火速赶往自己的站点候命。我们的线路两日后开始运作。"
   hide huyongan
   "是。（众人纷纷离开）"
   show huyongan at left
   a"呼，这一切跟做梦一样，任谁能想象到自己有朝一日能组班创建邮路。不过，既然大佬们给我搭好了戏台子，我得好好唱下去才行。"
   hide huyongan
   "（京津骑差邮路顺利开办，起初邮路在有条不紊的运行，但随着时间推移，各种问题开始出现）"
   stop music

   scene baiguang with eye_open1
   "半个月后"
   scene sence1out
   play music"audio/chunhan.mp3"
   "（初春的深夜，春寒料峭，一个经验丰富的邮差正载着邮件骑马奔驰在从杨村到河西务中继站的途中。马鞍侧面绑着装满邮件的邮袋）"
   show youchai1 at left
   d"（唉声叹气）最近邮路办的越来越红火，邮件数量也与日俱增。这虽说有中继站换班休整，但也架不住邮件数量多啊，整日奔驰，真的有点力不从心了。"
   d"真冷啊，这虽然开春了，却还是寒风刺骨。前些日子有几个兄弟染上了风寒，不少马匹也患上了背痛症病倒了。我的好伙计，你可要坚持住啊。（伸手抚了抚马的背部）"
   d"（自言自语）这世道，连送封信都不容易。不过，想到这些信件里可能藏着远方亲人的思念，甚至是改变命运的消息，我可不能懈怠，要尽快把信送到才行。"
   hide youchai1
   stop music
   "（突然，一阵急促的马蹄声从不远处传来，打破了夜的宁静。邮差立刻警觉起来，紧握缰绳，将马匹引向路边，避免可能的碰撞。不多时，一名同样身着邮差服饰的年轻人骑着快马飞驰而过，留下一串焦急的呼喊。）"
   play music"audio/mashen.mp3"
   show youchai2 at right
   e"前面的兄弟，小心路滑！我得先行一步！"
   stop music
   hide  youchai2
   show youchai1 at left
   play music"audio/chunhan.mp3"
   d"（高声回应）知道了，兄弟！一路平安！"
   "（他继续在马背上颠簸前行，月光稀薄，只能勉强照亮前方蜿蜒的小径。四周是寂静的田野，偶尔传来几声夜行鸟的啼鸣，更添了几分孤寂与清冷。）"
   "他在马背上渐渐失神，昏昏欲睡，突然一阵失重感传来，他从马背上跌落，倒在了路边的沟渠里。瞬间的吃痛让他清醒过来。"
   d"哎呦，摔死我了！这是哪啊，我怎么不记得这条路上有沟渠呢。看这样子应该是新掘的。算了，送信要紧。（缓缓站起，揉了揉酸痛的臂膀）"
   "（他起身把马牵回，熟练的翻身上马，拽动缰绳，驱马前进）"

   call demo2 from _call_demo2
   play music"audio/bgm4.mp3"
   scene sence2hyawork
   "胡永安翻看着过去两个月邮路的运转状况，紧皱眉头，具体情况并不能令人满意，邮路行程的时间不是规定的12小时，而是平均17.5小时，其中最快的是14小时，最慢的是30小时。加上多次发生的邮差坠马事件，胡永安感到头痛不已。"
   show huyongan at left
   a"原本以为邮路会顺利开办下去，现在状况百出，这可如何是好。"
   hide huyongan
   show xiaoli at right
   b"大人，德璀琳大人让您去他办公室一趟。"
   hide xiaoli
   show huyongan at left
   a"（放下手中的文件，揉了揉眉心，显得既疲惫又无奈，叹了口气）好的，我这就过去。"
   hide huyongan
   "（小吏微微欠身，转身离开，轻手轻脚地关上了办公室的门。胡永安站起身，在屋内踱了几步，心中盘算着即将面对的可能对话和解决方案。）"
   stop music

   scene sence2dclwork
   play music"audio/yequ.mp3"
   show huyongan at left
   a"（行礼）德璀琳大人，您找我？"
   hide huyongan
   show decuilin at right
   c"（抬头，目光锐利）胡先生，你来的正好。我听说了邮路运转的问题，情况确实不容乐观。"
   hide decuilin
   show huyongan at left
   a"（诚恳）是的，大人。邮路时间延误严重，加上邮差安全问题频发，这让我非常担忧。我已经在查找原因，并尝试制定改进方案，但效果尚不明显。"
   hide huyongan
   show decuilin at right
   c"（点头）我理解你的难处。邮路的顺畅不仅关乎效率，更直接影响到我们的声誉和民众的信心。但是经过近两个月的运行，你的队伍从来没有按照合同里规定的那样在12小时内送达邮件。"
   c"我也亲自骑马试验过，从天津到北京完全能够在12个小时以内到达。"
   hide decuilin
   show huyongan at left
   a"非常抱歉，德璀琳大人。但是邮差们已经是尽全力的在送邮，看着他们一个个人困马乏、筋疲力尽的窘境，我实在无法苛责他们。"
   hide huyongan
   show decuilin at right
   c"（不满）既然订立了合同，就要履行。我看，仅仅依靠超时罚款，并不能解决这样的问题。"
   hide decuilin
   show huyongan at left
   a"德璀琳大人，你那次试验是在白天，而且冬季和初春寒风刺骨，天气恶劣。一般很难在12小时内送达，我们的邮差最快也只能在14个小时内送达。"
   hide huyongan


   call demo3 from _call_demo3
   scene sence2dclwork
   play music"audio/bgm6.mp3"
   "（德璀琳坐在办公桌前，对面是一个身材魁梧的汉子。）"
   show decuilin at right
   c"佟先生，前不久我向华洋书信馆的刘桂芳经理表明了我想建立天津——镇江邮路的想法，他向我推荐你担任天津——镇江一线的邮路承办人。"
   hide decuilin
   show tong at left
   f "佟某一介武夫，能够被大人选中是我的幸运。"
   hide tong
   show decuilin at right
   c"佟先生过谦了，有了你的帮助，我们的邮路一定会顺利运行的。"
   hide decuilin
   show tong at left
   f "在下定然不会辜负大人的期望。"
   hide tong
   stop music

   scene black with eye_open1
   "李鸿章府邸"
   scene sence li
   play music"audio/moer.mp3"
   show decuilin at right
   c"中堂大人，天津——镇江一线邮路已经运行了一个月，我想请您为这条邮路的承办人佟在田签发一张护照。"
   hide decuilin
   show lihongzhang at left
   g"（惊讶）佟在田这个人，我略有耳闻。他是一位高级军官，刚刚被牵涉到一件诉讼案中，诉讼的另一方是天津知县，所以我不得不防范他。"
   hide lihongzhang
   show decuilin at right
   c"我对佟在田的过往了解不多，他的举荐人刘桂芳是位值得尊敬的人，由刘桂芳作保，我已同佟在田签订了合同"
   c"既然中堂向我说了这些情况，我想还是把合同撤销了为好。"
   hide decuilin
   show lihongzhang at left
   g"沉吟片刻）不，让他去承办。佟在田是个很能干的人，他会干得很好。但替我转告他，他要利用这次机会挽回他的名誉"
   g"如果他不好好干，行为不检点，我一定要拿他严办。"
   hide lihongzhang
   show decuilin at right
   c"明白了。"
   hide decuilin
   "（李鸿章命人写了护照，随后交给了德璀琳）"
   stop music

   scene sence2hyawork
   play music"audio/bgm4.mp3"
   show xiaoli at right
   b"（急匆匆进来禀告）大人，德璀琳大人有急事儿找你。"
   hide xiaoli
   show huyongan at left
   a"知道了，我马上过去。"
   a"（小声嘀咕）这么长时间没找我，这回难道让我重新接管京津骑差邮路吗？"
   hide huyongan
   stop music


   scene sence2dclwork
   play music"audio/aobi.mp3"
   "胡永安敲门后进入，映入眼帘的是德璀琳和两个陌生男人。"
   show huyongan at left
   a"（行礼）德璀琳大人，您找我？"
   hide huyongan
   show decuilin at right
   c"介绍一下，这位是刘桂芳先生，这位是佟在田先生。"
   hide decuilin
   show huyongan at left
   a"见过两位先生。"
   hide huyongan
   show tong at left
   f "胡先生客气，您的大名在下早有耳闻，京津骑差邮路办的可谓红火。"
   hide tong
   show huyongan at left
   a"（羞愧难当）佟先生莫要讽刺在下了，京津骑差邮路开办两个多月我就灰溜溜逃走了，何来红火。"
   hide huyongan
   show tong at left
   f "胡先生误会了，是我表述错误，在下没有讽刺您的意思。"
   f "您是第一个吃螃蟹的人，为我们开出了一条路，您的经验给了我们后来人很大帮助。"
   hide tong
   show huyongan at left
   a"(喜笑颜开）原来如此，哈哈哈哈哈，不过赶鸭子上架罢了，佟先生过誉了。"
   hide huyongan
   show decuilin at right
   c"你们二人就不要客套了，以后有的是机会合作。"
   c"现在人齐了，我们先谈正事。胡先生，你就在旁做个见证就行。"
   hide decuilin
   stop music
   play music"audio/yequ.mp3"
   show huyongan at left
   a"（失落）（心里想：我还想重新接手京津骑差邮路，一雪前耻呢。不过也好，无事也无愁）"
   a"（调整情绪）乐意效劳。"
   hide huyongan
   show decuilin at right
   c"昨日，我到李中堂（李鸿章）那里为佟在田先生办理护照，李中堂告知我，佟先生似乎牵涉到一件诉讼案中。"
   hide decuilin
   show tong at left
   f "（心里咯噔一下）确有此事，不过是族中弟弟与人发生冲突。"
   hide tong
   show liuguifang at left
   h "此话不假，这件案子与在田没有直接关系。"
   hide liuguifang
   show huyongan at left
   a"......"
   hide huyongan
   show decuilin at right
   c"李中堂的意思是让佟先生继续承办邮路，希望佟先生能利用好这次机会挽回你的名誉。"
   hide decuilin
   show liuguifang at left
   h "我依然愿意为在田作保，我相信他的为人。"
   hide liuguifang
   show decuilin at right
   c"既然如此，我愿意继续相信佟先生。"
   c"这是你的护照，好好把邮路办下去。"
   hide decuilin
   show tong at left
   f "谢过大人，在下往后一定洁身自好，尽心竭力的办好邮路，不负各位大人的厚望。"
   hide tong
   show decuilin at right
   c"今日事毕，各位请回吧。"
   hide decuilin
   show huyongan at left
   a"（拱手离开）（心里想：我有种预感，这里边事情绝对不简单，我还是不参合为好）"
   hide huyongan
   stop music

   scene black with eye_open1
   scene sence2dclwork
   play music"audio/bgm4.mp3"
   "（1878年12月21日） 德璀琳办公室"
   "（屋内德璀琳端坐办公桌前，神色凝重，桌子对面站着佟在田和刘桂芳）"
   show tong at left
   f "大人，今日前来是为了之前的诉讼纠纷，天津知县不停的状告我，要求将我革职查办。"
   f "希望大人能够出面帮我调解和说情。"
   hide tong
   show decuilin at right
   c"（不悦、无奈）我一直不愿意将自己搅和进他人的法律纠纷中，可是眼看着你的纠纷要影响到我们的邮路，这令我很难处理。"
   hide decuilin
   show liuguifang at left
   h "大人，只有您出面调解，在田才能顺利摆脱麻烦，专心负责邮路"
   hide liuguifang
   show decuilin at right
   c"不必多说了，我意已决。我是绝对不会参与你们的纠纷的。"
   c"而且李中堂一定会彻查此事，更轮不到我了。"
   hide decuilin
   show tong at left
   f "（沉默）。。。。。。"
   hide tong
   show decuilin at right
   c"在你彻底解决纠纷之前，我觉得有必要让刘桂芳先生代你履行合同。"
   hide decuilin
   show liuguifang at left
   h "事已至此，也只能这么办了"
   hide liuguifang
   show tong at left
   f "那邮路的事就拜托刘先生了。"
   hide tong
   stop music


   scene sence2hyawork
   play music"audio/aobi.mp3"
   show xiaoli at right
   b"（慌张）大人，大事不妙了，德璀琳大人找你。"
   hide xiaoli
   show huyongan at left
   a"哎呦哎呦，别慌，喘口气。"
   a"每个月准来一次这种戏码，能有啥事啊。"
   hide huyongan
   show xiaoli at right
   b"具体我也不知道，不过德璀琳大人特别愤怒。"
   hide xiaoli
   show huyongan at left
   a"（疑惑）行行行，我这就过去。"
   hide huyongan
   show decuilin at right
   c"快步走进来）不用了，事态紧急，我还是直接来找你吧。"
   hide decuilin
   show huyongan at left
   a"（急忙站起）到底什么事，让您这般上火。"
   a"王贵，你先忙你的吧。"
   show xiaoli at right
   b"是。（赶忙退出屋外）"
   hide xiaoli
   show huyongan at left
   a"当然记得，不过最近局里好像在传他惹上不小的麻烦。"
   hide huyongan
   show decuilin at right
   c"他可把我害惨了。"
   c"天津——镇江一线穿越山东境内，此前，山东当局以未提前告知他们要开办邮路为由，显示出要阻挠邮路的意图。"
   c"胡先生，我知道你是一个富有责任心和冒险精神的人，我想派你前往山东调和此事。"
   hide decuilin

   call demo4 from _call_demo4
   scene black with eye_open1
   scene sence12
   play music"audio/yequ.mp3"
   "山东巡抚府邸"
   "（胡永安抵达山东巡抚府邸，被引入会客厅。山东巡抚面色冷峻，显然对此事持强硬态度。）"
   show huyongan at left
   a"（行了个标准的作揖礼，声音沉稳而有力）巡抚大人，在下胡永安，此番前来，实乃为了解开误会，恢复邮路之畅通，还望大人海涵。"
   hide huyongan
   show shangdong at right
   i"(冷哼一声)胡先生，你口中的误会，对本官而言，却是关乎朝廷法度与地方安宁的大事。佟在田之事，你作何解释？"
   hide shangdong
   show huyongan at left
   a"（深吸一口气，缓缓道）巡抚大人，关于佟在田，在下确有新发现。经我方仔细调查，发现他所涉案件疑点重重，有被人陷害之嫌。至于邮路之事，确实是我们考虑不周，未能及时与大人沟通，但请大人念在国家通讯之重要，以及我等守护邮路之不易，给予我们一个改正的机会。。"
   a"在下这里还有一封李中堂的亲笔书信，请大人过目。"
   hide huyongan
   show shangdong at right
   i"哦？来人，速速将信封拿上来。"
   hide shangdong
   "（巡抚打开信封细细阅读，片刻后脸色逐渐缓和，片刻后，他放下信纸，目光复杂地看向胡永安）"
   show shangdong at right
   i"胡先生，你确实有备而来。但本官仍有一事不明，为何你们要如此急于恢复邮路？难道仅仅是为了传递几封信件吗？"
   hide shangdong
   show huyongan at left
   a"（正色道）巡抚大人，邮路之畅通，关乎国家政令之传达、商务之往来、民情之反馈，乃至边疆之安定。一旦邮路受阻，信息不畅，后果不堪设想。我等虽为小小邮差，但深知肩上责任重大。因此，无论遇到何种困难，我们都将全力以赴，确保邮路畅通无阻。"
   hide huyongan
   show shangdong at right
   i"（不禁点头赞许）胡先生言之有理，本官差点被一己之私蒙蔽了双眼。邮路之重要确如你所说，那么本官便网开一面，放还邮差与信件，并助你们恢复邮路。"
   hide shangdong
   show huyongan at left
   a"（大喜，再次行礼致谢）多谢巡抚大人深明大义！在下定当铭记在心，日后定当更加谨慎行事，不负大人所托。"
   hide huyongan
   stop music


   scene black with eye_open1
   scene sence2dclwork
   play music"audio/aobi.mp3"
   "德璀琳办公室"
   "（德璀琳满怀期待的打开胡永安从山东寄回的信件）"
   show xin
   "德璀琳先生：经过多日的调解与努力，从天津至济南沿途被扣留的邮件已获准放行，被拘的邮差也已得到释放，济南以北的邮路业已恢复畅通。"
   "然而，遗憾的是，济南以南的邮路仍有部分未能恢复。我观察到，山东当局的态度虽因李中堂的信函而有所缓和，但并未发生根本性转变。"
   "例如，驻济南的华洋书信馆代办人员已被迫撤离济南，现于黄河之畔的齐河县设立临时站点，以维持邮件的交换工作。"
   "鉴于此，我已决定即刻南下，继续追踪并寻回那些散失及仍被扣留的邮件。敬请放心，我将不遗余力，直至所有问题得以圆满解决。"
   show decuilin at right
   c"（兴奋）太好了，我果然没看错人。胡先生勇敢、聪慧、富有责任心。等他回来，我一定要好好奖励他一番。"
   hide decuilin
   hide xin
   stop music

   scene sence new
   play music"audio/yuan.mp3"
   "（日暮时分，夕阳如血，映照出一片繁忙而有序的景象。胡永安风尘仆仆地回到邮局，他们的身影刚一出现在大门口，就引起了一阵骚动。邮差们纷纷停下手中的工作，围了上来，眼中闪烁着敬佩与喜悦的光芒。）"
   show xiaoli at right
   b"（急切）胡先生，您回来了！怎么样？事情解决了吗？"
   hide xiaoli
   show huyongan at left
   a"（微笑着点了点头，声音洪亮而充满自信）：大家放心，经过一番努力，山东巡抚已经同意放还我们的邮差和信件，邮路也很快恢复畅通。"
   hide huyongan
   "（人群中爆发出一阵欢呼声。大家纷纷上前，有的握手祝贺，有的拥抱表示感激，整个邮局洋溢着一种久违的轻松与喜悦。）"
   show xiaoli at right
   b"来来来，大人，咱们到西街喝上一杯，好好庆祝庆祝。"
   hide xiaoli
   show huyongan at left
   a"嘿嘿，庆祝自然少不了。不过，容我先去跟德璀琳大人汇报一下工作。"
   hide huyongan
   stop music

   scene sence2dclwork
   play music"audio/moer.mp3"
   "（胡永安快步走进办公室，只见德璀琳早已等候在那里，脸上挂着满意的笑容。）"
   show decuilin at right
   c"（站起身来，迎上前去，与A紧紧握手）胡先生，你果然没有让我失望。多亏了你成功解决山东的问题，恢复了邮路的畅通，这真是太好了！"
   hide decuilin
   show huyongan at left
   a"（谦逊微笑）这都是大人领导有方，我只是尽了自己的一份绵薄之力。"
   hide huyongan
   show decuilin at right
   c"（摇了摇头）胡先生，你太谦虚了。你的勇气和智慧，你的责任心和冒险精神，都是我们邮局宝贵的财富。我代表邮局上下，向你表示最诚挚的感谢和最高的敬意。"
   hide decuilin
   "（说着，德璀琳从抽屉里取出一份文件，递给了胡永安）"
   show decuilin at right
   c"这是对你此次功绩的表彰决定，以及相应的奖励。请务必收下。"
   hide decuilin
   show huyongan at left
   a"（心里想：奖励200两啊，这么多，不枉费我跋山涉水走上这么一趟山东。）（喜悦）谢谢大人。"
   hide huyongan
   show decuilin at right
   c"不用客气，这都是你应得的。"
   c"（郑重）咳咳，我也知道你刚回来，但是还有一件重要的事需要你来办。"
   hide decuilin
   show huyongan at left
   a"（生无可恋）大人，你也知道我这刚回来，水都没来得及喝上一口。"
   hide huyongan
   show decuilin at right
   c"（目光狡黠）我也没办法，放眼局内，当下有能力胜任的唯有你一个。"
   hide decuilin
   show huyongan at left
   a"（心里想：完了，又是这种非我不可的活计，我这才来几天啊）大人，但讲无妨。"
   hide huyongan
   show decuilin at right
   c"鉴于你的过人能力和突出表现，我们决定由你负责组班天津——北京、天津——镇江、天津——牛庄三条线路的冬季邮运工作。"
   hide decuilin
   show huyongan at left
   a"（惊讶）（心里想：玩这么大，也罢，完成这次任务肯定能够回去）胡某领命，开办邮路，利国利民，在下定当竭尽全力，不辱使命。"
   hide huyongan
   stop music
   "此后，胡永安吸取之前承办京津骑差邮路的经验，整顿邮运组织机构；合理安排中继站点；雇佣的信差都为天津府人，都有保人，且大多数都在私营信局里工作五年以上，既可靠又有工作效率。三条线路的邮运工作如火如荼的开展起来。"
   scene sence2hyawork with eye_open
   play music"audio/BGM1.mp3"
   "一年后"
   "胡永安正在办公室查看线路地图，忽然一阵白光闪过"
   scene baiguang with eye_close
   show huyongan at left
   a"这久违的白色光芒，这熟悉的晕眩感，终于可以回去了吗？"
   a"不过，我居然有点舍不得这里。现在邮路刚刚进入正轨，我刚要大展拳脚，我不甘心啊."
   "......."
   hide huyongan
   stop music









   return
