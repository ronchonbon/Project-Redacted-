label shop:
    call set_the_scene(location = "bg_shop", fade = True)

    "You head into \"Urban Big-Titter's\". . ."

    while True:
        $ Girl = None

        menu:
            "What did you want to do?"
            "Shop for [Rogue.name]" if Rogue in Player.Party:
                $ Girl = Rogue
            "Shop for [Laura.name]" if Laura in Player.Party:
                $ Girl = Laura
            "Exit":
                call set_the_scene(location = "bg_mall", fade = True)

                return

        if Girl:
            call shopping(Girl)

    return

label shopping(Girl):
    $ quit = False

    $ cart = []

    while not quit:
        call screen shopping_picker(Girl)

        if _return != "quit":
            $ Clothing = _return

            Girl.voice "[Clothing.dialogue_lines[shopping]]"

            $ Girl.try_on(Clothing)

            if Clothing.price > Player.cash:
                $ cart.append((f"{Clothing.name.capitalize()} (locked)", Clothing))
            else:
                $ cart.append((Clothing.name.capitalize(), Clothing))
        else:
            $ quit = True

    if cart:
        $ cart.append(("Done", "done"))

    while cart:
        $ narrator("Would you like to buy anything?", interact = False)

        $ Clothing = renpy.display_menu(cart)

        if Clothing != "done":
            $ Player.cash -= Clothing.price

            $ Girl.give(Clothing)

            Girl.voice "[Clothing.dialogue_lines[purchased]]"

            python:
                for Item in cart:
                    if Clothing.name.capitalize() == Item[0]:
                        cart.remove(Item)
        else:
            $ cart = []

    return
