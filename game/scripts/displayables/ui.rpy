transform love_color:
    matrixcolor TintMatrix("#C11B17")

transform devotion_color:
    matrixcolor TintMatrix("#2554C7")

transform trust_color:
    matrixcolor TintMatrix("#FFF380")

transform desire_color:
    matrixcolor TintMatrix("#FAAFBE")

transform Rogue_color:
    matrixcolor TintMatrix("#6EDF31")

transform tiny_button:
    zoom 0.5

image full_action_bar:
    "images/UI/bars/full_action_bar.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.4

image empty_action_bar:
    "images/UI/bars/empty_action_bar.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.4

image map_hover:
    "images/UI/icons/map_hover.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5

image map_idle:
    "images/UI/icons/map_idle.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.5

layeredimage phone_hover:
    always:
        "images/UI/phone/phone_background.png" anchor (0.5, 0.5) pos (0.5, 0.2)

    always:
        "images/UI/phone/phone_foreground.png" anchor (0.5, 0.5) pos (0.5, 0.5)

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.025

layeredimage phone_idle:
    always:
        "images/UI/phone/phone_background.png" anchor (0.5, 0.5) pos (0.5, 0.2)

    always:
        "images/UI/phone/phone_foreground.png" anchor (0.5, 0.5) pos (0.5, 0.5)

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.025

image exit_hover:
    "images/UI/icons/exit_hover.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0

image exit_idle:
    "images/UI/icons/exit_idle.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0

image inventory_hover:
    "images/UI/icons/inventory_hover.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0

image inventory_idle:
    "images/UI/icons/inventory_idle.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 1.0

image phone_background:
    "images/UI/phone/phone_background.png"

    anchor (0.5, 0.5) pos (0.5, 0.375) zoom 0.28

image phone_foreground:
    "images/UI/phone/phone_foreground.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.28

image Rogue_hover:
    "images/UI/miniheads/Rogue_hover.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.3125

image Rogue_idle:
    "images/UI/miniheads/Rogue_idle.png"

    anchor (0.5, 0.5) pos (0.5, 0.5) zoom 0.3125

init python:

    def Girl_color(d):
        if Player.focused_Girl == Rogue:
            return Rogue_color(d)
