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
        ch_rogue "That's the last time I ask {i}you{/i} to be \"study buddies.\""
        "She storms off."
    else:
        "[Rogue.name] walks in the room. She spots you and looks away uncomfortably."
        "Eventually, she approaches you."
        ch_rogue "[Rogue.player_petname], hey. Did you. . . forget about studying together?"

        menu:
            "Shit, yeah I did. I'm sorry, [Rogue.name].":
                ch_rogue "That's okay, happens."
                ch_rogue "Maybe we can try again sometime?"
                ch_rogue "Anyways, I better head out. See you, [Rogue.player_petname]."
                "She walks away. That could have gone worse?"
            "What?":
                ch_rogue "Oh. Never mind. . ."
                "She turns away quickly and leaves without another word."
            "Nah, just didn't feel like it.":
                ch_rogue "Gee, real polite of you, [Player.name]."
                ch_rogue "Next time, give me a heads up if you're gonna be a jerk about it."
                "She walks away in a huff."

    call remove_Girl(Rogue)

    $ Player.History.remove("blew_Rogue_off")

    return
