label kiss_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

    if Girl.permanent_History["kiss"] > 10 and approval_check(Girl, "love", 70):
        $ lines = [
            f"{Girl.name} hungrily presses her lips against yours.",
            f"{Girl.name} confidently presses her lips against yours.",
            f"{Girl.name}'s lips part as you hold her close.",
            f"You nibble {Girl.name}'s neck as she groans in pleasure.",
            f"You squeeze {Girl.name} tightly as your tongues jostle.",
            f"{Girl.name}'s tongue dances around yours.",
            f"{Girl.name} nibbles your ear as her hands slide across your back.",
            f"Your hands slide down {Girl.name}'s body as your lips press hers."]
    elif Girl.permanent_History["kiss"] > 5:
        $ lines = [
            f"{Girl.name} confidently presses her lips against yours.",
            f"You softly kiss {Girl.name}'s plump lips.",
            f"{Girl.name}'s lips part as you hold her close.",
            f"You nibble {Girl.name}'s neck as she coos in pleasure.",
            f"You squeeze {Girl.name} tightly as your lips connect.",
            f"{Girl.name}'s tongue flickers out to meet yours.",
            f"Your hands slide down {Girl.name}'s body as your lips brush hers."]
    else:
        $ lines = [
            f"{Girl.name} tentatively presses her lips against yours.",
            f"You softly kiss {Girl.name}'s plump lips.",
            f"{Girl.name}'s lips part slightly as you hold her close.",
            f"You squeeze {Girl.name} tightly as your lips connect.",
            f"Your hands slide down {Girl.name}'s body as your lips brush hers."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label handjob_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

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
                f"{Girl.name} lightly strokes the shaft, fingers sliding along the vein.",
                f"{Girl.name} grasps the shaft firmly, and slowly slides along its length.",
                f"{Girl.name}'s hand slides slowly down your shaft."]
        else:
            $ lines = [
                f"{Girl.name} strokes the shaft vigorously, lightly touching the tip.",
                f"{Girl.name} lightly strokes the shaft, fingers sliding along the vein."]

        $ line = renpy.random.choice(lines)

        "[line]"

    if Girl.permanent_History["handjob"] > 4:
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
    elif 2 < Girl.permanent_History["handjob"] < 5:
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

label footjob_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

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

label titjob_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

    if not speed:
        if Girl.permanent_History["titjob"] > 2:
            "[Girl.name] begins to bounce her breasts up and down."
        else:
            "[Girl.name] squeezes her breasts together and slowly moves them along your shaft."

        $ Girl.breast_Action.speed += 1

        return

    if Girl.permanent_History["titjob"] > 4 and Girl.permanent_History["blowjob"]:
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

label blowjob_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

    if not speed:
        if Girl.permanent_History["blowjob"] > 2:
            "[Girl.name] stares at your cock. She seems pretty excited about it."
        else:
            "[Girl.name] stares at your cock with trepidation."

        if Girl.permanent_History["blowjob"] < 2:
            "She seems to be waiting for some instruction."
        else:
            "She gets started licking your cock."

            $ Girl.mouth_Action.speed += 1

        return
    elif speed == 1:
        "[Girl.name] licks your cock."
    else:
        "[Girl.name] sucks your cock."

    if speed == 1:
        if Girl.permanent_History["blowjob"] > 4:
            $ lines = [
                "Her deft licks are masterful, your cock twitches with each stroke.",
                "She gently blows across the head as she covers your cock in smooth licks.",
                "How many licks to the center of your cock? No way you're finding out.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She's really getting good at this, alternating between deep suction and gentle licks.",
                "She moves very smoothly, tongue dancing casually and very gently, like she's been doing this for years.",
                "She puts the tip into her mouth and her tongue dances around it."]
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
        if Girl.permanent_History["blowjob"] > 4:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She rapidly bobs up and down on your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the tip into her mouth and her tongue swirls rapidly around it."]
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
        if Girl.permanent_History["blowjob"] > 4:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She smoothly bobs up and down on your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She gobbles you up all the way to the base, then quickly draws out and plunges back in.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the shaft into her mouth and her tongue swirls rapidly around it."]
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
        if Girl.permanent_History["blowjob"] > 4:
            $ lines = [
                "She masterfully bobs on your cock, and it twitches with each stroke.",
                "She rapidly bobs to the base of your cock, a frenzy of motion.",
                "She's becoming something of an expert, making up for years of lost time.",
                "She gobbles you up all the way to the base, then quickly draws out and plunges back in.",
                "She's really getting good at this, alternating between deep suction and quick licks across the head.",
                "She moves very smoothly, bobbing in and out like she's been doing this for years.",
                "She puts the entire shaft into her mouth and her tongue swirls rapidly around it."]
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

