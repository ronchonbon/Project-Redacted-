label take_a_shower:
    python:
        showering_Girls = []

        for G in all_Girls:
            if G.location == "bg_shower":
                showering_Girls.append(G)

    if showering_Girls:
        ch_p "I'm taking a shower, care to join me?"

        python:
            for G in showering_Girls:
                G.undress()

    if showering_Girls:
        if len(showering_Girls) > 2:
            "You take a quick shower with the girls."
        elif len(showering_Girls) == 2:
            "You take a quick shower with [showering_Girls[0].name] and [showering_Girls[1].name]."
        else:
            "You take a quick shower with [showering_Girls[0].name]."
    else:
        "You take a quick shower."

        $ line = renpy.random.choice([
            "It was fairly uneventful.",
            "A few people came and went as you did so.",
            "That was refreshing."])

        "[line]"

    $ round -= 30 if round >= 30 else round

    return
