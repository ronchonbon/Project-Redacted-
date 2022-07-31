init python:

    class ActionClass(object):
        def __init__(self, Actors, type):
            self.Actors = Actors

            self.type = type

            self.speed = 0

            if type in ["kiss"]:
                self.number_of_speeds = 0
            elif type in ["blowjob", "sex", "anal"]:
                self.number_of_speeds = 4
