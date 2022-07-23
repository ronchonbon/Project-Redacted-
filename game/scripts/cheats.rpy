label cheat_menu(Girl):
    while True:
        menu:
            "[Girl.name]: Love: [Girl.love], Devotion: [Girl.devotion], Trust: [Girl.trust], Desire: [Girl.desire], Location: [Girl.location]"
            "Raise love":
                $ Girl.love += 10
            "Lower love":
                $ Girl.love -= 10
            "Raise devotion":
                $ Girl.devotion += 10
            "Lower devotion":
                $ Girl.devotion -= 10
            "Raise trust":
                $ Girl.trust += 10
            "Lower trust":
                $ Girl.trust -= 10
            "Raise desire":
                $ Girl.desire += 10
            "Lower desire":
                $ Girl.desire -= 10
            "Wardrobe":
                call wardrobe_editor(Girl)
            "Unlock all Girls":
                python:
                    for G in all_Girls:
                        if G not in active_Girls:
                            active_Girls.append(G)

                            Player.Phonebook.append(G)
            "Maximize all Girls' stats":
                python:
                    for G in active_Girls:
                        G.love = 100
                        G.devotion = 100
                        G.trust = 100
            "Add all Girls to Harem":
                python:
                    for G in active_Girls:
                        if G not in Player.Harem:
                            Player.Harem.append(G)
            "Unlock all clothes":
                python:
                    for G in active_Girls:
                        Clothes = register_Clothes(G)

                        for Clothing in Clothes:
                            if Clothing.name not in G.Wardrobe.Clothes.keys():
                                G.Wardrobe.Clothes[Clothing.name] = Clothing
            "Done":
                return

label wardrobe_editor(Girl):
    while True:
        menu wardrobe_menu:
            "View":
                while True:
                    menu:
                        "Default":
                            call show_Girl(Girl)
                        "Blowjob":
                            if not renpy.showing(f"{Girl.tag}_sprite blowjob"):
                                call show_blowjob(Girl)
                            else:
                                call show_Girl(Girl)
                        "Sex":
                            if not renpy.showing(f"{Girl.tag}_sprite sex"):
                                call show_sex(Girl)
                            else:
                                call show_Girl(Girl)
                        "Doggy":
                            if not renpy.showing(f"{Girl.tag}_sprite doggy"):
                                call show_doggy(Girl)
                            else:
                                call show_Girl(Girl)
                        "Back":
                            jump wardrobe_menu
            "Wardrobe":
                $ quit = False

                while not quit:
                    call screen Wardrobe_picker(Girl)

                    if _return != "quit":
                        $ new_Clothing = _return

                        $ currently_wearing = False

                        python:
                            for Clothing in Girl.Wardrobe.current_Outfit.Clothes.values():
                                if Clothing:
                                    if Clothing.name == new_Clothing.name:
                                        currently_wearing = True

                                        break

                        if currently_wearing:
                            $ Girl.change_out_of(new_Clothing.type)
                        else:
                            $ Girl.change_into(new_Clothing.name)
                    else:
                        $ quit = True
            "Back":
                return

    return
