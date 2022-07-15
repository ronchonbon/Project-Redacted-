init -1 python:

    def Item(Owner):
        name = "lace panties"
        string = "lace_panties"

        type = "panties"

        if Owner == Rogue:
            shopping = "Ooh, these are cute!"
            purchased = f"Aw, that's sweet of you, {Owner.player_petname}."
            gift = f"Thank you, {Owner.player_petname}!"
            change = "I do look good in those, don't I?"

        dialogue_lines = {
            "shopping": shopping,
            "purchased": purchased,
            "gift": gift,
            "change": change}

        shame = 1

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "standing",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
