label prologue:
    $ time_index = 2
    $ current_time = time_options[time_index]

    $ Player.location = "bg_entrance"

    scene background onlayer background
    scene

    show midground zorder 2
    show foreground zorder 4
    show cover zorder 7
    show Chibi_cock onlayer screens

    $ active_Girls.append(Rogue)

    $ Rogue.History.update("met")

    $ Player.focused_Girl = Rogue

    $ round = 10

    show screen status()

    jump player_room
