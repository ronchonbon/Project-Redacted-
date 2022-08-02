label prologue:
    $ chapter = 0

    menu:
        "Skip prologue?"
        "Yes":
            jump chapter_one_intro
        "No":
            pass

    "You’re in a college freshman seminar. Your professor is explaining something on the whiteboard, while you have your laptop open to CNN."
    ch_reporter ". . . from the wreckage here in downtown Manhattan, where first responders are still combing through the debris from the incident last night. . ."
    ch_reporter ". . . in addition to the multiple explosions, we have footage of what appears to be a massive hurricane swelling above the city before disappearing moments later. . ."
    ch_reporter ". . . I'm receiving confirmation that the wreckage is indeed that of a Sentinel. . ."
    ch_player "Holy shit, I was just there!"

    $ last_name = get_last_name(Player)

    ch_farouk "Mr. [last_name]!" with vpunch
    ch_farouk "Thrilling as world news may be today, could you muster an ounce of attention or respect for my lecture?"

    menu:
        extend ""
        "Sorry, Prof. Farouk. You know this class is the sole reason I wake up every morning.":
            call prologue_1A
        "Why so grumpy, Prof. Farouk?":
            call prologue_1B
        "You’re right, Prof. Farouk. I {i}don't{/i} respect your lecture. This sucks.":
            call prologue_1C

    "Your classmates' reactions range from horror to highly entertained."
    "Your professor's reaction is. . . worse."
    "For the briefest moment, a terrifying malice flashes on Prof. Farouk's face. . .{p}quickly replaced with a look of irritation."
    ch_farouk "I've had enough of your insolence, [last_name]. Get out of my lecture hall. Don't come back."

    show black_screen onlayer black

    "Shit, now you've done it. . ."

    pause 1.0

    "Some time later. . ."

    hide black_screen onlayer black

    "You've locked yourself in a campus bathroom stall, crouched on a toilet seat."
    ch_player "Fuck, suspended? What am I going to do. . ."
    ch_player "My dad is going to kill me this time, I know it."
    "Your mounting anxiety gives way to a sense of dread."
    "The hairs on your arms and the back of your neck rise up. You begin shivering uncontrollably."

    if Player.skin_color == "green":
        "Before your eyes, your skin begins to ripple and. . . change color."

    pause 1.0

    "Your attention suddenly shifts to the sound of the bathroom door slamming shut." with vpunch
    ch_unknown "Mr. [last_name]." with rumble
    "The deep, inhuman voice is like something from your nightmares."
    "You cover your ears in an almost primal reaction."
    ch_unknown "I know you're in there." with rumble
    "You realize the voice is coming from inside your head."
    "Panic fills your lungs. Something inside you knows it's already too late to call for help."
    "The stall door unlocks itself and begins to open."
    "You kick out to try to close it shut."
    ch_unknown "Don't resist. Sleep." with rumble
    "The command causes you to collapse to the floor."
    "An immense weight begins to press down upon you."
    "You are an insect being crushed under a boot."

    pause 1.0

    "You don't hear the sound of the bathroom door being forced open again."
    ". . . and then just like that, the weight is lifted."
    "As you drift out of consciousness, you again hear a voice."
    "A human voice."

    $ Xavier.name = "???"

    ch_xavier "You're okay, [Player.name]. . . You're safe. . . You're with friends now. . ."

    jump chapter_one_intro

label prologue_1A:
    "You succeed in making some of your classmates chuckle."
    ch_farouk "I’m honored by your enthusiasm, Mr. [last_name]."
    ch_farouk "Perhaps you would care to go one step further and share with us your thoughts on today’s subject?"

    menu:
        extend ""
        "Let's see. . . You were doing a terrible job discussing Jung’s Shadow, and failing to explain how it encompasses not only our darkest, most reprehensible tendencies, but also our strongest creative desires.":
            pass

    return

label prologue_1B:
    ch_farouk "Believe me, Mr. [last_name], you would not care to see me when I am grumpy."
    ch_farouk "At any rate, your lack of respect and plummeting academic performance does you more disservice than it does me."
    ch_farouk "Whether you succeed or fail, your tuition still funds my penthouse in Cairo."

    menu:
        extend ""
        "If I'm paying for your fancy crib, could I at least stay there for a couple of weeks next summer? I'll take good care of it. Hey, your wife can come too!":
            pass

    return

label prologue_1C:
    "You succeed in making some of your classmates chuckle."
    ch_farouk "If you dislike my class that much, you are free to attend whatever matters interest you the most in this weekly timeframe."
    ch_farouk "What you are not entitled to do, Mr. [last_name], is waste my time."

    menu:
        extend ""
        "Well, suck my dick, asshole!":
            pass

    return
