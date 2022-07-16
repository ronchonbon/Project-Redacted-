image black_screen:
    Solid("#000000")

    on show:
        alpha 0.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image rolling_steam_midground:
    "images/backgrounds/steam2.png"

    subpixel True
    xpos -1920
    block:
        linear 45.0 xpos 1920
        xpos -1920
        repeat

image rolling_steam_cover:
    "images/backgrounds/steam1.png"

    subpixel True
    xpos 1920
    block:
        linear 30.0 xpos -1920
        xpos 1920
        repeat

layeredimage background:
    always:
        "images/backgrounds/sky_[current_time].png"

    if Player.location in ["bg_campus", "bg_pool"]:
        "images/backgrounds/[Player.location]_[current_time].png"
    else:
        "images/backgrounds/[Player.location].png"

layeredimage midground:
    if Player.location == "bg_shower":
        "rolling_steam_midground"

layeredimage foreground:
    always:
        Null()

layeredimage cover:
    if Player.location == "bg_shower":
        "rolling_steam_cover" alpha 0.8
