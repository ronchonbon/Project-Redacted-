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

    $ Player.History.remove("offered_to_help_Rogue_study")
    $ Player.History.update("helped_Rogue_study")

    return
