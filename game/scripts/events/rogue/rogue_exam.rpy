init python:

    def Rogue_exam():
        label = "Rogue_exam"

        conditions = [
            "Rogue in active_Girls",
            "Rogue.location == Player.location",
            "Rogue.mood < 3",
            "time_index < 3",
            "not Player.History.check('offered_to_help_Rogue_study', tracker = 'persistent')",
            "not Player.History.check('blew_Rogue_off', tracker = 'persistent')",
            "Player.History.check('blew_Rogue_off') < 2"]

        conversation = True

        priority = False

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label Rogue_exam:
    $ subject = renpy.random.choice([
        "Biology",
        "Mutant History",
        "World Politics"])

    ch_rogue "I’m okay, [Rogue.player_petname]. Feeling really stressed about this [subject] exam."

    $ offered_to_help = False

    menu:
        extend ""
        "I bet you’ll do fine!":
            call Rogue_exam_1A
        "Me too. Maybe we can study together?":
            call change_Girl_stat(Rogue, "love", 1)
            call Rogue_exam_1B
        "Really? The material isn’t that hard.":
            call Rogue_exam_1C

    if Rogue.mood > 3:
        ch_rogue "Whatever, later."
    elif not offered_to_help:
        ch_rogue "Anyways, I’ll see you later, [Rogue.player_petname]."
    else:
        ch_rogue "Yay, I’m looking forward to it, [Rogue.player_petname]!"

        $ Player.History.update("offered_to_help_Rogue_study")

    return

label Rogue_exam_1A:
    if approval_check(Rogue, threshold = 80):
        ch_rogue "Thanks! I would feel better if I had someone to study with."

        menu:
            extend ""
            "I’d like a study partner too! Want to meet up and work together?":
                call change_Girl_stat(Rogue, "love", 1)
                call Rogue_exam_1B
            "Yeah, that would probably be helpful.":
                pass
            "Yep, good luck.":
                call change_Girl_stat(Rogue, "love", -1)
                call change_Girl_mood(Rogue, 1)

    return

label Rogue_exam_1B:
    call change_Girl_stat(Rogue, "trust", 1)

    if Player.History.check("blew_Rogue_off"):
        ch_rogue "Uh. . . you're not going to blow me off again, are you?"

        menu:
            extend ""
            "Definitely not.":
                ch_rogue "Okay. . . Tonight then? My room?"
            "Uh. . .":
                ch_rogue "Right. No thanks, [Rogue.player_petname]."

                return
    elif approval_check(Rogue, threshold = 80):
        ch_rogue "I would love that, [Rogue.player_petname]. Are you free tonight? We can study in my room."
    elif approval_check(Rogue, threshold = 40):
        ch_rogue "Yeah, that sounds like a good idea. Tonight? You can swing by my room."

    ch_player "Sure!"

    $ offered_to_help = True

    return

label Rogue_exam_1C:
    call change_Girl_stat(Rogue, "love", -1)
    call change_Girl_stat(Rogue, "trust", -2)
    call change_Girl_mood(Rogue, 2)

    ch_rogue "Okay. . . glad you’re finding it easy, [Rogue.player_petname]."

    menu:
        extend ""
        "I’d be happy to study together if you want. Want to meet up tonight to work together?":
            call Rogue_exam_1B
        "Yeah. Anyways, good luck.":
            call change_Girl_stat(Rogue, "love", -1)
        "Have you thought about finding a study group?":
            call Rogue_exam_2A

    return

label Rogue_exam_2A:
    ch_rogue "That’s a good idea, [Rogue.player_petname]. Maybe we could study together tonight?"

    menu:
        extend ""
        "Oh, I meant. . . like someone else.":
            call change_Girl_stat(Rogue, "love", -5)
            call change_Girl_stat(Rogue, "trust", -2)
            call change_Girl_mood(Rogue, 2)
        "I prefer to study alone, but maybe we can hang out another time.":
            pass
        "Uh. . . yeah okay!":
            $ offered_to_help = True

    return
