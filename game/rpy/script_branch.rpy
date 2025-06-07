label demo():
       scene sence2dclwork
       menu:
           "是：谢大人看重，在下定不负大人的厚望。":
             call script_a_1 from _call_script_a_1
             call script_c from _call_script_c


           "否：我再考虑考虑。":
            call script_b_1 from _call_script_b_1
            call script_b_2 from _call_script_b_2
            call script_c from _call_script_c_1
       menu:
           "是否要重新选择"
           "是":
               jump demo

           "否":
               pass

       return

label demo2():
       scene sence1fall
       menu:
           "向左":
            call script_d from _call_script_d



           "向右":
            call script_e from _call_script_e

       return

label demo3():
       scene sence2dclwork
       menu:
           "心想，真难伺候，我要摆烂了":
            call script_f from _call_script_f


           "我有一个建议，或许能够帮助我们走出这一困境。":
            call script_g from _call_script_g


       return

label demo4():
      scene sence1hyawork
      play music"audio/yequ.mp3"
      menu:
          "拒绝":
           call script_h from _call_script_h

          "接受":
           call script_i from _call_script_i
      return


label script_a_1:
    show huyongan at left
    a"谢大人看重，在下定不负大人的厚望。"
    hide huyongan
    return

label script_b_1:
    show huyongan at left
    a"我再考虑考虑。"
    hide huyongan
    return

label script_b_2:
    show decuilin at right
    c"按合同规定，每月付给承包人110两。"
    hide decuilin
    show huyongan at left
    a"好吧 我答应了。"
    hide huyongan
    return

label script_c:
    show decuilin at right
    c"这是合同细则，你仔细看一下。"
    hide decuilin
    scene hetong1
    "天津海关为办理邮递业务，与承办人胡永安签订合同，规定实施办法如下:承办人保证每天从天津到北京并从北京到天津运送邮件各一次，重量以四十磅为限，并保证在待运的信袋交给他或者他的信差以后，于十二小时以内送达."
    "除遇到很坏的天气，如因雨路途不能通行的情形外，信差往来运送邮件的时间如超过规定的时间每半小时，胡永安须受罚款一元的处分;同时，如因特殊情形并经特别指示，信差能提前将邮件送达时，每提前半小时，增加运费五角。"
    "邮件以外，不得带运其他邮件。违犯这项规定时，承办人应受罚款银50两的处分.信差应穿制服，制服包括制服帽和镶有红边和白色盾形胸杯的黑色号衣，上而有“津海关信差”字样。每一信差都由津海关税务司发给护照一份。"
    scene hetong2
    "规定每天日落前为天津发送邮件的时间，以便第二天清晨到达北京投递;但外国邮件如在夜间或者清晨到达天津，只要信差能在关闭城门以前到达北京，就应即刻发送。"
    "待发的邮件过多时，津海关书信馆应将电报、公文、信函和寄给总税务司的报纸先行运送;其余的留待下一次的信差或临时信差运送。"
    "从北京来天津的信差，每天规定在下午四时准时出发，以便邮件在第二天清晨到达天津，赶上出港的船只。为避免使信差一次负担过重，所有信函、公文等，每天于准备妥当后应即发出，以保证尽先送达目的地。"
    scene hetong3
    "寄往外国、上海或上海以南和以西各通商口岸的邮件，应用袋封装，或用坚固纸袋封装，写明交上海江海关书信馆;"
    "寄往天津、烟台或牛庄通商口岸的邮件，应写明交津海关书信馆。信差出发和到达的时间，仍照旧例分别由发送和收信的书信馆在路簿内注明。在另有规定以前，不收寄海关以外的邮件。公使馆如愿意承担费用，可以收寄它们的邮件，条件以后再订。"
    show huyongan at left
    a"这才刚来，就交给我这么重要的任务，真让人感到压力山大啊。"
    hide huyongan
    stop music
    return

label script_d:
    scene sence1out
    "顺利到达河西务"

    return
label script_e:
    scene sence1out
    "两个小时后，远远看见亮光，接近一个中继站"
    show youchai1 at left
    d"（费解）奇怪，这周遭的环境怎么这么熟悉？前方的驿站好像是杨村驿站。"
    "（他来到驿站门口，碰到了之前路上遇见的正在修整的邮差兄弟。）"
    hide youchai1
    scene sence1menkou
    show youchai2 at right
    e"兄弟，我记得咱们是相对而行的，怎么在这儿碰见了。"
    hide youchai2
    show youchai1 at left
    d"（恍然大悟、懊恼）我这下琢磨过味儿来了，我之前在路上打瞌睡坠了马，摔的晕头转向。那个地方前不着村后不着店的，我一时之间竟迷了方向。又回到了出发点。"
    hide youchai1
    show youchai2 at right
    e"快快快，进来坐着，你人咋样？受伤了吗？"
    hide youchai2
    show youchai1 at left
    d"谢谢关心，所幸并无大碍。我这一趟耽误不少时间，我还是尽快出发为好，下一站的兄弟还在等着接力送信呢。"
    hide youchai1
    show youchai2 at right
    e"（倒了一碗热水）兄弟，把这碗热水喝了暖暖身子再出发吧。"
    hide youchai2
    show youchai1 at left
    d"（接过热水）谢谢兄弟。"
    hide youchai1
    "他将热水喝下后，不做停留，上马向着河西务飞驰而去。"
    hide youchai1
    scene sence1out
    "顺利到达河西务"

    return
