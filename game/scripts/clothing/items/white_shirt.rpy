init -1 python:

    def white_shirt(Owner):
        name = "white shirt"
        string = "white_shirt"

        type = "top"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "I go through a ton of these.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": "Thanks.",
                "change": "Sure."})

        price = 50

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 1

        poses = [
            "standing"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
