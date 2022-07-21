label sex:
    show screen primary_Action_menu()
    show screen secondary_Action_menu()
    show screen Action_speed_menu()

    while True:
        menu:
            extend ""
            "Keep going" if Player.primary_Action.type or Player.focused_Girl.primary_Action.type:
                if Player.primary_Action.type:
                    call expression f"{Player.primary_Action.type}_narrations" pass (Player.primary_Action.Target, Player.primary_Action.speed)
                elif Player.focused_Girl.primary_Action.type:
                    call expression f"{Player.focused_Girl.primary_Action.type}_narrations" pass (Player.focused_Girl, Player.focused_Girl.primary_Action.speed)
            "Choose an action (locked)" if not Player.primary_Action.type and not Player.focused_Girl.primary_Action.type:
                pass
            "Turn [Player.focused_Girl.name] around" if Player.primary_Action.type in ["sex", "anal"]:
                if renpy.showing(f"{Player.focused_Girl.tag}_sprite sex"):
                    call show_doggy(Player.focused_Girl)
                elif renpy.showing(f"{Player.focused_Girl.tag}_sprite doggy"):
                    call show_sex(Player.focused_Girl)
            "Turn [Player.focused_Girl.name] around (locked)" if Player.primary_Action.type not in ["sex", "anal"]:
                pass
            "Done":
                hide screen primary_Action_menu
                hide screen secondary_Action_menu
                hide screen Action_speed_menu

                call stop_all_Actions

                return

label start_Action(Character, Target, Action_type, secondary = False):
    if Action_type in cock_Action_types:
        if Character.primary_Action.type in cock_Action_types:
            call stop_Action(Character)
        elif Character.secondary_Action.type in cock_Action_types:
            call stop_Action(Character, secondary = True)
        elif Target.primary_Action.type in cock_Action_types:
            call stop_Action(Target)
        elif Target.secondary_Action.type in cock_Action_types:
            call stop_Action(Target, secondary = True)

    if not secondary:
        $ Character.primary_Action = ActionClass(Action_type, Target = Target)
    else:
        $ Character.secondary_Action = ActionClass(Action_type, Target = Target)

    if Action_type == "blowjob":
        call show_blowjob(Character)
    elif Action_type == "sex":
        call show_sex(Target)
    elif Action_type == "anal":
        call show_doggy(Target)

    return

label stop_Action(Character, secondary = False):
    if Character in active_Girls:
        if renpy.showing(f"{Character.name}_sprite"):
            call show_Girl(Character)

        if not secondary:
            if Character.primary_Action.Target in active_Girls:
                call show_Girl(Character.primary_Action.Target)
        else:
            if Character.secondary_Action.Target in active_Girls:
                call show_Girl(Character.secondary_Action.Target)
    elif Character == Player:
        if not secondary:
            if Character.primary_Action.Target in active_Girls:
                call show_Girl(Character.primary_Action.Target)
        else:
            if Character.secondary_Action.Target in active_Girls:
                call show_Girl(Character.secondary_Action.Target)

    if not secondary:
        $ Character.primary_Action = ActionClass(None, None)
    else:
        $ Character.secondary_Action = ActionClass(None, None)

    return

label stop_all_Actions:
    $ temp_Girls = active_Girls[:]

    while temp_Girls:
        call stop_Action(temp_Girls[0])
        call stop_Action(temp_Girls[0], secondary = True)

        $ temp_Girls.remove(temp_Girls[0])

    call stop_Action(Player)
    call stop_Action(Player, secondary = True)

    return
