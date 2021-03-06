label chat_menu(Girl):
    hide screen Girl_picker

    $ Player.focused_Girl = Girl

    $ chatting = True

    while chatting:
        menu:
            "How's it going?":
                $ selected_Event = EventScheduler.choose_Event(conversation = True)

                if selected_Event:
                    $ selected_Event.start()
                else:
                    if Girl.tag == "Rogue":
                        $ lines = [
                            "Sorry, a little busy here!"]
                    elif Girl.tag == "Laura":
                        $ lines = [
                            "Let's talk later."]

                    $ line = renpy.random.choice(lines)

                    Girl.voice "[line]"
            "Did you want to fool around?":
                if approval_check(Girl, "love", 40) and approval_check(Girl, "trust", 20):
                    if Girl.tag == "Rogue":
                        Girl.voice "Heh, all right, [Girl.player_petname]."
                    elif Girl.tag == "Laura":
                        Girl.voice "Cool."

                    call screen Action_menu()
                else:
                    if Girl.tag == "Rogue":
                        Girl.voice "I'm not really interested, [Girl.player_petname]."
                    elif Girl.tag == "Laura":
                        Girl.voice "No thanks, [Girl.player_petname]."
            "Could I get your number?" if Girl not in Player.Phonebook:
                if approval_check(Girl, threshold = 20):
                    if Girl.tag == "Rogue":
                        Girl.voice "Sure, I suppose."
                    elif Girl.tag == "Laura":
                        Girl.voice "Oh, sure."

                    $ Player.Phonebook.append(Girl)
                else:
                    if Girl.tag == "Rogue":
                        Girl.voice "I don't really want you calling me."
                    elif Girl.tag == "Laura":
                        Girl.voice "Um, probably not."
            "Could you follow me for a bit?" if Girl not in Player.Party:
                if approval_check(Girl, threshold = 60):
                    if Girl.tag == "Rogue":
                        Girl.voice "Ok, Where did you want to go?"
                    elif Girl.tag == "Laura":
                        Girl.voice "Where to?"

                    $ Player.Party.append(Girl)
                elif not approval_check(Girl, threshold = 40):
                    if Girl.tag == "Rogue":
                        Girl.voice "Um, no thanks."
                    elif Girl.tag == "Laura":
                        Girl.voice "No."
            "You can stop following me if you want." if Girl in Player.Party:
                $ Player.Party.remove(Girl)
            "You can leave if you like.":
                call dismiss(Girl)

                $ chatting = False
            "Talk to you later.":
                if Girl.tag == "Rogue":
                    Girl.voice "Ok, later then."
                elif Girl.tag == "Laura":
                    Girl.voice "Ok."

                $ chatting = False

    show screen Girl_picker()

    return
