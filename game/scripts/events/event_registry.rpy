init python:

    def register_Events():
        Events = [Rogue_exam()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
