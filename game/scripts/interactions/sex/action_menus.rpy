label enter_main_sex_menu(Girl):
    call girl_sex_menu(Girl)

    return

label girl_sex_menu(Girl):
    $ having_sex = True

    while having_sex:
        if Girl == Rogue:
            $ main_line = "So what would you like to do?"
            $ job_line = f"What did you have in mind, {Girl.player_petname}?"

        menu:
            Girl.voice "[main_line]"
            "Do you want to make out?":
                call start_Action(Girl, "kiss")
            "Could you take care of something for me?":
                menu:
                    Girl.voice "[job_line]"
                    "Could you suck my cock?":
                        call start_Action(Girl, "blowjob")
                    "Maybe something else.":
                        pass
            "Could we maybe. . . ?":
                menu:
                    Girl.voice "[main_line]"
                    "Fuck your pussy.":
                        call start_Action(Girl, "sex")
                    "Fuck your ass.":
                        call start_Action(Girl, "anal")
                    "Maybe something else.":
                        pass
            "I'm done.":
                $ having_sex = False

        if _return == "stop":
            $ having_sex = False

    return

label kiss_menu(Girl):
    while True:
        menu:
            "Keep going. . .":
                return [None, "continue"]
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]

label job_menu(Girl, Action_type):
    while True:
        menu:
            "Keep going. . ." if Girl.primary_Action.speed:
                return [None, "continue"]
            "Lick it. . ." if Action_type == "blowjob" and Girl.primary_Action.speed != 1:
                $ Girl.primary_Action.speed = 1
            "Lick it. . . (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 1:
                pass
            "Just the head. . ." if Action_type == "blowjob" and Girl.primary_Action.speed != 2:
                $ Girl.primary_Action.speed = 2
            "Just the head. . . (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 2:
                pass
            "Suck on it." if Action_type == "blowjob" and Girl.primary_Action.speed != 3:
                $ Girl.primary_Action.speed = 3
            "Suck on it. (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 3:
                pass
            "Take it deeper." if Action_type == "blowjob" and Girl.primary_Action.speed != 4:
                $ Girl.primary_Action.speed = 4
            "Take it deeper. (locked)" if Action_type == "blowjob" and Girl.primary_Action.speed == 4:
                pass
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]

label sex_menu(Girl, Action_type):
    while True:
        menu:
            "Keep going. . ." if Player.primary_Action.speed:
                return [None, "continue"]
            "Keep going. . . (locked)" if not Player.primary_Action.speed:
                pass
            "Start moving? . ." if not Player.primary_Action.speed:
                $ Player.primary_Action.speed = 1
            "Speed up. . ." if 0 < Player.primary_Action.speed < 3:
                $ Player.primary_Action.speed += 1
            "Speed up. . . (locked)" if Player.primary_Action.speed > 2:
                pass
            "Slow down. . ." if Player.primary_Action.speed:
                $ Player.primary_Action.speed -= 1
            "Slow down. . . (locked)" if not Player.primary_Action.speed:
                pass
            "Shift primary action":
                menu:
                    "How about sex?" if Action_type != "sex":
                        return ["sex", "shift"]
                    "Just stick it in her pussy" if Action_type != "sex":
                        return ["sex", "auto"]
                    "How about anal?" if Action_type != "anal":
                        return ["anal", "shift"]
                    "Just stick it in her ass" if Action_type != "anal":
                        return ["anal", "auto"]
                    "Back":
                        pass
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]
