label end_of_Action_round(Girl, Action_type):
    $ Player.climax = 50 if not Player.semen and Player.climax >= 50 else Player.climax

    if Player.climax >= 100 or Girl.desire >= 100:
        $ orgasmed = False

        if Player.climax >= 100:
            $ orgasmed = True

        if orgasmed:
            if not Player.semen:
                if Action_type in sex_Action_types:
                    $ line = renpy.random.choice(["She's emptied you out, you'll need to take a break."
                        "You're pretty wiped, better stop for now."])

                    "[line]"

                    return [None, "stop"]
                else:
                    "You're emptied out, you should probably take a break."

    if round == 10:
        call ten_rounds_left_lines(Girl, Action_type)
    elif round == 5:
        call five_rounds_left_lines(Girl, Action_type)

    return [None, "continue"]

label set_secondary_Action(Girl):
    menu:
        "Also kiss her." if Player.primary_Action.type not in mouth_Action_types and Player.secondary_Action.type != "kiss":
            "You lean in and start kissing her."

            $ Action_type = "kiss"
        "Also fondle her breasts." if "fondle_breasts" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_breasts"
        "Also suck her breasts." if Player.primary_Action.type not in mouth_Action_types and Player.secondary_Action.type != "suck_breasts":
            $ Action_type = "suck_breasts"
        "Also fondle her pussy." if "fondle_pussy" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_pussy"
        "Also finger her pussy." if Player.primary_Action.type not in pussy_insertion_Action_types and Player.secondary_Action.type not in pussy_insertion_Action_types:
            $ Action_type = "finger_pussy"
        "Also put a dildo in her pussy." if Player.primary_Action.type not in pussy_insertion_Action_types and Player.secondary_Action.type not in pussy_insertion_Action_types:
            $ Action_type = "dildo_pussy"
        "Also fondle her ass." if "fondle_ass" not in [Player.primary_Action.type, Player.secondary_Action.type]:
            $ Action_type = "fondle_ass"
        "Also finger her ass." if Player.primary_Action.type not in anal_insertion_Action_types and Player.secondary_Action.type not in anal_insertion_Action_types:
            $ Action_type = "finger_ass"
        "Also put a dildo in her ass." if Player.primary_Action.type not in anal_insertion_Action_types and Player.secondary_Action.type not in anal_insertion_Action_types:
            $ Action_type = "dildo_ass"
        "Never mind.":
            return "continue"

    $ Player.secondary_Action = ActionClass(Action_type, Target = Girl)

    return "continue"
