init -1 python:

    def messy_hair(Owner):
        name = "messy hair"
        string = "messy_hair"

        type = "hair"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "n/a",
                "purchased": "n/a",
                "gift": "n/a",
                "change": "You like it all messed up?"})

        price = 0

        shame = 0

        hides = []
        covers = []

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = []

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
