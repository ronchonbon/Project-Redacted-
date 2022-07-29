init python:

    def Event():
        label = "Event_label"

        conditions = ["Rogue in active_Girls"]

        conversation = False

        priority = True

        repeatable = False

        return EventClass(label, conditions, priority = priority, repeatable = repeatable)

label Event_label:
    "Congrats, you triggered an event."

    return
