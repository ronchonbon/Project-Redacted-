init python:

    def chapter_one_finale():
        label = "chapter_one_finale"

        conditions = [
            "chapter == 1",
            "day > 6",
            "weekday < 5",
            "time_index == 0",
            "round == 100"]

        conversation = False

        priority = True

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_finale:
    "You wake up from a night full of vivid dreams."
    "Dreams of shouting, crashes, and even explosions around you.{p}You must be spending too much time in the Danger Room."
    ch_player "Shit, I'm going to miss the morning lecture!"

    call set_the_scene(location = "bg_classroom", show_Characters = False, fade = True)

    ch_player "Uh. . . hello?"

    return
