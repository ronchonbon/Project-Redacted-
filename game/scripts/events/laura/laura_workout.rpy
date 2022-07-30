init python:

    def Laura_workout():
        label = "Laura_workout"

        conditions = [
            "Laura in active_Girls",
            "Player.location == 'bg_dangerroom'",
            "Laura.location == Player.location",
            "Player.level < 5",
            "Laura.mood < 3"]

        conversation = False

        priority = False

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label Laura_workout:
    "You start a fairly intense simulation requiring a mixture of hand-to-hand combat and acrobatics."

    if Player.level < 3:
        "The exercise is probably too advanced for you, but you try your best."

    "You notice [Laura.name] glancing your way more than a few times."
    "You make eye contact with her as you attempt a particularly difficult maneuver. . ."
    ". . . and wipe out." with vpunch
    "[Laura.name] is there when you come to, and she helps you up to your feet."
    ch_laura "The settings might be too high on this sequence for you, [Player.name]."

    menu:
        "Whatever, I was doing fine.":
            ch_laura "Uh-huh."
        "Heh, yeah. Thought I'd challenge myself.":
            call change_Girl_stat(Laura, "love", 1)
        "Ow, you don't say.":
            pass

    ch_laura "Want a few pointers?"

    $ workout_accepted = False
    $ workout_ended = False

    menu:
        "Really? That would be awesome.":
            $ workout_accepted = True

            call change_Girl_stat(Laura, "love", 1)
            call change_Girl_stat(Laura, "trust", 1)
            call Laura_workout_1A
        "What, from you?":
            call change_Girl_stat(Laura, "love", -2)
            call change_Girl_stat(Laura, "trust", -2)
            call change_Girl_mood(Laura, 2)
            call Laura_workout_1B

    if workout_accepted and not workout_ended:
        "You spar together for a while."
        "[Laura.name] definitely goes easy on you, but you learn a lot in a short amount of time."

    return

label Laura_workout_1A:
    ch_laura "The main issue is your footwork - it's all over the place."
    ch_laura "Every step should have purpose."
    ch_laura "Here, practice with me."

    menu:
        "Are you sure you wouldn't like to take this \"practice\" elsewhere?":
            call Laura_workout_2A
        "[[Follow her directions]":
            pass

    return

label Laura_workout_1B:
    ch_laura "Rude."

    menu:
        "Sorry, that came out wrong. I'd really appreciate some pointers!":
            $ workout_accepted = True

            call change_Girl_stat(Laura, "love", 2)
            call change_Girl_stat(Laura, "trust", 3)
            call change_Girl_mood(Laura, -2)

            "She turns back to you, seemingly appeased."

            call Laura_workout_1A
        "I think I can handle myself.":
            "She turns to leave with a shrug."

    return

label Laura_workout_2A:
    if approval_check(Laura, "love", 80):
        ch_laura "Heh. Later, [Laura.player_petname]."
    elif approval_check(Laura, "love", 40):
        call change_Girl_stat("love", 1)

        ch_laura "Cute. Stay focused."
    else:
        call change_Girl_stat(Laura, "love", -2)
        call change_Girl_mood(Laura, 1)

        "She responds by effortlessly knocking you off your feet."
        ch_laura "Wow, you look real sexy gasping for breath on the ground."
        ch_laura "You can practice by yourself, [Laura.player_petname]."

        $ workout_ended = True

    return