label script_f:
    scene sence2dclwork
    play music"audio/bgm4.mp3"
    show huyongan at left
    a"事已至此，我觉得我无法胜任这项工作了，烦请大人另择他人。"
    hide huyongan
    show decuilin at right
    c"胡先生，你实在太令我失望了。即日起，我解除与你订立的合同，你这样的态度，恐怕也难以继续在海关邮政从事工作了。"
    stop music
    hide decuilin
    "任务失败"
    jump demo3
    return


label script_g:
    scene sence2dclwork
    play music"audio/bgm4.mp3"
    show decuilin at right
    c"（情绪缓和）说说看。"
    hide decuilin
    show huyongan at left
    a"我建议增加人手到12人，马匹增加到16匹，每名邮差月钱6两"
    hide huyongan
    "（动笔在纸上飞快演算着什么，随后眉头紧皱。）"
    show decuilin at right
    c"胡先生，如果按照你的建议，我们每月的开支将会达到200两。目前，我们的开支在110两左右，我认为不便于增加开支。目前邮路刚刚开办，等日后我们的邮递事业收入能够提供所需经费时，再考虑增加支出"
    hide decuilin
    show huyongan at left
    a"德璀琳大人，邮差们之前都是身强力壮、意气风发，如今都失去了劲头，坠马事件时有发生、有的还患上了疾病，落下了病根。如果不增加人手的话，我们的八名邮差在这样高强度工作下迟早会被累垮的。"
    a"而且，目前这样微薄的薪资让他们难以养家糊口、治疗伤病。"
    hide huyongan
    show decuilin at right
    c"（被打动）我也是受命于人，我向上司反应过这些情况，上司们有他们的想法，我也不能改变什么。"
    hide decuilin
    show huyongan at left
    a"......"
    hide huyongan
    show decuilin at right
    c"这样，最近你和你手下的邮差们都很劳累，我会解除跟你签订的合同。我授权你将邮差们安排到他们原来的岗位，先休整休整。放心，像你这样负责任的人不会被雪藏的，天津到牛庄一线的邮路也正在开办，就由你领班吧"
    hide decuilin
    show huyongan at left
    a"(感激）谢过大人，不过我们撤出之后，京津骑差邮路由谁负责呢？"
    hide huyongan
    show decuilin at right
    c"这个你不必担心，我自有人选。我会将这条邮路交给德诚信局的王长发，他出身民信局，或许他会有不一样的门道。"
    hide decuilin
    show huyongan at left
    a"既然大人已有安排，在下就告辞了。（拱手离开）"
    hide huyongan
    stop music
    return

label script_h:
    play music"audio/yequ.mp3"
    show huyongan at left
    a"（难以置信）（心里想：什么富有冒险精神，这不哄小孩子吗？）此事情况着实复杂，恐怕在下难以胜任。"
    hide huyongan
    show decuilin at right
    c"胡先生再考虑考虑，当下只有交给你我才放心。"
    hide decuilin
    show huyongan at left
    a"（心里想：还在道德绑架我，我才不上当）局内英才辈出，大人不妨另寻他人。"
    hide huyongan
    show decuilin at right
    c"（失望）既然如此，我也不再多说什么。"
    hide decuilin
    "德璀琳随后派邓启贤前往山东府调解此事，成功化解矛盾，解救下了被扣留的邮差和信件。胡永安渐渐失去了德璀琳的信任，事业不再顺利，日渐消沉。任务失败"
    jump demo4
    stop music
    return

label script_i:
    show huyongan at left
    a"（担忧）此事情况着实复杂，恐怕单靠我这一张嘴难以解决啊。"
    hide huyongan
    show decuilin at right
    c"放心，我已拜托李中堂写了一封信，有此信作为主药，辅以你的才能，我相信这件事一定会顺利解决的"
    hide decuilin
    show huyongan at left
    a"想来，有中堂大人的亲笔书信，山东巡抚定不会为难在下。"
    hide huyongan
    show decuilin at right
    c"胡先生果然深明大义，你的勇气和智慧正是我们所需要的。我已经为你准备了一份详细的资料，包括山东当局可能的立场、李中堂的信件。"
    c"此外，我也会安排人手在沿途保护你，确保你的安全。"
    hide decuilin
    show huyongan at left
    a"（抱拳行礼）大人放心，胡某定不负所托，定当竭尽全力，完成任务。"
    hide huyongan





    return
