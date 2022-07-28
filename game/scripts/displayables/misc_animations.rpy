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
