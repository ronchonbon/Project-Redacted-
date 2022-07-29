label summon(Girl):
    $ D20 = renpy.random.randint(1, 20)

    if D20 <= 3:
        $ line = "no"
    elif time_index > 2:
        if approval_check(Girl, "L", 70):
            if Girl.tag == "Rogue":
                Girl.text "ok, it's getting late but I can hang out for a bit"
            elif Girl.tag == "Laura":
                Girl.text "You're up too? Sure, we can hang."

            call add_Girls(Girl)
        else:
            if Girl.tag == "Rogue":
                Girl.text "it's a bit late, [Girl.player_petname], maybe tomorrow"
            elif Girl.tag == "Laura":
                Girl.text "Nah."

        return
    elif not approval_check(Girl, "L", 70):
        if not approval_check(Girl, threshold = 30):
            if Girl.tag == "Rogue":
                Girl.text "not really interested, [Girl.player_petname]"
            elif Girl.tag == "Laura":
                Girl.text "I'm busy, [Girl.player_petname]."

            return
        elif Girl.location == "bg_campus":
            if Girl.tag == "Rogue":
                Girl.text "im hanging out on campus, [Girl.player_petname], want to hang with me?"
            elif Girl.tag == "Laura":
                Girl.text "I'm napping under a tree here, want to come?"
        elif Girl.location == "bg_player":
            if Girl.tag == "Rogue":
                Girl.text "I happen to be in your room, [Girl.player_petname], im waiting for you. . ."
            elif Girl.tag == "Laura":
                Girl.text "I'm in your room, [Girl.player_petname], why aren't you?"
        elif Girl.location == Girl.home:
            if Girl.tag == "Rogue":
                Girl.text "im in my room, [Girl.player_petname], want to swing by?"
            elif Girl.tag == "Laura":
                Girl.text "I'm in my room, [Girl.player_petname], want to hang?"
        elif Girl.location == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.text "im kinda in class right now, [Girl.player_petname], you could join me"
            elif Girl.tag == "Laura":
                Girl.text "I'm in class, did you want to come too?"
        elif Girl.location == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.text "im training at the moment, [Girl.player_petname], care to join me?"
            elif Girl.tag == "Laura":
                Girl.text "I'm in the Danger Room, [Girl.player_petname], want in?"
        elif Girl.location == "bg_shower":
            if approval_check(Girl, threshold = 160):
                if Girl.tag == "Rogue":
                    Girl.text "im kinda in the shower right now, [Girl.player_petname], care to join me?"
                elif Girl.tag == "Laura":
                    Girl.text "I'm in the shower right now. Join me?"
            else:
                if Girl.tag == "Rogue":
                    Girl.text "im kinda in the shower right now, [Girl.player_petname], maybe we could touch base later"
                elif Girl.tag == "Laura":
                    Girl.text "I'm in the shower right now, [Girl.player_petname]. We can connect later."

                return
        elif Girl.location == "hold":
            if Girl.tag == "Rogue":
                Girl.text "im not really around right now, see you later?"
            elif Girl.tag == "Laura":
                Girl.text "I'm on task right now. Sorry."

            return
        else:
            if Girl.tag == "Rogue":
                Girl.text "why don't you come over here, [Girl.player_petname]?"
            elif Girl.tag == "Laura":
                Girl.text "Why don't you come to me?"

        menu(nvl = True):
            extend ""
            "Sure, I'll be right there.":
                Player.text "Sure, I'll be right there."

                if Girl.tag == "Rogue":
                    Girl.text "see you!"
                elif Girl.tag == "Laura":
                    Girl.text "See you when you get here."

                $ line = "go to"
            "Nah, we can talk later.":
                Player.text "Nah, we can talk later."

                if Girl.tag == "Rogue":
                    Girl.text "oh, ok. talk to you later then"
                elif Girl.tag == "Laura":
                    Girl.text "Ok. Later then."
            "Could you please come visit me? I'm lonely.":
                Player.text "Could you please come visit me? I'm lonely."

                if approval_check(Girl, "L", 60) or approval_check(Girl, threshold = 140):
                    $ line = "lonely"
                else:
                    if Girl.tag == "Laura":
                        Girl.text "Man, you are such a sap."

                    $ line = "no"
            "Come on, it'll be fun.":
                Player.text "Come on, it'll be fun."

                if approval_check(Girl, "L", 40) and approval_check(Girl, threshold = 80):
                    $ line = "fun"
                else:
                    $ line = "no"
            "I said come over here.":
                Player.text "I said come over here."

                if Girl.tag == "Rogue":
                    Girl.text "I don't know who you think you are, boss'in me around like that."
                elif Girl.tag == "Laura":
                    Girl.text "Don't even try it."

                if Girl.tag == "Rogue":
                    Girl.text "if you want to see me, you know where to find me."
                elif Girl.tag == "Laura":
                    Girl.text "I'm staying put."
    else:
        if Girl.tag == "Rogue":
            Girl.text "id love to, [Girl.player_petname]!"
        elif Girl == KittyX:
            Girl.text "sure!"
        elif Girl == EmmaX:
            Girl.text "I'd love to."
        elif Girl.tag == "Laura":
            Girl.text "Sure."
        elif Girl == JeanX:
            Girl.text "ok fine"
        elif Girl == StormX:
            Girl.text "On my way."
        elif Girl == JubesX:
            Girl.text "sure!"
        elif Girl == MystiqueX:
            Girl.text "On my way."

        $ line = "yes"

    if not line:
        return
    elif line == "go to":
        if Girl.location == "bg_campus":
            if Girl.tag == "Rogue":
                Girl.text "ill keep an eye out for you"
            elif Girl.tag == "Laura":
                Girl.text "Look for the biggest tree."
        elif Girl.location == "bg_player":
            if Girl.tag == "Rogue":
                Girl.text "ill be waiting"
            elif Girl.tag == "Laura":
                Girl.text "I'll be waiting."
        elif Girl.location == Girl.home:
            if Girl.tag == "Rogue":
                Girl.text "ill get tidied up"
            elif Girl.tag == "Laura":
                Girl.text "I'll. . . make some space."
        elif Girl.location == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.text "see you!"
            elif Girl.tag == "Laura":
                Girl.text "K, there's room next to me."
        elif Girl.location == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.text "ill be warming up!"
            elif Girl.tag == "Laura":
                Girl.text "I'll try to leave some bots for 'ya."
        elif Girl.location == "bg_shower":
            if Girl.tag == "Rogue":
                Girl.text "I guess ill be here"
            elif Girl.tag == "Laura":
                Girl.text "I'll leave you some hot water."

        call hide_all

        $ Player.traveling = True

        if Girl.location == "bg_campus":
            jump campus
        elif Girl.location == "bg_player":
            jump player_room
        elif Girl.location == Girl.home:
            $ Girl = Girl

            jump girls_room
        elif Girl.location == "bg_classroom":
            jump classroom
        elif Girl.location == "bg_dangerroom":
            jump danger_room
        elif Girl.location == "bg_pool":
            jump pool
        elif Girl.location == "bg_mall":
            jump mall
        elif Girl.location == "bg_shower":
            jump shower_room
    elif line == "no":
        if Girl.location == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.text "I seriously cant, [Girl.player_petname], big test coming up"
            elif Girl.tag == "Laura":
                Girl.text "I can't skip this lecture."
        elif Girl.location == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.text "wish I could, [Girl.player_petname], but I need to get some hours in"
            elif Girl.tag == "Laura":
                Girl.text "I'm just getting warmed up though!"
        else:
            if Girl.tag == "Rogue":
                Girl.text "sorry, [Girl.player_petname], but im kinda busy right now"
            elif Girl.tag == "Laura":
                Girl.text "Sorry, [Girl.player_petname], I'm kinda busy."

        return
    elif line == "lonely":
        if Girl.tag == "Rogue":
            Girl.text "oh, how could I say no to you, [Girl.player_petname]?"
        elif Girl.tag == "Laura":
            Girl.text "You are such a dork!"

    $ Girl.change_Outfit()

    call Girls_arrive(Girl)

    return

