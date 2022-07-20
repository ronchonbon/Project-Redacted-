label swim:
    python:
        Swimmers = []
        Chillers = []
        Changers = []

        for G in Present:
            if approval_check(G, threshold = 70):
                if G.Outfit.swimwear:
                    Swimmers.append(G)
                elif G.Wardrobe.current_Outfit.fully_nude:
                    Swimmers.append(G)
                elif G.Wardrobe.swimming_Outfit.name != "null":
                    Changers.append(G)
                else:
                    if G == Rogue:
                        G.voice("I don't really have a swimsuit I could wear. . .")

    if Changers:
        show black_screen onlayer black

        python:
            for G in Changers:
                G.change_Outfit(G.Wardrobe.swimming_Outfit.name, instant = True)

        hide black_screen onlayer black

    if len(Swimmers) > 1 and len(Chillers) > 1:
        "Some of the girls get changed and join you, while the others chill out poolside."
    elif len(Swimmers) > 1 and Chillers:
        "[Chillers[0].name] chills out poolside while the rest of the girls get changed and join you."
    elif len(Swimmers) > 1:
        "The girls get changed and join you."
    elif Swimmers and len(Chillers) > 1:
        "[Swimmers[0].name] gets changed and joins you while the rest of the girls chill out poolside."
    elif Swimmers:
        "[Swimmers[0].name] gets changed and joins you."
    elif len(Chillers) > 1:
        "The girls chill out poolside."
    elif Swimmers and Chillers:
        "[Swimmers[0].name] gets changed and joins you while [Chillers[0].name] chills out poolside."
    elif Chillers:
        "[Chillers[0].name] chills out poolside."

    $ D20 = renpy.random.randint(1, 20)

    if D20 >= 11 or time_index > 2:
        "You take a nice, refreshing swim."
    elif D20 < 3:
        "You join some of the others in a rousing game of Marco Polo."
    elif D20 == 3:
        "You manage to snag one of the floating chairs and drift lazily on the water."
    elif D20 == 4:
        "You manage to snag one of the floating chairs and drift lazily on the water."
        "Until, that is, Kurt teleports up in the air nearby and performs an admittedly awesome cannonball."
        "Too bad it capsizes your chair."
    elif D20 == 5:
        "You test yourself by swimming from one end of the pool to the other."
    elif D20 == 6:
        "You try to impress some of the girls by doing a running jump into the pool."
        "You wind up triggering a cannonball competition that’s ironically NOT won by Cannonball, much to his shock."
    elif D20 == 7:
        "You are about to get into the pool when you hear annoyed cries and shouts of, \"Bobby!\""
        "Looks like Iceman made himself a floating chair again."
        "You stick to the far end of the pool, where it isn’t freezing cold."
    elif D20 == 8:
        "You relax on one of the poolside chairs instead."
    elif D20 == 9:
        "Cyclops is instructing some of the other students in water rescues."
        "You listen in as he talks about approaching a drowning victim from behind so that their panicked flailing won’t cause you injury."
    elif D20 == 10:
        "You decide to make use of the diving board. You do a couple of dives before taking it easy and just swimming around."

    $ round -= 20 if round >= 20 else round

    if len(Swimmers) > 1:
        "You all get out of the pool and rest for a bit."
    elif Swimmers:
        "You both hop out of the pool and rest for a bit."
    else:
        "You hop out of the pool and rest for a bit."

    return
