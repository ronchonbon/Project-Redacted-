screen primary_Action_menu():
    style_prefix "choice_menu"

    fixed anchor (0.5, 0.0) pos (0.85, 0.25) xysize (int(config.screen_width*0.175), int(config.screen_height*0.45)):
        viewport:
            mousewheel True
            draggable True

            side_yfill True

            has vbox:
                style "menu"

                spacing 2

            text "Primary action"

            for Action_type in primary_Action_types:
                if Action_type in passive_Action_types:
                    showif Player.focused_Girl.primary_Action.type != Action_type:
                        button:
                            action Function(renpy.call, "start_Action", Player.focused_Girl, Player, Action_type, from_current = True)
                            text f"{Action_type.capitalize()}"

                    showif Player.focused_Girl.primary_Action.type == Action_type:
                        button:
                            background "#424242"
                            action None
                            text f"{Action_type.capitalize()}":
                                color "#6E6E6E"
                elif Action_type in active_Action_types:
                    showif Player.primary_Action.type != Action_type or Player.primary_Action.Target != Player.focused_Girl:
                        button:
                            action Function(renpy.call, "start_Action", Player, Player.focused_Girl, Action_type, from_current = True)
                            text f"{Action_type.capitalize()}"

                    showif Player.primary_Action.type == Action_type and Player.primary_Action.Target == Player.focused_Girl:
                        button:
                            background "#424242"
                            action None
                            text f"{Action_type.capitalize()}":
                                color "#6E6E6E"

            showif Player.primary_Action.type:
                button:
                    action Function(renpy.call, "stop_Action", Player, from_current = True)
                    text "Stop"

            showif Player.focused_Girl.primary_Action.type:
                button:
                    action Function(renpy.call, "stop_Action", Player.focused_Girl, from_current = True)
                    text "Stop"

            showif not Player.primary_Action.type and not Player.focused_Girl.primary_Action.type:
                button:
                    background "#424242"
                    action None
                    text "Stop":
                        color "#6E6E6E"

screen secondary_Action_menu():
    style_prefix "choice_menu"

    fixed anchor (0.5, 0.0) pos (0.85, 0.5) xysize (int(config.screen_width*0.175), int(config.screen_height*0.45)):
        viewport:
            mousewheel True
            draggable True

            side_yfill True

            has vbox:
                style "menu"

                spacing 2

            text "Secondary action"

            for Action_type in secondary_Action_types:
                if Action_type in passive_Action_types:
                    showif Player.focused_Girl.secondary_Action.type != Action_type:
                        button:
                            action Function(renpy.call, "start_Action", Player.focused_Girl, Player, Action_type, secondary = True, from_current = True)
                            text f"{Action_type.capitalize()}"

                    showif Player.focused_Girl.secondary_Action.type == Action_type:
                        button:
                            background "#424242"
                            action None
                            text f"{Action_type.capitalize()}":
                                color "#6E6E6E"
                elif Action_type in active_Action_types:
                    showif Player.secondary_Action.type != Action_type or Player.secondary_Action.Target != Player.focused_Girl:
                        button:
                            action Function(renpy.call, "start_Action", Player, Player.focused_Girl, Action_type, secondary = True, from_current = True)
                            text f"{Action_type.capitalize()}"

                    showif Player.secondary_Action.type == Action_type and Player.secondary_Action.Target == Player.focused_Girl:
                        button:
                            background "#424242"
                            action None
                            text f"{Action_type.capitalize()}":
                                color "#6E6E6E"

            showif Player.secondary_Action.type:
                button:
                    action Function(renpy.call, "stop_Action", Player, secondary = True, from_current = True)
                    text "Stop"

            showif Player.focused_Girl.secondary_Action.type:
                button:
                    action Function(renpy.call, "stop_Action", Player.focused_Girl, secondary = True, from_current = True)
                    text "Stop"

            showif not Player.secondary_Action.type and not Player.focused_Girl.secondary_Action.type:
                button:
                    background "#424242"
                    action None
                    text "Stop":
                        color "#6E6E6E"

screen Action_speed_menu():
    style_prefix "choice_menu"

    vbox anchor (0.5, 1.0) pos (0.5, 0.95):
        spacing 2

        hbox:
            for speed in range(4):
                showif Player.primary_Action.type and Player.primary_Action.speed != speed:
                    button:
                        action SetVariable("Player.primary_Action.speed", speed)
                        text f"Speed {speed}"

                showif not Player.primary_Action.type or Player.primary_Action.speed == speed:
                    button:
                        background "#424242"
                        action None
                        text f"Speed {speed}":
                            color "#6E6E6E"

        hbox:
            for speed in range(4):
                showif Player.focused_Girl.primary_Action.type and Player.focused_Girl.primary_Action.speed != speed:
                    button:
                        action SetVariable("Player.focused_Girl.primary_Action.speed", speed)
                        text f"Speed {speed}"

                showif not Player.focused_Girl.primary_Action.type or Player.focused_Girl.primary_Action.speed == speed:
                    button:
                        background "#424242"
                        action None
                        text f"Speed {speed}":
                            color "#6E6E6E"
