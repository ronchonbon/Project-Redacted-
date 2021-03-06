layeredimage Laura_sprite standing:
    always:
        "images/Laura_standing/Laura_standing_hair_back.png"

    always:
        "images/Laura_standing/Laura_standing_right_arm.png"

    if Laura.Clothes["bodysuit"].string:
        "images/Laura_standing/Laura_standing_bodysuit_[Laura.Clothes[bodysuit].string]_right_sleeve.png"

    always:
        "images/Laura_standing/Laura_standing_body.png"

    always:
        "images/Laura_standing/Laura_standing_breasts.png"

    if Laura.Clothes["bra"].string:
        "images/Laura_standing/Laura_standing_bra_[Laura.Clothes[bra].string].png"

    if Laura.Clothes["gloves"].string:
        "images/Laura_standing/Laura_standing_gloves_[Laura.Clothes[gloves].string]_right.png"

    if Laura.pubes:
        "images/Laura_standing/Laura_standing_pubes_[Laura.pubes].png"

    if Laura.Clothes["underwear"].string:
        "images/Laura_standing/Laura_standing_underwear_[Laura.Clothes[underwear].string].png"

    if Laura.Clothes["bodysuit"].string:
        "images/Laura_standing/Laura_standing_bodysuit_[Laura.Clothes[bodysuit].string].png"

    if Laura.Clothes["top"].string:
        "images/Laura_standing/Laura_standing_top_[Laura.Clothes[top].string].png"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket_[Laura.Clothes[jacket].string].png"

    always:
        "images/Laura_standing/Laura_standing_head.png"

    if Laura.eyes == "closed":
        "images/Laura_standing/Laura_standing_eyes_[Laura.eyes].png"
    else:
        "Laura_standing_blinking"

    always:
        "images/Laura_standing/Laura_standing_brows_[Laura.brows].png"

    always:
        "images/Laura_standing/Laura_standing_mouth_[Laura.mouth].png"

    if Laura.blush:
        "images/Laura_standing/Laura_standing_blush[Laura.blush].png"

    if Laura.claws:
        "images/Laura_standing/Laura_standing_right_claw.png"

    always:
        "images/Laura_standing/Laura_standing_left_arm.png"

    if Laura.Clothes["bodysuit"].string:
        "images/Laura_standing/Laura_standing_bodysuit_[Laura.Clothes[bodysuit].string]_left_sleeve.png"

    if Laura.Clothes["top"].string:
        "images/Laura_standing/Laura_standing_top_[Laura.Clothes[top].string]_left_sleeve.png"

    if Laura.Clothes["jacket"].string:
        "images/Laura_standing/Laura_standing_jacket_[Laura.Clothes[jacket].string]_left_sleeve.png"

    if Laura.wet:
        "images/Laura_standing/Laura_standing_hair_messy_hair.png"
    else:
        "images/Laura_standing/Laura_standing_hair_[Laura.Clothes[hair].string].png"

    if Laura.claws:
        "images/Laura_standing/Laura_standing_left_claw.png"

    if Laura.Clothes["pants"].string:
        "images/Laura_standing/Laura_standing_pants_[Laura.Clothes[pants].string].png"

    if Laura.Clothes["belt"].string:
        "images/Laura_standing/Laura_standing_belt_[Laura.Clothes[belt].string].png"

    if Laura.Clothes["face_inner_accessory"].string:
        "images/Laura_standing/Laura_standing_face_inner_accessory_[Laura.Clothes[face_inner_accessory].string].png"

    anchor (0.5, 0.0) offset (0, 25) zoom 0.55

image Laura_standing_blinking:
    "images/Laura_standing/Laura_standing_eyes_[Laura.eyes].png"
    choice:
        3.5
    choice:
        3.25
    choice:
        3
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.05
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.15
    "images/Laura_standing/Laura_standing_eyes_closed.png"
    0.05
    repeat
