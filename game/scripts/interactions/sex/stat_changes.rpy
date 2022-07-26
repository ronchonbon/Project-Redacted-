label first_Action_changes(Girl, Action_type):
    if Action_type == "fondle_thighs":
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "trust", 15)
    elif Action_type == "fondle_breasts":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 15)
    elif Action_type == "suck_breasts":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 15)
    elif Action_type == "fondle_pussy":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 15)
    elif Action_type == "finger_pussy":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 25)
    elif Action_type == "eat_pussy":
        call change_Girl_stat(Girl, "love", 35)
        call change_Girl_stat(Girl, "trust", 35)
    elif Action_type == "fondle_ass":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 20)
    elif Action_type == "finger_ass":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 25)
    elif Action_type == "eat_ass":
        call change_Girl_stat(Girl, "love", 35)
        call change_Girl_stat(Girl, "trust", 55)
    elif Action_type == "handjob":
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "trust", 20)
    elif Action_type == "footjob":
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "trust", 20)
    elif Action_type == "titjob":
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "trust", 30)
    elif Action_type == "blowjob":
        call change_Girl_stat(Girl, "love", 5)
        call change_Girl_stat(Girl, "trust", 40)
    elif Action_type == "dildo_pussy":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 45)
    elif Action_type == "dildo_ass":
        call change_Girl_stat(Girl, "love", 10)
        call change_Girl_stat(Girl, "trust", 45)
    elif Action_type == "sex":
        call change_Girl_stat(Girl, "love", 30)
        call change_Girl_stat(Girl, "trust", 60)
    elif Action_type == "anal":
        if not Girl.permanent_History["anal"]:
            call change_Girl_stat(Girl, "love", 10)
            call change_Girl_stat(Girl, "trust", 70)
        elif not Girl.used_to_anal:
            call change_Girl_stat(Girl, "trust", 5)
    elif Action_type == "hotdog":
        call change_Girl_stat(Girl, "love", 20)
        call change_Girl_stat(Girl, "trust", 20)

    return

label auto_approved_changes(Girl, Action_type):
    if Action_type == "fondle_thighs":
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "fondle_breasts":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "suck_breasts":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "fondle_pussy":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "finger_pussy":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "eat_pussy":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "fondle_ass":
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "finger_ass":
        call change_Girl_stat(Girl, "trust", 2)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type == "eat_ass":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type in dildo_Action_types or Action_type in sex_Action_types:
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 1)

    return

label Action_specific_changes(Girl, Action_type):
    if Action_type == "sex":
        call change_Girl_stat(Girl, "trust", 2)
        call change_Girl_stat(Girl, "trust", 1)
    elif Action_type == "anal":
        call change_Girl_stat(Girl, "trust", 3)
        call change_Girl_stat(Girl, "trust", 1)
    elif Action_type == "hotdog":
        call change_Girl_stat(Girl, "trust", 1)
        call change_Girl_stat(Girl, "trust", 1)

    return

label Action_accepted_changes(Girl, Action_type):
    if Action_type in ["fondle_thighs", "fondle_breasts", "suck_breasts", "fondle_pussy"]:
        call change_Girl_stat(Girl, "love", 1)
        call change_Girl_stat(Girl, "trust", 3)
    elif Action_type in ["masturbation", "finger_pussy", "eat_pussy", "finger_ass"]:
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type in ["fondle_ass"]:
        call change_Girl_stat(Girl, "trust", 1)
        call change_Girl_stat(Girl, "desire", 3)
    elif Action_type in ["eat_ass"]:
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type in ["handjob", "footjob", "dildo_pussy", "dildo_ass", "sex", "anal", "hotdog"]:
        call change_Girl_stat(Girl, "trust", 2)
    elif Action_type in ["titjob", "blowjob"]:
        call change_Girl_stat(Girl, "trust", 2)

    return
