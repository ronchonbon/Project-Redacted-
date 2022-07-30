init python:

    def Rogue_study():
        label = "Rogue_study"

        conditions = [
            "Rogue in active_Girls",
            "not Player.History.check('offered_to_help_Rogue_study', tracker = 'recent')",
            "Player.History.check('offered_to_help_Rogue_study', tracker = 'persistent')",
            "time_index in [0, 3]"]

        conversation = False

        priority = True

        repeatable = True

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label Rogue_study:
    if time_index == 0:
        ch_player "Looks like I missed studying with [Rogue.name]. . ."

        $ EventScheduler.Events["Rogue_study"].completed = False
        $ EventScheduler.Events["Rogue_study"].counter -= 1

        $ Player.History.remove("offered_to_help_Rogue_study")
        $ Player.History.update("blew_Rogue_off")

        return

    if Player.location != "bg_rogue":
        ch_player "I should probably head over to [Rogue.name]'s for our study session."

        menu:
            extend ""
            "Head over":
                $ Rogue.location = "bg_rogue"

                call set_the_scene(location = "bg_rogue")
            "Stay where I am":
                $ EventScheduler.Events["Rogue_study"].completed = False
                $ EventScheduler.Events["Rogue_study"].counter -= 1

                return
    elif Rogue.location != "bg_rogue":
        call add_Girls(Rogue)

    if round < 10:
        ch_rogue "Oh, hey [Rogue.player_petname]."
        ch_rogue "I'm about to turn it in, but hey, at least you showed up."
        ch_rogue "Goodnight, [Rogue.player_petname]."

        return

    ch_rogue "Hey [Rogue.player_petname]! Come on in."
    "You get settled and start quizzing each other on exam material."

    if approval_check(Rogue, threshold = 120):
        "The two of you have fun going over questions together."
    elif approval_check(Rogue, threshold = 80):
        "You make each other laugh a few times, and [Rogue.name] seems to be having a good time."
    elif approval_check(Rogue, threshold = 20):
        "[Rogue.name] seems unsure of you at first, but warms up after you explain a few questions well and make her laugh a couple times."

    if approval_check(Rogue, "love", 60):
        "[Rogue.name] makes sure you notice her brushing against your fingers, arms, and back whenever she gets a chance."
    elif approval_check(Rogue, "love", 40):
        "You notice [Rogue.name] shyly sneaking closer to you."
    elif approval_check(Rogue, "trust", 80):
        "[Rogue.name] is obviously comfortable with you and snuggles up to you more than once."

    $ round = 20

    "Before you know it, it's gotten quite late."

    if approval_check(Rogue, "love", 40) and approval_check(Rogue, "trust", 60):
        call Rogue_study_1A
    else:
        call Rogue_study_1B

    $ Player.History.remove("offered_to_help_Rogue_study")
    $ Player.History.update("helped_Rogue_study")

    return

label Rogue_study_1A:
    ch_rogue "So [Rogue.player_petname]. . . did you want to take a break from studying?"

    if approval_check(Rogue, "love", 60):
        ch_rogue "Maybe you wanted to do. . . something else?"

        menu:
            extend ""
            "Definitely. [[Kiss her]":
                "[Rogue.name] seems a little surprised, but quickly melts into your kiss."
            "Like what?":
                "[Rogue.name] rolls her eyes, then moves in for a kiss."
            "No thanks.":
                ch_rogue "Oh, right."
                "[Rogue.name] shifts away, clearly disappointed."
                ch_rogue "Well, goodnight then. I'll talk to you later?"

                return

        call Rogue_study_kiss
    else:
        menu:
            extend ""
            "Sounds good to me. Should we call it a night?":
                ch_rogue "Oh. Yeah, sure."
                ch_rogue "Thanks again for studying with me. I'll see you later!"
            "Yeah. . . maybe you wanted to get a little more comfortable?":
                ch_rogue "Maybe. . ."
                "[Rogue.name] moves in for a kiss."

                call Rogue_study_kiss

    return

label Rogue_study_1B:
    menu:
        extend ""
        "So, uh. . . do you want to make out?":
            if approval_check(Rogue, "love", 20) and approval_check(Rogue, "trust", 20):
                ch_rogue "Hmm. . . oh, what the hell."
                "She leans in, clearly expecting you to close the gap."

                call Rogue_study_kiss
            else:
                ch_rogue "Heh, nice try, [Rogue.player_petname]."
                ch_rogue "I'll see you later."
        "It's pretty late, we should probably take a break from studying.":
            ch_rogue "Yeah, you're right."
            ch_rogue "Thanks again for studying with me!"

            menu:
                extend ""
                "Can I get a goodnight kiss?":
                    if approval_check(Rogue, "love", 20) and approval_check(Rogue, "trust", 20):
                        ch_rogue "Hmm. . . oh, what the hell."
                        "She leans in, clearly expecting you to close the gap."

                        call Rogue_study_kiss
                    else:
                        ch_rogue "Heh, nice try, [Rogue.player_petname]."
                        ch_rogue "I'll see you later."
                "Talk to you later.":
                    if approval_check(Rogue, "love", 40):
                        ch_rogue "Oh. Yeah, sure."
                    else:
                        ch_rogue "Sounds good, [Rogue.player_petname]!"

                    ch_rogue "Thanks again for studying with me. I'll see you later!"
        "Want to call it a night?":
            if approval_check(Rogue, "love", 40):
                ch_rogue "Oh. Yeah, sure."
            else:
                ch_rogue "Sounds good, [Rogue.player_petname]!"

            ch_rogue "Thanks again for studying with me. I'll see you later!"

    return

label Rogue_study_kiss:
    call kiss_narrations(Rogue)
    call start_Action(Player, Rogue, "kiss", context = "auto")
    call sex

    return
