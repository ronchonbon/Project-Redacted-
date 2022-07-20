transform sprite_location(x_position = stage_right, y_position = 0):
    anchor (0.5, 0.0) pos (x_position, y_position)

transform silhouette:
    matrixcolor TintMatrix(Color(rgb = (0.3, 0.4, 0.4)))*OpacityMatrix(0.95)*BrightnessMatrix(-0.9)

transform morning:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.9)))*BrightnessMatrix(0.02)

transform daylight:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.02)

transform sunset:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.8, 0.65)))*BrightnessMatrix(0.01)

transform moonlight:
    matrixcolor TintMatrix(Color(rgb = (0.5, 0.6, 1.0)))*BrightnessMatrix(0.0)

transform indoors:
    matrixcolor TintMatrix(Color(rgb = (1.0, 1.0, 1.0)))*BrightnessMatrix(0.0)

transform lights_off:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.07)

transform candlelit:
    matrixcolor TintMatrix(Color(rgb = (1.0, 0.95, 0.95)))*BrightnessMatrix(-0.1)

transform theater:
    matrixcolor TintMatrix(Color(rgb = (0.45, 0.45, 0.65)))*BrightnessMatrix(-0.05)

transform null:
    alpha 1.0

label show_Girl(Girl, x_position = None, y_position = None, sprite_layer = None, color_transform = None, animation_transform = None, transition = None):
    if x_position:
        $ Girl.sprite_location = x_position

    if not y_position:
        $ y_position = 0

    if sprite_layer:
        $ Girl.sprite_layer = sprite_layer

    if color_transform and animation_transform and transition:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform with transition
    elif color_transform and animation_transform:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform, animation_transform
    elif color_transform and transition:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform with transition
    elif animation_transform and transition:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform with transition
    elif color_transform:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), color_transform
    elif animation_transform:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), animation_transform
    elif transition:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null with transition
    else:
        if Girl.tag == "Rogue":
            show Rogue_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null
        elif Girl.tag == "Laura":
            show Laura_sprite standing zorder Girl.sprite_layer at sprite_location(Girl.sprite_location, y_position), null

    return

label hide_Girl(Girl, transition = None):
    if transition is None:
        call get_transition
        $ transition = _return[1]

    if transition:
        if Girl.tag == "Rogue":
            hide Rogue_sprite with transition
        elif Girl.tag == "Laura":
            hide Laura_sprite with transition
    else:
        if Girl.tag == "Rogue":
            hide Rogue_sprite
        elif Girl.tag == "Laura":
            hide Laura_sprite

    return

label hide_all(fade = False):
    if fade:
        show black_screen onlayer black

    $ temp_Girls = all_Girls[:]

    while temp_Girls:
        if temp_Girls not in Player.Party and renpy.showing(f"{temp_Girls[0].tag}_sprite"):
            call hide_Girl(temp_Girls[0], transition = False)

        $ temp_Girls.remove(temp_Girls[0])

    if fade:
        hide black_screen onlayer black

    return

label get_color_transform:
    if Player.location in ["bg_campus", "bg_pool"] and time_index == 0:
        $ color_transform = morning
    elif Player.location in ["bg_campus", "bg_pool"] and time_index == 1:
        $ color_transform = daylight
    elif Player.location in ["bg_campus", "bg_pool"] and time_index == 2:
        $ color_transform = sunset
    elif Player.location in ["bg_campus", "bg_pool"] and time_index > 2:
        $ color_transform = moonlight
    elif time_index == 4:
        $ color_transform = lights_off
    elif Player.location == "bg_movies":
        $ color_transform = theater
    else:
        $ color_transform = indoors

    return color_transform

label get_transition:
    if Player.location in ["bg_jean", "bg_laura", "bg_player", "bg_pool", "bg_shower"]:
        $ entrance_transition = easeinleft
        $ exit_transition = easeoutleft
    else:
        if renpy.random.randint(0, 1):
            $ entrance_transition = easeinleft
            $ exit_transition = easeoutleft
        else:
            $ entrance_transition = easeinright
            $ exit_transition = easeoutright

    return entrance_transition, exit_transition

label add_Girls(Girls, fade = False):
    if Girls in all_Girls:
        $ Girls = [Girls]

    python:
        for G in Girls:
            G.location = Player.location

            if G not in Present:
                Present.append(G)

    call set_the_scene(fade = fade)

    return

label remove_Girl(Girl, transition = None):
    if Girl in Player.Party:
        $ Player.Party.remove(Girl)

    if Girl in Present:
        $ Present.remove(Girl)

    if Girl in Nearby:
        $ Nearby.remove(Girl)

    if Girl.destination != Girl.location:
        $ Girl.location = Girl.destination
    elif Player.location in ["bg_campus", "bg_pool"]:
        $ Nearby.append(Girl)

        $ Girl.location = "nearby"
    elif Player.location == Girl.home:
        $ Girl.location = "bg_campus"
    else:
        $ Girl.location = Girl.home

    call hide_Girl(Girl, transition = transition)

    return

label remove_all:
    call check_who_is_present

    if Present:
        $ temp_Girls = Present[:]

        while temp_Girls:
            if temp_Girls[0] not in Player.Party:
                call remove_Girl(temp_Girls[0])

            $ temp_Girls.remove(temp_Girls[0])

    return

label show_blowjob(Girl):
    call get_color_transform
    $ color_transform = _return

    if Girl.tag == "Rogue":
        show Rogue_sprite blowjob zorder Girl.sprite_layer at sprite_location(stage_center), color_transform

    return

label show_sex(Girl):
    call get_color_transform
    $ color_transform = _return

    if Girl.tag == "Rogue":
        show Rogue_sprite sex zorder Girl.sprite_layer at sprite_location(stage_center), color_transform

    return

label show_doggy(Girl):
    call get_color_transform
    $ color_transform = _return

    if Girl.tag == "Rogue":
        show Rogue_sprite doggy zorder Girl.sprite_layer at sprite_location(stage_center), color_transform

    return
