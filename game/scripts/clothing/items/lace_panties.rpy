init -1 python:

    def lace_panties(Owner):
        name = "lace panties"
        string = "lace_panties"

        type = "underwear"

        dialogue_lines = {}

        if Owner.tag == "Rogue":
            dialogue_lines.update({
                "shopping": "Ooh, these are cute!",
                "purchased": f"Aw, that's sweet of you, {Owner.player_petname}.",
                "gift": f"Thank you, {Owner.player_petname}!",
                "change": "I do look good in those, don't I?"})

        price = 50

        shame = 1

        hides = ["pussy"]
        covers = ["pussy"]

        number_of_states = 2

        poses = [
            "standing",
            "blowjob",
            "sex",
            "doggy"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
