init python:

    def register_Clothes(Girl):
        if Girl.tag == "Laura":
            Clothes = [
                black_cage_bra(Girl),
                black_finger_gloves(Girl),
                black_panties(Girl),
                black_thong(Girl),
                black_towel(Girl),
                blackwhite_Wolverine_mask(Girl),
                blackwhite_Wolverine_suit(Girl),
                blackyellow_Wolverine_mask(Girl),
                blackyellow_Wolverine_suit(Girl),
                blueyellow_Wolverine_mask(Girl),
                blueyellow_Wolverine_suit(Girl),
                leather_jacket(Girl),
                leather_pants(Girl),
                striped_shirt(Girl),
                white_shirt(Girl),
                X_belt(Girl)]

        return Clothes

    def default_Outfits(Girl):
        default = OutfitClass("default", wear_in_public = True, wear_in_private = True)
        alternate = OutfitClass("alternate", wear_in_public = True, wear_in_private = True)
        shower = OutfitClass("shower")

        if Girl.tag == "Laura":
            default.update_Clothes({
                "underwear": black_panties(Girl),
                "pants": leather_pants(Girl),
                "bra": black_cage_bra(Girl), "top": white_shirt(Girl),
                "belt": X_belt(Girl),
                "jacket": leather_jacket(Girl)})

            alternate.update_Clothes({
                "face_inner_accessory": blackwhite_Wolverine_mask(Girl),
                "bodysuit": blackwhite_Wolverine_suit(Girl),
                "gloves": black_finger_gloves(Girl), "belt": X_belt(Girl)})

            shower.update_Clothes({
                "jacket": black_towel(Girl)})

        for Outfit in [default, alternate, shower]:
            Girl.Wardrobe.Outfits.update({Outfit.name: Outfit})

        for Outfit in Girl.Wardrobe.Outfits.values():
            for Clothing in Outfit.Clothes.values():
                if Clothing.name:
                    Girl.Wardrobe.add_Clothing(Clothing)

        Girl.Wardrobe.choose_Outfits()
        Girl.change_Outfit(Girl.Wardrobe.public_Outfit.name, instant = True)

        return
