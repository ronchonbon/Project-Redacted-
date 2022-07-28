init python:

    def register_Clothes(Girl):
        Clothes = []

        return Clothes

    def default_Outfits(Girl):
        default = OutfitClass("default", wear_in_public = True, wear_in_private = True)
        alternate = OutfitClass("alternate", wear_in_public = True, wear_in_private = True)

        for Outfit in [default, alternate]:
            Girl.Wardrobe.Outfits.update({Outfit.name: Outfit})

        for Outfit in Girl.Wardrobe.Outfits.values():
            for Clothing in Outfit.Clothes.values():
                if Clothing.name:
                    Girl.Wardrobe.add_Clothing(Clothing)

        Girl.Wardrobe.choose_Outfits()
        Girl.change_Outfit(Girl.Wardrobe.public_Outfit.name, instant = True)

        return
