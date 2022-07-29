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
        love = 50, trust = 0, desire = 10)

    $ Laura = GirlClass(
        "Laura",
        voice = ch_laura, text = ch_laura_nvl,
        love = 50, trust = 0, desire = 10)

    $ Xavier = NPCClass(
        "Prof. X",
        voice = ch_xavier)

    $ Hank = NPCClass(
        "Dr. McCoy",
        voice = ch_hank)

    $ register_Events()

    jump prologue

return
