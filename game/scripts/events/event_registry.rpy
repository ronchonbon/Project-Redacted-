init python:

    def register_Events():
        Events = [Rogue_first_flirting()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
