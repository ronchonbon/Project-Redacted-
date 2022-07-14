layeredimage Rogue_sprite standing:
    # always:
    #     "images/Rogue_standing/Rogue_standing_head_reference.png"

    if RogueX.Clothes["jacket"].string == "green_hoodie":
        "images/Rogue_standing/Rogue_standing_jacket_[RogueX.Clothes[jacket].string]_back.png"

    if RogueX.Clothes["pants"].string == "jeans" and RogueX.Clothes["pants"].state:
        "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_back.png"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_hair_back" pos (0.314, 0.312) zoom 0.58

    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes]_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_body[RogueX.pubes].png"

    if RogueX.Clothes["neck"].string and RogueX.Clothes["gloves"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string]_[RogueX.Clothes[gloves].string].png"
    elif RogueX.Clothes["neck"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string].png"
    elif RogueX.Clothes["gloves"].string:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[gloves].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose].png"

    if RogueX.Clothes["body_piercings"].string:
        "images/Rogue_standing/Rogue_standing_breasts_[RogueX.Clothes[body_piercings].string].png"
    else:
        "images/Rogue_standing/Rogue_standing_breasts.png"

    if not RogueX.Clothes["underwear"].string:
        Null()
    elif RogueX.grool > 1 and RogueX.Clothes["underwear"].string in ["green_panties", "yellowgreen_shorts"]:
        "images/Rogue_standing/Rogue_standing_underwear_[RogueX.Clothes[underwear].string]_grool_[RogueX.Clothes[underwear].state].png"
    else:
        "images/Rogue_standing/Rogue_standing_underwear_[RogueX.Clothes[underwear].string]_[RogueX.Clothes[underwear].state].png"

    if not RogueX.Clothes["hose"].string:
        Null()
    elif RogueX.grool > 1 and RogueX.Clothes["hose"].string == "black_tights":
        "images/Rogue_standing/Rogue_standing_hose_[RogueX.Clothes[hose].string]_grool.png"
    else:
        "images/Rogue_standing/Rogue_standing_hose_[RogueX.Clothes[hose].string].png"

    if RogueX.grool and not RogueX.Outfit.pussy_covered:
        "images/Rogue_standing/Rogue_standing_grool[RogueX.grool].png"

    always:
        "Rogue_grool_animations"

    always:
        "Rogue_spunk_animations"

    if not renpy.showing("Rogue_sprite blowjob"):
        "Rogue_head" pos (0.314, 0.312) zoom 0.58

    if RogueX.Clothes["bra"].string:
        "images/Rogue_standing/Rogue_standing_bra_[RogueX.Clothes[bra].string]_[RogueX.Clothes[bra].state].png"

    if RogueX.Clothes["pants"].string:
        "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_[RogueX.Clothes[pants].state].png"

    if RogueX.Clothes["skirt"].string:
        "images/Rogue_standing/Rogue_standing_skirt_[RogueX.Clothes[skirt].string]_[RogueX.Clothes[skirt].state].png"

    if RogueX.Clothes["top"].string:
        "images/Rogue_standing/Rogue_standing_top[RogueX.arm_pose]_[RogueX.Clothes[top].string]_[RogueX.Clothes[top].state].png"

    if RogueX.Clothes["belt"].string:
        "images/Rogue_standing/Rogue_standing_belt[RogueX.arm_pose]_[RogueX.Clothes[belt].string].png"

    if RogueX.Clothes["jacket"].string:
        "images/Rogue_standing/Rogue_standing_jacket[RogueX.arm_pose]_[RogueX.Clothes[jacket].string]_[RogueX.Clothes[jacket].state].png"

    if RogueX.spunk["breasts"]:
        "images/Rogue_standing/Rogue_standing_spunk_breasts.png"

    if RogueX.spunk["belly"]:
        "images/Rogue_standing/Rogue_standing_spunk_belly.png"

    if RogueX.spunk["hand"] and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_spunk_hand.png"

    if RogueX.wet:
        "images/Rogue_standing/Rogue_standing_water_body[RogueX.arm_pose].png"

    if RogueX.wet == 3:
        "images/Rogue_standing/Rogue_standing_soap_body.png"

    if RogueX.held_item and RogueX.arm_pose == 2:
        "images/Rogue_standing/Rogue_standing_held_item_[RogueX.held_item].png"

    always:
        "Rogue_standing_fondling_animations" zoom 1.04

    anchor (0.5, 0.0) offset (5, 180) zoom 0.48

layeredimage Rogue_hair_back:
    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_hair_wet_hair_back.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string]_back.png"

    anchor (0.5, 0.5)

layeredimage Rogue_head:
    if renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing]_sucking.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"

    if renpy.showing("Rogue_sprite titjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 1:
        "Rogue_blowjob_mouth_animation[RogueX.primary_Action.speed]" pos (0.164, 0.55)
    elif RogueX.mouth == "sucking":
        "images/Rogue_blowjob/Rogue_blowjob_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_mouth_[RogueX.mouth].png"

    if not RogueX.spunk["mouth"]:
        Null()
    elif renpy.showing("Rogue_sprite titjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed == 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    elif renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 1:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_under.png"
    elif RogueX.mouth == "sucking":
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_tongue.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_[RogueX.mouth].png"

    if RogueX.spunk["chin"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_chin.png"

    if RogueX.blushing:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows]_blush.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows].png"

    if RogueX.eyes == "closed":
        "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
    else:
        "Rogue_blinking"

    if RogueX.spunk["mouth"] and renpy.showing("Rogue_sprite blowjob") and RogueX.primary_Action.speed > 2:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_mouth_sucking_over.png"

    if RogueX.spunk["face"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_face.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_hair_wet_hair.png"
    else:
        "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string].png"

    if RogueX.spunk["hair"]:
        "images/Rogue_blowjob/Rogue_blowjob_spunk_hair.png"

    if RogueX.wet:
        "images/Rogue_blowjob/Rogue_blowjob_water_head.png"

    anchor (0.5, 0.5)
