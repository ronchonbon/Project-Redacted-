init python:

    class HistoryClass(object):
        def __init__(self, default = True):
            self.recent = {}

            self.daily = {}

            self.permanent = {}

            if default:
                self.set_default_items()

        def initialize(self, item):
            for tracker in [self.recent, self.daily, self.permanent]:
                if item not in tracker:
                    tracker.update({item: 0})

        def update(self, item):
            for tracker in [self.recent, self.daily, self.permanent]:
                if item not in tracker:
                    tracker.update({item: 1})
                else:
                    tracker[item] += 1

            return

        def increment(self):
            self.recent = {}

            if time_index == 0:
                self.daily = {}

            return

        def set_default_items(self):
            items = [
                "seen_Player_naked", "underwear_seen", "breasts_seen", "pussy_seen",
                "orgasmed", "swallowed", "creampied", "anal_creampied",
                "had_sleepover",
                "been_with_girl", "seen_with_girl", "caught_Player_with_girl",
                "had_sex_in_public", "caught_in_public",
                "dumped"]

            for item in items:
                self.initialize(item)

            return
