label first_Action_approval(Girl, Action_type):
    if Girl.love >= Girl.devotion + Girl.trust:
        call first_Action_approval_mostly_love_reactions(Girl, Action_type)
    elif Girl.devotion >= Girl.trust:
        call first_Action_approval_mostly_devotion_reactions(Girl, Action_type)
    elif Action_type in cock_Action_types and Girl.addiction >= 50:
        call first_Action_approval_addicted_reactions(Girl, Action_type)
    else:
        call first_Action_approval_reactions(Girl, Action_type)

    return

label first_Action_response(Girl, Action_type):
    if Girl.love >= 50 and "unsatisfied" not in Girl.recent_History.keys():
        call satisfied_lines(Girl, Action_type)
    elif Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy", "finger_pussy", "eat_pussy", "fondle_ass", "finger_ass", "eat_ass", "dildo_pussy", "dildo_ass"] and Girl.devotion <= 50 and Player.desire <= 20:
        call was_that_enough_lines(Girl, Action_type)
    elif Action_type in cock_Action_types and Player.desire <= 20:
        call was_that_enough_lines(Girl, Action_type)

    return

label Action_approved(Girl, Action_type):
    if Girl.permanent_History[Action_type] < 3:
        call before_Action_less_than_three_times_lines(Girl, Action_type)
    else:
        call used_to_Action_lines(Girl, Action_type)

    return

label Action_disapproved(Girl, Action_type):
    if f"no_{Action_type}" in Girl.recent_History.keys():
        call said_no_recently_lines(Girl, Action_type)
    elif f"no_{Action_type}" in Girl.daily_History.keys():
        call said_no_today_lines(Girl, Action_type)
    elif not Girl.permanent_History[Action_type]:
        call Action_not_done_yet_lines(Girl, Action_type)
    else:
        call otherwise_not_interested_lines(Girl, Action_type)

    return

label Action_accepted(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call Action_accepted_enthusiastically_lines(Girl, Action_type)
    else:
        call accepted_without_question_lines(Girl, Action_type)

    call Action_accepted_changes(Girl, Action_type)

    return

label Action_rejected(Girl, Action_type):
    if f"no_{Action_type}" in Girl.daily_History.keys():
        call Action_already_rejected_lines(Girl, Action_type)

        $ Girl.History.update("angry")
    elif Girl.permanent_History[Action_type]:
        call previous_Action_rejected_lines(Girl, Action_type)
    else:
        call otherwise_rejected_reactions(Girl, Action_type)

    $ Girl.History.update(f"no_{Action_type}")

    return

label otherwise_rejected_reactions(Girl, Action_type):
    call otherwise_not_interested_lines(Girl, Action_type)

    $ Girl.History.update(f"no_{Action_type}")

    return

label first_Action_approval_mostly_love_reactions(Girl, Action_type):
    call first_Action_approval_mostly_love_lines(Girl, Action_type)

    return

label first_Action_approval_mostly_devotion_reactions(Girl, Action_type):
    call first_Action_approval_mostly_devotion_lines(Girl, Action_type)

    return

label first_Action_approval_addicted_reactions(Girl, Action_type):
    call first_Action_approval_addicted_lines(Girl, Action_type)

    return

label first_Action_approval_reactions(Girl, Action_type):
    call first_Action_approval_lines(Girl, Action_type)

    return

label recent_Action_reactions(Girl, Action_type):
    call recent_Action_lines(Girl, Action_type)

    return

label daily_Action_reactions(Girl, Action_type):
    call daily_Action_lines(Girl, Action_type)

    return

label first_time_asking_reactions(Girl, Action_type):
    call first_time_asking_lines(Girl, Action_type)

    # if Action_type == "titjob":
    #     if Girl.permanent_History["blowjob"]:
    #         call mouth_not_enough(Girl, Action_type)
    #     elif Girl.permanent_History["handjob"]:
    #         call hand_not_enough(Girl, Action_type)
    # elif Action_type == "blowjob":
    #     if Girl.permanent_History["handjob"]:
    #         call hand_not_enough(Girl, Action_type)

    return
