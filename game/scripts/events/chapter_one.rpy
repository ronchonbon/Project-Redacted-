label chapter_one_beginning:
    $ time_index = 2
    $ current_time = time_options[time_index]

    $ Player.location = "bg_player"

    scene background onlayer background
    scene

    show midground zorder 2
    show foreground zorder 4
    show cover zorder 7

    $ active_Girls.append(Rogue)

    $ Rogue.location = "bg_rogue"
    $ Rogue.History.update("met")

    $ Player.focused_Girl = Rogue

    show screen status()
    show screen Girl_picker()

    $ active_Girls.append(Laura)

    $ Laura.location = "bg_laura"

    jump player_room
