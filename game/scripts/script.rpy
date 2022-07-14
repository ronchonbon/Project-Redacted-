define ch_p = Character("[Player.name]", color = "#87CEEB")
define ch_p_nvl = Character("[Player.name]", kind = nvl)

define ch_r = Character("[RogueX.name]", color = "#85bb65", image = "Rogue_sprite")
define ch_r_nvl = Character("[RogueX.name]", kind = nvl)

label splashscreen:
    return

label start:
    python:
        renpy.start_predict("images/backgrounds/*.*")

        for G in all_Girls:
            renpy.start_predict(f"images/{G.tag}_standing/*.*")

        name = renpy.input("What is your name?", default = "Zero", length = 10)
        name = name.strip()

        if not name:
            name  = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ color = "green"
        "White":
            $ color = "white"
        "Black":
            $ color = "black"

    $ Player = PlayerClass(name, color)

    $ RogueX = GirlClass("Rogue", 500, 0, 0, 10)

    $ Xavier = NPCClass("Professor X")

    $ Player.cash = 100000

    jump prologue

return
