label take_class:
    if round >= 80:
        "You make it in time for the start of the class."
    elif round >= 50:
        "You get in a bit late, but there's plenty of class left."
    else:
        "You're pretty late, but catch the tail end of the class."

    $ renpy.random.shuffle(Present)

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
        "Capes: What Your name and Costume Say About You turns out to be pretty lively as you participate in a debate on costume designs.",
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

    return
