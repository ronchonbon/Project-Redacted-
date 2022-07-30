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
        voice = ch_player, text = ch_player_nvl,
        skin_color = color)

    $ Rogue = GirlClass(
        "Rogue",
        voice = ch_rogue, text = ch_rogue_nvl,
        love = 20, trust = 20, desire = 0)

    $ Laura = GirlClass(
        "Laura",
        voice = ch_laura, text = ch_laura_nvl,
        love = 10, trust = 10, desire = 0)

    $ Xavier = NPCClass(
        "Prof. X",
        voice = ch_xavier)

    $ Hank = NPCClass(
        "Dr. McCoy",
        voice = ch_hank)

    $ register_Events()

    jump prologue

return
