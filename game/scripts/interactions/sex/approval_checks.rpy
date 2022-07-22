init python:

    def Action_approval_checks(Girl, Action_type):
        if Action_type == "kiss":
            approval = approval_check(Girl, threshold = 70)
        elif Action_type == "masturbation":
            approval = approval_check(Girl, threshold = 120)
        elif Action_type == "fondle_thighs":
            approval = approval_check(Girl, threshold = 75)
        elif Action_type == "fondle_breasts":
            approval = approval_check(Girl, threshold = 95)
        elif Action_type == "suck_breasts":
            approval = approval_check(Girl, threshold = 105)
        elif Action_type == "fondle_pussy":
            approval = approval_check(Girl, threshold = 105)
        elif Action_type == "finger_pussy":
            approval = approval_check(Girl, threshold = 110)
        elif Action_type == "eat_pussy":
            approval = approval_check(Girl, threshold = 125)
        elif Action_type == "fondle_ass":
            approval = approval_check(Girl, threshold = 85)
        elif Action_type == "finger_ass":
            approval = approval_check(Girl, threshold = 130)
        elif Action_type == "eat_ass":
            approval = approval_check(Girl, threshold = 155)
        elif Action_type == "handjob":
            approval = approval_check(Girl, threshold = 110)
        elif Action_type == "footjob":
            approval = approval_check(Girl, threshold = 125)
        elif Action_type == "titjob":
            approval = approval_check(Girl, threshold = 120)
        elif Action_type == "blowjob":
            approval = approval_check(Girl, threshold = 130)
        elif Action_type == "dildo_pussy":
            approval = approval_check(Girl, threshold = 125)
        elif Action_type == "dildo_ass":
            approval = approval_check(Girl, threshold = 145)
        elif Action_type == "sex":
            approval = approval_check(Girl, threshold = 140)
        elif Action_type == "anal":
            approval = approval_check(Girl, threshold = 155)
        elif Action_type == "hotdog":
            approval = approval_check(Girl, threshold = 100)

        return approval
