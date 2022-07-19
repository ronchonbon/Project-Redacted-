screen Girl_picker():
    for Girl in active_Girls:
        if renpy.showing(f"{Girl.tag}_sprite"):
            button:
                background None
                anchor (0.5, 0.5) pos (Girl.sprite_location + 0.02, 0.6) xysize (250, 900)
                action Function(renpy.call, "chat_menu", Girl, from_current = True)

screen Wardrobe_picker(Girl):
    window anchor (0.5, 0.5) pos (0.5, 0.5) xysize (int(6.2*256), 800):
        vpgrid:
            cols 6
            spacing 0

            mousewheel True
            draggable True

            side_yfill True

            imagebutton:
                anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                auto "exit_%s"
                action Return("quit")

            for Clothing in Girl.Wardrobe.Clothes.values():
                imagebutton:
                    anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                    auto f"{Girl.tag}_%s"
                    action Return(Clothing)

screen shopping_picker(Girl):
    window anchor (0.5, 0.5) pos (0.5, 0.5) xysize (int(6.2*256), 800):
        vpgrid:
            cols 6
            spacing 0

            mousewheel True
            draggable True

            side_yfill True

            imagebutton:
                anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                auto "exit_%s"
                action Return("quit")

            for Clothing in Clothing_registry(Girl):
                if Clothing.name not in Girl.Wardrobe.Clothes.keys():
                    imagebutton:
                        anchor (0.5, 0.5) pos (0.5, 0.5) xysize (256, 256)
                        auto f"{Girl.tag}_%s"
                        action Return(Clothing)
