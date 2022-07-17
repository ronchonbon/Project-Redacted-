label start_Action(Girl, Action_type, context = None):
    while True:
        call before_Action(Girl, Action_type, context)

        if _return == "continue":
            call Action_cycle(Girl, Action_type)

            if _return[1] == "switch":
                call after_Action(Girl, Action_type, "switch")
                call stop_all_Actions

                return "switch"
            elif _return[1] == "stop":
                call after_Action(Girl, Action_type, "stop")
                call stop_all_Actions

                return "stop"
            else:
                $ Action_type = _return[0]
                $ context = _return[1]
        elif _return == "stop":
            call stop_all_Actions

            return "stop"

label before_Action(Girl, Action_type, context = None):
    if Action_type in active_Action_types:
        $ Actor = Player

        $ Target = Girl
    elif Action_type in passive_Action_types:
        $ Actor = Girl

        $ Target = Player

    $ Actor.primary_Action = ActionClass(Action_type, Target = Target)

    if Action_type == "blowjob":
        call show_blowjob(Girl)
    elif Action_type == "sex":
        call show_sex(Girl)
    elif Action_type == "anal":
        call show_doggy(Girl)

    return "continue"

label Action_cycle(Girl, Action_type):
    while round > 0:
        $ stack_depth = renpy.call_stack_depth()

        if Action_type == "kiss":
            call kiss_menu(Girl)
        elif Action_type in job_Action_types:
            call job_menu(Girl, Action_type)
        elif Action_type in sex_Action_types:
            call sex_menu(Girl, Action_type)

        if _return[1] == "switch":
            return [None, "switch"]
        elif _return[1] == "stop":
            return [None, "stop"]
        elif _return[1] != "continue":
            $ Action_type = _return[0]
            $ context = _return[1]

            return [Action_type, context]

        $ round -= 1

        if _return[1] == "switch":
            return [None, "switch"]
        elif _return[1] == "stop":
            return [None, "stop"]
        elif _return[1] != "continue":
            $ Action_type = _return[0]
            $ context = _return[1]

            return [Action_type, context]

    return [None, "stop"]

label after_Action(Girl, Action_type, context = None):
    $ Girl.permanent_History[Action_type] += 1

    return
