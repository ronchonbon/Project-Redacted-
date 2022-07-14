transform stat_rising(x_position):
    ypos 0.25 alpha 0.0
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.1
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.2
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.3
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.4
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.5
        xpos x_position alpha 1.0
    choice:
        pause 0.6
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.7
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.8
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.9
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 1.0 ypos 0.0
    parallel:
        linear 1.0 alpha 0.0

transform stat_falling(x_position):
    ypos 0.0 alpha 0.05
    choice:
        xpos x_position alpha 1.0
    choice:
        pause 0.1
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.2
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.3
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.4
        xpos x_position + 0.03 alpha 1.0
    choice:
        pause 0.5
        xpos x_position alpha 1.0
    choice:
        pause 0.6
        xpos x_position - 0.015 alpha 1.0
    choice:
        pause 0.7
        xpos x_position + 0.015 alpha 1.0
    choice:
        pause 0.8
        xpos x_position - 0.03 alpha 1.0
    choice:
        pause 0.9
        xpos x_position + 0.03 alpha 1.0
    parallel:
        linear 1.0 ypos 0.25
    parallel:
        linear 1.0 alpha 0.0

transform dripping(x_offset = 0, start = 0, transparency = 1.0):
    offset (x_offset, start) alpha transparency
    easeout 0.9 yoffset 350 alpha 0.0

image grool_dripping_animation:
    animation
    "images/misc/grool.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0 zoom 0.2
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10, 0.8)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15, 0.8)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5, 0.8)
        choice:
            pause 0.8
            dripping(6, 0, 0.8)
        repeat

image spunk_dripping_animation:
    animation
    "images/misc/sperm.png"

    subpixel True
    anchor (0.5, 0.5) alpha 0.0 zoom 0.3
    block:
        choice:
            pause 1
        choice:
            pause 0.5
        choice:
            dripping(8, 10)
            pause 1
        choice:
            pause 0.2
            dripping(3, 15)
            pause 0.4
        choice:
            pause 0.4
            dripping(0, 5)
        choice:
            pause 0.8
            dripping(6, 0)
        repeat
