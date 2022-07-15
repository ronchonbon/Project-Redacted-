label clothing_shop:
    call set_the_scene(location = "bg_shop")

    "You head into \"Urban Big-Titter's\". . ."

    while True:
        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to do?"
            "Exit":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                call set_the_scene(location = "bg_mall")

                return

    return
