init python:

    def register_Events():
        Events = [
            chapter_one_conversation_A(),
            chapter_one_conversation_B(),
            chapter_one_news_story_A(),
            chapter_one_news_story_B(),
            chapter_one_news_story_C(),

            Rogue_exam(),
            Rogue_study(),
            Rogue_blew_off(),

            Laura_workout()]

        for Event in Events:
            if Event.label not in EventScheduler.Events.keys():
                EventScheduler.add_Event(Event)

        return
