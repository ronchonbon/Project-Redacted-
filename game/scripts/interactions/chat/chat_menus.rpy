label chat_menu(Girl):
    hide screen Girl_picker

    $ Player.focused_Girl = Girl

    $ chatting = True

    while chatting:
        menu:
            "You should go.":
                call remove_Girl(Girl)

                $ chatting = False
            "Did you want to fool around?":
                if approval_check(Girl, "LT", 60):
                    if Girl == Rogue:
                        Girl.voice "Heh, all right, [Girl.player_petname]."

                    call enter_main_sex_menu(Girl)
                elif approval_check(Girl, "DT", 40):
                    if Girl == Rogue:
                        Girl.voice "If that's what you want, [Girl.player_petname]."

                    call enter_main_sex_menu(Girl)
                else:
                    if Girl == Rogue:
                        Girl.voice "I'm not really interested, [Girl.player_petname]."
            "Could I get your number?" if Girl not in Player.Phonebook:
                if approval_check(Girl, "L", 40) or approval_check(Girl, "T", 20):
                    if Girl == Rogue:
                        Girl.voice "Sure, I suppose."

                    $ Player.Phonebook.append(Girl)
                elif approval_check(Girl, "D", 20):
                    if Girl == Rogue:
                        Girl.voice "If you want it, I guess."

                    $ Player.Phonebook.append(Girl)
                else:
                    if Girl == Rogue:
                        Girl.voice "I don't really want you calling me."
            "Could you follow me for a bit?" if Girl not in Player.Party:
                if approval_check(Girl, threshold = 60):
                    if Girl == Rogue:
                        Girl.voice "Ok, Where did you want to go?"

                    $ Player.Party.append(Girl)
                elif not approval_check(Girl, threshold = 40):
                    if Girl == Rogue:
                        Girl.voice "Um, no thanks."
                else:
                    if Girl == Rogue:
                        Girl.voice "I'm fine here, thanks."
            "You can leave if you prefer." if Girl in Player.Party:
                python:
                    for G in Player.Party:
                        Player.Party.remove(G)
            "Never mind.":
                if Girl == Rogue:
                    Girl.voice "Ok, later then."

                $ chatting = False

    return

label text_menu(Girl):
    hide screen Girl_picker
    nvl clear

    Player.text "Hey."

    if Girl == Rogue:
        $ line = f"hey {Girl.player_petname}."

    menu(nvl = True):
        Girl.text "[line]"
        "Want to come over?":
            Player.text "Want to come over?"

            call add_Girls(Girl)
        "Never mind.":
            Player.text "Never mind."

            if Girl == Rogue:
                Girl.text "ok. . ."

    return
