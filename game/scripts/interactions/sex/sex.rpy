label start_Action(Character, Target, Action_type, context = None):
    hide screen Action_menu

    if context != "auto":
        if Character in all_Girls:
            call request_Action(Character, Action_type)
        elif Target in all_Girls:
            call request_Action(Target, Action_type)

        if _return == "rejected":
            return

    call stop_conflicting_Actions(Character, Target, Action_type)

    $ Action = ActionClass([Character, Target], Action_type)

    if Action_type == "kiss":
        $ Character.mouth_Action = Action
        $ Target.mouth_Action = Action
    elif Action_type == "blowjob":
        $ Character.mouth_Action = Action
        $ Target.cock_Action = Action

        call show_blowjob(Character)
    elif Action_type == "sex":
        $ Character.cock_Action = Action
        $ Target.pussy_Action = Action

        call show_sex(Target)
    elif Action_type == "anal":
        $ Character.cock_Action = Action
        $ Target.ass_Action = Action

        call show_doggy(Target)

    show screen Action_menu()

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
    hide screen Action_menu

    python:
        unique_Actions = []

        for organ in Player.all_Organs:
            Action = getattr(Player, f"{organ}_Action")

            if Action.type and Action not in unique_Actions:
                unique_Actions.append(Action)

        for G in active_Girls:
            for organ in G.all_Organs:
                Action = getattr(G, f"{organ}_Action")

                if Action.type and Action not in unique_Actions:
                    unique_Actions.append(Action)

        renpy.random.shuffle(unique_Actions)

    while unique_Actions:
        call expression f"{unique_Actions[0].type}_narrations" pass (unique_Actions[0])

        $ unique_Actions.remove(unique_Actions[0])

    show screen Action_menu()

    return

label stop_Actions(Character, organ = None):
    python:
        if not organ:
            for organ_A in Character.all_Organs:
                Action_A = getattr(Character, f"{organ_A}_Action")

                if Action_A.type:
                    for Actor_B in Action_A.Actors:
                        for organ_B in Actor_B.all_Organs:
                            Action_B = getattr(Actor_B, f"{organ_B}_Action")

                            if Action_B == Action_A:
                                setattr(Actor_B, f"{organ_B}_Action", ActionClass([], None))

                    setattr(Character, f"{organ_A}_Action", ActionClass([], None))
        else:
            Action_A = getattr(Character, f"{organ}_Action")

            if Action_A.type:
                for Actor_B in Action_A.Actors:
                    for organ_B in Actor_B.all_Organs:
                        Action_B = getattr(Actor_B, f"{organ_B}_Action")

                        if Action_B == Action_A:
                            setattr(Actor_B, f"{organ_B}_Action", ActionClass([], None))

                setattr(Character, f"{organ}_Action", ActionClass([], None))

    return

label stop_conflicting_Actions(Character, Target, Action_type):
    $ Actors = [Character, Target]

    while Actors:
        if Action_type == "kiss":
            call stop_Actions(Actors[0], organ = "mouth")
        elif Action_type == "blowjob":
            if Actors[0] == Player:
                call stop_Actions(Actors[0], organ = "cock")
            else:
                call stop_Actions(Actors[0], organ = "mouth")
        elif Action_type == "sex":
            if Actors[0] == Player:
                call stop_Actions(Actors[0], organ = "cock")
            else:
                call stop_Actions(Actors[0], organ = "pussy")
        elif Action_type == "anal":
            if Actors[0] == Player:
                call stop_Actions(Actors[0], organ = "cock")
            else:
                call stop_Actions(Actors[0], organ = "ass")

        $ Actors.remove(Actors[0])

    return

label stop_all_Actions:
    $ temp_Girls = active_Girls[:]

    while temp_Girls:
        call stop_Actions(temp_Girls[0])

        if renpy.showing(f"{temp_Girls[0].tag}_sprite"):
            call show_Girl(temp_Girls[0])

        $ temp_Girls.remove(temp_Girls[0])

    call stop_Actions(Player)

    return

label turn_Girl_around(Girl):
    if renpy.showing(f"{Girl.tag}_sprite sex"):
        call show_doggy(Girl)
    elif renpy.showing(f"{Girl.tag}_sprite doggy"):
        call show_sex(Girl)

    return
