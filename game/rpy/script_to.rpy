screen to:
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 200
        ypos 680
        auto "yd_%s.png"
        action [Hide("displayTextScreen"), Jump("yd")]

        hovered Show("displayTextScreen", displayText ="邮袋")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 680
        ypos 600
        auto "ld_%s.png"
        action [Hide("displayTextScreen"), Jump("ld")]

        hovered Show("displayTextScreen", displayText ="铃铛")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1625
        ypos 180
        auto "mz_%s.png"
        action [Hide("displayTextScreen"), Jump("mz")]

        hovered Show("displayTextScreen", displayText ="斗笠")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1725
        ypos 20
        auto "tiaoguo_%s.png"
        action [Hide("displayTextScreen"), Jump("tg")]

        hovered Show("displayTextScreen", displayText ="跳过")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1000
        ypos 590
        auto "bd_%s.png"
        action [Hide("displayTextScreen"), Jump("bd")]

        hovered Show("displayTextScreen", displayText ="扁担/木棍")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1625
        ypos 450
        auto "hy_%s.png"
        action [Hide("displayTextScreen"), Jump("hy")]

        hovered Show("displayTextScreen", displayText ="号衣")
        unhovered Hide("displayTextScreen")




screen displayTextScreen:
    default dispalyText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
