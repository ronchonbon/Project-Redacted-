label kiss_narrations(Girl, speed):
    if Girl.permanent_History["kiss"] > 10 and Girl.love >= 700:
        $ lines = [
            "She hungrily presses her lips against yours.",
            "She confidently presses her lips against yours.",
            "Her lips part as you hold her close.",
            "You nibble her neck as she groans in pleasure.",
            "You squeeze her tightly as your tongues jostle.",
            "Her tongue dances around yours.",
            "She nibbles your ear as her hands slide across your back.",
            "Your hands slide down her body as your lips press hers."]
    elif Girl.permanent_History["kiss"] > 5 or Girl == EmmaX:
        $ lines = [
            "She confidently presses her lips against yours.",
            "You softly kiss her plump lips.",
            "Her lips part as you hold her close.",
            "You nibble her neck as she coos in pleasure.",
            "You squeeze her tightly as your lips connect.",
            "Her tongue flickers out to meet yours.",
            "Your hands slide down her body as your lips brush hers."]
    else:
        $ line = [
            "She tentatively presses her lips against yours.",
            "You softly kiss her plump lips.",
            "Her lips part slightly as you hold her close.",
            "You squeeze her tightly as your lips connect.",
            "Your hands slide down her body as your lips brush hers."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label handjob_narrations(Girl, speed):
    if not speed:
        "[Girl.name] holds your cock in her hand."

        if Girl.permanent_History["handjob"] > 2:
            "She just seems to be enjoying the feel of it."
        else:
            "She just seems to be looking it over."

        return
    else:
        if speed < 2:
            $ lines = [
                "[Girl.name] lightly strokes the shaft, fingers sliding along the vein.",
                "[Girl.name] grasps the shaft firmly, and slowly slides along its length.",
                "[Girl.name]'s hand slides slowly down your shaft."]
        else:
            $ lines = [
                "[Girl.name] strokes the shaft vigorously, lightly touching the tip.",
                "[Girl.name] lightly strokes the shaft, fingers sliding along the vein."]

        $ line = renpy.random.choice(lines)

        "[line]"

    if Girl in [EmmaX, LauraX, StormX]:
        if speed < 2:
            $ lines = [
                "Her movements have become masterful, her slightest touch starts you twitching.",
                "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here.",
                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years.",
                "You can't tell where she is at any moment, all you know is that it works."]
        else:
            $ lines = [
                "Her movements have become masterful, her slightest touch starts you twitching.",
                "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here.",
                "Her expert strokes will have you boiling over in seconds.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, you can tell she's had plenty of practice.",
                "You can't tell where she is at any moment, all you know is that it works."]
    elif Girl.permanent_History["handjob"] > 4:
        if speed < 2:
            $ lines = [
                "Her movements have become almost masterful, her slightest touch starts you twitching.",
                "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years.",
                "You can't tell where she is at any moment, all you know is that it works."]
        else:
            $ lines = [
                "Her movements have become almost masterful, her slightest touch starts you twitching.",
                "She gently blows across the tip as her finger dance along the shaft. It's getting a bit hot in here.",
                "She's becoming something of an expert, making up for years of lost time.",
                "Her expert strokes will have you boiling over in seconds.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years.",
                "You can't tell where she is at any moment, all you know is that it works."]
    elif 2 < Girl.permanent_History["handjob"] <= 4:
        if speed < 2:
            $ lines = [
                "She's begining to figure things out, her fingers cause tingles as they caress the shaft.",
                "She's still learning, but learning fast. Her hands sure are smooth.",
                "She has a smooth motion going now, gentle and precise.",
                "Her lessons are paying off, she's really becoming very talented at this.",
                "She gently caresses the shaft, and cups the balls in her other hand, giving them a warm massage."]
        else:
            $ lines = [
                "She's begining to figure things out, her fingers cause tingles as they caress the shaft.",
                "She's still learning, but learning fast. Her hands sure are smooth.",
                "Her hands glide smoothly across your cock.",
                "She has a smooth motion going now, gentle and precise.",
                "Her lessons are paying off, she's really becoming very talented at this.",
                "She quickly strokes your cock, with a very deft pressure."]
    else:
        if speed < 2:
            $ lines = [
                "She makes up for her inexperience with determination, carefully stroking your cock.",
                "She moves her hands up and down the shaft. She's a little rough at this, but at least she tries.",
                "She strokes you gently. She isn't quite sure what to make of the balls.",
                "Her fingers fumble with your shaft a bit.",
                "She squeezes one of your balls too tightly, but stops when you wince.",
                "She has a firm grip, and she's not letting go. This may take a few tries."]
        else:
            $ lines = [
                "She really wasn't prepared for speeding up, and your cock often slips out of her hand.",
                "She rapidly moves her hands up and down the shaft. She's a little rough at this, but at least she tries.",
                "She strokes you a bit too quickly, the friction is a bit uncomfortable.",
                "Her fingers fumble with your shaft a bit.",
                "She squeezes one of your balls too tightly, but stops when you wince.",
                "She has a firm grip, and she's not letting go. This train is out of control."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label footjob_narrations(Girl, speed):
    "[Girl.name] strokes your cock with her feet."

    if not speed:
        if Girl.permanent_History["footjob"] > 2:
            "She just seems to be enjoying the feel of it."
        else:
            "She just seems to be looking it over."

        return
    elif Girl.permanent_History["footjob"] > 4:
        if speed < 2:
            $ lines = [
                "Her movements have become almost masterful, her slightest touch starts you twitching.",
                "She slowly caresses you in a way that makes your blood boil, then pulls back at the last second.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years.",
                "You can't tell where she is at any moment, all you know is that it works."]
        else:
            $ lines = [
                "Her movements have become almost masterful, her slightest touch starts you twitching.",
                "Her expert strokes will have you boiling over in seconds.",
                "She knows what to do now, and rubs your cock with smooth strokes, focusing occasionally on the head.",
                "She moves very smoothly, stroking casually and very gently, like she's been doing this for years.",
                "You can't tell where she is at any moment, all you know is that it works."]
    elif Girl.permanent_History["footjob"] > 4:
        if speed < 2:
            $ lines = [
                "She's begining to figure things out, her toes cause tingles as they caress the shaft.",
                "She's still learning, but learning fast.",
                "She has a smooth motion going now, gentle and precise.",
                "Her lessons are paying off, she's really becoming very talented at this.",
                "She gently caresses the shaft, and brushes the balls in her other foot, giving them a light massage."]
        else:
            $ lines = [
                "She's begining to figure things out, her toes cause tingles as they caress the shaft.",
                "She's still learning, but learning fast.",
                "Her feet glide smoothly across your cock.",
                "She has a smooth motion going now, gentle and precise.",
                "Her lessons are paying off, she's really becoming very talented at this.",
                "She quickly strokes your cock, with a very deft pressure."]
    else:
        if speed < 2:
            $ lines = [
                "She makes up for her inexperience with determination, carefully stroking your cock.",
                "She moves her feet up and down the shaft. She's a little rough at this, but at least she tries.",
                "She strokes you gently. She isn't quite sure what to do with the balls.",
                "Her toes fumble with your shaft a bit.",
                "She nudges one of your balls too tightly, but stops when you wince.",
                "She has a firm grip, and she's not letting go. This may take a few tries."]
        else:
            $ lines = [
                "She really wasn't prepared for speeding up, and your cock often slips between her feet.",
                "She rapidly moves her feet up and down the shaft. She's a little rough at this, but at least she tries.",
                "She strokes you a bit too quickly, the friction is a bit uncomfortable.",
                "Her toes fumble with your shaft a bit.",
                "She nudges one of your balls too tightly, but stops when you wince.",
                "She has a firm grip, and she's not letting go. This train is out of control."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label titjob_narrations(Girl, speed):
    if not speed:
        if Girl == KittyX:
            "[Girl.name] begins to rub her chest against you."
        elif Girl.permanent_History["titjob"] > 2:
            "[Girl.name] begins to bounce her breasts up and down."
        else:
            "[Girl.name] squeezes her breasts together and slowly moves them along your shaft."

        $ Girl.primary_Action.speed += 1

        return

    if Girl in [EmmaX, StormX] or (Girl.permanent_History["titjob"] > 4 and Girl.permanent_History["blowjob"]):
        if speed < 2:
            $ lines = [
                f"{Girl.name} rocks her breasts up and down around your cock.",
                f"{Girl.name} lightly licks the head as it pops up between her tits.",
                f"{Girl.name} has a smooth motion going now, gentle and precise.",
                f"{Girl.name} pauses to rub her nipples across the shaft.",
                f"In between strokes, {Girl.name} gently sucks on the head.",
                f"{Girl.name} drips some spittle down to make sure you're properly lubed.",
                f"{Girl.name} gently caresses the shaft between her tits."]
        else:
            $ lines = [
                f"{Girl.name} rapidly rocks her breasts up and down around your cock.",
                f"{Girl.name} licks away at the head every time it pops up between her tits.",
                f"{Girl.name} has a smooth motion going now, quick by efficient.",
                f"{Girl.name} dances her nipples across the shaft.",
                f"In as she strokes faster and faster, {Girl.name} bends down to suck on the head.",
                f"{Girl.name} covers her tits with drool to keep them well lubed.",
                f"{Girl.name} rapidly caresses the shaft between her tits."]
    elif Girl.permanent_History["titjob"] > 1:
        if speed < 2:
            $ lines = [
                f"{Girl.name} juggles her breasts up and down around your cock.",
                f"{Girl.name} lightly strokes the head as it pops up between her tits.",
                f"{Girl.name} has a smooth motion going now, gentle and precise.",
                f"{Girl.name} pauses to rub her nipples across the shaft.",
                f"{Girl.name} gently caresses the shaft between her tits."]
        else:
            $ lines = [
                f"{Girl.name} rapidly juggles her breasts up and down around your cock.",
                f"{Girl.name} lightly brushes the head with her chin as it pops up between her tits.",
                f"{Girl.name} moves them up and down in a fluid rocking motion.",
                f"{Girl.name} bounces her whole body up and down.",
                f"{Girl.name} rapidly slides the shaft between her tits."]
    else:
        if speed < 2:
            $ lines = [
                f"{Girl.name} sort of squishes her breasts back and forth around your cock.",
                f"{Girl.name} slides the cock up and down between her cleavage.",
                f"{Girl.name} kind of bounces her tits around your cock.",
                f"{Girl.name} smooshes her cleavage as tight as she can and rubs up and down."]
        else:
            $ lines = [
                f"{Girl.name} sort of bounces her breasts off your cock.",
                f"{Girl.name} tries to quickly slide the cock up and down between her cleavage, but it tends to slide out.",
                f"{Girl.name} slaps her tits against your dick.",
                f"{Girl.name} smooshes her cleavage as tight as she can and rubs up and down quite quickly."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label blowjob_narrations(Girl, speed):
    if not speed:
        if Girl.permanent_History["blowjob"] > 2:
            "[Girl.name] stares at your cock. She seems pretty excited about it."
        elif Girl == EmmaX:
            "[Girl.name] stares at your cock. She seems pretty intrigued by it."
        else:
            "[Girl.name] stares at your cock with trepidation."

        if Girl.permanent_History["blowjob"] < 2 or (Girl.devotion >= 500 and Girl.devotion > Girl.trust):
            "She seems to be waiting for some instruction."
        else:
            "She gets started licking your cock."

            $ Girl.primary_Action.speed += 1

        return
    elif speed == 1:
        "[Girl.name] licks your cock."
    else:
        "[Girl.name] sucks your cock."

    if speed == 1:
        if Girl.permanent_History["blowjob"] > 4 or Girl in [EmmaX, LauraX, StormX]:
            $ lines = [
                "Her deft licks are masterful, your cock twitches with each stroke.",
                "She gently blows across the head as she covers your cock in smooth licks.",
                "How many licks to the center of your cock? No way you're finding out.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She's really getting good at this, alternating between deep suction and gentle licks.",
                "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years.",
                "She puts the tip into her mouth and her tounge dances around it."]
        elif Girl.permanent_History["blowjob"] > 1:
            $ lines = [
                "She's begining to figure things out, her tongue makes your hair stand on end.",
                "She's still learning, but learning fast. She seems eager to use her mouth for more than talk.",
                "She's settled into a gentle licking pace that washes over you like a warm bath.",
                "She licks gently up and down the shaft. She's a little rough at this, but at least she tries.",
                "Her tongue moves carefully along the shaft.",
                "She's really starting to learn some clever tricks to making you feel good.",
                "She licks her way down the shaft, and gently teases the balls."]
        else:
            $ lines = [
                "She makes up for her inexperience with determination, carefully licking your cock.",
                "She takes a small lick and grimaces at the taste.",
                "She tentatively kisses around the head a bit.",
                "She nibbles one of your balls, but stops when you wince.",
                "She licks all over your dick, but she doesn't really have a handle on it."]
    elif speed == 2:
        if Girl.permanent_History["blowjob"] > 4 or Girl in [EmmaX, LauraX, StormX]:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She rapidly bobs up and down on your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the tip into her mouth and her tounge swirls rapidly around it."]
        elif Girl.permanent_History["blowjob"] > 1:
            $ lines = [
                "She's begining to figure things out, she bobs carefully up and down the head.",
                "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip.",
                "Her lips envelope you like a warm bath as she bobs in and out.",
                "She's really starting to learn some clever tricks to making you feel good.",
                "She rapidly licks her way around the head.",
                "Her mouth envelopes the head, then she quickly draws it in and draws back with a pop."]
        else:
            $ lines = [
                "She really wasn't prepared for speeding up, and your cock often pops out of her mouth.",
                "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries.",
                "Her head bobs rapidly, until she goes a bit too deep and starts to gag.",
                "She lets her teeth get a bit too much action.",
                "She bobs quickly on your cock, but clamps down a bit too tight for comfort."]
    elif speed == 3:
        if Girl.permanent_History["blowjob"] > 4 or Girl in [EmmaX, LauraX, StormX]:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She smoothly bobs up and down on your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She gobbles you up all the way to the base, then quickly draws out and plunges back in.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the shaft into her mouth and her tounge swirls rapidly around it."]
        elif Girl.permanent_History["blowjob"] > 1:
            $ lines = [
                "She's begining to figure things out, she bobs carefully up and down the shaft.",
                "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip.",
                "Her lips envelope you like a warm bath as she bobs in and out.",
                "She slowly draws you in to the base of your cock, then pulls back at the last second.",
                "She's really starting to learn some clever tricks to making you feel good.",
                "She rapidly licks her way up and down the shaft as her mouth envelopes you.",
                "Her mouth envelopes the shaft, then she quickly draws it in and draws back with a pop."]
        else:
            $ lines = [
                "She really wasn't prepared for putting it all the way in, and grimaces at the taste.",
                "She puts the tip in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries.",
                "She sucks up and down your cock very quickly, but gets a bit dizzy and has to slow down.",
                "Her head bobs rapidly, until she goes a bit too deep and starts to gag.",
                "She lets her teeth get a bit too much action.",
                "She bobs quickly on your cock, but clamps down a bit too tight for comfort."]
    else:
        if Girl.permanent_History["blowjob"] > 4 or Girl in [EmmaX, LauraX, StormX]:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She rapidly bobs to the base of your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She gobbles you up all the way to the base, then quickly draws out and plunges back in.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the entire shaft into her mouth and her tounge swirls rapidly around it."]
        elif Girl.permanent_History["blowjob"] > 1:
            $ lines = [
                "She's begining to figure things out, she bobs carefully up and down the shaft.",
                "She's still learning, but learning fast. She keeps her teeth well clear, aside from a playful nip.",
                "Her lips envelope you like a warm bath as she bobs in and out.",
                "She slowly draws you in to the base of your cock, then pulls back at the last second.",
                "She's really starting to learn some clever tricks to making you feel good.",
                "She completely envelops the shaft with her throat.",
                "Her mouth envelopes the head, then she quickly draws it all the way in and draws back with a pop."]
        else:
            $ lines = [
                "She really wasn't prepared for going so deep, and gags a bit.",
                "She puts the whole shaft in her mouth and starts to actually suck in as hard as she can. She's a little rough at this, but at least she tries.",
                "She draws your cock into her mouth very qucikly, but gets a bit dizzy and has to slow down.",
                "Her head bobs rapidly, until she goes a bit too deep and starts to gag.",
                "She lets her teeth get a bit too much action.",
                "She bobs quickly on your cock, but clamps down a bit too tight for comfort."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return
