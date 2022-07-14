label classroom_seating:
    call set_the_scene(location = "bg_classroom", fade = True)

    python:
        Girls = Present[:]

        for G in reversed(Girls):
            if G in [EmmaX, StormX]:
                Girls.remove(G)
            elif G in Player.Party:
                Girls.remove(G)

        renpy.random.shuffle(Girls)

    $ Present = Player.Party if Player.Party else []

    if len(Girls) == 2:
        $ D20 = renpy.random.randint(500, 1500)

        if Girls[0].likes[Girls[1].tag] + Girls[1].likes[Girls[0].tag] >= D20:
            "You see that [Girls[0].name] and [Girls[1].name] are sitting next to each other, which do you sit next to?"
        else:
            "You see that [Girls[0].name] and [Girls[1].name] are in the room, but on opposite sides."

        menu:
            "Who do you want to sit next to?"
            "[Girls[0].name].":
                $ Present.append(Girls[0])
            "[Girls[1].name].":
                $ Present.append(Girls[1])
            "Between them." if not Nearby:
                $ Present.append(Girls[0])
                $ Present.append(Girls[1])
            "Neither":
                "You decide to sit a distance away from either of them."
    elif len(Girls) > 2:
        $ flag = False

        while not flag:
            menu:
                "You see several girls are in the room, who would you like to sit near?"
                "[RogueX.name]" if RogueX in Girls and RogueX not in Present:
                    $ Present.append(RogueX)
                "[KittyX.name]" if KittyX in Girls and KittyX not in Present:
                    $ Present.append(KittyX)
                "[LauraX.name]" if LauraX in Girls and LauraX not in Present:
                    $ Present.append(LauraX)
                "[JeanX.name]" if JeanX in Girls and JeanX not in Present:
                    $ Present.append(JeanX)
                "[JubesX.name]" if JubesX in Girls and JubesX not in Present:
                    $ Present.append(JubesX)
                "Done":
                    $ flag = True
    elif Girls:
        menu:
            "You see [Girls[0].name] is there, do you sit next to her?"
            "Yes.":
                $ Present.append(Girls[0])
            "No, I'll sit away from her a bit.":
                pass

    python:
        for G in Girls:
            if G not in Present:
                Nearby.append(G)

                G.location = "nearby"

    if Present and Player.focused_Girl not in Present:
        $ shift_focus(Present[0])

    if len(Present) > 2:
        "You figure out seating arrangements with the girls."
    elif len(Present) == 2:
        "You look for a seat between [Present[0].name] and [Present[1].name]."
    elif len(Present) == 1:
        "You look for a seat next to [Present[0].name]."
    else:
        "You look for a seat off to the side."

    call set_the_scene

    if len(Girls) > len(Present):
        "The rest are scattered around the room."

    return

label take_class:
    # if "met" not in EmmaX.history and day >= 1:
    #     call meet_Emma
    #
    #     return

    if round >= 80:
        $ line = "You make it in time for the start of the class."
    elif round >= 50:
        $ line = "You get in a bit late, but there's plenty of class left."
    else:
        $ line = "You're pretty late, but catch the tail end of the class."

    $ renpy.random.shuffle(Present)

    $ D20 = renpy.random.randint(1, 20)

    # if D20 > 15 and Present and approval_check(Present[0], 300, "I"):
    #     "[line]"
    #
    #     call frisky_class(Present[0])
    if True:
        $ line = line + renpy.random.choice([
            " It was fairly boring.",
            " It was a lesson in mutant biology.",
            " You took a math course.",
            " You watched a movie about sealions.",
            " That was fun.",
            " Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
            " Geopolitical science: Latveria to Madripoor.",
            " Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
            " The topic of the day is Mutants and the larger superhuman community.",
            " Capes: What Your name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
            " The topic is \"Mutants VS Mutates.\" As it turns out, the terms aren’t interchangeable.",
            " Today's class is on how to present yourself to the public. She uses Spider-Man as an example of how bad PR makes your life harder than it needs to be.",
            " Mutant History, Apocalypse to Dark Phoenix.",
            " You spend some time learning about politics. Senator Trask seems like a real piece of work.",
            " You spend class learning about Aristotelian philosophy. Or about your teacher's breasts.",
            " You learn how civil laws apply to mutant powers by studying some high profile case studies. It's surprisingly interesting.",
            " You listen as a guest speaker describes working with a Genosha-based NGO trying to rehabilitate mutants in the States.",
            " Today the teacher is describing the theory behind mutant powers. For some reason, you get the impression she is glancing at you during the lecture.",
            " Game writing for dummies, eh?"])

        "[line]"

    $ Player.XP += 5 + int(round/10)

    return
