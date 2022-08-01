init -1 python:

    def striped_shirt(Owner):
        name = "striped shirt"
        string = "striped_shirt"

        type = "top"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "These look familiar.",
                "purchased": f"Thanks, {Owner.player_petname}.",
                "gift": "Heh, pre-ripped, huh?",
                "change": "Okay."})

        price = 50

        shame = 0

        hides = ["breasts"]
        covers = ["breasts"]

        number_of_states = 1

        poses = ["standing"]

        incompatibilities = ["bodysuit"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses, incompatibilities = incompatibilities)
