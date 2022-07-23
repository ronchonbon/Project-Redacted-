init python:

    def register_Events():
        Events = [meet_Laura()]

        for Event in Events:
            EventScheduler.add_Event(Event)

        return
