label find_a_seat:
    python:
        Girls = Present[:]

        for G in reversed(Girls):
            if G not in Students:
                Girls.remove(G)
            elif G in Player.Party:
                Girls.remove(G)

        renpy.random.shuffle(Girls)

    $ Present = Player.Party if Player.Party else []

    if len(Girls) > 1:
        $ flag = False

        while not flag:
            menu:
                "You see some familiar faces: who would you like to sit near?"
                "[Rogue.name]" if Rogue in Girls and Rogue not in Present:
                    $ Present.append(Rogue)
                "[Laura.name]" if Laura in Girls and Laura not in Present:
                    $ Present.append(Laura)
                "Done":
                    $ flag = True
    elif Girls:
        menu:
            "You see [Girls[0].name] already seated: do you sit next to her?"
            "Yes":
                $ Present.append(Girls[0])
            "No, sit away from her a bit":
                pass

    python:
        for G in Girls:
            if G not in Present:
                Nearby.append(G)

                G.location = "nearby"

    if Present and Player.focused_Girl not in Present:
        $ Player.focused_Girl = Present[0]

    if len(Present) > 2:
        "You figure out seating arrangements with the girls."
    elif len(Present) == 2:
        "You look for a seat between [Present[0].name] and [Present[1].name]."
    elif len(Present) == 1:
        "You look for a seat next to [Present[0].name]."
    else:
        "You look for a seat off to the side."

    call set_the_scene

    return

label take_class:
    if round >= 80:
        "You make it in time for the start of the class."
    elif round >= 50:
        "You get in a bit late, but there's plenty of class left."
    else:
        "You're pretty late, but catch the tail end of the class."

    $ line = renpy.random.choice([
        "It was fairly boring.",
        "It was a lesson in mutant biology.",
        "You took a math course.",
        "You watched a movie about sealions.",
        "That was fun.",
        "Applied trigonometry is surprisingly interesting, especially when Cyclops demonstrates using it for trick shots.",
        "Geopolitical science: Latveria to Madripoor.",
        "Today's lecture is on reading body language. You suppose if anyone would know about reading people. . .",
        "The topic of the day is Mutants and the larger superhuman community.",
        "Capes: What Your Name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
        "The topic is \"Mutants VS Mutates.\" As it turns out, the terms aren’t interchangeable.",
        "Today's class is on how to present yourself to the public. She uses Spider-Man as an example of how bad PR makes your life harder than it needs to be.",
        "Mutant History, Apocalypse to Dark Phoenix.",
        "You spend some time learning about politics. Senator Trask seems like a real piece of work.",
        "You spend class learning about Aristotelian philosophy. Or about your teacher's breasts.",
        "You learn how civil laws apply to mutant powers by studying some high profile case studies. It's surprisingly interesting.",
        "You listen as a guest speaker describes working with a Genosha-based NGO trying to rehabilitate mutants in the States.",
        "Today the teacher is describing the theory behind mutant powers. For some reason, you get the impression she is glancing at you during the lecture.",
        "Game writing for dummies, eh?"])

    "[line]"

    call wait

    $ Player.XP += 5 + int(round/10)

    return