label sex_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

    if Girl.permanent_History["sex"] > 4:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You quickly grind back and forth inside {Girl.name}.",
                "You alternate between shallow rapid thrusts, and the occasional deep, slow one.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} grinds furiously back and forth along your cock."]
        else:
            $ lines = [
                f"{Girl.name} bumps slowly against your cock.",
                f"You thrust into {Girl.name} and she coos a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                "You alternate between long and slow thrusts, and the occasional quick one.",
                f"You slowly slide back and forth near {Girl.name}'s entrance.",
                f"{Girl.name} slides slowly back and forth along your cock, teasing you."]
    elif Girl.permanent_History["sex"] > 1:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You quickly grind back and forth inside {Girl.name}.",
                "You alternate between shallow rapid thrusts, and the occasional deep, slow one.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} grinds furiously back and forth along your cock."]
        else:
            $ lines = [
                f"{Girl.name} bumps slowly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                "You alternate between long and slow thrusts, and the occasional quick one.",
                f"You slowly slide back and forth near {Girl.name}'s entrance.",
                f"{Girl.name} slides slowly back and forth along your cock."]
    else:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock.",
                f"You thrust into {Girl.name} and she squeaks in pain.",
                f"You quickly grind back and forth inside {Girl.name} but she doesn't seem to have the rhythm down.",
                f"{Girl.name} bounces rapidly against your cock, occasionally popping out and having to stick it back in.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} moves rapidly back and forth along your cock, but seems a bit uncomfortable."]
        else:
            $ lines = [
                f"{Girl.name} bumps slowly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                "You alternate between long and slow thrusts, and the occasional quick one.",
                f"You slowly slide back and forth near {Girl.name}'s entrance.",
                f"{Girl.name} slides slowly back and forth along your cock."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return

label anal_narrations(Action):
    python:
        for Actor in Action.Actors:
            if Actor in all_Girls:
                Girl = Actor

                break

        speed = Action.speed

    if not speed:
        "She seems to be waiting for you to do something. . ."

        return
    elif speed < 2:
        "You continue to pound into [Girl.name]'s ass. "
    else:
        "You continue to push into [Girl.name]'s ass. "

    if Girl.permanent_History["anal"] >= 5:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You quickly grind back and forth inside {Girl.name}.",
                "You alternate between shallow rapid thrusts, and the occasional deep, slow one.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} grinds furiously back and forth along your cock."]
        else:
            $ lines = [
                f"{Girl.name} bumps slowly against your cock.",
                f"You thrust into {Girl.name} and she coos a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                "You alternate between long and slow thrusts, and the occasional quick one.",
                f"You slowly slide back and forth near {Girl.name}'s rim.",
                f"{Girl.name} slides slowly back and forth along your cock, teasing you."]
    elif Girl.used_to_anal:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You quickly grind back and forth inside {Girl.name}.",
                "You alternate between shallow rapid thrusts, and the occasional deep, slow one.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} grinds furiously back and forth along your cock."]
        elif speed:
            $ lines = [
                f"{Girl.name} bumps slowly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                "You alternate between long and slow thrusts, and the occasional quick one.",
                f"You slowly slide back and forth near {Girl.name}'s rim.",
                f"{Girl.name} slides slowly back and forth along your cock."]
    else:
        if speed > 1:
            $ lines = [
                f"{Girl.name} bounces rapidly against your cock but seems to be in pain.",
                f"You thrust into {Girl.name} and she squeaks in pain.",
                f"You quickly grind back and forth inside {Girl.name} but she doesn't seem to have the rhythm down.",
                f"{Girl.name} bounces rapidly against your cock, occasionally popping out and having to stick it back in.",
                f"You pound away at {Girl.name}.",
                f"{Girl.name} moves rapidly back and forth along your cock, but seems a bit uncomfortable."]
        elif speed:
            $ lines = [
                f"{Girl.name} grits her teeth and slides slowly against your cock.",
                f"You thrust into {Girl.name} and she squeaks a bit.",
                f"You slowly grind back and forth inside {Girl.name}.",
                f"You slowly slide back and forth near {Girl.name}'s rim.",
                f"{Girl.name} slides slowly back and forth along your cock."]

    $ line = renpy.random.choice(lines)

    "[line]"

    return
