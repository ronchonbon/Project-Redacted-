layeredimage Rogue_sprite standing:
    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_hair_back" pos (0.314, 0.312) zoom 0.58

    always:
        "images/Rogue_standing/Rogue_standing_body.png"

    always:
        "images/Rogue_standing/Rogue_standing_arms.png"

    always:
        "images/Rogue_standing/Rogue_standing_breasts.png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_head" pos (0.314, 0.312) zoom 0.58

    anchor (0.5, 0.0) offset (5, 180) zoom 0.48

layeredimage Rogue_hair_back:
    always:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[Rogue.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if renpy.showing("Rogue_sprite blowjob") and Rogue.primary_Action.speed:
        "images/Rogue_blowjob/Rogue_blowjob_face[Rogue.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[Rogue.blushing].png"

    if renpy.showing("Rogue_sprite blowjob") and Rogue.primary_Action.speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and Rogue.primary_Action.speed > 1:
        "Rogue_blowjob_mouth_animation[Rogue.primary_Action.speed]" pos (0.164, 0.55)
    elif Rogue.mouth == "sucking":
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_[Rogue.mouth].png"

    if Rogue.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[Rogue.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[Rogue.brows].png"

    if Rogue.eyes == "closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    else:
        "Rogue_blinking"

    always:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[Rogue.Clothes[hair].string].png"

    anchor (0.5, 0.5)

layeredimage Rogue_blowjob_mouth:
    always:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_sucking.png"

    anchor (0.4, 0.65)

layeredimage Rogue_sex_body:
    always:
        "Rogue_hair_back" pos (0.287, 0.075) rotate -10 zoom 0.37

    always:
        "images/Rogue_sex/Rogue_sex_body.png"

    always:
        "Rogue_head" pos (0.287, 0.075) rotate -10 zoom 0.37

    anchor (0.5, 0.5)

layeredimage Rogue_sex_legs:
    always:
        "images/Rogue_sex/Rogue_sex_legs.png"

    if Player.primary_Action.type == "anal":
        "Rogue_sex_anus_animation[Player.primary_Action.speed]" pos (0.292, 0.386)
    else:
        "images/Rogue_sex/Rogue_sex_anus_tight.png"

    if Player.primary_Action.type == "sex" and Player.primary_Action.speed >= 2:
        "images/Rogue_sex/Rogue_sex_pussy_fucking.png"
    elif Player.primary_Action.type == "sex" and Player.primary_Action.speed:
        "images/Rogue_sex/Rogue_sex_pussy_open.png"
    else:
        "images/Rogue_sex/Rogue_sex_pussy_closed.png"

    always:
        "Rogue_sex_feet" pos (0.291, 0.391)

    anchor (0.5, 0.5)

layeredimage Rogue_sex_feet:
    always:
        "images/Rogue_sex/Rogue_sex_feet.png"

    anchor (0.5, 0.5)

image Rogue_sex_anus:
    "images/Kitty_sex/Kitty_sex_anus_open.png"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_body:
    if Rogue.Clothes["hair"].string == "Evolutions_hair":
        "images/Rogue_doggy/Rogue_doggy_hair_back.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_body.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_mouth_[Rogue.mouth].png"

    if Rogue.blushing:
        "images/Rogue_doggy/Rogue_doggy_blush.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_brows_[Rogue.brows].png"

    if Rogue.eyes == "closed":
        "images/Rogue_doggy/Rogue_doggy_eyes_closed.png"
    else:
        "Rogue_doggy_blinking"

    always:
        "images/Rogue_doggy/Rogue_doggy_hair_[Rogue.Clothes[hair].string].png"

    anchor (0.5, 0.5)

layeredimage Rogue_doggy_ass:
    always:
        "images/Rogue_doggy/Rogue_doggy_ass.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_pussy_closed.png"

    if Player.primary_Action.type == "sex":
        "images/Rogue_doggy/Rogue_doggy_pussy_base.png"

    if Player.primary_Action.type == "sex":
        "Rogue_doggy_pussy_hole_animation[Player.primary_Action.speed]" pos (0.113, 0.475)

    always:
        "images/Rogue_doggy/Rogue_doggy_anus_tight.png"

    if Player.primary_Action.type == "anal" and Player.primary_Action.speed:
        "images/Rogue_doggy/Rogue_doggy_anus_full_base.png"

    if Player.primary_Action.type == "anal" and Player.primary_Action.speed:
        "Rogue_doggy_anus_anal_animation[Player.primary_Action.speed]" pos (0.113, 0.475)

    if Player.primary_Action.type == "anal" and Player.primary_Action.speed > 1:
        "images/Rogue_doggy/Rogue_doggy_anus_full_cheeks.png"

    anchor (0.5, 0.5)

image Rogue_doggy_pussy_hole:
    "images/Rogue_doggy/Rogue_doggy_pussy_hole.png"

    anchor (0.52, 0.69)

image Rogue_doggy_anus_hole:
    "images/Rogue_doggy/Rogue_doggy_anus_full_hole.png"

    anchor (0.515, 0.69)

layeredimage Rogue_doggy_shins:
    always:
        "images/Rogue_doggy/Rogue_doggy_shins.png"

    always:
        "images/Rogue_doggy/Rogue_doggy_feet.png"

    anchor (0.5, 0.5)

image Rogue_doggy_feet:
    AlphaMask("Rogue_doggy_shins", "images/Rogue_doggy/Rogue_doggy_toes.png")

    anchor (0.5, 0.5)
