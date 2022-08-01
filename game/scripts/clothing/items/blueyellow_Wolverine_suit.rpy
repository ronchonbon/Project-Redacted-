init -1 python:

    def blueyellow_Wolverine_suit(Owner):
        name = "Wolverine suit"
        string = "blueyellow_Wolverine_suit"

        type = "bodysuit"

        dialogue_lines = {}

        if Owner.tag == "Laura":
            dialogue_lines.update({
                "shopping": "Yeah, this is awesome.",
                "purchased": f"Heh, thanks, {Owner.player_petname}.",
                "gift": f"Heh, thanks, {Owner.player_petname}.",
                "change": "It does kick ass, huh?"})

        price = 250

        shame = 0

        hides = ["breasts", "pussy"]
        covers = ["breasts", "pussy", "thighs"]

        number_of_states = 1

        poses = [
            "standing"]

        return ClothingClass(Owner, name, string, type, dialogue_lines, price = price, shame = shame, hides = hides, covers = covers, number_of_states = number_of_states, poses = poses)
