label showering:
    python:
        showering_Girls = []

        for G in all_Girls:
            if G.location == "bg_shower":
                showering_Girls.append(G)

    if showering_Girls:
        ch_p "I'm taking a shower, care to join me?"

        $ temp_Girls = showering_Girls[:]

        while temp_Girls:
            if temp_Girls[0].location == Player.location:
                $ temp_Girls[0].undress()
                $ temp_Girls[0].wet = True

                python:
                    for key in temp_Girls[0].spunk.keys():
                        temp_Girls[0].spunk[key] = False

            $ temp_Girls.remove(temp_Girls[0])

    if showering_Girls:
        $ renpy.random.shuffle(showering_Girls)

        $ shift_focus(showering_Girls[0])

        if len(showering_Girls) > 1:
            "You take a quick shower with [showering_Girls[0].name] and [showering_Girls[1].name]."
        else:
            "You take a quick shower with [showering_Girls[0].name]."
    else:
        $ line = "You take a quick shower" + renpy.random.choice([". It was fairly uneventful.",
            ". A few people came and went as you did so.",
            ". That was refreshing."])

        "[line]"

    $ round -= 30 if round >= 30 else round

    call get_dressed

    python:
        for G in showering_Girls:
            G.change_Outfit("shower")

    return
