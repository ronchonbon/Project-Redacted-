init -1 python:

    def black_finger_gloves(Owner):
        name = "black finger gloves"
        string = "black_finger_gloves"

        type = "gloves"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "I like these.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": "I can always use more of these.",
                "change": "Kay."})

        price = 45

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
