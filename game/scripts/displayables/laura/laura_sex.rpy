image Laura_sex_body:
    "images/Laura_sex/Laura_sex_body.png"

    anchor (0.5, 0.5)

layeredimage Laura_sex_legs:
    always:
        "images/Laura_sex/Laura_sex_legs.png"

    if Laura.ass_Action.type == "anal":
        "Laura_sex_anus_animation[Laura.ass_Action.speed]" pos (0.805, 1.505)
    else:
        "images/Laura_sex/Laura_sex_anus_closed.png" anchor (0.5, 0.5) pos (0.805, 1.505)

    if Laura.pussy_Action.type == "sex":
        "Laura_sex_pussy_animation[Laura.pussy_Action.speed]" pos (0.77, 1.4)
    else:
        "images/Laura_sex/Laura_sex_pussy_closed.png" anchor (0.5, 0.5) pos (0.77, 1.4)

    if Laura.pubes:
        "images/Laura_sex/Laura_sex_pubes_[Laura.pubes].png"

    anchor (0.5, 0.5)

image Laura_sex_feet:
    "images/Laura_sex/Laura_sex_feet.png"

    anchor (0.5, 0.5)

image Laura_sex_body_animation0:
    "Laura_sex_body"

image Laura_sex_body_animation1:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.8 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.8 xpos 0.0
        repeat

image Laura_sex_body_animation2:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.8 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.8 xpos 0.0
        repeat

image Laura_sex_body_animation3:
    animation
    "Laura_sex_body"

    subpixel True
    pos (0.0, 0.015)
    parallel:
        pause 0.1
        ease 0.2 ypos 0.0
        pause 0.1
        ease 1.8 ypos 0.015
        repeat
    parallel:
        pause 0.1
        ease 0.2 xpos -0.015
        pause 0.1
        ease 1.8 xpos 0.0
        repeat

image Laura_sex_legs_animation0:
    "Laura_sex_legs"

image Laura_sex_legs_animation1:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_legs_animation2:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_legs_animation3:
    animation
    "Laura_sex_legs"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_feet_animation0:
    "Laura_sex_feet"

image Laura_sex_feet_animation1:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_feet_animation2:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_feet_animation3:
    animation
    "Laura_sex_feet"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        pause 0.05
        ease 0.2 ypos -0.02
        easeout 0.45 ypos -0.015
        easein 1.5 ypos 0.0
        repeat
    parallel:
        pause 0.05
        ease 0.2 xpos -0.02
        easeout 0.45 xpos -0.015
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_pussy_animation0:
    "images/Laura_sex/Laura_sex_pussy_closed.png"

    anchor (0.5, 0.5)

image Laura_sex_pussy_animation1:
    animation
    "images/Laura_sex/Laura_sex_pussy_open.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_pussy_animation2:
    animation
    "images/Laura_sex/Laura_sex_pussy_fucking.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_pussy_animation3:
    animation
    "images/Laura_sex/Laura_sex_pussy_fucking.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_anus_animation0:
    "images/Laura_sex/Laura_sex_anus_closed.png"

    anchor (0.5, 0.5)

image Laura_sex_anus_animation1:
    animation
    "images/Laura_sex/Laura_sex_anus_open.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_anus_animation2:
    animation
    "images/Laura_sex/Laura_sex_anus_fucking.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_anus_animation3:
    animation
    "images/Laura_sex/Laura_sex_anus_fucking.png"

    subpixel True
    anchor (0.5, 0.5)
    block:
        ease 0.2 zoom 1.02
        easeout 0.5 zoom 1.0
        easein 1.5 zoom 1.0
        repeat

image Laura_sex_cock_animation0:
    "Zero_cock"

image Laura_sex_cock_animation1:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_animation2:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_animation3:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation0:
    "Zero_cock"

image Laura_sex_cock_anal_animation1:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation2:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

image Laura_sex_cock_anal_animation3:
    animation
    "Zero_cock"

    subpixel True
    pos (0.0, 0.0)
    parallel:
        ease 0.2 ypos -0.05
        easeout 0.5 ypos -0.04
        easein 1.5 ypos 0.0
        repeat
    parallel:
        ease 0.2 xpos -0.04
        easeout 0.5 xpos -0.03
        easein 1.5 xpos 0.0
        repeat

layeredimage Laura_sex_cock_animations:
    if Player.cock_Action.type == "sex":
        "Laura_sex_cock_animation[Player.cock_Action.speed]" offset (150, 205) rotate -35 zoom 1.25
    elif Player.cock_Action.type == "anal":
        "Laura_sex_cock_anal_animation[Player.cock_Action.speed]" offset (150, 250) rotate -35 zoom 1.25

image Laura_sprite sex:
    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_body_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_body_animation0")

    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_legs_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_legs_animation0")

    # contains:
    #     "Laura_sex_cock_animations"

    contains:
        ConditionSwitch(
            "Laura in Player.cock_Action.Actors", "Laura_sex_feet_animation[Player.cock_Action.speed]",
            "True", "Laura_sex_feet_animation0")

    anchor (0.5, 0.0) offset (500, 550) zoom 0.45
