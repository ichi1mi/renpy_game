screen ck:
    imagebutton:
        xanchor 0
        yanchor 0
        xpos 10
        ypos 10
        auto "dcl_%s.png"
        action [Hide("displayTextScreen"), Jump("end")]

        hovered Show("displayTextScreen", displayText ="人物简介")
        unhovered Hide("displayTextSreen")

screen displayTextScreen:
    default dispalyText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