label dismiss(Girl):
    if Girl in Player.Party:
        $ Player.Party.remove(Girl)

    $ leaving = False

    if not approval_check(Girl, "L", 80):
        if Girl.tag == "Rogue":
            Girl.voice "Thanks, but I think I'll stick around."
        elif Girl.tag == "Laura":
            Girl.voice "Ok. [[she does not seem to be moving. . .]"
    else:
        if Girl.tag == "Rogue":
            Girl.voice "Sure, ok. See you later."
        elif Girl.tag == "Laura":
            Girl.voice "Ok."

        $ leaving = True

    if leaving:
        call remove_Girl(Girl)
    elif not leaving:
        menu:
            extend ""
            "I insist, get going.":
                if approval_check(Girl, "L", 50):
                    if Girl.tag == "Rogue":
                        Girl.voice "Ok, if you insist."
                    elif Girl.tag == "Laura":
                        Girl.voice "Ok, fine."

                    $ leaving = True
                elif approval_check(Girl, "L", 20):
                    if Girl.tag == "Rogue":
                        Girl.voice "Fine, if you're going to be a dick about it."
                    elif Girl.tag == "Laura":
                        Girl.voice "I've got stuff to do anyway."

                    $ leaving = True
                else:
                    if Girl.tag == "Rogue":
                        Girl.voice "Like hell I will."
                    elif Girl.tag == "Laura":
                        Girl.voice "Not until I see what you have planned here."
            "Ok, never mind.":
                pass

    if leaving:
        call remove_Girl(Girl)

    return

