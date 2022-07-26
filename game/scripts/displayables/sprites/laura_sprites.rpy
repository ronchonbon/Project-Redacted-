image Laura_sex_body:
    "images/Laura_sex/Laura_sex_body.png"

    anchor (0.5, 0.5)

layeredimage Laura_sex_legs:
    always:
        "images/Laura_sex/Laura_sex_legs.png"

    if Player.primary_Action.type == "anal":
        "Laura_sex_anus_animation[Player.primary_Action.speed]" pos (0.399, 0.747) zoom 0.5
    else:
        "images/Laura_sex/Laura_sex_anus_closed.png" anchor (0.5, 0.5) pos (0.399, 0.747) zoom 0.5

    if Player.primary_Action.type == "sex":
        "Laura_sex_pussy_animation[Player.primary_Action.speed]" pos (0.386, 0.696) zoom 0.5
    else:
        "images/Laura_sex/Laura_sex_pussy_closed.png" anchor (0.5, 0.5) pos (0.386, 0.696) zoom 0.5

    anchor (0.5, 0.5)

image Laura_sex_feet:
    "images/Laura_sex/Laura_sex_feet.png"

    anchor (0.5, 0.5)
