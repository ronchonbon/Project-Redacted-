init -1 python:

    def X_belt(Owner):
        name = "X-Men belt"
        string = "X_belt"

        type = "belt"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Oh, I like this one.",
                "purchased": "Cool, thanks.",
                "gift": "Oh, thanks.",
                "change": "Okay."})

        price = 75

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = [
            "standing"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
