init python:

    def Rogue_blew_off():
        label = "Rogue_blew_off"

        conditions = [
            "Rogue in active_Girls",
            "Player.History.check('blew_Rogue_off', tracker = 'persistent')",
            "Player.location != 'bg_player'",
            "time_index < 3"]

        conversation = False

        priority = True

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label Rogue_blew_off:
    call add_Girls(Rogue)

    if Player.History.check("blew_Rogue_off") > 1:
        "[Rogue.name] walks in the room. When she spots you, her eyes narrow."
        ch_rogue "[Player.name]! You blew me off! Again!"

        call change_Girl_stat(Rogue, "love", -5)
        call change_Girl_stat(Rogue, "trust", -5)
        call change_Girl_mood(Rogue, 4)

        ch_rogue "That's the last time I ask {i}you{/i} to be \"study buddies.\""
        "She storms off."
    else:
        "[Rogue.name] walks in the room. She spots you and looks away uncomfortably."
        "Eventually, she approaches you."
        ch_rogue "[Rogue.player_petname], hey. Did you. . . forget about studying together?"

        call change_Girl_stat(Rogue, "love", -2)
        call change_Girl_stat(Rogue, "trust", -2)
        call change_Girl_mood(Rogue, 1)

        menu:
            extend ""
            "Shit, yeah I did. I'm sorry, [Rogue.name].":
                ch_rogue "That's okay, happens."

                call change_Girl_stat(Rogue, "love", 1)
                call change_Girl_stat(Rogue, "trust", 1)
                call change_Girl_mood(Rogue, -1)

                ch_rogue "Maybe we can try again sometime?"
                ch_rogue "Anyways, I better head out. See you, [Rogue.player_petname]."
                "She walks away. That could have gone worse?"
            "What?":
                ch_rogue "Oh. Never mind. . ."

                call change_Girl_stat(Rogue, "love", -1)
                call change_Girl_stat(Rogue, "trust", -1)
                call change_Girl_mood(Rogue, 1)

                "She turns away quickly and leaves without another word."
            "Nah, just didn't feel like it.":
                ch_rogue "Gee, real polite of you, [Player.name]."

                call change_Girl_stat(Rogue, "love", -2)
                call change_Girl_stat(Rogue, "trust", -2)
                call change_Girl_mood(Rogue, 2)

                ch_rogue "Next time, give me a heads up if you're gonna be a jerk about it."
                "She walks away in a huff."

    call remove_Girl(Rogue)

    $ Player.History.remove("blew_Rogue_off")

    return
