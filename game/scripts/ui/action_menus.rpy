screen Action_menu():
    style_prefix "choice_menu"

    for G in active_Girls:
        if renpy.showing(f"{G.tag}_sprite"):
            button:
                background None
                anchor (0.5, 0.5) pos (G.sprite_location, 0.6) xysize (250, 900)
                action SetVariable("Player.focused_Girl", G)

    fixed anchor (0.5, 0.0) pos (0.12, 0.35) xysize (int(config.screen_width*0.175), int(config.screen_height*0.45)):
        viewport:
            mousewheel True
            draggable True

            side_yfill True

            has vbox:
                style "menu"

                spacing 2

            showif Player.mouth_Action.type or Player.hand_Action.type or Player.cock_Action.type:
                button:
                    action Function(renpy.call, "continue_Actions", from_current = True)
                    text "Keep going"

            showif not Player.mouth_Action.type and not Player.hand_Action.type and not Player.cock_Action.type:
                button:
                    background "#424242"
                    action None
                    text "Choose an action":
                        color "#6E6E6E"

            showif (Player.mouth_Action.type or Player.hand_Action.type or Player.cock_Action.type) and not Player.focused_Girl.mouth_Action.type:
                button:
                    action Function(renpy.call, "turn_Girl_around", Player.focused_Girl, from_current = True)
                    text "Turn [Player.focused_Girl.name] around"

            showif (not Player.mouth_Action.type and not Player.hand_Action.type and not Player.cock_Action.type) or Player.focused_Girl.mouth_Action.type:
                button:
                    background "#424242"
                    action None
                    text "Turn [Player.focused_Girl.name] around":
                        color "#6E6E6E"

            button:
                action Function(renpy.call, "stop_all_Actions")
                text "Done"

    fixed anchor (0.5, 0.0) pos (0.88, 0.25) xysize (int(config.screen_width*0.175), int(config.screen_height*0.5)):
        viewport:
            mousewheel True
            draggable True

            side_yfill True

            has vbox:
                style "menu"

                spacing 2

            showif Player.mouth_Action.type != "kiss" or Player.focused_Girl not in Player.mouth_Action.Actors:
                button:
                    action Function(renpy.call, "start_Action", Player, Player.focused_Girl, "kiss", from_current = True)
                    text "Kiss"

            showif Player.mouth_Action.type == "kiss" and Player.focused_Girl in Player.mouth_Action.Actors:
                button:
                    action Function(renpy.call, "stop_Actions", Player, "mouth", from_current = True)
                    text f"Stop kissing"

            showif Player.cock_Action.type != "blowjob" or Player.focused_Girl not in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "start_Action", Player.focused_Girl, Player, "blowjob", from_current = True)
                    text "Blowjob"

            showif Player.cock_Action.type == "blowjob" and Player.focused_Girl in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "stop_Actions", Player, "cock", from_current = True)
                    text f"Stop blowjob"

            showif Player.cock_Action.type != "sex" or Player.focused_Girl not in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "start_Action", Player, Player.focused_Girl, "sex", from_current = True)
                    text "Sex"

            showif Player.cock_Action.type == "sex" and Player.focused_Girl in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "stop_Actions", Player, "cock", from_current = True)
                    text f"Stop sex"

            showif Player.cock_Action.type != "anal" or Player.focused_Girl not in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "start_Action", Player, Player.focused_Girl, "anal", from_current = True)
                    text "Anal"

            showif Player.cock_Action.type == "anal" and Player.focused_Girl in Player.cock_Action.Actors:
                button:
                    action Function(renpy.call, "stop_Actions", Player, "cock", from_current = True)
                    text f"Stop anal"

    vbox anchor (0.5, 1.0) pos (0.5, 0.95):
        spacing 2

        if Player.cock_Action.type:
            hbox:
                for speed in range(Player.cock_Action.number_of_speeds):
                    showif Player.cock_Action.type and Player.cock_Action.speed != speed:
                        button:
                            action [SetVariable("Player.cock_Action.speed", speed), Function(renpy.call, "continue_Actions", from_current = True)]
                            text f"Speed {speed}"

                    showif not Player.cock_Action.type or Player.cock_Action.speed == speed:
                        button:
                            background "#424242"
                            action None
                            text f"Speed {speed}":
                                color "#6E6E6E"
