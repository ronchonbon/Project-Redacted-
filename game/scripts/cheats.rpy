label cheat_menu(Girl):
    while True:
        menu:
            "[Girl.name]: Love: [Girl.love], Devotion: [Girl.devotion], Trust: [Girl.trust], Desire: [Girl.desire], Location: [Girl.location]"
            "Raise love":
                $ Girl.love += 100
            "Lower love":
                $ Girl.love -= 100
            "Raise devotion":
                $ Girl.devotion += 100
            "Lower devotion":
                $ Girl.devotion -= 100
            "Raise trust":
                $ Girl.trust += 100
            "Lower trust":
                $ Girl.trust -= 100
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
                    for G in all_Girls:
                        G.love = 100
                        G.devotion = 100
                        G.trust = 100
            "Add all Girls to Harem":
                python:
                    for G in all_Girls:
                        if G not in Player.Harem:
                            Player.Harem.append(G)
            "Unlock all clothes":
                python:
                    for G in all_Girls:
                        Clothes = Clothing_registry(G)

                        for Clothing in Clothes:
                            if Clothing.name not in G.Wardrobe.Clothes.keys():
                                G.Wardrobe.Clothes[Clothing.name] = Clothing
            "Done":
                $ checkout()

                return

label wardrobe_editor(Girl):
    while True:
        menu wardrobe_menu:
            "View":
                while True:
                    menu:
                        "Default":
                            call show_full_body(Girl)
                        "Handjob":
                            if not renpy.showing(f"{Girl.tag}_sprite handjob"):
                                call show_handjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Titjob":
                            if not renpy.showing(f"{Girl.tag}_sprite titjob"):
                                call show_titjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Blowjob":
                            if not renpy.showing(f"{Girl.tag}_sprite blowjob"):
                                call show_blowjob(Girl)
                            else:
                                call show_full_body(Girl)
                        "Sex":
                            if not renpy.showing(f"{Girl.tag}_sprite sex"):
                                call show_sex(Girl)
                            else:
                                call show_full_body(Girl)
                        "Doggy":
                            if not renpy.showing(f"{Girl.tag}_sprite doggy"):
                                call show_doggy(Girl)
                            else:
                                call show_full_body(Girl)
                        "Back":
                            jump wardrobe_menu
            "Wardrobe":
                $ quit = False

                while not quit:
                    call screen Clothing_picker(Girl)

                    if _return != "quit":
                        $ Clothing_name = _return

                        $ currently_wearing = False

                        python:
                            for Clothing in Girl.Wardrobe.current_Outfit.Clothes.values():
                                if Clothing:
                                    if Clothing.name == Clothing_name:
                                        currently_wearing = True

                                        break

                        if currently_wearing:
                            $ Girl.change_out_of(Girl.Wardrobe.Clothes[Clothing_name].type)
                        else:
                            $ Girl.change_into(Clothing_name)
                    else:
                        $ quit = True
            "Back":
                return

    return
