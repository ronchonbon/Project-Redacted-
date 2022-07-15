# layeredimage Rogue_sprite standing:
#     if Rogue.Clothes["jacket"].string == "green_hoodie":
#         "images/Rogue_standing/Rogue_standing_jacket_[Rogue.Clothes[jacket].string]_back.png"
#
#     if Rogue.Clothes["pants"].string == "jeans" and Rogue.Clothes["pants"].state:
#         "images/Rogue_standing/Rogue_standing_pants_[Rogue.Clothes[pants].string]_back.png"
#
#     always:
#         "Rogue_hair_back" pos (0.314, 0.312) zoom 0.58
#
#     if Rogue.Clothes["body_piercings"].string:
#         "images/Rogue_standing/Rogue_standing_body[Rogue.pubes]_[Rogue.Clothes[body_piercings].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_body[Rogue.pubes].png"
#
#     if Rogue.Clothes["neck"].string and Rogue.Clothes["gloves"].string:
#         "images/Rogue_standing/Rogue_standing_arms[Rogue.arm_pose]_[Rogue.Clothes[neck].string]_[Rogue.Clothes[gloves].string].png"
#     elif Rogue.Clothes["neck"].string:
#         "images/Rogue_standing/Rogue_standing_arms[Rogue.arm_pose]_[Rogue.Clothes[neck].string].png"
#     elif Rogue.Clothes["gloves"].string:
#         "images/Rogue_standing/Rogue_standing_arms[Rogue.arm_pose]_[Rogue.Clothes[gloves].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_arms[Rogue.arm_pose].png"
#
#     if Rogue.Clothes["body_piercings"].string:
#         "images/Rogue_standing/Rogue_standing_breasts_[Rogue.Clothes[body_piercings].string].png"
#     else:
#         "images/Rogue_standing/Rogue_standing_breasts.png"
#
#     if Rogue.Clothes["underwear"].string:
#         "images/Rogue_standing/Rogue_standing_underwear_[Rogue.Clothes[underwear].string]_[Rogue.Clothes[underwear].state].png"
#
#     if Rogue.Clothes["hose"].string:
#         "images/Rogue_standing/Rogue_standing_hose_[Rogue.Clothes[hose].string].png"
#
#     always:
#         "Rogue_head" pos (0.314, 0.312) zoom 0.58
#
#     if Rogue.Clothes["bra"].string:
#         "images/Rogue_standing/Rogue_standing_bra_[Rogue.Clothes[bra].string]_[Rogue.Clothes[bra].state].png"
#
#     if Rogue.Clothes["pants"].string:
#         "images/Rogue_standing/Rogue_standing_pants_[Rogue.Clothes[pants].string]_[Rogue.Clothes[pants].state].png"
#
#     if Rogue.Clothes["skirt"].string:
#         "images/Rogue_standing/Rogue_standing_skirt_[Rogue.Clothes[skirt].string]_[Rogue.Clothes[skirt].state].png"
#
#     if Rogue.Clothes["top"].string:
#         "images/Rogue_standing/Rogue_standing_top[Rogue.arm_pose]_[Rogue.Clothes[top].string]_[Rogue.Clothes[top].state].png"
#
#     if Rogue.Clothes["belt"].string:
#         "images/Rogue_standing/Rogue_standing_belt[Rogue.arm_pose]_[Rogue.Clothes[belt].string].png"
#
#     if Rogue.Clothes["jacket"].string:
#         "images/Rogue_standing/Rogue_standing_jacket[Rogue.arm_pose]_[Rogue.Clothes[jacket].string]_[Rogue.Clothes[jacket].state].png"
#
#     if Rogue.held_item and Rogue.arm_pose == 2:
#         "images/Rogue_standing/Rogue_standing_held_item_[Rogue.held_item].png"
#
#     anchor (0.5, 0.0) offset (5, 180) zoom 0.48
#
# layeredimage Rogue_hair_back:
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_hair_[Rogue.Clothes[hair].string]_back.png"
#
#     anchor (0.5, 0.5)
#
# layeredimage Rogue_head:
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_face[Rogue.blushing].png"
#
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_mouth_[Rogue.mouth].png"
#
#     if Rogue.blushing:
#         "images/Rogue_blowjob/Rogue_blowjob_brows_[Rogue.brows]_blush.png"
#     else:
#         "images/Rogue_blowjob/Rogue_blowjob_brows_[Rogue.brows].png"
#
#     if Rogue.eyes == "closed":
#         "images/Rogue_blowjob/Rogue_blowjob_eyes_closed.png"
#     else:
#         "Rogue_blinking"
#
#     always:
#         "images/Rogue_blowjob/Rogue_blowjob_hair_[Rogue.Clothes[hair].string].png"
#
#     anchor (0.5, 0.5)
