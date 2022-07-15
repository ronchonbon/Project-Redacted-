# layeredimage Rogue_sprite standing:
#     if RogueX.Clothes["jacket"].string == "green_hoodie":
#         "images/Rogue_standing/Rogue_standing_jacket_[RogueX.Clothes[jacket].string]_back.png"
#
#     if RogueX.Clothes["pants"].string == "jeans" and RogueX.Clothes["pants"].state:
#         "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_back.png"
#
#     always:
#         "Rogue_hair_back" pos (0.314, 0.312) zoom 0.58
#
#     if RogueX.Clothes["body_piercings"].string:
#         "images/Rogue_standing/Rogue_standing_body[RogueX.pubes]_[RogueX.Clothes[body_piercings].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_body[RogueX.pubes].png"
#
#     if RogueX.Clothes["neck"].string and RogueX.Clothes["gloves"].string:
#         "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string]_[RogueX.Clothes[gloves].string].png"
#     elif RogueX.Clothes["neck"].string:
#         "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[neck].string].png"
#     elif RogueX.Clothes["gloves"].string:
#         "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose]_[RogueX.Clothes[gloves].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_arms[RogueX.arm_pose].png"
#
#     if RogueX.Clothes["body_piercings"].string:
#         "images/Rogue_standing/Rogue_standing_breasts_[RogueX.Clothes[body_piercings].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_breasts.png"
#
#     if RogueX.Clothes["underwear"].string:
#         "images/Rogue_standing/Rogue_standing_underwear_[RogueX.Clothes[underwear].string]_[RogueX.Clothes[underwear].state].png"
#
#     if RogueX.Clothes["hose"].string:
#         "images/Rogue_standing/Rogue_standing_hose_[RogueX.Clothes[hose].string].png"
#
#     always:
#         "Rogue_head" pos (0.314, 0.312) zoom 0.58
#
#     if RogueX.Clothes["bra"].string:
#         "images/Rogue_standing/Rogue_standing_bra_[RogueX.Clothes[bra].string]_[RogueX.Clothes[bra].state].png"
#
#     if RogueX.Clothes["pants"].string:
#         "images/Rogue_standing/Rogue_standing_pants_[RogueX.Clothes[pants].string]_[RogueX.Clothes[pants].state].png"
#
#     if RogueX.Clothes["skirt"].string:
#         "images/Rogue_standing/Rogue_standing_skirt_[RogueX.Clothes[skirt].string]_[RogueX.Clothes[skirt].state].png"
#
#     if RogueX.Clothes["top"].string:
#         "images/Rogue_standing/Rogue_standing_top[RogueX.arm_pose]_[RogueX.Clothes[top].string]_[RogueX.Clothes[top].state].png"
#
#     if RogueX.Clothes["belt"].string:
#         "images/Rogue_standing/Rogue_standing_belt[RogueX.arm_pose]_[RogueX.Clothes[belt].string].png"
#
#     if RogueX.Clothes["jacket"].string:
#         "images/Rogue_standing/Rogue_standing_jacket[RogueX.arm_pose]_[RogueX.Clothes[jacket].string]_[RogueX.Clothes[jacket].state].png"
#
#     if RogueX.held_item and RogueX.arm_pose == 2:
#         "images/Rogue_standing/Rogue_standing_held_item_[RogueX.held_item].png"
#
#     anchor (0.5, 0.0) offset (5, 180) zoom 0.48
#
# layeredimage Rogue_hair_back:
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string]_back.png"
#
#     anchor (0.5, 0.5)
#
# layeredimage Rogue_head:
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_face[RogueX.blushing].png"
#
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_mouth_[RogueX.mouth].png"
#
#     if RogueX.blushing:
#         "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows]_blush.png"
#     else:
#         "images/Rogue_blowjob/Rogue_blowjob_brows_[RogueX.brows].png"
#
#     if RogueX.eyes == "closed":
#         "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
#     else:
#         "Rogue_blinking"
#
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_hair_[RogueX.Clothes[hair].string].png"
#
#     anchor (0.5, 0.5)
