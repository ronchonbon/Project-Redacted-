label prologue:

    menu:
        "Skip prologue?"
        "Yes":
            jump chapter_one_beginning
        "No":
            pass

    "You’re in a freshman college seminar. Your professor is explaining something he had written on the whiteboard, while you have your laptop open to CNN. A journalist is covering a calamity live."
    ch_reporter "We have confirmation of the identity of the body found in the wreckage of the Harrier aircraft that was blown out of the Colorado sky this morning:{p}John Proudstar, former U.S Marine."
    ch_reporter "Proudstar had been reported missing from the Apache reservation in Camp Verde, Arizona three months ago. At the moment, Colorado authorities are trying to find the motive behind his presence in the State."
    ch_player "Holy shit!"

    $ last_name = get_last_name(Player)

    ch_farouk "I heard that, Mr. [last_name]."
    "Your classmates turn around to stare at you. Some are tired of you, while others burst into laughter."
    ch_farouk "I'm not narcissistic enough to believe you are {i}that{/i} thrilled about my teaching, Mr. [last_name]."

    menu:
        "Your very presence thrills me beyond belief, Prof. Farouk. Everybody knows this class is the sole reason I wake up every morning.":
            call prologue_1A
        "That was rude, Prof. Farouk. Why don't you love me?":
            call prologue_1B
        "You’re right, Prof. Farouk, your class doesn’t thrill me in the slightest. This sucks.":
            call prologue_1C

    "Oh shit, now you've done it. . ."
    "Some time later. . ."
    "You are locked in a campus bathroom stall, crouched on the toilet seat."
    ch_player "Shit, I can't believe I got suspended. That fucking prick! What am I going to do now?"
    ch_player "My dad is going to kill me this time, I know it."
    "A couple pairs of feet appear underneath the stall door."
    "BANG BANG BANG" with vpunch
    ch_classmate "We know you're in there, [Player.name]. Get the fuck out, we want to talk to you."
    "BANG BANG BANG" with vpunch
    ch_classmate "Oh, so now you decide to keep your mouth shut?"
    "With a crash, the door is kicked open revealing four of your classmates. They are pissed."

    menu:
        "You people don't know what you're doing. Please, I don't want to hurt you.":
            pass
        "Please, leave me alone.":
            pass
        "Do you guys want to talk through this?":
            pass
        "Go fuck yourselves!":
            pass

    "You cover your head as your classmates knock you to the floor and start kicking you mercilessly."
    ch_classmate "We are fucking tired of you ruining every class with your bullshit!"
    ch_classmate "My family pays good money for this place. I won't let you shit on the best time of my life!"
    ch_player "Stop, please!"
    "The others don't notice that your eyes have turned black and are emitting a bright halo, like a solar eclipse."
    "One of the students is wearing shorts, his calves exposed. You reach out to grab his exposed leg."
    ch_player "I said {i}STOP{/i}!" with vpunch
    ch_classmate "AHHHHH!"
    "He falls to the ground, unconscious."
    ch_classmate "What the fuck?"
    ch_classmate "What the fuck did you just do to him?"
    ch_classmate "Shit, he's one of them! What do we do?"
    "One of your assailants runs off, but the remaining two continue to kick with you increased vigor."
    "Suddenly, the door to the bathroom flings open."
    "Your classmates panic and make a break for it."
    "You see the silhouette of a woman approaching you, before your vision fades to black."

    jump chapter_one_beginning

label prologue_1A:
    ch_classmate "Jesus, [Player.name] is such an asshole."
    ch_farouk "I’m honored by your enthusiasm, Mr. [last_name]."
    ch_farouk "Given that my class is the reason you woke up this fine morning, would you care to share with us your thoughts on today’s subject?"
    ch_classmate "This prick is so annoying. Why doesn't [Player.name] just fuck off?"

    menu:
        "You were eloquently explaining Jung’s concept of the human shadow, and how it encompasses our darkest, most reprehensible tendencies, as well as our strongest creative desires.":
            pass

    return

label prologue_1B:
    ch_classmate "Jesus, [Player.name] is such an asshole."
    ch_farouk "I’m not here to love you, Mr. [last_name], but to give you the tools to enter the job marketplace."
    ch_farouk "That way, you can pay the student loan that funds my penthouse in Cairo."
    ch_classmate "Burn!"

    menu:
        "If I'm paying for your fancy crib, could I at least stay there for a couple of days next summer? I promise I will take good care of it. Your wife can come too!":
            pass

    return

label prologue_1C:
    ch_classmate "Jesus, [Player.name] is such an asshole."
    ch_farouk "If you dislike my class that much, you are free to attend whatever matters interest you the most in this weekly timeframe."
    ch_farouk "What you are not entitled to do, Mr. [last_name], is waste my time and that of your classmates."
    ch_classmate "Yeah, why don't you just fuck off, [Player.name]?"

    menu:
        "Well, suck my dick, asshole!":
            pass

    return
