init -1 python:

    def leather_jacket(Owner):
        name = "leather jacket"
        string = "leather_jacket"

        type = "jacket"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Think I'd look good in this?",
                "purchased": f"That's nice of you, {Owner.player_petname}.",
                "gift": "Oh, I like it.",
                "change": "Sure."})

        price = 150

        shame = 0

        hides = []
        covers = ["breasts"]

        number_of_states = 1

        poses = [
            "standing"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
