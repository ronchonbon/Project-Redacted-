label splashscreen:
    return

label start:
    python:
        name = renpy.input("What is your name?", default = "Zero", length = 10)
        name = name.strip()

        if not name:
            name = "Zero"

    menu:
        "What is your skin color?"
        "Green":
            $ color = "green"
        "White":
            $ color = "white"
        "Black":
            $ color = "black"

    $ Player = PlayerClass(
        name,
        voice = ch_p, text = ch_p_nvl,
        skin_color = color)

    $ Rogue = GirlClass(
        "Rogue",
        voice = ch_r, text = ch_r_nvl,
        love = 50, devotion = 0, trust = 0, desire = 10)

    $ Laura = GirlClass(
        "Laura",
        voice = ch_l, text = ch_l_nvl,
        love = 50, devotion = 0, trust = 0, desire = 10)

    jump prologue

return