label Girls_arrive(arriving_Girls):
    if arriving_Girls in all_Girls:
        $ arriving_Girls = [arriving_Girls]

    $ arriving_Girls = sort_Girls_by_approval(arriving_Girls)

    call add_Girls(arriving_Girls)

    python:
        for G in arriving_Girls:
            if G.tag == "Rogue":
                G.voice("Hey, [G.player_petname].")
            elif G.tag == "Laura":
                G.voice("Hey.")

        for G in active_Girls:
            if G in Nearby:
                G.location = "nearby"

    return

label Girl_leaves(Girl):
    if not approval_check(Girl, threshold = 70):
        if Girl.destination == "bg_campus":
            if Girl.tag == "Rogue":
                Girl.voice "I'm going to hang out on campus, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I'm taking a nap in the quad."
        elif Girl.destination == "bg_player":
            if Girl.tag == "Rogue":
                Girl.voice "I'll be heading to your room, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I'm gonna hang out in your room for a bit."
        elif Girl.destination == Girl.home:
            if Girl.tag == "Rogue":
                Girl.voice "I'm heading back to my room, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I'm headed back to my room."
        elif Girl.destination == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.voice "I'm headed to class right now, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I've got class."
        elif Girl.destination == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.voice "I'm hitting the Danger Room, [Girl.player_petname]."
            elif Girl.tag == "Laura":
                Girl.voice "I'm hitting the Danger Room."
        elif Girl.destination == "bg_pool":
            if Girl.tag == "Rogue":
                Girl.voice "I'm headed for the pool."
            elif Girl.tag == "Laura":
                Girl.voice "I was hitting the pool."
        elif Girl.destination == "bg_shower":
            if approval_check(Girl, threshold = 140):
                if Girl.tag == "Rogue":
                    Girl.voice "I'm hitting the showers, later."
                elif Girl.tag == "Laura":
                    Girl.voice "I'm hitting the showers, later."
            else:
                if Girl.tag == "Rogue":
                    Girl.voice "I'm . . . headed out, see you later."
                elif Girl.tag == "Laura":
                    Girl.voice "I'm headed out."
        else:
            if Girl.tag == "Rogue":
                Girl.voice "I'm headed out, see you later."
            elif Girl.tag == "Laura":
                Girl.voice "I'm headed out, later."

        call hide_Girl(Girl)

        return

    if Girl.destination == "bg_campus":
        if Girl.tag == "Rogue":
            Girl.voice "I'm going to hang out on campus, [Girl.player_petname], want to hang with me?"
        elif Girl.tag == "Laura":
            Girl.voice "I'm taking a nap on the quad, you want in?"
    elif Girl.destination == "bg_player":
        if Girl.tag == "Rogue":
            Girl.voice "I'll be heading to your room, [Girl.player_petname]."
        elif Girl.tag == "Laura":
            Girl.voice "I'm going to hang out in your room for a bit, you coming?"
    elif Girl.destination == Girl.home:
        if Girl.tag == "Rogue":
            Girl.voice "I'm heading back to my room, [Girl.player_petname], want to swing by?"
        elif Girl.tag == "Laura":
            Girl.voice "I'm headed back to my room, you want in?"
    elif Girl.destination == "bg_classroom":
        if Girl.tag == "Rogue":
            Girl.voice "I'm headed to class right now, [Girl.player_petname], you could join me."
        elif Girl.tag == "Laura":
            Girl.voice "I've got class, want in?"
    elif Girl.destination == "bg_dangerroom":
        if Girl.tag == "Rogue":
            Girl.voice "I'm hitting the Danger Room, [Girl.player_petname], care to join me?"
        elif Girl.tag == "Laura":
            Girl.voice "I've got some Danger Room time, want in?"
    elif Girl.destination == "bg_pool":
        if Girl.tag == "Rogue":
            Girl.voice "I'm headed for the pool. Wanna come?"
        elif Girl.tag == "Laura":
            Girl.voice "I was hitting the pool. Wanna come?"
    elif Girl.destination == "bg_shower":
        if approval_check(Girl, threshold = 160):
            if Girl.tag == "Rogue":
                Girl.voice "I'm hitting the showers, [Girl.player_petname], care to join me?"
            elif Girl.tag == "Laura":
                Girl.voice "I'm hitting the showers, you could use one too."
        else:
            if Girl.tag == "Rogue":
                Girl.voice "I'm hitting the showers, [Girl.player_petname], maybe we could touch base later."
            elif Girl.tag == "Laura":
                Girl.voice "I'm hitting the showers, see you later."

            return
    else:
        if Girl.tag == "Rogue":
            Girl.voice "Why don't you come with me, [Girl.player_petname]?"
        elif Girl.tag == "Laura":
            Girl.voice "Wanna join me?"

    $ D20 = renpy.random.randint(1, 20)

    menu:
        extend ""
        "Sure, I'll catch up.":
            $ line = "go to"
        "Nah, we can talk later.":
            if Girl.tag == "Rogue":
                Girl.voice "Oh, ok. Talk to you later then."
            elif Girl.tag == "Laura":
                Girl.voice "Sure, whatever."

            $ line = None
        "Could you please stay with me? I'll get lonely.":
            if approval_check(Girl, "L", 60) or approval_check(Girl, threshold = 140):
                $ line = "lonely"
            else:
                $ line = "no"
        "Come on, it'll be fun.":
            if approval_check(Girl, "L", 40) and approval_check(Girl, threshold = 80):
                $ line = "fun"
            else:
                $ line = "no"
        "No, stay here.":
            if Girl.tag == "Rogue":
                Girl.voice "I don't know who you think you are, boss'in me around like that."
                Girl.voice "If you want to see me, you know where to find me."
            elif Girl.tag == "Laura":
                Girl.voice "Don't tell me what to do."
                Girl.voice "I'm out of here."

            $ line = None

    if not line:
        call hide_Girl(Girl)

        return
    elif line == "no":
        if Girl.destination == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.voice "I seriously can't, [Girl.player_petname], big test coming up."
            elif Girl.tag == "Laura":
                Girl.voice "I really can't miss this one."
        elif Girl.destination == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.voice "Wish I could, [Girl.player_petname], but I need to get some hours in."
            elif Girl.tag == "Laura":
                Girl.voice "Sorry [Girl.player_petname], but I'm going a little stir crazy."
        else:
            if Girl.tag == "Rogue":
                Girl.voice "I'm sorry, [Girl.player_petname], but I'm kinda busy right now."
            elif Girl.tag == "Laura":
                Girl.voice "Sorry, I have stuff to do."

        call hide_Girl(Girl)

        return
    elif line == "go to":
        call hide_Girl(Girl)

        if Girl.destination == "bg_campus":
            if Girl.tag == "Rogue":
                Girl.voice "Let's head over there."
            elif Girl.tag == "Laura":
                Girl.voice "Ok, nice."
        elif Girl.destination == "bg_player":
            if Girl.tag == "Rogue":
                Girl.voice "I'll be waiting."
            elif Girl.tag == "Laura":
                Girl.voice "Good."
        elif Girl.destination == Girl.home:
            if Girl.tag == "Rogue":
                Girl.voice "I'll meet you there."
            elif Girl.tag == "Laura":
                Girl.voice "Ok."
        elif Girl.destination == "bg_classroom":
            if Girl.tag == "Rogue":
                Girl.voice "See you then!"
            elif Girl.tag == "Laura":
                Girl.voice "Ok, get a move on then."
        elif Girl.destination == "bg_dangerroom":
            if Girl.tag == "Rogue":
                Girl.voice "I'll be warming up!"
            elif Girl.tag == "Laura":
                Girl.voice "I'll get warmed up."
        elif Girl.destination == "bg_pool":
            if Girl.tag == "Rogue":
                Girl.voice "Let's head over there."
            elif Girl.tag == "Laura":
                Girl.voice "Cool."
        elif Girl.destination == "bg_shower":
            if Girl.tag == "Rogue":
                Girl.voice "I guess I'll see you there."
            elif Girl.tag == "Laura":
                Girl.voice "Ok, nice."

        call hide_all

        $ Player.traveling = False

        if Girl.destination == "bg_campus":
            jump campus
        elif Girl.destination == "bg_player":
            jump player_room
        elif Girl.destination == Girl.home:
            $ Girl = Girl

            jump girls_room
        elif Girl.destination == "bg_classroom":
            jump classroom
        elif Girl.destination == "bg_dangerroom":
            jump danger_room
        elif Girl.destination == "bg_pool":
            jump pool
        elif Girl.destination == "bg_mall":
            jump mall
        elif Girl.destination == "bg_shower":
            jump shower_room
    elif line == "lonely":
        if Girl.tag == "Rogue":
            Girl.voice "Oh, how could I say \"no\" to you, [Girl.player_petname]?"
        elif Girl.tag == "Laura":
            Girl.voice "Well, I guess you should never go alone. . ."

    if Girl.tag == "Rogue":
        Girl.voice "I can stay for a bit."
    elif Girl.tag == "Laura":
        Girl.voice "I'll stick around."

    $ Girl.destination = Player.location

    return
