screen status():
    add "images/UI/backdrops/[Player.focused_Girl.tag]_backdrop.png"

    vbox pos (0.005, 0.005):
        hbox:
            bar range 100 value Player.focused_Girl.love xmaximum 200 ymaximum 40 left_bar At("full_bar", love_color) right_bar "empty_bar" thumb None

        hbox:
            bar range 100 value Player.focused_Girl.desire xmaximum 200 ymaximum 40 left_bar At("full_bar", desire_color) right_bar "empty_bar" thumb None

    vbox pos (0.155, 0.005):
        hbox:
            bar range 100 value Player.focused_Girl.devotion xmaximum 200 ymaximum 40 left_bar At("full_bar", devotion_color) right_bar "empty_bar" thumb None

    vbox pos (0.305, 0.005):
        hbox:
            bar range 100 value Player.focused_Girl.trust xmaximum 200 ymaximum 40 left_bar At("full_bar", trust_color) right_bar "empty_bar" thumb None

    imagebutton pos (0.715, 0.0415):
        auto "phone_%s"
        action ToggleScreen("focus_map")
        focus_mask True

    showif config.developer:
        imagebutton pos (0.755, 0.016):
            auto f"{Player.focused_Girl.tag}_%s"
            action Function(renpy.call, "cheat_menu", Player.focused_Girl, from_current = True)
            focus_mask True

    imagebutton pos (0.8, 0.01):
        auto "inventory_%s"
        action ToggleScreen("inventory")
        focus_mask True

    vbox pos (0.58, 0.015):
        hbox:
            text "Money: $[Player.cash]" size 18

        hbox:
            text "Level: [Player.level]" size 18

        hbox:
            text "[Player.focused_Girl.tag] Level: [Player.focused_Girl.level]" size 18

    frame pos (0.905, 0.047):
        background None

        add "images/UI/icons/clock_base.png":
            anchor (0.5, 0.5) yzoom -1.0

        if round < 50:
            add "images/UI/icons/clock_red.png" at rotate_red(round):
                anchor (0.5, 0.5)
        else:
            add "images/UI/icons/clock_white.png" at rotate_white(round):
                anchor (0.5, 0.5)

        add "images/UI/icons/clock_face.png":
            anchor (0.5, 0.5)

    vbox pos (0.935, 0.0225):
        hbox:
            text "Day: [day] [day_of_week]" size 18

        hbox:
            text "Time: [current_time]" size 16

        hbox:
            text "Stack depth: [stack_depth]" size 14

    vpgrid pos (0.905, 0.1):
        cols 4

        for G in Nearby:
            add f"{G.tag}_hover" at tiny_button

        if len(Nearby) % 4:
            for i in range(4 - len(active_Girls) % 4):
                null

    showif not renpy.get_screen("primary_Action_menu"):
        imagebutton anchor (0.0, 1.0) pos (0.01, 0.99):
            auto "exit_%s"
            action Function(renpy.call, "world_map", from_current = True)
            focus_mask True

screen focus_map():
    vpgrid pos (0.71, 0.09):
        cols 4

        for G in active_Girls:
            if G.location != Player.location:
                imagebutton:
                    auto f"{G.tag}_%s"
                    action [Function(renpy.call, "text_menu", G, from_current = True), Hide("focus_map")]
                    focus_mask True
            else:
                add f"{G.tag}_idle"

        if len(active_Girls) % 4:
            for i in range(4 - len(active_Girls) % 4):
                null

screen inventory():
    vbox pos (0.83, 0.125):
        text "Inventory:" size 20
