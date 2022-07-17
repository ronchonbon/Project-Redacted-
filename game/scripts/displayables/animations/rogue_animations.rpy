image Rogue_blinking:
    "images/Rogue_blowjob/Rogue_blowjob_eyes_[Rogue.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_blowjob/Rogue_blowjob_eyes_half.png"
    0.05
    "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    0.15
    "images/Rogue_blowjob/Rogue_blowjob_eyes_half.png"
    0.05
    repeat

image Rogue_blowjob_hair_back_animation0:
    "Rogue_hair_back"

image Rogue_blowjob_hair_back_animation1:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_hair_back_animation2:
    animation
    "Rogue_hair_back"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_hair_back_animation3:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_hair_back_animation4:
    animation
    "Rogue_hair_back"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_body_animation0:
    "Rogue_sprite standing"

image Rogue_blowjob_body_animation1:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (20, 55)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_body_animation2:
    animation
    "Rogue_sprite standing"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_body_animation3:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 yoffset 45
        ease 1.5 yoffset 30
        repeat

image Rogue_blowjob_body_animation4:
    animation
    "Rogue_sprite standing"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1.2 yoffset 70
        pause 0.5
        ease 1.8 yoffset 40
        repeat

image Rogue_blowjob_head_animation0:
    "Rogue_head"

    ease 1.5 offset (0, 0)

image Rogue_blowjob_head_animation1:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (2, -20)
    block:
        ease 2.5 offset (15, 60)
        ease 2 offset (2, -20)
        pause 0.5
        repeat

image Rogue_blowjob_head_animation2:
    animation
    "Rogue_head"

    subpixel True
    block:
        ease 1 yoffset 35
        ease 1.5 yoffset 0
        repeat

image Rogue_blowjob_head_animation3:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 30)
    block:
        ease 1 offset (-0.3, 60)
        ease 1.5 offset (0, 30)
        repeat

image Rogue_blowjob_head_animation4:
    animation
    "Rogue_head"

    subpixel True
    ease 0.5 offset (0, 40)
    block:
        ease 1 offset (0.5, 85)
        pause 0.5
        ease 2 offset (0, 40)
        repeat

image Rogue_blowjob_mouth_animation2:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        pause 0.10
        ease 0.55 zoom 0.94
        linear 0.10 zoom 0.84
        ease 0.30 zoom 0.94
        pause 0.15
        ease 0.40 zoom 0.84
        linear 0.10 zoom 0.94
        ease 0.45 zoom 0.6
        pause 0.35
        repeat

image Rogue_blowjob_mouth_animation3:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.9
    block:
        ease 0.5 zoom 0.9
        ease 0.5 zoom 0.97
        ease 0.75 zoom 0.94
        ease 0.75 zoom 0.97
        repeat

image Rogue_blowjob_mouth_animation4:
    animation
    "Rogue_blowjob_mouth"

    subpixel True
    zoom 0.94
    block:
        ease 0.5 zoom 0.94
        ease 0.5 zoom 1.0
        pause 0.5
        ease 0.5 zoom 0.96
        ease 1.5 zoom 1.0
        repeat

layeredimage Rogue_sprite blowjob:
    always:
        "Rogue_blowjob_hair_back_animation[Rogue.primary_Action.speed]" pos (0.031, 0.317) zoom 0.2755

    always:
        "Rogue_blowjob_body_animation[Rogue.primary_Action.speed]"

    always:
        "Rogue_blowjob_head_animation[Rogue.primary_Action.speed]" pos (0.031, 0.317) zoom 0.2755

    anchor (0.5, 0.0) offset (220, -320) zoom 2.75

image Rogue_sex_body_animation0:
    "Rogue_sex_body"

image Rogue_sex_body_animation1:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.5
        ease 0.75 yoffset -5
        pause 1.25
        ease 2.5 yoffset 0
        repeat

image Rogue_sex_body_animation2:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.6
        ease 0.4 yoffset -10
        ease 0.25 yoffset -5
        pause 1
        ease 2.75 yoffset 10
        repeat

image Rogue_sex_body_animation3:
    animation
    "Rogue_sex_body"

    subpixel True
    block:
        pause 0.17
        ease 0.13 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 10
        repeat

image Rogue_sex_legs_animation0:
    "Rogue_sex_legs"

image Rogue_sex_legs_animation1:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.25
        ease 1 yoffset -5
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation2:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.5
        ease 0.5 yoffset -15
        ease 0.25 yoffset -10
        pause 1
        ease 2.75 yoffset 0
        repeat

image Rogue_sex_legs_animation3:
    animation
    "Rogue_sex_legs"

    subpixel True
    block:
        pause 0.15
        ease 0.15 yoffset -20
        ease 0.10 yoffset -15
        pause 0.20
        ease 1.4 yoffset 0
        repeat

