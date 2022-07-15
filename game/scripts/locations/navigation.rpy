label world_map:
    hide screen Girl_picker

    $ stack_depth = renpy.call_stack_depth()

    while True:
        $ Player.destination = None

        menu:
            "Where would you like to go?"
            "My room" if Player.location != "bg_player":
                $ Player.destination = "bg_player"
            "Girl's rooms":
                menu:
                    "[RogueX.name]'s room" if Player.location != "bg_rogue":
                        $ Player.destination = RogueX
                    "Back":
                        pass
            "Campus" if Player.location != "bg_campus":
                $ Player.destination = "bg_campus"
            "The showers" if Player.location != "bg_shower":
                $ Player.destination = "bg_shower"
            "The pool" if Player.location != "bg_pool":
                $ Player.destination = "bg_pool"
            "Stay where I am.":
                return

        if Player.destination:
            $ stack_depth = renpy.call_stack_depth()

            while stack_depth > 0:
                $ stack_depth -= 1

                $ renpy.pop_call()

            call hide_all

            if Player.destination == "bg_player":
                jump player_room
            elif Player.destination in all_Girls:
                $ Girl = Player.destination

                jump girls_room
            elif Player.destination == "bg_campus":
                jump campus
            elif Player.destination == "bg_shower":
                jump showers
            elif Player.destination == "bg_pool":
                jump pool

label player_room:
    $ door_locked = False

    if Player.destination != Player.location:
        $ Nearby = []

        call set_the_scene(location = "bg_player", fade = True)
    else:
        call set_the_scene(location = "bg_player")

    if round <= 10:
        call wait

    while True:
        show screen Girl_picker()

        menu:
            "You are in your room. What would you like to do?"
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Sleep" if time_index > 2:
                call wait
            "Wait" if time_index < 3:
                call wait
            "Leave":
                call world_map

label girls_room:
    $ door_locked = False

    if Player.destination != Player.location:
        $ Nearby = []

        call set_the_scene(location = Girl.home, fade = True)
    else:
        call set_the_scene(location = Girl.home)

    if round <= 10:
        call wait

    while True:
        if Girl.location == Player.location:
            $ line = f"You are in {Girl.name}'s room. What would you like to do?"
        else:
            $ line = f"You are in {Girl.name}'s room, but she isn't here. What would you like to do?"

        show screen Girl_picker()

        menu:
            "[line]"
            "Lock the door" if not door_locked:
                $ door_locked = True
            "Unlock the door" if door_locked:
                $ door_locked = False
            "Sleep" if time_index > 2:
                call wait
                call set_the_scene
            "Wait" if time_index < 3:
                call wait
                call set_the_scene
            "Leave":
                call world_map

label campus:
    $ door_locked = False

    if Player.destination != Player.location:
        $ Nearby = []

        call set_the_scene(location = "bg_campus", fade = True)
    else:
        call set_the_scene(location = "bg_campus")

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room

        call wait

    while True:
        show screen Girl_picker()

        menu:
            "You are in the campus square. What would you like to do?"
            "Wait" if time_index < 3:
                call wait
            "Leave":
                call world_map

label showers:
    $ door_locked = False

    if Player.destination != Player.location:
        $ Nearby = []

        call set_the_scene(location = "bg_shower", fade = True)
    else:
        call set_the_scene(location = "bg_shower")

    if round <= 10:
        if time_index == 3:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room

        call wait

    while True:
        show screen Girl_picker()

        menu:
            "You're in the showers. What would you like to do?"
            "Shower" if round >= 30:
                call take_a_shower
            "Shower (locked)" if round < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Leave":
                call world_map

label pool:
    $ door_locked = False

    if Player.destination != Player.location:
        $ Nearby = []

        call set_the_scene(location = "bg_pool", fade = True)
    else:
        call set_the_scene(location = "bg_pool")

    if round <= 10:
        if time_index > 2:
            "You're getting tired, you head back to your room."

            $ Player.destination = "bg_player"

            jump player_room

        call wait

    while True:
        show screen Girl_picker()

        menu:
            "You're at the pool. What would you like to do?"
            "Want to swim?" if round >= 30:
                call swim
            "Want to swim? (locked)" if round < 30:
                pass
            "Wait" if time_index < 3:
                call wait
            "Leave":
                call world_map
