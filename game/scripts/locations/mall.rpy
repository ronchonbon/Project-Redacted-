label clothing_shop:
    call set_the_scene(location = "bg_shop")

    "You head into \"Urban Big-Titter's\". . ."

    while True:
        $ Girl = None

        if round <= 20:
            "It's getting late, you head back into the mall. . ."

            return

        menu:
            "What did you want to do?"
            "Have [RogueX.name] try something on." if RogueX in Player.Party:
                $ Girl = RogueX
            "Have [KittyX.name] try something on." if KittyX in Player.Party:
                $ Girl = KittyX
            "Have [EmmaX.name] try something on." if EmmaX in Player.Party:
                $ Girl = EmmaX
            "Have [LauraX.name] try something on." if LauraX in Player.Party:
                $ Girl = LauraX
            "Have [JeanX.name] try something on." if JeanX in Player.Party:
                $ Girl = JeanX
            "Have [StormX.name] try something on." if StormX in Player.Party:
                $ Girl = StormX
            "Have [JubesX.name] try something on." if JubesX in Player.Party:
                $ Girl = JubesX
            "Exit.":
                "You head back into the mall. . ."

                $ round -= 10 if round > 20 else round - 10

                call set_the_scene(location = "bg_mall")

                return

        if Girl:
            $ shift_focus(Girl)

            $ Girl.change_face("smile", 1)

            # if approval_check(Girl, 800) or approval_check(Girl, 600, "L") or approval_check(Girl, 300, "O"):
            "This is placeholder dialogue."

        if Girl:
            $ Player.Party.remove(Girl)
            $ Player.Party.append(Girl)

            "You grab some things and head into one of the dressing rooms with [Girl.name]."

            if len(Player.Party) > 2:
                menu:
                    Player.Party[0].voice "Should we come in too?"
                    "Sure.":
                        "The rest follow you in."
                    "Stay out here.":
                        Player.Party[0].voice "Fine, we'll wait out here."

                        $ Player.Party = [Girl]
            elif len(Player.Party) == 2:
                menu:
                    Player.Party[0].voice "Should I come in too?"
                    "Sure.":
                        "[Player.Party[0].name] follows you in."
                    "Stay out here.":
                        Player.Party[0].voice "Fine, I'll just wait here then."

                        $ Player.Party = [Girl]

            $ door_locked = True

            call set_the_scene(location = "bg_dressing")
            call set_Character_taboos

            $ cart = []
            $ leave = False

            while Girl:
                $ item = None

                menu:
                    "What did you want to try on here?"
                    "Raven cloak" if Girl == RogueX and Girl.Clothes["cloak"] != "Raven_cloak":
                        $ item = "Raven_cloak"
                    "Raven cloak (locked)" if Girl.Clothes["cloak"] == "Raven_cloak":
                        pass
                    "Classic jacket" if Girl == RogueX and Girl.Clothes["jacket"] != "classic_jacket":
                        $ item = "classic_jacket"
                    "Classic jacket (locked)" if Girl.Clothes["jacket"] == "classic_jacket":
                        pass
                    "Opaque fetish top" if Girl == RogueX and Girl.Clothes["top"] != "opaque_fetish_top":
                        $ item = "opaque_fetish_top"
                    "Opaque fetish top (locked)" if Girl.Clothes["top"] == "opaque_fetish_top":
                        pass
                    "Sheer fetish top" if Girl == RogueX and Girl.Clothes["top"] != "sheer_fetish_top":
                        $ item = "sheer_fetish_top"
                    "Sheer fetish top (locked)" if Girl.Clothes["top"] == "sheer_fetish_top":
                        pass
                    "Opaque fetish pants" if Girl == RogueX and Girl.Clothes["bottom"] != "opaque_fetish_pants":
                        $ item = "opaque_fetish_pants"
                    "Opaque fetish pants (locked)" if Girl.Clothes["bottom"] == "opaque_fetish_pants":
                        pass
                    "Sheer fetish pants" if Girl == RogueX and Girl.Clothes["bottom"] != "sheer_fetish_pants":
                        $ item = "sheer_fetish_pants"
                    "Sheer fetish pants (locked)" if Girl.Clothes["bottom"] == "sheer_fetish_pants":
                        pass
                    "Red dress" if Girl == RogueX and Girl.Clothes["dress"] != "red_dress":
                        $ item = "red_dress"
                    "Red dress (locked)" if Girl.Clothes["dress"] == "red_dress":
                        pass
                    "Blue dress" if Girl == RogueX and Girl.Clothes["dress"] != "blue_dress":
                        $ item = "blue_dress"
                    "Blue dress (locked)" if Girl.Clothes["dress"] == "blue_dress":
                        pass
                    "Raven suit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "Raven_suit":
                        $ item = "Raven_suit"
                    "Raven suit (locked)" if Girl.Clothes["bodysuit"] == "Raven_suit":
                        pass
                    "Swimsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "swimsuit":
                        $ item = "swimsuit"
                    "Swimsuit (locked)" if Girl.Clothes["bodysuit"] == "swimsuit":
                        pass
                    "Sexy swimsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "sexy_swimsuit":
                        $ item = "sexy_swimsuit"
                    "Sexy swimsuit (locked)" if Girl.Clothes["bodysuit"] == "sexy_swimsuit":
                        pass
                    "Classic catsuit" if Girl == RogueX and Girl.Clothes["bodysuit"] != "catsuit":
                        $ item = "catsuit"
                    "Classic catsuit (locked)" if Girl.Clothes["bodysuit"] == "catsuit":
                        pass
                    "Violet shirt" if Girl == KittyX and Girl.Clothes["top"] != "violet_shirt":
                        $ item = "violet_shirt"
                    "Violet shirt (locked)" if Girl.Clothes["top"] == "violet_shirt":
                        pass
                    "Black and blue pants" if Girl == KittyX and Girl.Clothes["bottom"] != "black_and_blue_pants":
                        $ item = "black_and_blue_pants"
                    "Black and blue pants (locked)" if Girl.Clothes["bottom"] == "black_and_blue_pants":
                        pass
                    "Qipao" if Girl == KittyX and Girl.Clothes["dress"] != "qipao":
                        $ item = "qipao"
                    "Qipao (locked)" if Girl.Clothes["dress"] == "qipao":
                        pass
                    "Domme outfit" if Girl == EmmaX and Girl.Clothes["bodysuit"] != "domme_suit":
                        $ item = "domme_suit"
                    "Domme outfit (locked)" if Girl.Clothes["bodysuit"] == "domme_suit":
                        pass
                    "Spiked collar" if Girl == EmmaX and Girl.Clothes["neck"] != "spiked_collar":
                        $ item = "spiked_collar"
                    "Spiked collar (locked)" if Girl.Clothes["neck"] == "spiked_collar":
                        pass
                    "Domme boots" if Girl == EmmaX and Girl.Clothes["boots"] != "domme_boots":
                        $ item = "domme_boots"
                    "Domme boots (locked)" if Girl.Clothes["boots"] == "domme_boots":
                        pass
                    "Bunny suit" if Girl == LauraX and Girl.Clothes["bodysuit"] != "bunny_suit":
                        $ item = "bunny_suit"
                    "Bunny suit (locked)" if Girl.Clothes["bodysuit"] == "bunny_suit":
                        pass
                    "Bunny ears" if Girl == LauraX and Girl.Clothes["face_outer_accessory"] != "bunny_ears":
                        $ item = "bunny_ears"
                    "Bunny ears (locked)" if Girl.Clothes["face_outer_accessory"] == "bunny_ears":
                        pass
                    "Bunny cuffs" if Girl == LauraX and Girl.Clothes["gloves"] != "bunny_gloves":
                        $ item = "bunny_gloves"
                    "Bunny cuffs (locked)" if Girl.Clothes["gloves"] == "bunny_gloves":
                        pass
                    "Sci-fi suit" if Girl == JeanX and Girl.Clothes["bodysuit"] != "sci_fi_suit":
                        $ item = "sci_fi_suit"
                    "Sci-fi suit (locked)" if Girl.Clothes["bodysuit"] == "sci_fi_suit":
                        pass
                    "Take off the [Girl.Clothes[cloak].name]." if Girl.Clothes["cloak"]:
                        $ Girl.take_off("cloak")
                    "Take off the [Girl.Clothes[top].name]." if Girl.Clothes["top"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_top(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.Clothes[dress].name]." if Girl.Clothes["dress"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_dress(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.Clothes[bottom].name]." if Girl.Clothes["bottom"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_bottom(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.Clothes[bodysuit].name]." if Girl.Clothes["bodysuit"]:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I suppose. . ."
                            else:
                                Girl.voice "Ok. . ."

                            call change_bodysuit(Girl, "")

                            Girl.voice ". . ."
                        else:
                            if Girl in [EmmaX, StormX]:
                                Girl.voice "I do not think so. . ."
                            else:
                                Girl.voice "No thanks. . ."
                    "Take off the [Girl.Clothes[face_outer_accessory].name]." if Girl.Clothes["face_outer_accessory"]:
                        $ Girl.take_off("face_outer_accessory")
                    "Take off the [Girl.Clothes[neck].name]." if Girl.Clothes["neck"]:
                        $ Girl.take_off("neck")
                    "Take off the [Girl.Clothes[gloves].name]." if Girl.Clothes["gloves"]:
                        $ Girl.take_off("gloves")
                    "Take off the [Girl.Clothes[boots].name]." if Girl.Clothes["boots"]:
                        $ Girl.take_off("boots")
                    "Leave dressing area.":
                        $ leave = True

                if item:
                    if item in jackets:
                        if Girl.Clothes["top"] or Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            Girl.voice "Sure. . ."

                            call change_jacket(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["jacket"] = item

                            hide black_screen onlayer black
                    elif item in tops:
                        if Girl.seen_breasts or approval_check(Girl, 500, taboo_modifier = 2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_top(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["top"] = item

                            hide black_screen onlayer black
                    elif item in dresses or item in bodysuits:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            if item in dresses:
                                call change_dress(Girl, item, redress = False)
                            elif item in bodysuits:
                                call change_bodysuit(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            if item in dresses:
                                $ Girl.Clothes["dress"] = item
                            elif item in bodysuits:
                                $ Girl.Clothes["bodysuit"] = item

                            hide black_screen onlayer black
                    elif item in bras:
                        if Girl.seen_breasts or approval_check(Girl, 1000, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bra(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.take_off("jacket")
                            $ Girl.take_off("top")
                            $ Girl.take_off("dress")
                            $ Girl.take_off("bodysuit")
                            $ Girl.Clothes["bra"] = item

                            hide black_screen onlayer black
                    elif item in pants or item in skirts or item in shorts:
                        if Girl.seen_underwear or approval_check(Girl, 500, taboo_modifier=2):
                            $ Girl.change_face("sexy")

                            Girl.voice "Sure. . ."

                            call change_bottom(Girl, item, redress = False)

                            Girl.voice ". . ."
                        else:
                            Girl.voice "I'll need some privacy here. . ."

                            show black_screen onlayer black

                            "You back out of the room for a moment. . ."

                            $ Girl.Clothes["bottom"] = item

                            hide black_screen onlayer black
                    elif item in cloaks:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("cloak")

                        pause 0.2

                        $ Girl.Clothes["cloak"] = item
                    elif item in face_outer_accessories:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("face_outer_accessory")

                        pause 0.2

                        $ Girl.Clothes["face_outer_accessory"] = item
                    elif item in necks:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("neck")

                        pause 0.2

                        $ Girl.Clothes["neck"] = item
                    elif item in gloves:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("gloves")

                        pause 0.2

                        $ Girl.Clothes["gloves"] = item
                    elif item in boots:
                        Girl.voice "Sure. . ."

                        $ Girl.take_off("boots")

                        pause 0.2

                        $ Girl.Clothes["boots"] = item

                    if item in cart:
                        pass
                    elif item in Girl.inventory:
                        if item in bras or item in tops:
                            Girl.voice "I do already have one of these though."
                        elif item in underwears or item in hoses or item in socks or item in boots:
                            Girl.voice "I do already have some of these though."
                    else:
                        $ cart.append(item)
                elif leave:
                    if cart and len(Player.Party) > 1:
                        if Player.Party[0].location == Player.location and Player.Party[0] not in [LauraX, JeanX] and Player.Party[0].likes[Girl.tag] >= 500:
                            $ Player.Party[0].change_face("smile")

                            if Player.Party[0] == RogueX:
                                ch_r "Look'in good there. . ."
                            elif Player.Party[0] == KittyX:
                                ch_k "Oh, that looks cute on you!"
                            elif Player.Party[0] == EmmaX:
                                ch_e "You really do wear that well. . ."
                            elif Player.Party[0] == StormX:
                                ch_s "That really does suit you. . ."
                            elif Player.Party[0] == JubesX:
                                ch_v "So cute!"

                            $ Girl.change_face("smile")

                            if Girl == RogueX:
                                ch_r "Aw, thanks. . ."
                            elif Girl == KittyX:
                                ch_k "Right?"
                            elif Girl == EmmaX:
                                ch_e "Obviously. . ."
                            elif Girl == LauraX:
                                ch_l "Ok, cool. . ."
                            elif Girl == JeanX:
                                ch_j "Of course it does. . ."
                            elif Girl == StormX:
                                ch_s "Oh, thank you. . ."
                            elif Girl == JubesX:
                                ch_v "I know, right?"

                            $ Girl.likes[Player.Party[0].tag] += 5

                            $ Player.Party[0].likes[Girl.tag] += 3

                    $ Girl.change_Outfit()

                    $ door_locked = False

                    $ Player.Party = Present[:]
                    $ Player.Party.remove(Girl)
                    $ Player.Party.append(Girl)

                    call set_the_scene(location = "bg_shop")
                    call set_Character_taboos

                    if not cart:
                        "That was fun, but since there wasn't anything she was interested in, she put it all back."

                    while cart:
                        $ item = None

                        menu:
                            "So what did you want to buy?"
                            "The Raven cloak." if "Raven_cloak" in cart:
                                $ item = "Raven_cloak"
                            "Rogue's classic jacket." if "classic_jacket" in cart:
                                $ item = "classic_jacket"
                            "The opaque fetish top." if "opaque_fetish_top" in cart:
                                $ item = "opaque_fetish_top"
                            "The sheer fetish top." if "sheer_fetish_top" in cart:
                                $ item = "sheer_fetish_top"
                            "The opaque fetish pants." if "opaque_fetish_pants" in cart:
                                $ item = "opaque_fetish_pants"
                            "The sheer fetish pants." if "sheer_fetish_pants" in cart:
                                $ item = "sheer_fetish_pants"
                            "The red dress." if "red_dress" in cart:
                                $ item = "red_dress"
                            "The blue dress." if "blue_dress" in cart:
                                $ item = "blue_dress"
                            "The Raven suit." if "Raven_suit" in cart:
                                $ item = "Raven_suit"
                            "The swimsuit." if "swimsuit" in cart:
                                $ item = "swimsuit"
                            "The sexy swimsuit." if "sexy_swimsuit" in cart:
                                $ item = "sexy_swimsuit"
                            "Rogue's classic outfit." if "catsuit" in cart:
                                $ item = "catsuit"
                            "The violet shirt." if "violet_shirt" in cart:
                                $ item = "violet_shirt"
                            "The qipao." if "qipao" in cart:
                                $ item = "qipao"
                            "The black and blue pants." if "black_and_blue_pants" in cart:
                                $ item = "black_and_blue_pants"
                            "The domme outfit." if "domme_suit" in cart:
                                $ item = "domme_suit"
                            "The spiked collar." if "spiked_collar" in cart:
                                $ item = "spiked_collar"
                            "The domme boots." if "domme_boots" in cart:
                                $ item = "domme_boots"
                            "The bunny suit." if "bunny_suit" in cart:
                                $ item = "bunny_suit"
                            "The bunny ears." if "bunny_ears" in cart:
                                $ item = "bunny_ears"
                            "The bunny cuffs." if "bunny_cuffs" in cart:
                                $ item = "bunny_cuffs"
                            "The sci-fi suit." if "sci_fi_suit" in cart:
                                $ item = "sci_fi_suit"
                            "Nothing." if "purchased" not in Player.recent_history:
                                $ Girl.change_face("sad")

                                if "shopblock" not in Girl.daily_history:
                                    $ Girl.add_word(1, "shopblock", "shopblock")
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "love", -2)
                                    call change_Girl_stat(Girl, "devotion", 3)
                                    call change_Girl_stat(Girl, "devotion", 3)

                                "You put all the stuff back."

                                if Girl in [EmmaX, StormX]:
                                    Girl.voice "How disappointing."
                                elif Girl in [LauraX, JeanX]:
                                    pass
                                else:
                                    Girl.voice "Aw. . ."

                                $ cart = []
                            "Done." if "purchased" in Player.recent_history:
                                "You put all the remaining stuff back."

                                $ cart = []

                        if item:
                            if Girl.tag + item in Player.inventory:
                                if item in dresses or item in bodysuits or item in tops or item in skirts or item in cloaks:
                                    "Wait, you already have one of those."
                                    "You pull out the one in your bag and give it to [Girl.name]."
                                elif item in pants or item in shorts or item in gloves or item in face_outer_accessories:
                                    "Wait, you already have a pair of these."
                                    "You pull out the pair in your bag and give them to [Girl.name]."
                            else:
                                if item in ["Raven_suit", "catsuit", "domme_suit"]:
                                    $ cost = 200
                                elif item in ["Raven_cloak", "opaque_fetish_top", "sheer_fetish_top", "opaque_fetish_pants", "sheer_fetish_pants", "red_dress", "blue_dress"]:
                                    $ cost = 100
                                elif item in ["classic_jacket", "swimsuit", "sexy_swimsuit", "violet_shirt", "black_and_blue_pants", "domme_boots"]:
                                    $ cost = 75
                                elif item in ["qipao", "sci_fi_suit"]:
                                    $ cost = 300
                                elif item == "bunny_suit":
                                    $ cost = 150
                                elif item == ["spiked_collar", "bunny_cuffs"]:
                                    $ cost = 25
                                elif item == "bunny_ears":
                                    $ cost = 15

                                if Player.cash < cost:
                                    "You look at the tag - it's $[cost]. You can't afford it."

                                    $ cart.remove(item)
                                else:
                                    $ Player.cash -= cost

                            if item in cart:
                                $ cart.remove(item)

                                $ Player.add_word(1, "purchased")

                                $ Girl.inventory.append(item)
                                $ Girl.change_face("bemused", 1)

                                if item == "Raven_suit":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 20)
                                    call change_Girl_stat(Girl, "trust", 20)
                                elif item == "Raven_cloak":
                                    call change_Girl_stat(Girl, "love", 15)
                                    call change_Girl_stat(Girl, "devotion", 20)
                                    call change_Girl_stat(Girl, "trust", 10)
                                elif item in ["opaque_fetish_top", "opaque_fetish_pants"]:
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 30)
                                    call change_Girl_stat(Girl, "trust", 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item in ["sheer_fetish_top", "sheer_fetish_pants"]:
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 30)
                                    call change_Girl_stat(Girl, "trust", 20)

                                    ch_r "Always did like mesh."

                                    $ Girl.change_face("smile")

                                    ch_r "Thanks, [Girl.player_petname]."
                                elif item == "qipao":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 20)
                                    call change_Girl_stat(Girl, "trust", 20)
                                elif item == "bunny_suit":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 20)
                                    call change_Girl_stat(Girl, "trust", 20)
                                elif item == "bunny_cuffs":
                                    call change_Girl_stat(Girl, "love", 25)
                                    call change_Girl_stat(Girl, "devotion", 20)
                                    call change_Girl_stat(Girl, "trust", 20)
                                elif item == "bunny_ears":
                                    call change_Girl_stat(Girl, "love", 5)
                                    call change_Girl_stat(Girl, "devotion", 5)
                                    call change_Girl_stat(Girl, "trust", 5)

                    $ Player.drain_word("purchased")

                    $ Girl = None

    return