image Rogue_sex_anus_animation0:
    "Rogue_sex_anus"

    xzoom 0.6

image Rogue_sex_anus_animation1:
    animation
    "Rogue_sex_anus"

    subpixel True
    xzoom 0.6
    block:
        ease 0.75 xzoom 1.0
        ease 0.25 xzoom 0.9
        pause 1.50
        ease 0.25 xzoom 1.0
        ease 2.25 xzoom 0.6
        repeat

image Rogue_sex_anus_animation2:
    "Rogue_sex_anus"

image Rogue_sex_anus_animation3:
    "Rogue_sex_anus"

layeredimage Rogue_sprite sex:
    if Player.primary_Action.type in ["sex", "anal"]:
        "Rogue_sex_body_animation[Player.primary_Action.speed]"

    if Player.primary_Action.type in ["sex", "anal"]:
        "Rogue_sex_legs_animation[Player.primary_Action.speed]"

    anchor (0.5, 0.0) offset (370, 770)

image Rogue_doggy_blinking:
    "images/Rogue_doggy/Rogue_doggy_eyes_[Rogue.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Rogue_doggy/Rogue_doggy_eyes_squint.png"
    0.05
    "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    0.15
    "images/Rogue_doggy/Rogue_doggy_eyes_squint.png"
    0.05
    repeat

image Rogue_doggy_body_animation0:
    "Rogue_doggy_body"

image Rogue_doggy_body_animation1:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        pause 0.4
        ease 0.3 yoffset -5
        ease 1 yoffset 0
        pause 0.8
        repeat

image Rogue_doggy_body_animation2:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        ease 0.5 yoffset 5
        pause 0.25
        ease 1.75 yoffset 15
        repeat

image Rogue_doggy_body_animation3:
    animation
    "Rogue_doggy_body"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset 0
        pause 0.1
        ease 0.5 yoffset 20
        pause 0.05
        repeat

image Rogue_doggy_ass_animation0:
    "Rogue_doggy_ass"

image Rogue_doggy_ass_animation1:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.4
        ease 0.2 yoffset -10
        ease 0.1 yoffset -7
        ease 0.9 yoffset 0
        pause 0.9
        repeat

image Rogue_doggy_ass_animation2:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        ease 0.3 yoffset -15
        ease 0.2 yoffset -5
        pause 0.25
        ease 1.75 yoffset 0
        repeat

image Rogue_doggy_ass_animation3:
    animation
    "Rogue_doggy_ass"

    subpixel True
    block:
        pause 0.15
        ease 0.1 yoffset -25
        ease 0.1 yoffset -15
        pause 0.1
        ease 0.4 yoffset 5
        pause 0.05
        repeat

image Rogue_doggy_pussy_hole_animation0:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.65
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation1:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 1
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_pussy_hole_animation2:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_hole_animation3:
    "Rogue_doggy_pussy_hole"

image Rogue_doggy_pussy_hole_fingering:
    animation
    "Rogue_doggy_pussy_hole"

    subpixel True
    xzoom 0.6
    block:
        ease 1 xzoom 0.67
        pause 1
        ease 3 xzoom 0.6
        repeat

image Rogue_doggy_anus_anal_animation1:
    animation
    "Rogue_doggy_anus_hole"

    subpixel True
    zoom 0.5
    block:
        ease 0.5 zoom 1
        pause 0.5
        ease 1.5 zoom 0.5
        repeat

image Rogue_doggy_anus_anal_animation2:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_anal_animation3:
    "Rogue_doggy_anus_hole"

    zoom 0.9

image Rogue_doggy_anus_fingering_animation:
    animation
    "Rogue_doggy_anus_hole"

    subpixel True
    zoom 0.6
    block:
        ease 0.5 zoom 0.67
        pause 0.5
        ease 1.5 zoom 0.6
        repeat

layeredimage Rogue_sprite doggy:
    if Player.primary_Action.type == "anal":
        "Rogue_doggy_body_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "sex" and Player.primary_Action.speed > 1:
        "Rogue_doggy_body_animation[Player.primary_Action.speed]"
    else:
        "Rogue_doggy_body"

    if Player.primary_Action.type == "anal":
        "Rogue_doggy_ass_animation[Player.primary_Action.speed]"
    elif Player.primary_Action.type == "sex" and Player.primary_Action.speed > 1:
        "Rogue_doggy_ass_animation[Player.primary_Action.speed]"
    else:
        "Rogue_doggy_ass"

    always:
        "Rogue_doggy_shins"

    always:
        "Rogue_doggy_feet"

    anchor (0.5, 0.0) offset (150, 700) zoom 1.2
