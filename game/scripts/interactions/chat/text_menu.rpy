label text_menu(Girl):
    hide screen Girl_picker
    nvl clear

    Player.text "Hey."

    if Girl == Rogue:
        $ line = f"hey {Girl.player_petname.lower()}"
    elif Girl == Laura:
        $ line = f"Hey"

    $ texting = True

    while texting:
        menu(nvl = True):
            Girl.text "[line]"
            "Want to come over?":
                Player.text "Want to come over?"

                call add_Girls(Girl)

                $ texting = False
            "Never mind.":
                Player.text "Never mind."

                if Girl == Rogue:
                    Girl.text "ok. . ."
                elif Girl == Laura:
                    Girl.text "Huh?"

                $ texting = False

    show screen Girl_picker()

    return
