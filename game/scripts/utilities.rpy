init python:

    def get_last_name(character):
        split_name = character.name.split()

        return split_name[character.name.count(" ")]

    def sort_Girls_by_approval(Girls):
        sorted_Girls = [Girls[0]]

        Girls.remove(Girls[0])

        for G in Girls:
            for g in range(len(sorted_Girls)):
                if approval_check(G) > approval_check(sorted_Girls[g]):
                    sorted_Girls.insert(g, G)

            if G not in sorted_Girls:
                sorted_Girls.append(G)

        return sorted_Girls

    def get_random_name(base = None):
        if not base:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            index = renpy.random.randint(0, 25)
            base = str(alphabet[index])

        names = {
            "A": "Abe",
            "B": "Barry",
            "C": "Carl",
            "D": "Dennis",
            "E": "Erik",
            "F": "Foggy",
            "G": "Gil",
            "H": "Hunk",
            "I": "Ike",
            "J": "Jeff",
            "K": "Kirk",
            "L": "Lance",
            "M": "Mitch",
            "N": "Norm",
            "O": "Ollie",
            "P": "Pete",
            "Q": "Quince",
            "R": "Rory",
            "S": "Sonny",
            "T": "Todd",
            "U": "Uri",
            "V": "Vince",
            "W": "Wally",
            "X": "Ray",
            "Y": "Yuri",
            "Z": "Zoro"}

        while base not in names.key() or names[base] == Player.name:
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            index = renpy.random.randint(0, 25)
            base = str(alphabet[index])

        return names[base]

label change_Player_stat(flavor, update):
    $ stat = getattr(Player, flavor)

    $ stat += update

    $ stat = 100 if stat > 100 else stat

    $ setattr(Player, flavor, stat)

    if update > 0:
        show Text(f"+{update}", size = 40, color = "#FFFFFF") at stat_rising(0.75) onlayer screens
    elif update < 0:
        show Text(f"{update}", size = 40, color = "#FFFFFF") at stat_falling(0.75) onlayer screens

    return

label change_Girl_stat(Girl, flavor, update, alternate_values = {}):
    if Girl in alternate_values.keys():
        $ check = alternate_values[Girl][0]
        $ update = alternate_values[Girl][1]

    $ stat = getattr(Girl, flavor)

    $ stat += update

    if update:
        if flavor == "love":
            $ shade = "#c11b17"
        elif flavor == "devotion":
            $ shade = "#2554c7"
        elif flavor == "trust":
            $ shade = "#FFF380"
        elif flavor == "desire":
            $ shade = "#FAAFBE"

        if update > 0:
            show expression Text(f"+{update}", size = 40, color = shade) at stat_rising(Girl.sprite_location) onlayer screens
        elif update < 0:
            show expression Text(f"{update}", size = 40, color = shade) at stat_falling(Girl.sprite_location) onlayer screens

        $ stat = 100 if stat > 100 else stat

        $ setattr(Girl, flavor, stat)

    return

label set_the_scene(location = None, show_Characters = True, fade = False):
    if fade:
        show black_screen onlayer black

        pause 0.4

    if location:
        $ Player.location = location
    else:
        $ location = Player.location

    python:
        for G in active_Girls:
            if G in Player.Party:
                G.location = Player.location

    if show_Characters:
        $ check_who_is_present(location = Player.location)

        if Present:
            $ offset = (stage_far_far_right - stage_far_left)/len(Present)
            $ total_offset = offset

            call get_color_transform
            $ color_transform = _return

            if not fade:
                call get_transition
                $ transition = _return[0]
            else:
                $ transition = False

            $ number_of_Girls = len(Present)

            $ temp_Girls = all_Girls[:]
            $ temp_Girls.remove(Player.focused_Girl)
            $ renpy.random.shuffle(temp_Girls)

            while temp_Girls:
                if temp_Girls[0].location == Player.location:
                    call show_Girl(temp_Girls[0], x_position = stage_center + total_offset, sprite_layer = 5, color_transform = color_transform, transition = transition)

                    $ number_of_Girls -= 1

                    if stage_center + total_offset + offset >= stage_far_far_right:
                        $ total_offset = -offset*(number_of_Girls - 1)
                    else:
                        $ total_offset += offset
                elif renpy.showing(f"{temp_Girls[0].tag}_sprite"):
                    call hide_Girl(temp_Girls[0])

                $ temp_Girls.remove(temp_Girls[0])

            if Player.focused_Girl.location == Player.location:
                call show_Girl(Player.focused_Girl, x_position = stage_center, sprite_layer = 6, color_transform = color_transform, transition = transition)
            elif renpy.showing(f"{Player.focused_Girl.tag}_sprite"):
                call hide_Girl(Player.focused_Girl)
    else:
        call hide_all

    hide black_screen onlayer black

    return

label set_Girls_locations:
    call set_the_scene(location = Player.location)

    pause 0.4

    $ Nearby = []

    python:
        leaving_Girls = []
        arriving_Girls = []

        for G in active_Girls:
            G.travel()

            if G.destination == G.location:
                pass
            elif G.location == Player.location:
                leaving_Girls.append(G)
            elif G.destination == Player.location:
                arriving_Girls.append(G)

        renpy.random.shuffle(leaving_Girls)
        renpy.random.shuffle(arriving_Girls)

    while leaving_Girls:
        call remove_Girl(leaving_Girls[0])

        $ leaving_Girls.remove(leaving_Girls[0])

    if arriving_Girls:
        call add_Girls(arriving_Girls)

    return

label wait:
    show black_screen onlayer black

    pause 0.4

    $ stack_depth = renpy.call_stack_depth()

    if time_index < 3:
        $ time_index += 1
        $ current_time = time_options[time_index]

        $ round = 100

        pause 0.4

        hide black_screen onlayer black

        call set_Girls_locations
    else:
        $ time_index = 0
        $ current_time = time_options[time_index]

        $ round = 100

        $ day += 1

        if weekday < 6:
            $ weekday += 1
        else:
            $ weekday = 0

        $ day_of_week = week[weekday]

        pause 0.4

        hide black_screen onlayer black

    return
