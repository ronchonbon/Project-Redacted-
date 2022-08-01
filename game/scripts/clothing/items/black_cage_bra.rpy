init -1 python:

    def black_cage_bra(Owner):
        name = "black cage bra"
        string = "black_cage_bra"

        type = "bra"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Straps, huh?",
                "purchased": f"I see what you're into, {Owner.player_petname}.",
                "gift": "Oh, you want me to wear this?",
                "change": "If you insist."})

        price = 75

        shame = 1

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
