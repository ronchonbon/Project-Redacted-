init python:

    def meet_Laura():
        label = "meet_Laura_label"

        conditions = ["Rogue in active_Girls"]

        priority = True

        repeatable = False

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label meet_Laura_label:
    "Congrats, you triggered an event."

    return
