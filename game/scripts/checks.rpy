init python:

    def approval_check(Girl, flavor = "LDT", threshold = None, spread = 15, alternate_thresholds = {}):
        if Girl in alternate_thresholds.keys():
            threshold = alternate_thresholds[Girl]

        if "L" in flavor:
            L = Girl.love
        else:
            L = 0

        if "D" in flavor:
            D = Girl.devotion
        else:
            D = 0

        if "T" in flavor:
            T = Girl.trust
        else:
            T = 0

        if not threshold:
            return L + D + T

        if L + D + T >= threshold + 2*spread:
            return 3
        elif L + D + T >= threshold + spread:
            return 2
        elif L + D + T >= threshold:
            return 1
        else:
            return 0

    def check_who_is_present(location = None):
        Present = Player.Party[:] if Player.Party else []

        if not location:
            location = Player.location

        for G in all_Girls:
            if G not in Player.Party:
                if G not in Present and G.location == location:
                    Present.append(G)
                elif G in Present and G.location != location:
                    Present.remove(G)

        for G in Present:
            if G in Nearby:
                Nearby.remove(G)

        if Present and Player.focused_Girl not in Present:
            renpy.random.shuffle(Present)

            Player.focused_Girl = Present[0]

        return
