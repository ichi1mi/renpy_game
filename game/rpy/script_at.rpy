screen at:
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 110
        ypos 110
        auto "bj_%s.png"
        action [Hide("displayTextScreen"), Jump("bj")]

        hovered Show("displayTextScreen", displayText ="北京")
        unhovered Hide("displayTextScreen")


    imagebutton:
        xanchor 0
        yanchor 0
        xpos 910
        ypos 120
        auto "zwj_%s.png"
        action [Hide("displayTextScreen"), Jump("zwj")]

        hovered Show("displayTextScreen", displayText ="张家湾")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1400
        ypos 540
        auto "hxw_%s.png"
        action [Hide("displayTextScreen"), Jump("hxw")]

        hovered Show("displayTextScreen", displayText ="河西务")
        unhovered Hide("displayTextScreen")


    imagebutton:
        xanchor 0
        yanchor 0
        xpos 850
        ypos 790
        auto "yc_%s.png"
        action [Hide("displayTextScreen"), Jump("yc")]

        hovered Show("displayTextScreen", displayText ="杨村")
        unhovered Hide("displayTextScreen")


    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1600
        ypos 900
        auto "tj_%s.png"
        action [Hide("displayTextScreen"), Jump("tj")]

        hovered Show("displayTextScreen", displayText ="天津")
        unhovered Hide("displayTextScreen")

    imagebutton:
        xanchor 0
        yanchor 0
        xpos 1725
        ypos 20
        auto "tiaoguo2_%s.png"
        action [Hide("displayTextScreen"), Jump("tg2")]

        hovered Show("displayTextScreen", displayText ="跳过")
        unhovered Hide("displayTextScreen")


screen displayTextScreen:
    default dispalyText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
