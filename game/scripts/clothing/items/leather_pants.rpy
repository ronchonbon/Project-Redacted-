init -1 python:

    def leather_pants(Owner):
        name = "leather pants"
        string = "leather_pants"

        type = "pants"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Huh, these look cool.",
                "purchased": f"Thanks, {Owner.player_petname}, these are nice.",
                "gift": "Oh, thanks.",
                "change": "Cool."})

        price = 150

        shame = 0

        hides = ["pussy"]
        covers = ["pussy", "thighs"]

        number_of_states = 1

        poses = [
            "standing"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
