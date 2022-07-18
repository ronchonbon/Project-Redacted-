screen status():
    add At("images/UI/backdrops/backdrop.png", Girl_color)

    add At("images/UI/backdrops/backdrop_edges.png", Girl_color)

    vbox anchor (0.0, 0.5) pos (0.005, 0.0325):
        spacing 3

        text f"{Player.name}" size 26

        hbox:
            spacing 50

            text f"Level {Player.level}" size 26
            text f"${Player.cash}" size 26

    bar pos (0.3, 0.047):
        range 100
        value Player.desire
        left_bar "images/UI/bars/full_desire_bar.png"
        right_bar "images/UI/bars/empty_desire_bar.png"
        thumb None

    hbox pos (0.4015, 0.03):
        spacing -25

        for i in range(Player.semen):
            add "full_action_bar"

        for i in range(Player.max_semen - Player.semen):
            add "empty_action_bar"

    bar pos (0.0, 0.067):
        range Player.XP_goal
        value Player.XP
        left_bar "images/UI/bars/full_XP_bar.png"
        right_bar "images/UI/bars/empty_XP_bar.png"
        thumb None

    showif not renpy.get_screen("primary_Action_menu"):
        imagebutton pos (0.495, 0.01):
            auto "map_%s"
            action Function(renpy.call, "world_map", from_current = True)
            focus_mask True

    showif renpy.get_screen("primary_Action_menu"):
        imagebutton pos (0.495, 0.01):
            hover "map_hover" idle "map_idle"
            action None

    imagebutton pos (0.59, 0.037):
        auto "phone_%s"
        action Function(renpy.call, "text_menu", Player.focused_Girl, from_current = True)
        focus_mask True

    imagebutton pos (0.635, 0.001):
        auto "inventory_%s"
        action ToggleScreen("inventory")
        focus_mask True

    hbox anchor (0.0, 0.5) pos (0.705, 0.017):
        text f"Day {day}, {current_time.capitalize()} ({day_of_week})" size 26

    hbox anchor (1.0, 0.5) pos (0.99, 0.048):
        text f"{location_names[Player.location]}" size 26

    showif config.developer:
        imagebutton anchor (0.0, 1.0) pos (0.01, 0.99):
            auto f"{Player.focused_Girl.tag}_%s"
            action Function(renpy.call, "cheat_menu", Player.focused_Girl, from_current = True)
            focus_mask True

screen inventory():
    vbox pos (0.83, 0.125):
        text "Inventory:" size 20
