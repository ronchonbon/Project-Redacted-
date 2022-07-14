image Rogue_blinking:
    "images/Rogue_blowjob/Rogue_blowjob_eyes_[RogueX.eyes].png"
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

layeredimage Rogue_grool_dripping_animation:
    always:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

    if RogueX.grool > 1 and not RogueX.Outfit.pussy_covered:
        "grool_dripping_animation" pos (0.26, 1.2)

layeredimage Rogue_grool_animations:
    if not RogueX.grool:
        Null()
    elif RogueX.Clothes["pants"].state:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.Clothes["underwear"].state:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif not RogueX.Outfit.pussy_covered:
        AlphaMask("Rogue_grool_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_spunk_dripping_animation:
    always:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

    if not RogueX.Outfit.pussy_covered:
        "spunk_dripping_animation" pos (0.26, 1.2)

layeredimage Rogue_spunk_animations:
    if not RogueX.spunk["pussy"] and not RogueX.spunk["anus"]:
        Null()
    elif RogueX.Clothes["pants"].state:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_pants.png")
    elif RogueX.Clothes["underwear"].state:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask_underwear.png")
    elif not RogueX.Outfit.pussy_covered:
        AlphaMask("Rogue_spunk_dripping_animation", "images/Rogue_standing/Rogue_standing_grool_mask.png")

layeredimage Rogue_standing_fondling_animations:
    if RogueX.primary_Action.Target != RogueX:
        Null()
    elif RogueX.primary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_right_animation" pos (0.17, 0.72)
    elif RogueX.primary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.235, 1.07)
    elif RogueX.primary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.242, 1.135)

    if RogueX.secondary_Action.Target != RogueX:
        Null()
    elif RogueX.secondary_Action.type == "fondle_breasts":
        "Girl_fondle_breast_left_animation" pos (0.313, 0.725)
    elif RogueX.secondary_Action.type == "fondle_pussy":
        "Girl_fondle_pussy_animation" pos (0.235, 1.07)
    elif RogueX.secondary_Action.type in "finger_pussy":
        "Girl_finger_pussy_animation" pos (0.242, 1.135)

    if Player.primary_Action.Target != RogueX:
        Null()
    elif Player.primary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.185, 1.3)
    elif Player.primary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_left_animation" pos (0.277, 0.715)
    elif Player.primary_Action.type == "suck_breasts":
        "Zero_suck_breasts_left_animation" pos (0.305, 0.685)
    elif Player.primary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.245, 1.05)
    elif Player.primary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.215, 1.25)
    elif Player.primary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.25, 1.17)

    if Player.secondary_Action.Target != RogueX:
        Null()
    elif Player.secondary_Action.type == "fondle_thighs":
        "Zero_fondle_thigh_animation" pos (0.185, 1.3)
    elif Player.secondary_Action.type == "fondle_breasts":
        "Zero_fondle_breasts_right_animation" pos (0.212, 0.725)
    elif Player.secondary_Action.type == "suck_breasts":
        "Zero_suck_breasts_right_animation" pos (0.15, 0.66)
    elif Player.secondary_Action.type == "fondle_pussy":
        "Zero_fondle_pussy_animation" pos (0.245, 1.05)
    elif Player.secondary_Action.type == "finger_pussy":
        "Zero_finger_pussy_animation" pos (0.215, 1.25)
    elif Player.secondary_Action.type == "eat_pussy":
        "Zero_eat_pussy_animation" pos (0.25, 1.17)
