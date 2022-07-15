label enter_main_sex_menu(Girl):
    call girl_sex_menu(Girl)

    return

label girl_sex_menu(Girl):
    $ having_sex = True

    while having_sex:
        if Girl == Rogue:
            $ main_line = "So what would you like to do?"
            $ fondle_line = f"Well where exactly were you interested in touching, {Girl.player_petname}?"
            $ handjob_line = f"What did you have in mind, {Girl.player_petname}?"
            $ show_line = "What sort of show were you expecting?"

        menu:
            Girl.voice "[main_line]"
            "Do you want to make out?":
                call start_Action(Girl, "kiss")
            "Could I touch you?":
                menu:
                    Girl.voice "[fondle_line]"
                    "Your thighs?":
                        call start_Action(Girl, "fondle_thighs")
                    "Your breasts?":
                        call start_Action(Girl, "fondle_breasts")
                    "Suck your nipples?":
                        call start_Action(Girl, "suck_breasts")
                    "Your pussy?":
                        call start_Action(Girl, "fondle_pussy")
                    "Eat your pussy?":
                        call start_Action(Girl, "eat_pussy")
                    "Your ass?":
                        call start_Action(Girl, "fondle_ass")
                    "Eat your ass?":
                        call start_Action(Girl, "eat_ass")
                    "Maybe something else.":
                        pass
            "Could you take care of something for me?":
                menu:
                    Girl.voice "[handjob_line]"
                    "Could you give me a handjob?":
                        call start_Action(Girl, "handjob")
                    "Could use your feet?":
                        call start_Action(Girl, "footjob")
                    "Could you give me a titjob?":
                        call start_Action(Girl, "titjob")
                    "Could you suck my cock?":
                        call start_Action(Girl, "blowjob")
                    "Maybe something else.":
                        pass
            "Could we maybe. . . ?":
                menu:
                    Girl.voice "[main_line]"
                    "Come over here, I've got something in mind. . .":
                        call start_Action(Girl, "hotdog")
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
            "Move a hand to her thighs. . .":
                return ["fondle_thighs", "auto"]
            "Move a hand to her breasts. . .":
                return ["fondle_breasts", "auto"]
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]

label fondle_menu(Girl, Action_type):
    while True:
        menu:
            "Keep going. . .":
                return [None, "continue"]
            "I want to stick a finger in. . ." if Action_type == "fondle_pussy":
                menu:
                    "Ask her first":
                        return ["finger_pussy", "shift"]
                    "Just slip it in":
                        return ["finger_pussy", "auto"]
                    "Back":
                        pass
            "Pull out. . ." if Action_type == "finger_pussy":
                return ["fondle_pussy", "pullback"]
            "Pull back a bit. . ." if Action_type == "fondle_pussy":
                return ["fondle_thighs", "pullback"]
            "Shift primary action":
                menu:
                    "Can I go a little deeper?" if Action_type == "fondle_thighs":
                        return ["fondle_pussy", "shift"]
                    "Shift your hands a bit higher without asking" if Action_type == "fondle_thighs":
                        return ["fondle_pussy", "auto"]
                    "I want to finger you." if Action_type == "fondle_pussy":
                        return ["finger_pussy", "shift"]
                    "Just slip a finger in." if Action_type == "fondle_pussy":
                        return ["finger_pussy", "auto"]
                    "Ask to suck on them." if Action_type == "fondle_breasts":
                        return ["suck_breasts", "shift"]
                    "Just suck on them without asking." if Action_type == "fondle_breasts":
                        return ["suck_breasts", "auto"]
                    "Pull back to fondling." if Action_type = = "suck_breasts":
                        return ["fondle_breasts", "pullback"]
                    "I want to lick your pussy." if Action_type in ["fondle_pussy", "finger_pussy"]:
                        return ["eat_pussy", "shift"]
                    "Just start licking." if Action_type in ["fondle_pussy", "finger_pussy"]:
                        return ["eat_pussy", "auto"]
                    "Pull back to the thighs." if Action_type in ["fondle_pussy"]:
                        return ["fondle_thighs", "auto"]
                    "Pull out and start rubbing again." if Action_type in ["finger_pussy"]:
                        return ["fondle_pussy", "pullback"]
                    "I want to stick a finger in." if Action_type in ["fondle_ass", "eat_ass"]:
                        return ["finger_ass", "shift"]
                    "Just stick a finger in without asking." if Action_type in ["fondle_ass", "eat_ass"]:
                        return ["finger_ass", "auto"]
                    "I want to lick your asshole." if Action_type in ["fondle_ass", "finger_ass"]:
                        return ["eat_ass", "shift"]
                    "Just start licking." if Action_type in ["fondle_ass", "finger_ass"]:
                        return ["eat_ass", "auto"]
                    "Pull out and start rubbing again." if Action_type in ["finger_ass"]:
                        return ["fondle_ass", "pullback"]
                    "Switch to fondling." if Action_type = = "eat_ass":
                        return ["fondle_ass", "pullback"]
                    "Back":
                        pass
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]

label handjob_menu(Girl, Action_type):
    while True:
        menu:
            "Keep going. . ." if Girl.primary_Action.speed:
                return [None, "continue"]
            "Start moving? . ." if Action_type in ["handjob", "footjob", "titjob"] and not Girl.primary_Action.speed:
                $ Girl.primary_Action.speed = 1
            "Speed up. . ." if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed < 2:
                $ Girl.primary_Action.speed = 2
            "Speed up. . . (locked)" if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed > 1:
                pass
            "Slow down. . ." if Action_type in ["handjob", "footjob", "titjob"] and Girl.primary_Action.speed:
                $ Girl.primary_Action.speed -= 1
            "Slow down. . . (locked)" if Action_type in ["handjob", "footjob", "titjob"] and not Girl.primary_Action.speed:
                pass
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
                    "Pull back to hotdog her" if Action_type != "hotdog":
                        return ["hotdog", "pullback"]
                    "Back":
                        pass
            "Back to Sex Menu":
                ch_p "Let's try something else."

                return [None, "switch"]
            "End scene":
                ch_p "Let's stop for now."

                return [None, "stop"]
