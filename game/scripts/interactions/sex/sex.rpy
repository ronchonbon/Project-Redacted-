label sex:
    show screen primary_Action_menu()
    show screen secondary_Action_menu()
    show screen Action_speed_menu()

    while True:
        menu:
            extend ""
            "Keep going" if Player.primary_Action.type or Player.focused_Girl.primary_Action.type:
                call continue_Actions
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

label start_Action(Character, Target, Action_type, secondary = False, context = None):
    hide screen primary_Action_menu
    hide screen secondary_Action_menu
    hide screen Action_speed_menu

    if context != "auto":
        if Character in all_Girls:
            call request_Action(Character, Action_type)
        elif Target in all_Girls:
            call request_Action(Target, Action_type)

        if _return == "rejected":
            return

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

        if Action_type == "kiss":
            $ Target.primary_Action = ActionClass(Action_type, Target = Character)
    else:
        $ Character.secondary_Action = ActionClass(Action_type, Target = Target)

    if Action_type == "blowjob":
        call show_blowjob(Character)
    elif Action_type == "sex":
        call show_sex(Target)
    elif Action_type == "anal":
        call show_doggy(Target)

    show screen primary_Action_menu()
    show screen secondary_Action_menu()
    show screen Action_speed_menu()

    return

label request_Action(Girl, Action_type):
    $ approval = Action_approval_checks(Girl, Action_type)

    $ accepted = False

    if Action_type in Girl.recent_History.keys():
        call recent_Action_reactions(Girl, Action_type)

        $ accepted = True
    elif Action_type in Girl.daily_History.keys():
        call daily_Action_reactions(Girl, Action_type)

        $ accepted = True

    if not accepted:
        if not Girl.permanent_History[Action_type] and f"no_{Action_type}" not in Girl.recent_History.keys():
            call first_time_asking_reactions(Girl, Action_type)

        if not Girl.permanent_History[Action_type] and approval:
            call first_Action_approval(Girl, Action_type)
        elif approval:
            call Action_approved(Girl, Action_type)

        if approval >= 2:
            call Action_accepted(Girl, Action_type)

            $ accepted = True
        else:
            call Action_disapproved(Girl, Action_type)

    if not accepted:
        call Action_rejected(Girl, Action_type)

        return "rejected"
    else:
        if not Girl.permanent_History[Action_type]:
            call first_Action_changes(Girl, Action_type)

        $ Girl.History.remove(f"no{Action_type}")
        $ Girl.History.update(Action_type)

        return "accepted"

label continue_Actions:
    hide screen primary_Action_menu
    hide screen secondary_Action_menu
    hide screen Action_speed_menu

    if Player.primary_Action.type:
        call expression f"{Player.primary_Action.type}_narrations" pass (Player.primary_Action.Target, Player.primary_Action.speed)
    elif Player.focused_Girl.primary_Action.type:
        call expression f"{Player.focused_Girl.primary_Action.type}_narrations" pass (Player.focused_Girl, Player.focused_Girl.primary_Action.speed)

    show screen primary_Action_menu()
    show screen secondary_Action_menu()
    show screen Action_speed_menu()

    return

label stop_Action(Character, secondary = False):
    if not secondary:
        $ temp_Action_type = Character.primary_Action.type
    else:
        $ temp_Action_type = Character.secondary_Action.type

    if Character in active_Girls:
        $ Girl = Character
    elif Character == Player:
        if not secondary:
            $ Girl = Character.primary_Action.Target
        else:
            $ Girl = Character.secondary_Action.Target

    # if Girl.permanent_History[temp_Action_type] == 1:
    #     call first_Action_response(Girl, temp_Action_type)
    # elif (temp_Action_type in cock_Action_types or temp_Action_type == "kiss") and Girl.permanent_History[temp_Action_type] == 5:
    #     call Action_done_five_times_lines(Girl, temp_Action_type)

    if Character in active_Girls:
        call show_Girl(Character)

    if not secondary:
        if Character.primary_Action.Target in active_Girls:
            call show_Girl(Character.primary_Action.Target)

            $ Character.primary_Action.Target.History.update(temp_Action_type)
    else:
        if Character.secondary_Action.Target in active_Girls:
            call show_Girl(Character.secondary_Action.Target)

            $ Character.secondary_Action.Target.History.update(temp_Action_type)

    if not secondary:
        $ Character.primary_Action = ActionClass(None, None)
    else:
        $ Character.secondary_Action = ActionClass(None, None)

    return

label stop_all_Actions:
    $ temp_Girls = active_Girls[:]

    while temp_Girls:
        if temp_Girls[0].primary_Action.type:
            call stop_Action(temp_Girls[0])

        if temp_Girls[0].secondary_Action.type:
            call stop_Action(temp_Girls[0], secondary = True)

        $ temp_Girls.remove(temp_Girls[0])

    if Player.primary_Action.type:
        call stop_Action(Player)

    if Player.secondary_Action.type:
        call stop_Action(Player, secondary = True)

    return
