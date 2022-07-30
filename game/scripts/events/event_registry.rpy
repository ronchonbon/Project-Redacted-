init python:

    def register_Events():
        Events = [
            Rogue_exam(),
            Rogue_study(),
            Rogue_blew_off()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
