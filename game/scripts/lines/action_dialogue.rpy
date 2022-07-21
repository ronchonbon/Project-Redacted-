label out_of_Actions_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Sorry {Girl.player_petname}, but I'm a bit worn out.",
            f"I'm a bit worn out right now {Girl.player_petname}, maybe later."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Sorry {Girl.player_petname}, but I'm a bit worn out.",
            f"I'm kinda tired right now {Girl.player_petname}, later?"]
    elif Girl.tag == "Emma":
        $ lines = [
            f"I'm sorry {Girl.player_petname} but I need a break.",
            f"I'm rather tired right now {Girl.player_petname}, rain check?"]
    elif Girl.tag == "Laura":
        $ lines = [
            "Maybe in a minute, I need a break.",
            f"Maybe later, {Girl.player_petname}."]
    elif Girl.tag == "Jean":
        $ lines = ["Gimme a minute, k?"]
    elif Girl.tag == "Storm":
        $ lines = [f"I am sorry {Girl.player_petname}, I need to take a break."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "I could use a short break first.",
            f"Maybe later, {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_sex_menu_not_multiaction_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["That's it. . . for now."]
    elif Girl.tag == "Kitty":
        $ lines = ["That's it. . . for now."]
    elif Girl.tag == "Emma":
        $ lines = ["That's all you get. . . for now."]
    elif Girl.tag == "Laura":
        $ lines = ["That's all. . . for now at least."]
    elif Girl.tag == "Jean":
        $ lines = ["That's all. . . for now at least."]
    elif Girl.tag == "Storm":
        $ lines = ["I think that you have had enough for the moment."]
    elif Girl.tag == "Jubes":
        $ lines = ["Ok, that should be plenty for now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_caught_or_angry_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["I don't want to deal with you right now."]
    elif Girl.tag == "Kitty":
        $ lines = ["I don't want to deal with you right now."]
    elif Girl.tag == "Emma":
        $ lines = ["I'd rather not deal with you at the moment."]
    elif Girl.tag == "Laura":
        $ lines = ["You really don't want to try me right now."]
    elif Girl.tag == "Jean":
        $ lines = ["You really don't want to try me right now."]
    elif Girl.tag == "Storm":
        $ lines = ["I do not want to deal with you right now."]
    elif Girl.tag == "Jubes":
        $ lines = ["I'm definitely not in the mood for you right now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_less_than_five_rounds_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["We've been at it for a while now, let's take a breather."]
    elif Girl.tag == "Kitty":
        $ lines = ["We've been at it for a while now, let's take a breather."]
    elif Girl.tag == "Emma":
        $ lines = ["I think we could both do with a short break."]
    elif Girl.tag == "Laura":
        $ lines = ["You're looking a bit worn out, maybe take a break."]
    elif Girl.tag == "Jean":
        $ lines = ["You're looking a bit worn out, maybe take a break."]
    elif Girl.tag == "Storm":
        $ lines = ["I think we could both do with a short break."]
    elif Girl.tag == "Jubes":
        $ lines = ["Hey, I could use a break, how 'bout you?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label generic_exit_sex_menu_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Huh? Ok."]
    elif Girl.tag == "Kitty":
        $ lines = ["Ok, fine."]
    elif Girl.tag == "Emma":
        $ lines = ["Fine."]
    elif Girl.tag == "Laura":
        $ lines = ["Ok, fine."]
    elif Girl.tag == "Jean":
        $ lines = ["Ok, fine."]
    elif Girl.tag == "Storm":
        $ lines = ["That is fine."]
    elif Girl.tag == "Jubes":
        $ lines = ["Sure, fine."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_first_round_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [f"Are you sure, {Girl.player_petname}? I could really use some company."]
    elif Girl.tag == "Kitty":
        $ lines = [f"Are you sure, {Girl.player_petname}? I wasn't exactly. . . finished."]
    elif Girl.tag == "Emma":
        $ lines = [f"Are you certain, {Girl.player_petname}? Are you perhaps forgetting something?"]
    elif Girl.tag == "Laura":
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could go another round. . . or two. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could go another round. . . or two. . ."]
    elif Girl.tag == "Storm":
        $ lines = [f"Are you certain, " + Girl.player_petname + "? Are you perhaps forgetting something?"]
    elif Girl.tag == "Jubes":
        $ lines = ["Are you sure, " + Girl.player_petname + "?{p}I could keep going. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_addicted_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["I still need a little. . . contact."]
    elif Girl.tag == "Kitty":
        $ lines = ["I need more touching."]
    elif Girl.tag == "Emma":
        $ lines = ["I need more contact."]
    elif Girl.tag == "Laura":
        $ lines = ["I need more contact."]
    elif Girl.tag == "Jean":
        $ lines = ["I need some more skin contact.{p}}You gonna leave me hanging?"]
    elif Girl.tag == "Storm":
        $ lines = ["I need your touch."]
    elif Girl.tag == "Jubes":
        $ lines = ["I'm a little drained, I need more contact."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_experienced_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [f"Don't leave me hang'in, {Girl.player_petname}."]
    elif Girl.tag == "Kitty":
        $ lines = ["I still need some more attention."]
    elif Girl.tag == "Emma":
        $ lines = ["I'm afraid that still wasn't enough."]
    elif Girl.tag == "Laura":
        $ lines = ["Aren't you forgetting something?"]
    elif Girl.tag == "Jean":
        $ lines = ["Hey, you'd better get me off here.{p}You gonna leave me hanging?"]
    elif Girl.tag == "Storm":
        $ lines = ["That was not enough to satisfy me."]
    elif Girl.tag == "Jubes":
        $ lines = ["Hey! Don't leave me hanging here."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_done_for_now_unsatisfied_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Way to leave a girl in the lurch. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["Rude!"]
    elif Girl.tag == "Emma":
        $ lines = ["Well! This might count against you next time."]
    elif Girl.tag == "Laura":
        $ lines = ["You'll regret that one."]
    elif Girl.tag == "Jean":
        $ lines = ["The die has been cast."]
    elif Girl.tag == "Storm":
        $ lines = ["Perhaps I need to teach you to be more generous."]
    elif Girl.tag == "Jubes":
        $ lines = ["Well, that sucks."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_done_for_now_satisfied_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Well, you did at least do your part. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["I guess I'll take what I can get. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["I suppose I'll have to blame myself as an educator."]
    elif Girl.tag == "Laura":
        $ lines = ["Selfish. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Booo. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Perhaps I need to teach you to be more generous."]
    elif Girl.tag == "Jubes":
        $ lines = ["So selfish. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_gave_it_a_shot_unsatisfied_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Way to leave a girl in the lurch. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["Rude!"]
    elif Girl.tag == "Emma":
        $ lines = ["Yes, disappointingly so. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Not a very good one."]
    elif Girl.tag == "Jean":
        $ lines = ["If that's what you want to call it. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["So that was the best you could achieve. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Well try again."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_gave_it_a_shot_satisfied_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Well, fair enough. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["I guess I'll take what I can get. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["I suppose you did. . . shame you couldn't do better. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Selfish. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Booo. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["So that was the best you could achieve. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["So selfish. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_did_my_part_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["I guess you did at that. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["Well. . . yeah, but. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["Take it as a compliment that I expected more."]
    elif Girl.tag == "Laura":
        $ lines = ["Well. . . yeah, but. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Stingy. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["I had hoped for better.  . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Yeah, but. . . keep doing that. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_out_of_semen_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Huh, can't be helped, I s'pose."]
    elif Girl.tag == "Kitty":
        $ lines = [f"Yeah, but {Girl.like}. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["I suppose that can't be helped. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Well, you could always try something else. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Your hands don't seem to be broken."]
    elif Girl.tag == "Storm":
        $ lines = ["Well, I cannot push you to breaking. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Well, you could always try something else. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_less_than_two_rounds_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Mmmm. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["Hehe. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["Excellent. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Good. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Good. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Thank you."]
    elif Girl.tag == "Jubes":
        $ lines = ["Cool. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_more_than_two_rounds_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Yeah, again. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["You know it. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["Always. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Always. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Always. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Always. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Yup. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label exit_sex_menu_girl_also_tired_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [f"I guess I'm a bit tuckered out too, {Girl.player_petname}. I guess we can take a breather."]
    elif Girl.tag == "Kitty":
        $ lines = ["I guess I'm kinda tired too, " + Girl.player_petname + ". We can take a break. . .{p}. . .for now."]
    elif Girl.tag == "Emma":
        $ lines = [f"I suppose I'm tired as well, {Girl.player_petname}. We can take a breather. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Yeah, you look like you've had enough. We can take a break. . .{p}}. . .for now."]
    elif Girl.tag == "Jean":
        $ lines = ["Ok, sounds good. . ."]
    elif Girl.tag == "Storm":
        $ lines = [f"I could use some rest as well, {Girl.player_petname}."]
    elif Girl.tag == "Jubes":
        $ lines = ["Sure, I guess we can take a little break. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sex_menu_cleanup_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = ["Oh?"]
    elif Girl.tag == "Kitty":
        $ lines = ["Huh?"]
    elif Girl.tag == "Emma":
        $ lines = ["Huh?"]
    elif Girl.tag == "Laura":
        $ lines = ["What?"]
    elif Girl.tag == "Jean":
        $ lines = ["What?"]
    elif Girl.tag == "Storm":
        $ lines = ["Oh, what do you mean?"]
    elif Girl.tag == "Jubes":
        $ lines = ["What?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label end_of_Action_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"Ok, {Girl.player_petname} that's enough of that for now."]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Time to take a little break, for now.",
            "Ok, we need to take a break.",
            "Ok, I'm kinda done for now, I need a break."]

        if Action_type == "blowjob":
            $ lines.append("Ok, I gotta rest my jaw for a minute. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "We need to stop for a moment, let me catch my breath.",
            f"All right, {Girl.player_petname}, that's plenty for now.",
            f"Ok, {Girl.player_petname}, that's enough of that for now.",
            "That's probably enough of that.",
            "Ok, that's enough, for now. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("Ok, seriously, I'm putting it down for a minute.")

            if Action_type == "blowjob":
                $ lines.append("Ok, I need to rest my jaw for a minute. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            f"Ok, {Girl.player_petname} breaktime.",
            "Ok, I'm kinda done for now, I need a break."]

        if Action_type in passive_Action_types:
            $ lines.append("Ok, I'm taking a quick break. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            f"Ok, {Girl.player_petname} time for a break.",
            "Ok, that's it, break time."]
    elif Girl.tag == "Storm":
        $ lines = [
            "I need to take a moment to collect myself.",
            "That is enough of that."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "Ok, that's it, I need a break.",
            f"{Girl.player_petname}, that will be enough for now."]

    Girl.voice "[line]"

    return

label ten_rounds_left_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["You might want to wrap this up, it's getting late."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"It's{Girl.like}getting kinda late.",
            "It's kind of time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl.tag == "Emma":
        $ lines = [
            "It's getting late. . .",
            "It's about time for a break.",
            "It's getting a bit late. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You might want to wrap this up, it's getting late.")
            $ lines.append("You might want to think about your endgame here. . .")
        elif Action_type in passive_Action_types:
            $ lines.append("I think I'll probably take a break soon.")
    elif Girl.tag == "Laura":
        $ lines = [
            "It's getting late, we should wrap this up.",
            "It's kinda time to get moving.",
            "We might want to wrap this up, it's getting late."]
    elif Girl.tag == "Jean":
        $ lines = ["Wow, look at the time. . ."]
    elif Girl.tag == "Storm":
        $ lines = [f"It is getting late, {Girl.player_petname}. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You might want to consider finishing. . .")
        elif Action_type in passive_Action_types:
            $ lines.append("I will probably take a break soon.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "I could use a break soon. . .",
            "Wow, look at the time. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label five_rounds_left_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Seriously, it'll be time to stop soon."]
    elif Girl.tag == "Kitty":
        $ lines = ["We should wrap this up.",
            f"For real{Girl.like}time's up.",
            "Seriously, it'll be time to stop soon."]
    elif Girl.tag == "Emma":
        $ lines = ["We should take a break soon.",
            "Seriously, it'll be time to stop soon.",
            "Do you mind if we take a break?",
            "We'll need a break soon."]

        if Action_type == "masturbation":
            $ lines.append("Ung, I'm almost finished. . .")
    elif Girl.tag == "Laura":
        $ lines = [f"Tick tock, {Girl.player_petname}."]

        if Action_type == "masturbation":
            $ lines.append("Five minutes, maybe.")
    elif Girl.tag == "Jean":
        $ lines = [f"We should probably wrap this up, {Girl.player_petname}.",
            "Ok, can we take a break?"]
    elif Girl.tag == "Storm":
        $ lines = ["We should take a break soon.",
            "We shall require a break soon."]

        if Action_type == "masturbation":
            $ lines.append("Ah! I am nearly finished. . .")
    elif Girl.tag == "Jubes":
        $ lines = [". . . I could really use a break here. . ."]

        if Action_type == "masturbation":
            $ lines.append("Five minutes, maybe.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label tired_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["I'm actually getting a little tired, so maybe we could wrap this up?"]
    if Girl.tag == "Kitty":
        $ lines = [
            "I'm actually getting a little tired, so maybe we could wrap this up?",
            "I kinda need a break, so if we could wrap this up?"]
    elif Girl.tag == "Emma":
        $ lines = [
            "Actually, could we wrap this up soon?",
            "I'm actually getting a little tired, perhaps we could wrap this up?"]
    elif Girl.tag == "Laura":
        $ lines = ["I need a break, can we wrap on this?"]
    elif Girl.tag == "Jean":
        $ lines = []
    elif Girl.tag == "Storm":
        $ lines = []
    elif Girl.tag == "Jubes":
        $ lines = []

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label pull_back_before_get_in_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        if Girl.permanent_History[action]:
            $ lines = [f"Well ok, {Girl.player_petname}, no harm done. Just give me a little warning next time.",
                f"Well ok, {Girl.player_petname}, it has been kinda fun."]
        else:
            $ lines = [f"Well ok, {Girl.player_petname}, I'm not really ready for that, but maybe if you ask nicely next time . . ."]

            if Action_type in anal_insertion_Action_types:
                $ lines.append(f"Well ok, {Girl.player_petname}, that's a bit dirty, maybe ask a girl?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label would_you_like_more_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["You maybe want to try something more?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label caught_masturbating_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"H- how long you been stand'in there, {Girl.player_petname}?"]
    elif Girl.tag == "Kitty":
        $ lines = ["Eeep!{p}When did you get here?!"]
    elif Girl.tag == "Emma":
        $ lines = ["!{p}How long have you been there?!"]
    elif Girl.tag == "Laura":
        $ lines = ["Huh.{p}}When did you get here?"]
    elif Girl.tag == "Jean":
        $ lines = ["Oh, hey. . ." + Girl.player_petname + ".{p}}When did you get here?"]
    elif Girl.tag == "Storm":
        $ lines = ["!{p}}How long have you been there?!"]
    elif Girl.tag == "Jubes":
        $ lines = ["Oh!{p}}How long were you standing there?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label notices_penis_is_out_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["And why is your cock out like that?!"]
    elif Girl.tag == "Kitty":
        $ lines = ["And um. . . your cock is out. . . "]
    elif Girl.tag == "Emma":
        $ lines = ["And I see you've been busy. . . "]
    elif Girl.tag == "Laura":
        $ lines = ["And um. . . you have your penis out. . . "]
    elif Girl.tag == "Jean":
        $ lines = ["I see you've been making yourself at home. . . "]
    elif Girl.tag == "Storm":
        $ lines = [". . . I notice you're taken care of yourself. . . "]
    elif Girl.tag == "Jubes":
        $ lines = ["And um. . . you have your penis out. . . "]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

label too_late_to_masturbate_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["It's getting too late to do much about it right now though."]
    elif Girl.tag == "Kitty":
        $ lines = ["It's getting kinda late to do anything about it. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["Unfortunately it's getting rather late."]
    elif Girl.tag == "Laura":
        $ lines = ["I kinda needed a break anyway. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["I could use a break anyway. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["It seems that it has gotten late while I was. . . distracted."]
    elif Girl.tag == "Jubes":
        $ lines = ["Well, I kinda needed a break anyway. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label begging_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Heh, I suppose I can hardly refuse ya when you use the magic words . . .",
            "Well, if you're gonna beg. . .",
            "No problem.",
            "Sure, I guess.",
            "Okay.",
            "I guess. . .",
            "Ok, [She gestures for you to come over].",
            "Heh, ok.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . give it a go.",
            "Heh, ok, ok.",
            "Well, sure, ahhhhhh.",
            "Well. . . ok.",
            "Heh, ok, alright."]

        if Action_type in cock_Action_types:
            $ lines.append("Ok, lemme see it.")
            $ lines.append("Sure. Drop trou.")
            $ lines.append("I suppose, whip it out.")
            $ lines.append("I guess I could. . . whip it out.")
            $ lines.append("Sure, put'im here.")

            if Action_type == "blowjob":
                $ lines.append("Fine. . . [She licks her lips].")
                $ lines.append("I guess a taste couldn't hurt.")
        elif Action_type == "masturbation":
            $ lines.append("I suppose it would help to have something nice to look at. . .")
            $ lines.append("I've kind of needed this anyways. . .",)
        elif Action_type == "suck_breasts":
            $ lines.append("You better work your mouth that hard on these.")
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Well{Girl.like}if you ask nicely. . .",
            "Only if you make it worth it.",
            "I like it when you beg. . .",
            "Well, sure, I guess.",
            "Well. . . ok.",
            "Heh, ok, fine.",
            "Sure, I guess.",
            "Ooooookay.",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok."]

        if Action_type in cock_Action_types:
            $ lines.append("Cool, lemme see it.")

            if Action_type == "blowjob":
                $ lines.append("Fiiine. . . [She licks her lips].")

        if Action_type in passive_Action_types:
            $ lines.append("I could maybe give it a try.")
            $ lines.append("I guess I could. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "Politeness can be rewarded. . .",
            "Oh, if you insist. . .",
            "I do enjoy hearing you beg. . .",
            "Well, I suppose.",
            "Well. . . ok.",
            "Hmph, ok, fine.",
            "Oh, I suppose.",
            "Fine. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Sure, I suppose.",
            "Fine.",
            "Hmm, ok.",
            "Huh. Ok.",
            "K.",
            "Sure, why not?",
            "Lol, ok."]

        if Action_type in cock_Action_types:
            $ lines.append("Very well, bring it out.")
            $ lines.append("Well, give it here.")

            if Action_type == "blowjob":
                $ lines.append("Fine. . . [She licks her lips].")
            elif Action_type == "hotdog":
                $ lines.append("Two birds with one stone. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I'll do it.")
            $ lines.append("I could perhaps give it a try.")
            $ lines.append("I suppose I could. . .")

            if Action_type == "masturbation":
                $ lines.append("Couldn't hurt having you around. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "Well if you're going to be a little bitch about it. . .",
            "Ok, fine. . .",
            "Oooh, beg for me. . .",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Sure, I guess.",
            "OK.",
            "Heh, ok, ok.",
            "Ok.",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

        if Action_type in cock_Action_types:
            $ lines.append("Sure, whip it out.")
            $ lines.append("Alright, let's see it.")
            $ lines.append("Fine, lemme see it.")

            if Action_type == "blowjob":
                $ lines.append("Ok. . . [She licks her lips].")

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
            $ lines.append("I guess I could. . .")

            if Action_type == "masturbation":
                $ lines.append("It couldn't hurt having you around. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            "Oh, fine, just don't start crying.",
            "Ok, fine. . .",
            "Oooh, beg for me. . .",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "Sure, I guess.",
            "Okay. . . ",
            "Fine.",
            "Ok. . . Get over here. . .",
            "Ok, ok.",
            "OK.",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Sure. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Sure, why not. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("Sure, whip it out.")
            $ lines.append("Alright, let's see it.")
            $ lines.append("Fine, lemme see it.")

            if Action_type == "blowjob":
                $ lines.append("Ok. . . [She licks her lips].")

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
            $ lines.append("I guess I could. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "Well, I suppose. . .",
            "Oh, if you insist. . .",
            "I suppose it does not hurt. . .",
            "I suppose it could not hurt. . .",
            "Well, one could not hurt. . .",
            "Well, I suppose.",
            "Well. . . ok.",
            "Hmph, ok, fine.",
            ". . . Fine. [She gestures for you to come over]",
            "Ok, ok.",
            "Hmm, I suppose.",
            "Fine.",
            "Hmm, ok.",
            "Once more?",
            "You enjoy watching me do that?"]

        if Action_type in cock_Action_types:
            $ lines.append("Very well, give it here.")
            $ lines.append("Very well, bring it out.")

            if Action_type == "blowjob":
                $ lines.append("Fine. . . [She licks her lips].")

        if Action_type in sex_Action_types or Action_type == "kiss":
            $ lines.append("Oh, I suppose we might.");

        if Action_type in passive_Action_types:
            $ lines.append("I could perhaps give it a try.")
            $ lines.append("I suppose that I could. . .")
            $ lines.append("I would do this.")

            if Action_type == "masturbation":
                $lines.append("You want me to take care of myself?")
                $lines.append("You enjoy watching me do that?")
                $lines.append("You really do like to watch.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Geeze, don't whine about it. . .",
            "Ok, fine. . .",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label please_not_good_enough_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"I'm afraid not this time, sorry {Girl.player_petname}."]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Um, still no.",
            "Nuh uh."]
    elif Girl.tag == "Emma":
        $ lines = [
            "This wasn't a \"tone\" issue.",
            "No."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Well if you're going to be a little bitch about it. . .",
            "No."]
    elif Girl.tag == "Jean":
        $ lines = [
            "No way.",
            "Oh, don't cry.",
            "No."]
    elif Girl.tag == "Storm":
        $ lines = [
            "No, thank you.",
            "No, I do not think so. . .",
            "It is not appropriate.",
            "No."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "Geeze, don't whine about it. . .",
            "No."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label Action_accepted_enthusiastically_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Oooooooh. . .",
            "God yes.",]

        if Action_type in insertion_Action_types:
            $ lines.append("Sure, get in there.")

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname} go ahead.")

            if Action_type == "fondle_breasts":
                $ lines.append(f"Ok {Girl.player_petname} come and get'em.")
            elif Action_type == "fondle_ass":
                $ lines.append("Sure, grab a cheek.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Ok, fiiiine.",
            "Ok, whatever.",
            "Mmmmmm.",
            "Oooooooh. . .",
            "Mmmmm. . .",
            "Wha. . ."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")
            $ lines.append("Ok, go for it.")

            if Action_type == "fondle_breasts":
                $ lines.append(f"Ok {Girl.player_petname}, come and get'em.")
    elif Girl.tag == "Emma":
        $ lines = [
            "Oh very well. . .",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "I can't exactly refuse. . .",
            "Mmm. . . naughty."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")

            if Action_type in fondle_Action_types:
                $ lines.append("That sounds lovely, ravish me.")
    elif Girl.tag == "Laura":
        $ lines = [
            "Sure, sounds fun.",
            "Sure.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Sure, sounds fun.",
            "Sure.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")
    elif Girl.tag == "Storm":
        $ lines = [
            "Oh very well. . .",
            "Mmmm, I could not refuse. . .",
            "Mmmmmm. . .",
            "I suppose that is reasonable. . .",
            "Mmm. . . naughty."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")
            $ lines.append("I would love that. . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Sure, sounds fun.",
            "Sure.",
            "Mmmm, I couldn't refuse. . .",
            "Mmmmmm. . .",
            "Yeah, ok. . .",
            "Mmm. . . naughty."]

        if Action_type in active_Action_types:
            $ lines.append(f"Ok {Girl.player_petname}, go ahead.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label alternative_rejected_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [
            "Ok, whatever.",
            "Ok, your loss."]
    elif Girl.tag == "Kitty":
        $ lines = ["Nah."]
    elif Girl.tag == "Emma":
        $ lines = [
            "Well, that's too bad.",
            "Pity."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Nah.",
            "Fine, be that way."]
    elif Girl.tag == "Jean":
        $ lines = [
            "Well then too bad, I guess.",
            "Too bad then."]
    elif Girl.tag == "Storm":
        $ lines = [
            "Well. That is unfortunate. . .",
            "That is unfortunate."]
    elif Girl.tag == "Jubes":
        $ lines = []

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label maybe_handjob_instead_lines(Girl):
    if Girl.permanent_History["handjob"]:
        if Girl.tag == "Rogue":
            $ lines = ["Maybe you'd settle for a handy?"]
        elif Girl.tag == "Kitty":
            $ lines = [
                "Maybe I could just use my hand?",
                f"Maybe you'd{Girl.like}settle for a handy?"]
        elif Girl.tag == "Emma":
            $ lines = [
                "I could just stroke you off, perhaps?",
                "Perhaps a handjob?"]
        elif Girl.tag == "Laura":
            $ lines = [
                "Couldn't I just use my hand again?{p}You seemed to like that.",
                "I could give you a handy?"]
        elif Girl.tag == "Jean":
            $ lines = ["I could give you a hand job?"]
        elif Girl.tag == "Storm":
            $ lines = [
                "I could just stroke you off, perhaps?",
                "Perhaps a handjob?"]
        elif Girl.tag == "Jubes":
            $ lines = []
    else:
        if Girl.tag == "Rogue":
            $ lines = ["I could maybe. . . [she makes a jerking motion with her hand]?"]
        elif Girl.tag == "Kitty":
            $ lines = ["I could maybe. . . [she makes a jerking motion with her hand]?"]
        elif Girl.tag == "Emma":
            $ lines = ["Would my hand be an adequate substitute?"]
        elif Girl.tag == "Laura":
            $ lines = ["I could maybe use my hand instead, how's that sound?"]
        elif Girl.tag == "Jean":
            $ lines = ["I could give you a hand job?"]
        elif Girl.tag == "Storm":
            $ lines = ["Would my hand be an adequate substitute?"]
        elif Girl.tag == "Jubes":
            $ lines = []

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label maybe_blowjob_instead_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [
            "I could just. . . blow you instead?",
            "I could maybe. . . you know, [she pushes her tongue against the side of her cheek]?"]
    elif Girl.tag == "Kitty":
        $ lines = [f"Could I{Girl.like}. . . blow you instead?"]
    elif Girl.tag == "Emma":
        $ lines = [
            "You seemed to enjoy blowjobs, would that work instead?",
            "Would you perhaps prefer a blowjob?"]
    elif Girl.tag == "Laura":
        $ lines = ["I could maybe blow you?"]
    elif Girl.tag == "Jean":
        $ lines = ["What about a blowjob then?"]
    elif Girl.tag == "Storm":
        $ lines = [
            "You seemed to enjoy blowjobs, would that work instead?",
            "Would you perhaps prefer a blowjob?"]
    elif Girl.tag == "Jubes":
        $ lines = []

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label first_Action_approval_mostly_devotion_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"If that's what you want, {Girl.player_petname}. . .",
            "If that's what you want. . .",
            "I suppose, if that's what you want. . .",
            f"Ok, {Girl.player_petname}, I'm ready."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"If you want, {Girl.player_petname}. . .",
            "I mean. . .",
            f"Ok by me, {Girl.player_petname}. .",
            f"If that's what you want, {Girl.player_petname}. . .",
            f"I suppose if it's you, {Girl.player_petname}. . .",
            "Well. . .",
            "If you want. . ."]

        if Action_type in passive_Action_types:
            $ lines.append("If you want me to. . .")
        elif Action_type in fondle_Action_types or Action_type == "massage":
            $ lines.append("You don't have to do that.")
    elif Girl.tag == "Emma":
        $ lines = [
            "Is that what gets you off?",
            f"If that's what you'd like, {Girl.player_petname}. . .",
            "If that's what you want. . .",
            f"If that's what you want, {Girl.player_petname}. . .",
            f"If you enjoy that, {Girl.player_petname}. . .",
            f"If you insist, {Girl.player_petname}. . .",
            f"If that's what you're into, {Girl.player_petname}. . .",
            "If that's what works for you. . ."]

        if Action_type in ["sex", "anal"]:
            $ lines.append("I expected we would get here at some point. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "Is that what gets you off?",
            f"If you want, {Girl.player_petname}. . .",
            "If you'd like that. . .",
            "If that's what you want. . .",
            "If that's what you're into. . .",
            f"If that's what you want, {Girl.player_petname}. . .",
            f"Yes, {Girl.player_petname}. . .",
            "I expected that. . .",
            "If that's what works for you. . ."]
    elif Girl.tag == "Jean":
        $ lines = [
            "Is that what gets you off?",
            "If you'd want that. . .",
            "If that's what you're into. . .",
            f"If that's what you want, {Girl.player_petname}. . .",
            f"If you want, {Girl.player_petname}. . .",
            f"Ok, {Girl.player_petname}. . .",
            "I expected that. . .",
            "Ok, we can start with that. . ."]

        if Action_type in passive_Action_types:
            $ lines.append("I could do that, I guess. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "That is what you want?",
            f"If that is what you want, {Girl.player_petname}. . .",
            "If that is what you want. . .",
            f"If you enjoy that, {Girl.player_petname}. . .",
            f"If that is what you wish, {Girl.player_petname}. . .",
            "If that is what works for you. . ."]

        if Action_type == "masturbation":
            $ lines.append(f"If you enjoy watching, {Girl.player_petname}. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("I expected we would get here at some point. . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Is that what gets you off?",
            "If that's what you're into. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label satisfied_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "That was. . . nice.",
            f"That was . . . real pleasant, {Girl.player_petname}.",
            f"I . . . really liked that, {Girl.player_petname}.",
            "Certainly different with someone else at the wheel.",
            "I. . . how'd I taste?",
            "That felt. . . interesting. . .",
            "Was. . . that something you liked?",
            "Well, it's really nice to finally be able to reach out and touch someone.",
            "That was a real interesting experience. . .",
            "Well, that was certainly interesting.",
            "That really wasn't half bad.",
            "Well I liked that. . .",
            "Well that was a bit rough. . .",
            f"That was . . . interesting {Girl.player_petname}. We'll have to do that again sometime.",
            f"That was pretty hot, {Girl.player_petname}, we'll have to do that again sometime.",
            f"That was really great, {Girl.player_petname}, we'll have to do that again sometime."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"I hope there was{Girl.like}enough to work with.",
            "I hope they were enough for you. . .",
            "I liked that.",
            "Your hand is. . . bigger than mine.",
            "Was it. . . good?",
            "Huh. . . um. . .",
            "That was odd. . .",
            "That was. . . good for you?",
            "It was so warm to the touch. . .",
            "That was kinda fun.",
            "Huh, that wasn't bad.",
            "Thanks for the extra hand. . .",
            "I could feel you down there. . .",
            f"I feel like I've been waiting{Girl.like}a million years for that.",
            "Anal. . . huh, who knew?",
            "Well, did that work for you?",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl.tag == "Emma":
        $ lines = [
            "I'm sure it exceeded your expectations. . .",
            "Delectable, weren't they.",
            "That was. . . pleasant.",
            "I do appreciate some rather. . . aggressive attention down there.",
            "I could really take advantage of your services more often. . .",
            "That was. . . nice. . .",
            "You certainly surprise me. . .",
            "That was. . . invigorating.",
            "What a lovely experience. . .",
            "Mmm, was that as good for you as it was for me?",
            "Hmm, better than I'd imagined. . .",
            "I appreciate the work you put in. . .",
            "Your cock was so warm . .",
            "I assume I rocked your entire world.",
            "You really took to that well.",
            "Was that enough for you?",
            "That was. . . engaging. . ."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Did you enjoy that?",
            "That was kinda nice.",
            "That was. . . interesting.",
            "You're really getting into the good stuff.",
            "That was a really good use of that tongue of yours.",
            "That was. . . nice. . .",
            "That was kinda wild. . .",
            "That was. . . interesting.",
            "That was kind of. . . pleasant. . .",
            "That was fun.",
            "Hey, whaddaya know, that wasn't bad.",
            "Thanks for the extra hand. . .",
            "Did you like that? . .",
            "I can tell, I was the best you've had.",
            "You seem to know your way around back there.",
            "Enough for you?",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl.tag == "Jean":
        $ lines = [
            "I bet you enjoyed that.",
            "Well that was fun.",
            "Well that was. . . something.",
            "Well, that was a nice surprise. . .",
            "You really put that tongue to work. . .",
            "That was. . . nice. . .",
            "That was. . . interesting.",
            "That was kinda fun. . .",
            "OK, that was fun.",
            "Mmm, yeah, that was as good as I expected. . .",
            "Thanks for the extra hand. . .",
            "Did you enjoy that? . .",
            "Blew your mind, uh?",
            "Hmmm, that was nice. . .",
            "I guess that could have gone worse. . .",
            "That was. . . interesting. . .",
            "Ouch. . ."]
    elif Girl.tag == "Storm":
        $ lines = [
            "That was quite fun. . .",
            "That was certainly enjoyable.",
            "Thank you for that.",
            "You certainly. . . reached some interesting places there. . .",
            "You really do have a talent for that. . .",
            "That was. . . nice. . .",
            "That one caught me by surprise. . .",
            "That was. . . certainly interesting. . .",
            "That was more enjoyable than I had expected. . .",
            "Mmm, I did quite enjoy that!",
            "Hmm, that certainly was enjoyable . .",
            "I appreciate the work you put in. . .",
            "That certainly was an interesting experience. . .",
            "I hope that was as enjoyable for you as it was for me.",
            "Was that satisfactory?",
            "That was. . . engaging. . ."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "Did you like that?",
            "That was kinda nice.",
            "That was. . . interesting.",
            "Wow. . . that was nice. . .",
            "You really give me a run for my money. . .",
            "That was. . . nice. . .",
            "That was kinda weird. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label was_that_enough_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Was that enough for you?",
            "Did you get your jollies?",
            "Did you like the taste?",
            "Well, I hope that got your rocks off.",
            "Did that work for you?",
            "Well, I hope that was enough for you.",
            "Ouch.",
            "Did you get what you needed here?",
            "Did you like that?"]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Not a disappointment, right?",
            "Did that satisfy you?",
            "Was that enough?",
            "Did you get what you needed?",
            "Well, did you like the taste?",
            "Did you like that?",
            "Well? Satisfied?",
            "Did that work for you?",
            "Did that work out for you?",
            "Well I hope you got something out of that.",
            "I hope you enjoyed that.",
            "Did that work out for you?",
            "I hope that was worth the wait.",
            "Ouch.",
            "I guess you got what you needed?",
            "Did you like that?"]
    elif Girl.tag == "Emma":
        $ lines = [
            "Well you certainly hit the jackpot.",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I suppose that worked out for both of us. . .",
            "Did you enjoy that?",
            "Was it everything you dreamed?",
            "Was it all you dreamed of?",
            "Was that sufficient?",
            "I hope that lived up to expectations.",
            "Was it all you dreamed of?",
            "Did you enjoy that?",
            "I hope you enjoyed that.",
            "Oooh.",
            "It's been a while."]
    elif Girl.tag == "Laura":
        $ lines = [
            "That worked out for you?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I suppose we both got something out of that. . .",
            "Was that good for you?",
            "Did that do it for you?",
            "Well I hope you got something out of that.",
            "I hope you enjoyed that.",
            "Did you like that?",
            "Satisfied?",
            "That was pleasant.",
            "Did you like that?"]
    elif Girl.tag == "Jean":
        $ lines = [
            "You get what you wanted out of that?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find what you were looking for?",
            "I guess that wasn't so bad. . .",
            "I bet you enjoyed that.",
            "Was that good for you?",
            "Pretty nice, right?",
            "I hope that worked out for you. . .",
            "Well, got what you wanted from that?",
            "Did that do it for you?",
            "That was great. . .",
            "Did you like that?"]
    elif Girl.tag == "Storm":
        $ lines = [
            "I expect you enjoyed that. . .",
            "Did you get enough?",
            "Ok, was that good?",
            "That was not so bad. . .",
            "Did you enjoy that?",
            "Did that work for you?",
            "Did that satisfy you?",
            "I hope that met your standards.",
            "Did that meet your expectations?",
            "I hope you found that satisfactory.",
            "Well. . .",
            "That was quite an experience. . ."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "That worked out for you?",
            "Did you get enough?",
            "Was that enough?",
            "Did you find anything in there?",
            "Well, that wasn't so bad. . .",
            "Did you like that?",
            "Was that good for you?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label get_out_lines(Girl):
    if Girl.tag == "Rogue":
        $ lines = [
            "I don't want to deal with you right now.",
            "Buzz off already.",
            "I really think you should leave."]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Nooope.",
            "GTFO.",
            "Go. Now."]
    elif Girl.tag == "Emma":
        $ lines = [
            "I haven't any time for this.",
            "Out.",
            "I think you should leave now."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Nope.",
            "Fuck off.",
            "Get out before we both regret it."]
    elif Girl.tag == "Jean":
        $ lines = ["Out!"]
    elif Girl.tag == "Storm":
        $ lines = [
            "Get out.",
            "Out. Now."]
    elif Girl.tag == "Jubes":
        $ lines = ["Out!"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_time_pussy_eaten_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"That's pretty intimate, {Girl.player_petname}. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_time_ass_eaten_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        if Girl.love >= Girl.devotion and Girl.love >= Girl.trust:
            Girl.voice "I'm not really sure I want you lick'in down there. . ."
        elif Girl.devotion >= Girl.trust:
            Girl.voice "You really don't have to if you don't want to."
        else:
            $ Girl.eyes = "_sexy"

            Girl.voice "Hmm. . . it's worth a shot. . ."

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_not_done_today_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"You could have been a bit more gentle last time, {Girl.player_petname}. . ."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"You could have been a bit more gentle last time, {Girl.player_petname}. . .",
            "That was kind of. . . rough last time?"]
    elif Girl.tag == "Emma":
        $ lines = ["Perhaps we can work up to that."]
    elif Girl.tag == "Laura":
        $ lines = [
            f"You could have been a bit more gentle last time, {Girl.player_petname}. . .",
            "Maybe eventually. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Maybe eventually. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Perhaps we could work up to that."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label anal_insertion_not_loose_done_today_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Sorry, I just need a little break back there, {Girl.player_petname}.",
            f"I'm still a little sore from earlier, {Girl.player_petname}."]
    elif Girl.tag == "Kitty":
        $ lines = [
            "I'm not really over the last time, but. . .",
            f"I'm still a little sore from earlier, {Girl.player_petname}.",
            f"I'm still{Girl.like}sore from earlier. . .",
            f"Sorry, I just need a little break back there, {Girl.player_petname}.",
            f"I'm{Girl.like}a little sore here?"]
    elif Girl.tag == "Emma":
        $ lines = ["Don't wear me out here."]
    elif Girl.tag == "Laura":
        $ lines = [
            "I'm still sore from earlier. . .",
            f"Sorry, I just need a little break back there, {Girl.player_petname}.",
            "Not right now."]
    elif Girl.tag == "Jean":
        $ lines = ["Not right now."]
    elif Girl.tag == "Storm":
        $ lines = ["Do not wear me out here."]
    elif Girl.tag == "Jubes":
        $ lines = [f"I'm still a little sore from earlier, {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label hard_cock_lines(Girl, Action_type):
    if Girl.tag == "Emma":
        $ lines = [f"My word {Girl.player_petname}, your member is hard enough to crack diamond. . . and I should know."]
    elif Girl.tag == "Laura":
        $ lines = ["Nice to see you're ready for business. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["I see you won't need any encouragement. . ."]
    elif Girl.tag == "Storm":
        $ lines = [f"I must say {Girl.player_petname}, you certainly do seem to be. . . excited."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_time_asking_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("You want me to get myself off, while you watch?")
        elif Action_type == "handjob":
            $ lines.append("You want me to rub your cock, with my hand?")
        elif Action_type == "footjob":
            $ lines.append("Huh, so like a handy, but with my feet?")
        elif Action_type == "titjob":
            $ lines.append("You want me to rub your cock with my breasts?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to put your dick. . . in my mouth?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("So, you'd like to take this to the next level? Actual sex? . . .")
        elif Action_type == "anal":
            $ lines.append("Wait, so you want to stick it in my butt?!")
        elif Action_type == "hotdog":
            $ lines.append("Wait, so you want to grind against my butt?!")
    elif Girl.tag == "Kitty":
        $ lines = ["I haven't really had much experience with this. . . "]

        if Action_type == "masturbation":
            $ lines.append("You want me to. . . touch myself?{p}And you're going to . . .watch?")
        elif Action_type == "handjob":
            $ lines.append("So you want a handy then?")
        elif Action_type == "footjob":
            $ lines.append("Huh, so you'd like me to touch your cock with my feet?")
        elif Action_type == "titjob":
            $ lines.append("You want to rub your cock against my. . . breasts?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to suck your dick?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("You want to go in the \"out\" door?!")
        elif Action_type == "hotdog":
            $ lines.append("So, just grinding against me?")

        if Action_type in ["sex", "anal"] or Action_type in dildo_Action_types:
            $ lines.append("You want to try and fit that. . .?")
    elif Girl.tag == "Emma":
        $ lines = [
            f"Hmm, are you sure you can handle that, {Girl.player_petname}?",
            "Hmm, are you sure you're really prepared for this? . . ",
            "Hmm, you don't take half measures. . ."]

        if Action_type == "masturbation":
            $ lines.append("So you enjoy a good show then. . .")
        elif Action_type == "footjob":
            $ lines.append(f"Mmm, so you're into feet then, {Girl.player_petname}?")
        elif Action_type == "blowjob":
            $ lines.append("So you'd like me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("Oooh, naughty boy. Anal?")
        elif Action_type == "hotdog":
            $ lines.append("You just want me to grind against you then?")

        if Action_type in ["handjob", "footjob", "titjob", "blowjob"]:
            $ lines.append("You'd like me to take care of that for you?")
    elif Girl.tag == "Laura":
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("So you want me to masturbate while you watch?")
        elif Action_type == "handjob":
            $ lines.append("Handjob, huh. . .")
        elif Action_type == "footjob":
            $ lines.append("Standard footjob?")
        elif Action_type == "titjob":
            $ lines.append("You want a titjob, huh?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to suck your cock?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("Huh, you wanna fuck me? . . ")
        elif Action_type == "anal":
            $ lines.append("Huh, anal?")
        elif Action_type == "hotdog":
            $ lines.append("What, just grinding?")

        if Action_type in ["sex", "anal"] or Action_type in dildo_Action_types:
            $ lines.append("You want to try and fit that. . .?")
    elif Girl.tag == "Jean":
        $ lines = ["I can't blame you. . ."]

        if Action_type == "masturbation":
            $ lines.append("Oh, so you want to watch while I get off?")
        elif Action_type == "handjob":
            $ lines.append("You want a handjob, hmm. . .")
        elif Action_type == "footjob":
            $ lines.apppend("Oh, a foot person, eh?")
        elif Action_type == "titjob":
            $ lines.append("Oh, you want me to put these to work. . .")
        elif Action_type == "blowjob":
            $ lines.append("Oh! You want me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "sex":
            $ lines.append("Oh, you wanna fuck . . ")
        elif Action_type == "anal":
            $ lines.append("Oh, you're into anal?")
        elif Action_type == "hotdog":
            $ lines.append("What, just grinding?")
    elif Girl.tag == "Storm":
        $ lines = [
            "Hmm, are you certain you are prepared for this? . . ",
            "Hmm, you don't take half measures. . ."]

        if Action_type == "masturbation":
            $ lines.append("Oh, so you like the watch? . .")
        elif Action_type == "handjob":
            $ lines.append("You would like me to jerk you off?")
        elif Action_type == "footjob":
            $ lines.append(f"Oh, you would like me to use my feet, {Girl.player_petname}?")
        elif Action_type == "blowjob":
            $ lines.append("You would like me to suck on your penis?")
        elif Action_type in dildo_Action_types:
            $ lines.append("Hmmm, so you'd like to try out some toys?")
        elif Action_type == "anal":
            $ lines.append("I am shocked! Anal?")
        elif Action_type == "hotdog":
            $ lines.append("You would just like to press against each other like this?")
        elif Action_type in breast_Action_types:
            $ lines.append(f"My breasts are really appealing to you, {Girl.player_petname}?")
    elif Girl.tag == "Jubes":
        $ lines = []

        if Action_type == "masturbation":
            $ lines.append("So you like watching me masturbate?")
        elif Action_type == "handjob":
            $ lines.append("Handjob, huh. . .")

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label auto_rejected_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Ah, ah, Just keep doing what you were doing, {Girl.player_petname}.",
            f"Hey, just keep doing what you were doing, {Girl.player_petname}.",
            f"Oh! No, no thank you, {Girl.player_petname}.",
            "Um, no, I'm not really. . . don't."]

        if Action_type in hand_Action_types:
            $ lines.append(f"Hands off the merchandise, {Girl.player_petname}.")
            $ lines.append(f"Hands off, {Girl.player_petname}.")

            if Action_type in finger_Action_types:
                $ lines.append(f"Keep it out of there, {Girl.player_petname}.")
                $ lines.append(f"Keep it outside, {Girl.player_petname}.")
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Nuh-uh, {Girl.player_petname}, get back to what you were doing.",
            "Oooo! Um, no, no thanks. No. . .",
            f"Whoa, back off, {Girl.player_petname}.",
            "Um, don't do that. . .",
            "Um, what do you think you're doing?",
            f"Hmm, kinda rude, {Girl.player_petname}."]

        if Action_type in hand_Action_types:
            $ lines.append(f"Hands off, {Girl.player_petname}.")

        if Action_type in ass_Action_types:
            $ lines.append(f"Um{Girl.like}what are you doing back there?!")

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append(f"Heh, keep it above the belt, {Girl.player_petname}.")

        if Action_type in insertion_Action_types:
            $ lines.append("Um, no take that out.")
    elif Girl.tag == "Emma":
        $ lines = [
            f"Whoa, back off, {Girl.player_petname}.",
            f"{Girl.player_petname}! Not now. . .",
            "Do you really think you can handle that?"]

        if Action_type in hand_Action_types:
            $ lines.append(f"Hands off, {Girl.player_petname}.")

        if Action_type in finger_Action_types:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if Action_type in mouth_Action_types:
            $ lines.append("I like where your head is at, so to speak, but perhaps hold off on that.")

        if Action_type in ass_Action_types:
            $ lines.append("Oh? What exactly are you doing back there?")

        if Action_type in fondle_Action_types:
            $ lines.append("Down boy, you were doing so well. . .")

        if Action_type in dildo_Action_types:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append(f"Perhaps we keep it above the waist, {Girl.player_petname}.")
        elif Action_type == "hotdog":
            $ lines.append(f"You might want to take a step back, {Girl.player_petname}?")
    elif Girl.tag == "Laura":
        $ lines = [
            f"Roll it back, {Girl.player_petname}. . .",
            f"Whoa, back off, {Girl.player_petname}.",
            f"{Girl.player_petname}! No. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append(f"Maybe we keep it above the waist, {Girl.player_petname}.")

            if Action_type == "eat_pussy":
                $ lines.append("Hey, good instincts, but maybe hold off?")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Oh? A backdoor intruder?")

        if Action_type in hand_Action_types:
            $ lines.append("Watch your hands, or lose them.")
            $ lines.append(f"Hands off, {Girl.player_petname}.")
        elif Action_type == "sex":
            $ lines.append("Oh, taking it all the way, are we?")
        elif Action_type == "hotdog":
            $ lines.append(f"You might want to take a step back, {Girl.player_petname}?")
    elif Girl.tag == "Jean":
        $ lines = [
            f"Not so fast, {Girl.player_petname}. . .",
            f"Hmmm, not yet, {Girl.player_petname}.",
            f"Ooo! Not right now, {Girl.player_petname}.",
            f"Whoa there, {Girl.player_petname}!"]

        if Action_type in dildo_Action_types:
            $ lines.append("Hey, what are you planning to do with that?!")

        if Action_type in below_Action_types:
            $ lines.append(f"Keep it above the waist, {Girl.player_petname}.")

        if Action_type in insertion_Action_types:
            $ lines.append("Just sticking it in?")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Sticking in the back?")
        elif Action_type == "hotdog":
            $ lines.append(f"Little close there, {Girl.player_petname}?")
    elif Girl.tag == "Storm":
        $ lines = [
            "Probably not, right now. . .",
            "Show some self control. . .",
            "Perhaps show some control. . .",
            f"You go too far, {Girl.player_petname}.",
            f"{Girl.player_petname}! Not now. . .",
            "Are you certain that is what you want?"]

        if Action_type in finger_Action_types:
            $ lines.append("Careful what you put in there, you may not get it back.")

        if Action_type in hand_Action_types:
            $ lines.append(f"Release me, {Girl.player_petname}.")

        if Action_type in dildo_Action_types:
            $ lines.append("Excuse yourself, what are you planning to do with that?!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Excuse me, what are you aiming at?")

        if Action_type in below_Action_types:
            $ lines.append(f"Perhaps we keep it above the waist, {Girl.player_petname}.")

            if Action_type == "eat_pussy":
                $ lines.append("I appreciate the intent, but this is not the time for it.")
        elif Action_type == "hotdog":
            $ lines.append(f"You are rather close, {Girl.player_petname}. . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            f"Cool your jets, {Girl.player_petname}. . .",
            f"Whoa, back off, {Girl.player_petname}.",
            f"{Girl.player_petname}! No. . ."]

        if Action_type in hand_Action_types:
            $ lines.append("Watch your hands, or lose them.")
            $ lines.append(f"Hands off, {Girl.player_petname}.")

        if Action_type in below_Action_types:
            $ lines.append(f"Maybe we keep it above the waist, {Girl.player_petname}.")

            if Action_type == "eat_pussy":
                $ lines.append("Hey, good instincts, but maybe hold off?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label recent_Action_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Mmm, again? Ok.",
            "Mmm, again? Ok, let's get to it.",
            "Again? Ok.",
            "Mmmm. . .",
            "I guess I have a bit more in me. . .",
            "Again? K."]

        if Action_type == "handjob":
            $ lines.append("Mmm, again? Let me flex my hand a bit. . .")
        elif Action_type == "footjob":
            $ lines.append("I don't want to wear them out. . .")
        elif Action_type == "titjob":
            $ lines.append("Mmm, again? Ok, let me get the girls ready.")
        elif Action_type == "blowjob":
            $ lines.append("Mmm, again? [stretches her jaw]")
        elif Action_type in sex_Action_types:
            $ lines.append("You want to go again? Ok.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I think I'm warmed up. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Mmm, again? Ok.",
            "Mmm, again?",
            "Mmmm. . .",
            "I guess I could give it another go. . .",
            "Prrr. . .",
            "Mmm, again? Ok, let's get to it."]

        if Action_type == "handjob":
            $ lines.append("You're giving me carpal tunnel. . .")
        elif Action_type == "footjob":
            $ lines.append("I'm getting foot cramps. . .")
        elif Action_type == "blowjob":
            $ lines.append("Mmm, again? [stretches her jaw]")
        elif Action_type in sex_Action_types:
            $ lines.append("Another round? {i}Fine.{/i}")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I guess I'm warmed up. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "Mmmm, again? I suppose. . .",
            "Oh! Back for more?",
            "Mmm, again? Ok, let's get to it.",
            "Again? Oh, very well.",
            "I still have some. . . work I could be doing. . .",
            "Mmmm. . .",
            "Alright."]


        if Action_type in passive_Action_types:
            $ lines.append("Well, I guess another wouldn't hurt. . .")

            if Action_type == "handjob":
                $ lines.append("I will need to grade papers later, you know. . .")
            elif Action_type == "footjob":
                $ lines.append("You know, heels are nightmare on the arches. . .")
            elif Action_type == "blowjob":
                $ lines.append("Mmm, again? [yawns]")
        elif Action_type in sex_Action_types:
            $ lines.append(f"Again? {Girl.player_petname}, you're insatiable!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am warmed up. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "I have built up some more tension. . .",
            "Mmmm. . .",
            "Again? Fine, whatever."]

        if Action_type == "handjob":
            $ lines.append("Hmm, another handy then. . .")
        elif Action_type == "blowjob":
            $ lines.append("Mmm, again? [yawns]")

        if Action_type in insertion_Action_types:
            $ lines.append("Sure, get in there.")

            if Action_type in anal_insertion_Action_types:
                $ lines.append("I am warmed up. . .")

        if Action_type in sex_Action_types:
            $ lines.append("Again? Your funeral.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Mmmm, again? I guess. . .",
            "Huh, again?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "More of that, huh. . .",
            "Mmmm. . .",
            "Ok, sure.",
            "Again? Fine, whatever."]

        if Action_type in passive_Action_types:
            $ lines.append("Well, I guess another wouldn't hurt. . .")
        elif Action_type in sex_Action_types:
            $ lines.append("Again? Your funeral.")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am warmed up. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "Mmmm, again? I suppose. . .",
            "You cannot get enough?",
            "Mmm, again?",
            "Mmm, again? Ok, let's get to it.",
            "I suppose so. . .",
            "Again? Oh, very well.",
            "I suppose that I was not. . . finished. . .",
            "Mmmm. . .",
            "Of course."]

        if Action_type in passive_Action_types:
            $ lines.append("I do not know if I have it in me. . .")
        elif Action_type in sex_Action_types:
            $ lines.append(f"Again? {Girl.player_petname}, you are a lion!")

        if Action_type in anal_insertion_Action_types:
            $ lines.append("I am properly stretched out. . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Mmmm, again? I guess. . .",
            "I have built up some more stress. . ."]

        if Action_type == "handjob":
            $ lines.append("Hmm, another handy then. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label daily_Action_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Didn't get enough earlier?",
            "Again? Oh, you're insatiable!",
            "Must be my lucky day!",
            "Mmm. . .",
            "Back again so soon?",
            "Another one?",
            "So you'd like another go?",
            "You can't stay away from this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Gimme some sugar, sugar.")
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("You do have a smooth touch. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Maybe not so hard this time though.")
            $ lines.append("Maybe not so rough this time though.")
            $ lines.append("I'm still a bit sore from earlier.")

            if Action_type == "anal":
                $ lines.append("You can't stay away from this booty. . .")

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("You sure know how to keep a girl satisfied. . .")
            $ lines.append("I'm still tingling a bit from earlier.")
            $ lines.append("Take it a bit gently, I'm still quivering from earlier.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")
            $ lines.append("It is nice to have an audience. . .")
        elif Action_type == "blowjob":
            $ lines.append("{i}I'm{/i} used to being the one sucking people dry. . .")
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("You're going to give me lockjaw.")
        elif Action_type == "titjob":
            $ lines.append("My tits are still a bit sore from earlier.")
        elif Action_type == "handjob":
            $ lines.append("My arm's still a bit sore from earlier.")
            $ lines.append("You're going to give me calluses.")
        elif Action_type == "footjob":
            $ lines.append("My feet are kinda sore from earlier.")
            $ lines.append("My feet are a bit sore from earlier.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Didn't get enough earlier?",
            "Meow.",
            "Another one?",
            "Huh? Again?",
            "I must have done something right.",
            "Mmm. . .",
            "Was it that good?",
            "You're really digging this. . .",
            "Back again so soon?",
            "So you'd like another round?",
            "You can't stay away from this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
                $ lines.append("Come'ere tasty.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Maybe not so rough this time though.")
            $ lines.append("You're going to make me sore.")
            $ lines.append("I'm still a bit sore from earlier.")
            $ lines.append("I'm still a little sore from earlier.")

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("You're going to wear me out.")
            $ lines.append("You're wearing me out here!")
            $ lines.append("Take it a bit gently, I'm still shaking from earlier.")
            $ lines.append("Take it easy though.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type == "eat_pussy":
                $ lines.append("What a girl wants. . .")
        elif Action_type == "masturbation":
            $ lines.append("I kinda liked the audience. . .")
        elif Action_type == "blowjob":
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("You're going to give me lockhee- . . . jaw.")
        elif Action_type == "titjob":
            $ lines.append("My tits are still kinda sore from earlier.")
        elif Action_type == "handjob":
            $ lines.append("You're going to give me calluses")
            $ lines.append("My hand's kinda sore from earlier.")
        elif Action_type == "footjob":
            $ lines.append("My feet are kinda sore from earlier.")
    elif Girl.tag == "Emma":
        $ lines = [
            "You didn't get enough earlier?",
            "Back again so soon?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Didn't get enough earlier?",
            "Back again?",
            "You'd like another round?",
            "I suppose I am irresistible. . .",
            "Back so soon?",
            "Huh? Again?",
            "Mmmm. . .",
            "Mmm. . .",
            "Come and get it.",
            "Another?",
            "I was that good?",
            "I must have done something right."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("Relax, gently. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Perhaps not so rough this time?")
            $ lines.append("I'm still a bit sore from earlier.")
            $ lines.append("I'm still a little sore from earlier.")

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append(f"You're wearing me out, {Girl.player_petname}.")
            $ lines.append("You're going to wear me out.")
            $ lines.append("Take it a bit gently, I'm still shaking from earlier.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type == "eat_pussy":
                $ lines.append("What a queen deserves. . .")
        elif Action_type == "masturbation":
            $ lines.append("I did enjoy the audience participation. . .")
        elif Action_type == "blowjob":
            $ lines.append("My jaw's still a bit sore from earlier.")
            $ lines.append("My jaw's still sore from our prior engagement.")
        elif Action_type == "titjob":
            $ lines.append("You're going to wear them out.")
        elif Action_type == "handjob":
            $ lines.append("I'd rather not get calluses.")
            $ lines.append("You're going to wear out my arm.")
            $ lines.append("My hand's a bit sore from earlier.")
            $ lines.append("My hand's rather sore from before.")
        elif Action_type == "footjob":
            $ lines.append("My feet are rather sore from earlier.")
    elif Girl.tag == "Laura":
        $ lines = [
            "You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right."
            "I do like this treatment. . .",
            "Mmm, you like that? . .",
            "Mmm. . .",
            "Another one?",
            "Mmmmmm.",
            "Get over here.",
            "Did you enjoy that?",
            "Didn't get enough earlier?",
            "I guess you want more.",
            "Back for more?",
            "I must be too good at this."
            "Again? Sure.",
            "You're really into this. . .",
            "Back again so soon?",
            "So you'd like another round?",
            "Back again?",
            "You'd like another round?",
            "I must be better than I thought."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type == "kiss":
                $ lines.append("Let me get some saliva going.")
            elif Action_type in hand_Action_types:
                $ lines.append("Chill. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("I'm still a bit sore from earlier.")

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it slow, I'm still shaking from earlier.")
            $ lines.append("Wear'in me out here.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("I liked having an audience. . .")
        elif Action_type == "titjob":
            $ lines.append("You're really working these puppies.")
        elif Action_type == "handjob":
            $ lines.append("I'm glad I don't grow calluses.")
            $ lines.append("Again the with handjobs, huh?")

        if sex_Action_types in Girl.recent_history:
            $ lines.append(f"Your funeral, {Girl.player_petname}.")
    elif Girl.tag == "Jean":
        $ lines = [
            "You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I do like this. . .",
            "Mmm, you like that? . .",
            "Mmm. . .",
            "MmMmmm. . .",
            "Oh, get over here.",
            "Did you enjoy that?",
            "Another one?",
            "Didn't get enough earlier?",
            "I guess you want more.",
            "Back for more?",
            "I must be too good at this.",
            "Back again?",
            "You'd like another round?",
            "I must be better than I thought.",
            "Back again so soon?",
            "So you'd like another round?",
            "Again? Sure.",
            "You're really into this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that's all you want?")

            if Action_type in hand_Action_types:
                $ lines.append("Chill. . .")
        elif Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it slow, I'm still shaking from earlier.")
            $ lines.append("You're wearing me out here.")
            $ lines.append("You're going to wear me out.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
        elif Action_type == "masturbation":
            $ lines.append("I do like having an audience. . .")
        elif Action_type == "titjob":
            $ lines.append("You're really working these babies.")
        elif Action_type == "handjob":
            $ lines.append("Again the with handjobs, huh?")

        if sex_Action_types in Girl.recent_history:
            $ lines.append(f"Your funeral, {Girl.player_petname}.")
    elif Girl.tag == "Storm":
        $ lines = [
            "You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "Mmm. . .",
            "You did not get enough earlier?",
            "Back so soon?",
            "Mmmm. . .",
            "Yes, let's.",
            "I must prepare myself.",
            "You did not get enough earlier?",
            "Another?",
            "Back again?",
            "You would like another round?",
            "I suppose that I can be irresistible. . .",
            "Did you not get enough earlier?",
            "Back again so soon?",
            "So you would like another round?",
            "You really are into this. . ."]

        if Action_type in hand_Action_types or Action_type in mouth_Action_types or Action_type == "hotdog":
            $ lines.append("Are you sure that is all you would want?")

            if Action_type in hand_Action_types:
                $ lines.append("Relax, gently. . .")
                $ lines.append("Gently. . . gently. . .")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Perhaps not so rough this time?")
            $ lines.append("I am still a bit sore from earlier.")
            $ lines.append("I am still rather sore from earlier.")

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types or Action_type in ["sex", "anal"]:
            $ lines.append("Take it a bit gently, I am still glowing from earlier.")
            $ lines.append("You're going to wear me out.")
            $ lines.append(f"You are wearing me out, {Girl.player_petname}.")
            $ lines.append(f"You are tiring me, {Girl.player_petname}.")

            if Action_type in dildo_Action_types:
                $ lines.append("Breaking out the toys again?")
            elif Action_type == "eat_pussy":
                $ lines.append("What a queen deserves. . .")
                $ lines.append("I did enjoy the audience participation. . .")
        elif Action_type == "masturbation":
            $ lines.append("I put on quite the show?")
        elif Action_type == "blowjob":
            $ lines.append("My jaw is still rather sore.")
            $ lines.append("My jaw is still recovering.")
        elif Action_type == "titjob":
            $ lines.append("You will wear them out like this.")
        elif Action_type == "handjob":
            $ lines.append("My arm will wear out.")
            $ lines.append("My hand is quite sore from earlier.")
            $ lines.append("My hand is rather sore from before.")
        elif Action_type == "footjob":
            $ lines.append("My feet are rather sore from earlier.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "You didn't get enough earlier?",
            "Huh? Again?",
            "I must have done something right.",
            "I guess fair's fair. . .",
            "Mmmm. . .",
            "Sure, come to me.",
            "Mmm, you like that? . .",
            "Did you enjoy that?",
            "Mmm. . .",
            "Another one?",
            "I guess you want more."]

        if Action_type in hand_Action_types:
            $ lines.append("Relax. . .")
            $ lines.append("Take it slow, I'm still shaking from earlier.")
        elif Action_type == "masturbation":
            $ lines.append("I enjoyed having an audience. . .")
        elif Action_type == "handjob":
            $ lines.append("I'm glad I don't grow calluses.")
            $ lines.append("Again with the handjobs, huh?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label Action_done_five_times_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I think I've got the hang of this.",
            "We're making a regular habit of this.",
            "This is. . . interesting.",
            "We're really making this a regular thing."]

        if Action_type == "handjob":
            $ lines.append("I think I've got this well in hand.")
        elif Action_type == "footjob":
            $ lines.append("I kinda like this sensation.{p}}Never thought about touching people with my feet.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Why did we not do this sooner?!",
            "I'm really starting to love this.",
            "I'm surprised how much I enjoy this."]

        if Action_type == "handjob":
            $ lines.append("Let me know any time you need me to give you a hand.")
        elif Action_type == "footjob":
            $ lines.append("Let me know any time you need me to \"foot you up\".")
        elif Action_type == "titjob":
            $ lines.append("Huh, I guess these are good for something.")
        elif Action_type == "blowjob":
            $ lines.append("I'm getting better at this. . . right?")
    elif Girl.tag == "Emma":
        $ lines = [
            "Please do call again. . .",
            "I'm enjoying this experience.",
            "We really should have done this sooner.",
            "I can't imagine why I waited so long."]

        if Action_type in cock_Action_types or Action_type in fondle_Action_types:
            $ lines.append("Best you've had, I'm sure.")

            if Action_type == "titjob":
                $ lines.append("You certainly get a lot of mileage out of these.")

        if Action_type in active_Action_types:
            $ lines.append("You're pretty good at that.")
    elif Girl.tag == "Laura":
        $ lines = [
            "I think I've got this down, maybe I should get a punch card.",
            "You seem to enjoy that.",
            "I'm getting used to this. . .",
            "You know, this was a good idea.",
            "I'm glad you're into this."]

        if Action_type in passive_Action_types:
            $ lines.append("I'm really getting the hang of this. . . right?")
    elif Girl.tag == "Jean":
        $ lines = [
            "Fun, right?",
            "I am loving this. You too, right?",
            "I'm getting used to this. . .",
            "I'm glad we have similar interests. . ."]

        if Action_type in active_Action_types:
            $ lines.append("You're pretty good at this. . .")
        elif Action_type in passive_Action_types:
            $ lines.append("I'm pretty good at this, right?")
    elif Girl.tag == "Storm":
        $ lines = [
            "I have gotten used to these. . .",
            "You do seem to enjoy this.",
            "I expect that you enjoyed that.",
            "I'm enjoying this experience.",
            "I am glad you \"bumped into\" me.",
            "You do certainly make the experience enjoyable."]

        if Action_type in active_Action_types:
            $ lines.append("You are quite skilled at this.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_Action_approval_addicted_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I guess. . .",
            "Hmmmm. . . ."]

        if Action_type == "handjob":
            $ lines.append("I think, if I could just touch that. . .")
        elif Action_type == "blowjob":
            $ lines.append("I think. . . for some reason I really do want that in my mouth. . .")
        elif Action_type in below_Action_types:
            $ lines.append("Well. . . I bet it would feel really good down there.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "I kind of {i}need{/i} to. . .",
            "Hmmmm. . . .",
            "Okay. . .",
            "I have kind of been hoping you might. . .",
            "I. . . if that's how you want to do it. . . maybe?",
            "Hmmm. . ."]

        if Action_type in ["blowjob", "kiss"]:
            $ lines.append("My mouth is watering. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "Mmmmmmmm. . .",
            "Hmmmm. . . .",
            "I don't know if I could wait. . .",
            "Very well. . .",
            "I was wondering how it would feel with you. . .",
            "Hmm, that would be an interesting experience. . .",
            "Hrmm. . ."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Hmmmm. . . .",
            "Okay. . .",
            "Sounds fun. . .",
            "Hmm, sounds fun. . .",
            "Hrmm. . ."]

        if Action_type in ["blowjob", "kiss"]:
            $ lines.append("[wipes away a little drool]")
    elif Girl.tag == "Jean":
        $ lines = [
            "Hmmmm. . . .",
            "Mmmmm. . .",
            "Okay. . .",
            "That does sound fun. . .",
            "Hmm, sounds fun. . .",
            "Hrmm. . ."]
    elif Girl.tag == "Storm":
        $ lines = [
            "Mmmmmmmm. . .",
            "Hmmmm. . . .",
            "I might enjoy that. . .",
            "Very well. . .",
            "I was curious as to the effect that would have. . .",
            "Hmm, that would certainly be interesting. . .",
            "Hrmm. . ."]
    elif Girl.tag == "Jubes":
        $ lines = [f"If you want, {Girl.player_petname}. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label before_Action_less_than_three_times_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Again?",
            "So you'd like another go?"]

        if Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
        elif Action_type == "titjob":
            $ lines.append("So you'd like another titjob?")
        elif Action_type == "blowjob":
            $ lines.append("So you'd like another blowjob?")
        elif Action_type == "masturbation":
            $ lines.append("You like to watch, huh?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
        elif Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Did you. . . like it last time?",
            "So you'd like another round?"]

        if Action_type == "handjob":
            $ lines.append("Hmm, magic fingers. . .")
        elif Action_type == "footjob":
            $ lines.append("Hmm, magic toes. . .")
        elif Action_type == "titjob":
            $ lines.append("So you'd like another titjob?")
        elif Action_type == "blowjob":
            $ lines.append("So you'd like another blowjob?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
        elif Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl.tag == "Emma":
        $ lines = [
            "Enjoyed last time. . . ?",
            "Oh, very well. . .",
            "Oh? Another round?"]

        if Action_type == "titjob":
            $ lines.append("Hmm, another titjob?")
        elif Action_type == "blowjob":
            $ lines.append("Another blowjob?")
        elif Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
        elif Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl.tag == "Laura":
        $ lines = [
            "You seem to like this one. . .",
            "Did you. . . like it last time?",
            "Oh? Another round?"]

        if Action_type == "footjob":
            $ lines.append("Hmm, magic toes. . .")
        elif Action_type == "titjob":
            $ lines.append("Another titjob??")
        elif Action_type == "blowjob":
            $ lines.append("You'd like another blowjob?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
        elif Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl.tag == "Jean":
        $ lines = [
            "You enjoyed that, huh.",
            "Hmm, it is kinda fun. . .",
            "Oh? Another round?"]

        if Action_type == "titjob":
            $ lines.append("Again with the tits, uh?")
        elif Action_type == "blowjob":
            $ lines.append("You'd like another blowjob?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")

        if Action_type == job_Action_types:
            $ lines.append("I guess you're getting used to these. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "You enjoyed it last time. . . ?",
            "Oh, very well. . .",
            "Oh? Another round?"]

        if Action_type == "titjob":
            $ lines.append("Hmm, another titjob?")
        elif Action_type == "blowjob":
            $ lines.append("Another blowjob?")
        elif Action_type == "masturbation":
            $ lines.append("You enjoyed the show?")
        elif Action_type in ["dildo_pussy", "sex"]:
            $ lines.append("You want to stick it in my pussy again?")
        elif Action_type in ["dildo_ass", "anal"]:
            $ lines.append("You want to stick it in my ass again?")
    elif Girl.tag == "Jubes":
        $ lines = [
            "You seem to like this one. . .",
            "Was last time fun?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_Action_rejected_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I really don't think this is the right place for that!",
            f"{Girl.player_petname}! Not in public!",
            f"This just really isn't the time or place, {Girl.player_petname}!",
            f"Not in such an exposed place, {Girl.player_petname}.",
            "Not here!",
            "I'd be a bit embarassed doing that here."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?")
            $ lines.append("You really expect me to do that here?")
            $ lines.append("Even if I wanted to, it certainly wouldn't be here!")

            if Action_type in sex_Action_types:
                $ lines.append("That you would even suggest such a thing in a place like this. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I can't do that here!")
    elif Girl.tag == "Kitty":
        $ lines = [
            "I don't like being so. . . exposed.",
            f"Time and place, {Girl.player_petname}!",
            f"This just really isn't the time or place, {Girl.player_petname}!",
            f"{Girl.player_petname}! Not here!",
            f"{Girl.player_petname}! Time and place!",
            "This is way too exposed!",
            "Not here!",
            "Certainly not here!",
            "Not here, not anywhere near here.",
            f"{Girl.Like}not here though?"]

        if Action_type in cock_Action_types:
            $ lines.append("You're being ridiculous. That? Here?!")

            if Action_type in sex_Action_types:
                $ lines.append("I can't believe you'd even consider it around here!")

        if Action_type in passive_Action_types:
            $ lines.append("You really expect me to do that here? You realize how. . . exposed that would be?")
    elif Girl.tag == "Emma":
        $ lines = [
            "I can't be seen doing that with you.",
            "I have a reputation to maintain.",
            "I couldn't possibly do that. . . here!",
            "This is way too exposed!",
            "Obviously not in someplace so exposed.",
            "Not here!",
            "This truly isn't an appropriate place for that.",
            "How can you imagine this would be an appropriate location?",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("Can you imagine the scandal? Here?")

            if Action_type == "anal":

                if approval_check(Girl, 500, "I"):
                    $ lines.append("How can you imagine this would be an appropriate location?.{p}This place, I mean, not anal.{p}Anal can be nice, sometimes.")
                else:
                    $ lines.append("How can you imagine this would be an appropriate location?.{p}This place, I mean, not anal.{p}Anal can be nice, sometimes.{p}Maybe not with you.")
    elif Girl.tag == "Laura":
        $ lines = [
            "I try to stay off the radar.",
            "This area's too exposed.",
            "Not here!",
            "This is too exposed.",
            "This place is way too exposed."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here? This isn't exactly \"covert\".")
            $ lines.append("This area is a bit too exposed for that sort of thing. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I couldn't do that in public.")
    elif Girl.tag == "Jean":
        $ lines = [
            "I'm. . . not comfortable. . . in public. . .",
            "I'm not comfortable in public right now. . .",
            "Not here!",
            "This is too public.",
            "I'm just not comfortable with that right now. . .",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("You really expect me to do that here?{p}You know I can't \"take care of that\" anymore. . .")

        if Action_type in passive_Action_types:
            $ lines.append("I. . . couldn't do that in public. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "I should not be seen doing that.",
            "I do not wish to make a spectacle.",
            "This is much too exposed.",
            "Not here!",
            "This truly is not an appropriate place for that.",
            "This area is a bit too exposed for that sort of thing. . ."]

        if Action_type in cock_Action_types:
            $ lines.append("I could not possibly do that here.")

            if Action_type in sex_Action_types:
                $ lines.append("How could you imagine that this would be an appropriate location?")

        if Action_type in passive_Action_types:
            $ lines.append("I cannot do that here.")
    elif Girl.tag == "Jubes":
        $ lines = ["I don't wanna make a scene."]

        if Action_type in passive_Action_types:
            $ lines.append("I don't want to do this in public!")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I told you not in public!",
            "I already told you this is too public!",
            "This is just way too exposed!",
            "I said not in public!"]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
        elif Action_type == "hotdog":
            $ lines.append("I told you that I didn't want you rubb'in up on me in public!")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Not here!",
            "This is just way too exposed!",
            "I told you this is too public!",
            "I said not in public!",
            "I already told you this is too public!",
            "I{i}just{/i}" + Girl.like + "told you, not in public!"]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Emma":
        $ lines = [
            f"As I said, not here, {Girl.player_petname}.",
            "This is not an appropriate place for that.",
            "I told you this is too public!",
            "I told you, not in public!",
            "I already told you this is too public!",
            "I already told you. . . not in such an exposed location."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop showing that thing around in public!")
    elif Girl.tag == "Laura":
        $ lines = [
            f"I told you, not here, {Girl.player_petname}.",
            "I said not in public.",
            "This is just way too exposed!",
            "Like I told you, too public!",
            "I said not in public!",
            "I already told you this is too public!",
            "I told you. . . this place is too exposed."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Jean":
        $ lines = [
            f"I told you. . . not here, {Girl.player_petname}.",
            "I told you I wasn't comfortable in public. . .",
            "Like I said, too public!",
            "I said not in public!",
            "I told you, I'm not comfortable with that. . .",
            "I'm not comfortable with that. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
        elif Action_type == "striptease":
            $ lines.append("I don't want to show off the goods like that!")
    elif Girl.tag == "Storm":
        $ lines = [
            f"This area is too public, {Girl.player_petname}.",
            f"As I said, not here, {Girl.player_petname}.",
            "I was very clear, this is too public.",
            "This is not an appropriate place for that.",
            "I told you this is too public!",
            "I informed you, not in public!",
            "I have already informed you, this is too public!",
            "I already informed you. . . not in such an exposed location."]

        if Action_type in passive_Action_types:
            $ lines.append("I already told you that I wouldn't do that out here!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop showing that thing around in public!")
    elif Girl.tag == "Jubes":
        $ lines = [
            f"I told you, not here, {Girl.player_petname}.",
            "I said not in public."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label Action_not_done_yet_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"I just don't think I'm ready yet, {Girl.player_petname}. . .",
            "I. . . don't think that's. . .",
            f"That's. . . a little intimate, {Girl.player_petname}.",
            f"Not now, {Girl.player_petname}.",
            f"Let's not, ok {Girl.player_petname}?",
            f"Not yet, {Girl.player_petname}. . .",
            "Oh, um, no, I'm not really comfortable with that. . .",
            f"I'm not really up for that, {Girl.player_petname}. . .",
            f". . . well I don't know about that, {Girl.player_petname}. . .",
            f"I just don't think I'm ready yet, {Girl.player_petname}. . .",
            f"I'm just not into that, {Girl.player_petname}. . .",
            "I. . . don't think that's. . ."]

        if Action_type in ass_Action_types:
            $ lines.append(f"That's kinda naughty, {Girl.player_petname}. . .")

        if Action_type in below_Action_types:
            $ lines.append(f"Um, not down there, {Girl.player_petname}. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")
        elif Action_type == "handjob":
            $ lines.append(f"I don't really want to touch it, {Girl.player_petname}. . .")
        elif Action_type == "blowjob":
            $ lines.append(f"I don't think I'd like the taste, {Girl.player_petname}. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            f"I'm{Girl.like}not ready for that, {Girl.player_petname}. . .",
            "Not. . . yet. . . maybe later.",
            f"Not yet, {Girl.player_petname}. . .",
            "I. . . don't think that's. . .",
            f"I'm not really up for that, {Girl.player_petname}. . .",
            f"I don't know that I'm. . .{Girl.like}ready? . .",
            f"I don't know, {Girl.player_petname}. . .",
            f"That's kinda hot, {Girl.player_petname}. . ."]

        if Action_type in pussy_Action_types:
            $ lines.append(f"Um, not down there, {Girl.player_petname}. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

        if Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append(f"That's pretty intimate, {Girl.player_petname}. . .")

        if Action_type in ["eat_ass", "dildo_ass", "anal"]:
            $ lines.append(f"I don't know that I'm. . .{Girl.like}that kind of girl?")
        elif Action_type == "masturbation":
            $ lines.append("That's. . . private? You know?")
        elif Action_type == "blowjob":
            $ lines.append(f"I don't know about the taste, {Girl.player_petname}. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "Let's work up to that, perhaps. . .",
            f"Seems a bit forward, {Girl.player_petname}.",
            f"I don't think we're there yet, {Girl.player_petname}. . .",
            f"I'm not sure we're at that stage, {Girl.player_petname}. . .",
            f"Not yet, {Girl.player_petname}. . .",
            f"Are you sure though, {Girl.player_petname}. . . ?",
            f"Perhaps later, {Girl.player_petname}. . .",
            f"I'm unsure, {Girl.player_petname}. . .",
            "I don't know that you're ready for that yet.",
            f"Hmm, that could be amusing, {Girl.player_petname}. . ."]

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my usual style. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm a bit past toys, {Girl.player_petname}. . .")
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

        if Action_type in sex_Action_types:
            $ lines.append("I really doubt you understand what you're in for. . .")
        elif Action_type in breast_Action_types:
            $ lines.append(f"I highly doubt you could handle them, {Girl.player_petname}. . .")
        elif Action_type == "masturbation":
            $ lines.append("I don't know that I want to perform.")
        elif Action_type == "blowjob":
            $ lines.append(f"I'm not sure you're up to my usual tastes, {Girl.player_petname}. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            f"Look, I don't know if we're ready for that, {Girl.player_petname}. . .",
            "Let's work up to that maybe. .",
            f"Seems a bit aggressive, {Girl.player_petname}.",
            f"I don't think we're there yet, {Girl.player_petname}. . .",
            f"Not yet, {Girl.player_petname}. . .",
            f"Seriously, {Girl.player_petname}. . .",
            f"Eh, {Girl.player_petname}. . .",
            "I don't know that I want to do that right now.",
            f"Hmm, that could be amusing, {Girl.player_petname}. . ."]

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")
            $ lines.append(f"I'm not really into that, {Girl.player_petname}. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Oh, you have no idea what you're in for. . .")
            $ lines.append("I don't know that you're ready for that yet.")
        elif Action_type == "blowjob":
            $ lines.append(f"I don't know if your taste will match your scent, {Girl.player_petname}. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            "Let's work up to that maybe. .",
            f"I don't think we're there yet, {Girl.player_petname}. . .",
            f"Mmmm, not right now, {Girl.player_petname}. . .",
            f"Not yet, {Girl.player_petname}. . .",
            f"Seriously, {Girl.player_petname}. . .",
            "Well. . .",
            "I don't know, it's kind of a bad time. . .",
            f"Hmm, that could be amusing, {Girl.player_petname}. . ."]

        if Action_type in hand_Action_types:
            $ lines.append(f"Look, don't touch, {Girl.player_petname}. . .")

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")
            $ lines.append(f"Not really my thing, {Girl.player_petname}. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Oh, this would be interesting. . .")
            $ lines.append("I don't know that you're ready for that yet.")
        elif Action_type == "blowjob":
            $ lines.append(f"I have been wondering what you taste like, {Girl.player_petname}. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            f"Perhaps some other time, {Girl.player_petname}. . .",
            "Mmm. . . that would. . . no. . .",
            f"Perhaps go slower, {Girl.player_petname}. . .",
            f"Oh, that would. . .perhaps not, {Girl.player_petname}. . .",
            f"I would rather not, {Girl.player_petname}. . .",
            "I am unsure about that. . .",
            "I am unsure about this.",
            f"Are you certain, {Girl.player_petname}? . .",
            f"I am not sure I would enjoy this, {Girl.player_petname}. . .",
            f"I am unsure, {Girl.player_petname}. . .",
            f"Hmm, that could be entertaining, {Girl.player_petname}. . ."]

        if Action_type in active_Action_types:
            $ lines.append(f"I would rather you did not, {Girl.player_petname}.")

            if Action_type in dildo_Action_types:
                $ lines.append(f"I'm a bit past toys, {Girl.player_petname}. . .")
                $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

        if Action_type in ["sex", "anal"]:
            $ lines.append("I seriously doubt that you understand what you would be in for. . .")
            $ lines.append("I do not know that you are yet prepared for that.")
    elif Girl.tag == "Jubes":
        $ lines = [
            f"Look, I don't know if we're ready for that, {Girl.player_petname}. . .",
            "Let's work up to that maybe. .",
            "I don't know, I'm not really into it right now.",
            f"Kinda forward, {Girl.player_petname}.",
            f"I don't think we're there yet, {Girl.player_petname}. . .",
            f"I'm not sure we're there yet, {Girl.player_petname}. . .",
            f"Not yet, {Girl.player_petname}. . .",
            f"Seriously, {Girl.player_petname}. . ."]

        if Action_type in ass_Action_types:
            $ lines.append("That's really not my style. . .")

        if Action_type in dildo_Action_types:
            $ lines.append(f"I'm just not into toys, {Girl.player_petname}. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label sorry_never_mind_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Ok, no problem, {Girl.player_petname}.",
            f"Yeah, fine, {Girl.player_petname}.",
            f"Yeah, ok, {Girl.player_petname}.",
            "Fine.",
            "No problem."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"It's cool, {Girl.player_petname}.",
            "No problem.",
            f"Yeah, ok, {Girl.player_petname}.",
            f"Aw, it's ok, {Girl.player_petname}.",
            "Yeah.",
            "It's cool."]
    elif Girl.tag == "Emma":
        $ lines = [
            f"Don't concern yourself, {Girl.player_petname}.",
            "No offense taken. I get it.",
            "I appreciate your restraint.",
            f"I appreciate your restraint, {Girl.player_petname}.",
            "Quite alright.",
            f"That's all right, {Girl.player_petname}.",
            f"No harm done, {Girl.player_petname}.",
            f"I thought as much, {Girl.player_petname}.",
            f"I'm sure, {Girl.player_petname}.",
            "Thank you.",
            "I can appreciate your. . . drive.",
            "I don't blame you for your. . . enthusiasm.",
            "No harm in asking. Once."]
    elif Girl.tag == "Laura":
        $ lines = [
            "No worries.",
            "It's cool.",
            f"It's cool, {Girl.player_petname}.",
            "It's fine.",
            f"Yeah, ok, {Girl.player_petname}.",
            "Cool.",
            "Sure, no problem.",
            "Well, you are persistent.",
            "Hey, I can't blame you.",
            "So long as you don't push it."]
    elif Girl.tag == "Jean":
        $ lines = [
            "It's fine, I get it.",
            "It's fine.",
            f"Ok, fine, {Girl.player_petname}.",
            "Ok then.",
            f"Yeah, ok, {Girl.player_petname}.",
            "Sure, it's fine.",
            "Keep trying. . .",
            "I get it.",
            "So long as you don't push it."]
    elif Girl.tag == "Storm":
        $ lines = [
            f"Don't concern yourself, {Girl.player_petname}.",
            "No offense taken. I get it.",
            "I appreciate your restraint.",
            f"I appreciate your restraint, {Girl.player_petname}.",
            "I understand.",
            f"That is fine, {Girl.player_petname}.",
            f"It is fine, {Girl.player_petname}.",
            f"I thought as much, {Girl.player_petname}.",
            f"I'm sure, {Girl.player_petname}.",
            "Thank you.",
            "I can appreciate your. . . desires.",
            "I cannot blame you for your. . . desires.",
            "There is no harm in asking."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "Yeah, whatever.",
            "It's fine."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label maybe_later_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"I'll give it some thought, {Girl.player_petname}.",
            f"It's. . . possible, {Girl.player_petname}.",
            f"I'll be thinking about it, {Girl.player_petname}.",
            f"Anything's possible, {Girl.player_petname}.",
            f"Heh, maybe, {Girl.player_petname}.",
            f"I'll give it some thought, {Girl.player_petname}.",
            ". . .{p}I guess?",
            "We'll have to see.",
            f"Yeah, maybe, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "blowjob":
            $ lines.append(f"I might get hungry, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("Well, definitely later. . . but I'll have to think about inviting you.")
            else:
                $ lines.append("Hmm, maybe. . . I'll let you know.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Um, yeah, maybe later.",
            f"I'll give it some thought, {Girl.player_petname}.",
            f"Heh, maybe, {Girl.player_petname}.",
            f"It's. . . possible, {Girl.player_petname}.",
            ". . .{p}}Maybe.",
            "Maybe.",
            f"You{Girl.like}never know, {Girl.player_petname}.",
            "Maybe, you never know.",
            f"Yeah, maybe, {Girl.player_petname}.",
            f"I'll be thinking about it, {Girl.player_petname}.",
            f"Anything's possible, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("Well, I know what {i}I'll{/i} be doing later. Not sure if you can come.{p}I mean- you know, be there.{p}I'm not sure you'll {i}be{/i} there.{p}. . .coming.")
            else:
                $ lines.append("Hmm, maybe. . . I'll text you?")
    elif Girl.tag == "Emma":
        $ lines = [
            "Well, I can't rule it out. . .",
            f"I'll give it some thought, {Girl.player_petname}.",
            f"It's. . . possible, {Girl.player_petname}.",
            ". . .{p}}I couldn't rule it out. . .",
            "Perhaps.",
            f"I wouldn't rule it out, {Girl.player_petname}.",
            ". . .{p}Perhaps.",
            "Oh, most certainly. . .",
            "I imagine we will. . .{p}}. . . often.",
            f"I imagine it will happen at some point, {Girl.player_petname}.",
            f"I'll be thinking about it, {Girl.player_petname}.",
            f"Anything's possible, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
            $ lines.append(f"Perhaps I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("I have plans for. . . later, but perhaps you could take part.")
            else:
                $ lines.append("I couldn't say.")
    elif Girl.tag == "Laura":
        $ lines = [
            "Eh. Maybe.",
            "Maybe?",
            f"Maybe, {Girl.player_petname}.",
            f"It's. . . possible, {Girl.player_petname}.",
            "Maybe.",
            f"Yeah, maybe, {Girl.player_petname}.",
            ". . .{p}}Maybe.",
            "Probably. . .",
            "Oh, probably. . .{p}. . . often.",
            "I gues eventually. . .",
            f"I'll be thinking about it, {Girl.player_petname}.",
            f"Anything's possible, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("I probably will be, but not with an audience.")
            else:
                $ lines.append("Hmm, maybe. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            ". . . I guess? Maybe.",
            "Maybe.",
            ". . . maybe.",
            f"Sure, whatever, {Girl.player_petname}.",
            "Well. . .{p}}Maybe.",
            "Sure, whatever. . .",
            "Oh, probably. . .",
            "I guess eventually. . .",
            f"Well, I'll give it some thought, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("Well -I- will, but after you leave.")
            else:
                $ lines.append("Well. . . maybe. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            f"I will give it some thought, {Girl.player_petname}.",
            ". . .{p}Perhaps. . .",
            "Perhaps.",
            f"I would not rule it out, {Girl.player_petname}.",
            ". . .{p}Perhaps.",
            "Oh, of that I am certain. . .",
            "I imagine at some point we shall. . .{p}. . . frequently.",
            f"I expect it will happen at some point, {Girl.player_petname}.",
            f"I will give it some thought, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
            $ lines.append(f"Perhaps I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("I expect that I will be finished by then. . .")
            else:
                $ lines.append("We shall see.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Eh. Maybe.",
            f"Maybe, {Girl.player_petname}.",
            "Maybe?",
            f"It's. . . possible, {Girl.player_petname}.",
            "Maybe.",
            f"I'll be thinking about it, {Girl.player_petname}.",
            f"Anything's possible, {Girl.player_petname}."]

        if Action_type in dildo_Action_types:
            $ lines.append(f"Maybe I'll practice on my own time, {Girl.player_petname}.")
        elif Action_type == "masturbation":

            if Girl.desire > 50:
                $ lines.append("Maybe, just not with so many eyes on me. . .")
            else:
                $ lines.append("Hmm, maaaybe. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label since_you_are_so_nice_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Well, since you're be'in so nice about it, I guess we can give it a go. . .",
            "I guess if you really want to try it. . ."]

        if Action_type in active_Action_types or Action_type == "masturbation":
            $ lines.append("I guess it doesn't feel so bad. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            "{i}Well. . .{/i} I didn't say I didn't want to. . .",
            "Well, now that you mention it. . ."]

        if Action_type in active_Action_types or Action_type == "masturbation":
            $ lines.append("I guess it doesn't feel so bad. . .")

            if Action_type in active_Action_types:
                $ lines.append(f"Well{Girl.like}just take it easy, ok? . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "I am willing to give it a try if you are. . .",
            "Or not. . .",
            "Well, now that you mention it. . .",
            "I didn't say I was opposed. . ."]

        if Action_type in active_Action_types:
            $ lines.append("Well, so long as you know what you're doing . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "No no, not a problem. . .",
            "Hey, whatever floats your boat. . .",
            "Or not. . .",
            "Well, now that you mention it. . ."]

        if Action_type in insertion_Action_types:
            $ lines.append("Get in there.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Oh, no, it's fine.",
            "Sure, works for me. . .",
            "I didn't say I minded. . .",
            "Well, now that you mention it. . ."]

        if Action_type in insertion_Action_types:
            $ lines.append("Get in there.")
    elif Girl.tag == "Storm":
        $ lines = [
            "I am willing to give it a try if you are. . .",
            "Oh, that is unfortunate. . .",
            "I did not say that I was opposed. . .",
            "Or perhaps not. . .",
            "Well, now that you mention it. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["No no, not a problem. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label auto_accepted_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Ok, {Girl.player_petname}, let's do this.",
            "Hmm, I've apparently got someone's attention. . ."]

        if Action_type in insertion_Action_types:
            $ lines.append("Hmm, stick it in. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Oh. . . game on, {Girl.player_petname}.",
            "Oookay. . .",
            "Hmm, I've apparently got someone's attention. . ."]

        if Action_type in insertion_Action_types:
            $ lines.append("Hmm, stick it in. . .")

            if Action_type in dildo_Action_types:
                $ lines.append(f"Ooo, {Girl.player_petname}, toys!")
    elif Girl.tag == "Emma":
        $ lines = [
            f"Mmm, if you insist, {Girl.player_petname}.",
            "Oooh, naughty boy. . ."]

        if Action_type in job_Action_types:
            $ lines.append("Now what shall we do with that . .")

            if Action_type in dildo_Action_types:
                $ lines.append(f"Mmmm, {Girl.player_petname}, toys. . .")
                $ lines.append(f"Hmm, {Girl.player_petname}, toys!")
    elif Girl.tag == "Laura":
        $ lines = [
            f"Fine by me, {Girl.player_petname}.",
            "Yeah, ok. . ."]

        if Action_type in job_Action_types:
            $ lines.append("Oh, what did you have in mind with that? . .")

            if Action_type in dildo_Action_types:
                $ lines.append(f"Ooo, {Girl.player_petname}, toys!")
    elif Girl.tag == "Jean":
        $ lines = [
            f"Oh, if you must, {Girl.player_petname}.",
            "Oh! Sure. . ."]

        if Action_type in job_Action_types:
            $ lines.append("Oh, what did you have in mind with that? . .")

            if Action_type in dildo_Action_types:
                $ lines.append(f"Ooo, {Girl.player_petname}, toys!")
    elif Girl.tag == "Storm":
        $ lines = [
            f"Mmm, if you insist, {Girl.player_petname}.",
            f"{Girl.player_petname}, I am surprised at you. . ."]

        if Action_type in job_Action_types:
            $ lines.append("Now what shall we do with that . .")

            if Action_type in dildo_Action_types:
                $ lines.append(f"Mmmm, {Girl.player_petname}, toys. . .")
                $ lines.append(f"Hmm, {Girl.player_petname}, toys!")
    elif Girl.tag == "Jubes":
        $ lines = [f"Fine by me, {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label were_done_here_lines(Girl, Action_type):
    $ lines = [
        f"{Girl.name} shoves you away and slaps you in the face.",
        f"{Girl.name} shoves you away."]

    "[line]"

    if Girl.tag == "Rogue":
        $ lines = [
            "Jackass!{p}If that's how you want to treat me, we're done here!",
            "Dick!{p}}If that's how you want want to act, I'm out of here!"]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Jerk!{p}}I am not putting up with that shit!",
            "Asshole!{p}You need to ask nicer than that!",
            "Jerk!{p}}I'm not into that!"]

        if Action_type in pussy_insertion_Action_types:
            $ lines.append("Jerk!{p}Ask nice if you want to stick something in my pussy!")
        elif Action_type in anal_insertion_Action_types:
            $ lines.append("Jerk!{p}}Ask nice if you want to stick something in my ass!")
    elif Girl.tag == "Emma":
        $ lines = [
            "Impertinent!{p}Do not test my patience with you.",
            "Impertinent!{p}You need to ask a lady first.",
            f"Don't push your luck, {Girl.player_petname}.",
            "Ask nicely before trying anything like that!"]

        if Action_type in anal_insertion_Action_types:
            $ lines.append("Ask nicely if you want to stick something in my ass!")
    elif Girl.tag == "Laura":
        $ lines = [
            "Dick.{p}Don't push me.",
            "Yeah, not like that you won't.",
            f"Don't push it, {Girl.player_petname}."]

        if Action_type in pussy_insertion_Action_types:
            $ lines.append("Jerk!{p}Ask nice if you want to stick something in my pussy!")
        elif Action_type in anal_insertion_Action_types:
            $ lines.append("Jerk!{p}}Ask nice if you want to stick something in my ass!")
    elif Girl.tag == "Jean":
        $ lines = [
            "Hey, I don't need my powers to hurt you.",
            "Tsk tsk.{p}Don't push it, " + Girl.player_petname + "."]

        if Action_type in pussy_insertion_Action_types:
            $ lines.append("Jerk!{p}Ask nice if you want to stick something in my pussy!")
        elif Action_type in anal_insertion_Action_types:
            $ lines.append("Jerk!{p}}Ask nice if you want to stick something in my ass!")
    elif Girl.tag == "Storm":
        $ lines = [
            "That is unfortunate.",
            "I am afraid that is -not- what will happen here.",
            f"Do not go beyond yourself, {Girl.player_petname}.",
            "Ask nicely before trying anything like that!"]

        if Action_type in pussy_insertion_Action_types:
            $ lines.append("Jerk!{p}Ask nice if you want to stick something in my pussy!")
        elif Action_type in anal_insertion_Action_types:
            $ lines.append("Ask nicely if you want to stick something in my ass!")
    elif Girl.tag == "Jubes":
        $ lines = ["Dick.{p}Don't push me."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label Action_already_rejected_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            f"I just don't want to, {Girl.player_petname}.",
            "I'aint tellin you again.",
            f"Look, I already told you no thanks, {Girl.player_petname}.",
            "Read my lips, no.",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Look, I already told you no thanks, {Girl.player_petname}.",
            "I'm not telling you again.",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            "{i}Listen{/i}!",
            "How many times do I have to say \"no\"?"
            f"Not even, {Girl.player_petname}.",
            f"Maybe{Girl.like}take \"no\" for an answer?",
            "I'm just not into that."]

        if Action_type == "blowjob":
            $ lines.append("You can eat a dick, 'cos I'm not.")
    elif Girl.tag == "Emma":
        $ lines = [
            "Don't make me repeat myself.",
            "I've refused, end of story.",
            "I won't repeat myself.",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            "You need to pay attention when I speak to you.",
            f"I don't appreciate having to repeat myself, {Girl.player_petname}.",
            f"I really can't, {Girl.player_petname}.",
            "Don't question me again.",
            "I've made myself clear."]

        if Action_type == "handjob":
            $ lines.append("Then I hope you can take care of yourself.")
    elif Girl.tag == "Laura":
        $ lines = [
            "Don't ask again.",
            "Look, I already told you no.",
            "I'm not telling you again.",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            "Listen to the words that are coming out of my mouth.",
            f"I don't like to repeat myself, {Girl.player_petname}.",
            f"I really can't, {Girl.player_petname}.",
            "Don't push me.",
            "Don't push it.",
            "What did I tell you?"]

        if Action_type == "blowjob":
            $ lines.append("Suck this then.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Don't ask again.",
            "I already told you no.",
            "I'm not telling you again.",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            "I don't want to have to go through this again.",
            f"I really can't, {Girl.player_petname}.",
            f"Don't push your luck, {Girl.player_petname}.",
            "Know when to stop.",
            "What did I tell you?"]

        if Action_type in passive_Action_types:
            $ lines.append("Damn. . . forgot I can't do that. . .")

            if Action_type == "blowjob":
                $ lines.append("You want me to make you suck yourself?")
    elif Girl.tag == "Storm":
        $ lines = [
            "Do not make me repeat myself.",
            "I have refused. Learn to accept that.",
            "I shall not repeat myself.",
            "You go too far!",
            f"Learn to take \"no\" for an answer, {Girl.player_petname}.",
            "I have been clear on this.",
            "Do not question me again.",
            "I believe I have made myself clear."]

        if Action_type == "handjob":
            $ lines.append("Then I hope you can take care of yourself.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "I'm pretty clear on this, NO.",
            f"I really can't, {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label forced_Action_rejected_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Um, no way.",
            f"Not even, {Girl.player_petname}.",
            "Not even that much.",
            "I'm not that kind of girl!",
            "That isn't something I'd want!",
            "Even that's not worth it.",
            "That's a bit much, even for you."]

        if Action_type in kinky_Action_types:
            $ lines.append("Ew, no way.")

        if Action_type in hand_Action_types:
            $ lines.append("I don't want you touching me.")

            if Action_type == "fondle_ass":
                $ lines.append("Hands off the booty!")

        if Action_type in mouth_Action_types:
            $ lines.append("I don't want your lips on me.")

        if Action_type in below_Action_types:
            $ lines.append(f"Stay out of my pants, {Girl.player_petname}.")

            if Action_type in dildo_Action_types:
                $ lines.append("I'm not going to let you use that on me.")

        elif Action_type in passive_Action_types:
            $ lines.append("I'm not doing that just because you have me over a barrel.")

            if Action_type == "masturbation":
                $ lines.append("I'm not doing something so. . . intimate with you watching.")
            elif Action_type == "footjob":
                $ lines.append("Not even with my feet.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Not even.",
            "Back off!",
            "Um, no way.",
            "Ew, no way.",
            "I just can't do that!",
            "Not even.",
            "That's a bit much, even for you.",
            "Yeah, not happening."]

        if Action_type in kinky_Action_types:
            $ lines.append("No, that's just weird.")

        if Action_type in pussy_Action_types:
            $ lines.append(f"Keep away from my kitty, {Girl.player_petname}.")

        if Action_type in mouth_Action_types:
            $ lines.append(f"{Girl.Like}get your mouth away from me.")

        if Action_type in dildo_Action_types:
            $ lines.append("I'm not going to let you use that on me.")

        if Action_type == "blowjob" or Action_type == "handjob":
            $ lines.append("Not even if you had a ten foot pole.{p}I mean. . .{p}}You know what I mean!")
        elif Action_type == "masturbation":
            $ lines.append("I. . . can't, not with you watching.")
        elif Action_type == "footjob":
            $ lines.append("I don't even want to step on it.")
    elif Girl.tag == "Emma":
        $ lines = [
            "Don't push your luck.",
            f"I don't think so, {Girl.player_petname}.",
            "I'm not going that far today.",
            "I don't think so.",
            "Even that is asking too much.",
            "I couldn't put you through that.",
            "That's something I won't do.",
            "You go too far!",
            "Not worth it.",
            "I just don't see the benefit."]

        if Action_type in finger_Action_types:
            $ lines.append("Do you want to keep those fingers?")
        elif Action_type in dildo_Action_types:
            $ lines.append("I'm not going to let you use that on me.")
        elif Action_type in passive_Action_types:
            $ lines.append("Don't overestimate your leverage here.")
            $ lines.append("You're really shooting for the fences on that one.")
        elif Action_type == "footjob":
            $ lines.append("You really don't want my heels near your manhood.")
    elif Girl.tag == "Laura":
        $ lines = [
            "No.",
            f"I don't think so, {Girl.player_petname}.",
            "I'm not going there today.",
            "I don't think so.",
            "No.",
            "No, try something else.",
            "That's just pushing it.",
            "You're going too far.",
            "Not worth it.",
            "There's no point trying."]

        if Action_type in kinky_Action_types:
            $ lines.append("This is just too weird for me.")

        if Action_type in finger_Action_types:
            $ lines.append("Do you want to keep those fingers?")

        elif Action_type in passive_Action_types:
            $ lines.append("I'm over taking orders.")

            if Action_type == "footjob":
                $ lines.append("You understand that I have claws down there too. . .")

        elif Action_type in mouth_Action_types:
            $ lines.append("Not worth it.")
        elif Action_type in dildo_Action_types:
            $ lines.append("I'm not going to let you use that on me.")
    elif Girl.tag == "Jean":
        $ lines = [
            "No.",
            f"I don't think so, {Girl.player_petname}.",
            "Mmmm, no.",
            "I'm not going there today.",
            "I don't think so.",
            "No.",
            "No, try something else.",
            "Don't push it. . .",
            ". . . no, not worth it.",
            "There's no point trying."]

        if Action_type in dildo_Action_types:
            $ lines.append("I'm not going to let you use that on me.")

        elif Action_type in passive_Action_types:
            $ lines.append("I'm not doing that.")
            $ lines.append("You're overestimating your power here.")
            $ lines.append("I'm the queen here!")

            if Action_type == "footjob":
                $ lines.append("Nope, too kinky.")
    elif Girl.tag == "Storm":
        $ lines = [
            "You go too far.",
            "I am not comfortable with that.",
            "I do not wish to do this.",
            "I will not do that.",
            "I just do not understand the benefit."]

        if Action_type in dildo_Action_types:
            $ lines.append("I'm not going to let you use that on me.")

        elif Action_type in passive_Action_types:
            $ lines.append("Do not overestimate your power here.")
            $ lines.append("You certainly are not wasting your shot.")

            if Action_type == "footjob":
                $ lines.append("Do not tempt me to show you what my feet can do.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "No.",
            f"I don't think so, {Girl.player_petname}.",
            "I'm not going there today.",
            "This isn't something I'm into.",
            "I don't think so."]

        if Action_type in finger_Action_types:
            $ lines.append("Do you want to keep those fingers?")
        elif Action_type == "blowjob":
            $ lines.append("Suck yourself.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_Action_approval_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Hmm, could be fun. . .",
            "Sure. . .",
            "Heh, might be fun.",
            "I guess. . .",
            "Hmm, it has been on my list. . ."]

        if Action_type == "masturbation":
            $ lines.append("I guess it could be fun with you watching. . .")
        elif Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("Hmm, you look ready for it, at least. . .")
            $ lines.append("Hmm, I've always wanted to try it. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            "I guess. . .",
            "Hadn't really considered that.",
            f"{Girl.Like}sure. . .",
            "This could be kinda fun . . .",
            "Sure. . .",
            "Anything's worth a shot. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("Hmm, you look ready to go. . .")
            $ lines.append("I can't say it hasn't crossed my mind. . .")
            $ lines.append("I guess it could be fun two-player. . .")

        if Action_type in kinky_Action_types:
            $ lines.append("That's kinda gross. . .")
    elif Girl.tag == "Emma":
        $ lines = [
            "I suppose. . .",
            "I suppose I could enjoy that. . .",
            "Very well. . .",
            "I was hoping you'd ask. . .",
            "I was getting tired of waiting. . ."]

        if Action_type in kinky_Action_types:
            $ lines.append("Hm, I didn't know that's what you were into.")

            if Action_type == "masturbation":
                $ lines.append("I do enjoy a good performance . . .")

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("Hmm, I was wondering when you'd ask. . .")
            $ lines.append("Well if that's what gets you off. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "Hmm. . .",
            "Sounds fun. . .",
            "Huh. . .",
            "Sure. . .",
            "I was hoping you'd ask. . .",
            "I was tired of waiting. . ."]

        if Action_type in kinky_Action_types:
            $ lines.append("Hm, I didn't know that's what you were into.")

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("I guess it could be fun two-player. . .")
            $ lines.append("Well if that's what gets you off. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            "Hmm. . .",
            "Sounds fun, but. . .",
            "Huh. . .",
            "I do have some free time. . .",
            "I do have some time. . .",
            "Sure. . .",
            "I was tired of waiting. . ."]

        if Action_type in kinky_Action_types:
            $ lines.append("Mmmm, you're into that?")

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("I was wondering when this would come up. . .")
        elif Action_type in fondle_Action_types:
            $ lines.append("Ok, we can start with that. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "Hmmm, an interesting proposal. . .",
            "I suppose. . .",
            "I suppose I could enjoy that. . .",
            "Very well. . .",
            "I was hoping you would ask. . .",
            "I was getting tired of waiting. . .",
            "Well if that is what satisfies you. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("I guess it could be fun with a partner. . .")
        elif Action_type in cock_Action_types:
            $ lines.append("Hmm, I was expecting you to ask. . .")
        elif Action_type == "masturbation":
                $ lines.append("I do not mind an audience . . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Hm, I hadn't thought. . .",
            "Hmm. . ."]

        if Action_type == "masturbation":
            $ lines.append("I could work off some stress. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label first_Action_approval_mostly_love_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["If that's what you like. . ."]

        if Action_type in dildo_Action_types:
            $ lines.append("I've had a reasonable amount of experience with these, you know. . .")

        if Action_type in cock_Action_types:
            $ lines.append("It looks like you need some relief. . .")
            $ lines.append("Huh, well that's certainly one way to get off.")

        if Action_type in contact_Action_types:
            $ lines.append("Well, I've never really been able to touch people without draining them, this could be an interesting experience. . .")
            $ lines.append("Well, I've never been able to do this before now, so this might be fun.")

        if Action_type in kinky_Action_types:
            $ lines.append("I guess if you really want to try it. . .")

        if Action_type == "masturbation":
            $ lines.append("Since my love life's been a bit. . . limited, I've gotten pretty good at this.")

        if Action_type == "blowjob":
            $ lines.append("I've never really put something like that in my mouth. . . might be interesting.")

        if Action_type == "dildo_ass":
            $ lines.append("I haven't actually used one of these, back there before. . .")
    elif Girl.tag == "Kitty":
        $ lines = [
            "That's, I don't know. . .",
            "I guess it could be interesting. . .",
            "It's nice that you even thought about it.",
            "I have wondered what you. . . taste like.",
            "This is kind of {i}intimate{/i} . . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            f"I{Girl.like}haven't actually used one of these, back there before. . .",
            "I guess it couldn't hurt. . .",
            "I don't want you to think I'm some kind of slut. . .",
            "I guess? . .",
            "It does look a bit swollen. . ."]
    elif Girl.tag == "Emma":
        $ lines = [
            "Oh, are we there now?",
            "I suppose you've earned something. . .",
            "I suppose you've earned something special. . .",
            "I am curious if it tastes as good as it looks. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose you might enjoy that. . .",
            "I suppose it couldn't hurt. . .",
            "I don't usually show this side . . .",
            "I wouldn't want you to get hurt. . .",
            "I was wondering when you'd ask. . .",
            "I wouldn't want to leave you. . . unattended. . ."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Oh, we're there now?",
            "You'd like that. . .",
            "Well, maybe you deserve it.",
            "I have wondered how you taste.",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I haven't actually used one of these, back there before. . .",
            "I guess it couldn't hurt. . .",
            "I don't know, are you sure?",
            "Well, you look so cute when you ask. . .",
            "I was hoping you'd ask. . .",
            "If that's what you're into. . ."]
    elif Girl.tag == "Jean":
        $ lines = [
            "Oh, we're there now?",
            "Well, I guess it wouldn't be so bad. . .",
            "I'd love to, but. . .",
            "Well, I could hardly turn down that offer. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose. . .",
            "I was wondering when this would come up. . .",
            "Well. . .",
            "I was expecting this. . .",
            "Ok, we can start with that. . ."]
    elif Girl.tag == "Storm":
        $ lines = [
            "Oh, that is a bit forward!",
            "I might enjoy that. . .",
            "I suppose you've earned something special. . .",
            "I have been curious. . .",
            "I've had a reasonable amount of experience with these, you know. . .",
            "I suppose you might enjoy that. . .",
            "I am usually alone for this . . .",
            "I could enjoy that. . .",
            "I would not want to. . . overwhelm you. . .",
            "I was hoping that you would ask. . .",
            "I would not wish to leave you. . . un-tended. . ."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "What? What're you talking about?",
            "You'd like that. . .",
            "I don't know, are you sure?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label this_is_boring_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = []

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types:
            $ lines.append("Well if that's your attitude, I don't need your \"help\".")
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Hey, I've got better things to do if you're{Girl.like}going to be a dick about it.",
            "Well fuck you then."]

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types:
            $ lines.append("Well if that's your attitude, I don't need your \"help\".")
        elif Action_type in ["footjob", "handjob", "titjob", "blowjob"]:
            $ lines.append("Fun for you maybe, I'm tired of it.")
            $ lines.append("Not with that attitude, mister!")
    elif Girl.tag == "Laura":
        $ lines = [
            "Well, I've got better things to be doing.",
            "I'm kinda bored here.",
            "I have better things to do with my time.",
            "Not interested."]

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types:
            $ lines.append("Well if that's your attitude, I don't need your \"help\".")
        elif Action_type in ["footjob", "handjob", "titjob", "blowjob"]:
            $ lines.append("Not with that attitude.")
            $ lines.append("Well fuck you then.")
    elif Girl.tag == "Emma":
        $ lines = [
            "No, I think not.",
            "You know, I do have better things to do with my time than this.",
            "Well then.",
            "I do have better things I could be doing."]

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types:
            $ lines.append("Well if that's your attitude, I don't need your \"help\".")
        elif Action_type in ["footjob", "handjob", "titjob", "blowjob"]:
            $ lines.append("You may be enjoying yourself, but I'm getting a bit sore.")
            $ lines.append("Well perhaps you are enjoying yourself, but I'm tired of this.")
            $ lines.append("Then I suppose you can handle this yourself.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Well, I've got better things to be doing.",
            "Well -I'm- bored.",
            "Don't overestimate yourself.",
            "I have better things to do with my time.",
            "Not interested."]

        if Action_type in ["footjob", "handjob", "titjob", "blowjob"]:
            $ lines.append("Ok, have fun with that then.")
            $ lines.append("Well fuck you then.")
    elif Girl.tag == "Storm":
        $ lines = [
            "No, I think not.",
            "Perhaps some time alone would help you better evaluate your choices.",
            "Well then.",
            "I do have better things I could be doing."]

        if Action_type in fondle_Action_types or Action_type in dildo_Action_types:
            $ lines.append("Well if that's your attitude, I don't need your \"help\".")
        elif Action_type in ["footjob", "handjob", "titjob", "blowjob"]:
            $ lines.append("Well however much you are enjoying yourself, I need to take a break.")
            $ lines.append("Then I suppose you can handle this yourself.")
    elif Girl.tag == "Jubes":
        $ lines = ["This is kinda boring. . ."]

    $ line = renpy.random.choice(lines)

    if len(lines) > 0:
        $ line = renpy.random.choice(lines)

        Girl.voice "[line]"

    return

label otherwise_not_interested_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Nah, I don't think I'm interested.",
            "Not hap'nin.",
            f"Not hap'nin, {Girl.player_petname}.",
            f"No luck, {Girl.player_petname}.",
            f"Tsk, not this time, {Girl.player_petname}.",
            f"Shoo, {Girl.player_petname}.",
            f"Um, no thanks, {Girl.player_petname}.",
            "I'd really rather not.",
            f"How about let's not, {Girl.player_petname}.",
            "Not interested.",
            "No way.",
            "Not happening.",
            "I'd really rather not.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            f"Not right now, {Girl.player_petname}. . .",
            "Maybe not right now, ok?"]

        if Action_type in passive_Action_types:
            $ lines.append("Heh, no, I'm not doing that.")

            if Action_type == "footjob":
                $ lines.append("That isn't really how I planned to use my feet today.")

        if Action_type in kinky_Action_types:
            $ lines.append("What?! Gross!")
            $ lines.append("Ew!")

            if Action_type in dildo_Action_types:
                $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
            elif Action_type in ass_Action_types:
                $ lines.append("I. . . not there!!")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Um, no.",
            f"Um, no thanks, {Girl.player_petname}.",
            "Oh, um, no, I'm not really comfortable with that. . .",
            f"Let's not, ok {Girl.player_petname}?",
            f"Not now, {Girl.player_petname}.",
            f"Not, right now {Girl.player_petname}. . .",
            f"Later, {Girl.player_petname}!",
            "Not now, ok?",
            f"Maybe{Girl.like}not right now? . .",
            "Not. . . now. . .",
            "Um, no.",
            "No way.",
            "Nooope.",
            f"No luck {Girl.player_petname}.",
            "Ugh!",
            f"Scram, {Girl.player_petname}.",
            "That's. . . not cool.",
            "Ew.",
            f"How about let's not, {Girl.player_petname}.",
            "Nope.",
            "No way.",
            "Nuhuh.",
            "Noooope.",
            "Noooop."]

        if Action_type == "handjob":
            $ lines.append("I don't wanna touch that.")
        elif Action_type == "footjob":
            $ lines.append("I don't know about using my feet for. . . that.")
        elif Action_type in dildo_Action_types:
            $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
    elif Girl.tag == "Emma":
        $ lines = [
            "You wish.",
            "Hmmm, no."
            f"I don't think so, {Girl.player_petname}.",
            "I'm really not comfortable with that. . .",
            f"Let's not, ok {Girl.player_petname}?",
            "I'd rather not today. . .",
            f"Not now, {Girl.player_petname}.",
            "I'd rather not right now though.",
            f"Perhaps later, {Girl.player_petname}.",
            f"Not now, {Girl.player_petname}. . .",
            "Perhaps another time would be better? . .",
            "I don't think that would be appropriate. . .",
            "No.",
            f"No thank you, {Girl.player_petname}.",
            "I know, I'm as disappointed as you are.",
            f"Not today, {Girl.player_petname}.",
            "I'm sorry, not now.",
            f"No, I don't think so, {Girl.player_petname}.",
            "No way.",
            "I'm afraid not.",
            "No, thank you."]

        if Action_type in passive_Action_types:
            $ lines.append("I don't think I will.")
            $ lines.append("I don't think you've earned that yet.")

            if Action_type == "footjob":
                $ lines.append("I'm not in the mood for footplay today. . .")

        elif Action_type in dildo_Action_types:
            $ lines.append(f"We don't need any toys, do we, {Girl.player_petname}?")
            $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
    elif Girl.tag == "Laura":
        $ lines = [
            "Keep dreaming.",
            "You wish.",
            "Nope.",
            "I'm really not cool with that. . .",
            f"Let's not, ok {Girl.player_petname}?",
            "I'd rather not today. . .",
            f"Not now, {Girl.player_petname}.",
            "Nah.",
            f"Not right now {Girl.player_petname}. . .",
            f"I don't know, {Girl.player_petname}!",
            "Not now, ok?",
            "Maybe later? . .",
            "I don't think that would be appropriate. . .",
            "No.",
            f"No thank you, {Girl.player_petname}.",
            "Yeah, sorry.",
            f"Not today, {Girl.player_petname}.",
            "I'm sorry, not now.",
            "Nah.",
            "Nope.",
            "Um, no.",
            "No way.",
            "I'd rather not.",
            "Yeah, no.",
            "No thanks."]

        if Action_type in passive_Action_types:
            $ lines.append("You haven't earned it yet.")

            if Action_type == "blowjob":
                $ lines.append("I don't know where that's been lately.")

        elif Action_type in dildo_Action_types:
            $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
    elif Girl.tag == "Jean":
        $ lines = [
            "Yeah, you wish.",
            "You wish.",
            "You wish. . .",
            "Nope.",
            "I'd rather not.",
            f"Let's not, ok {Girl.player_petname}?",
            "I'd rather not today. . .",
            f"Not now, {Girl.player_petname}.",
            "Nope.",
            f"Not right now {Girl.player_petname}. . .",
            f"I don't know, {Girl.player_petname}. . .",
            "Not now, ok?",
            "I'm not in the mood right now . .",
            "I don't think that would be appropriate. . .",
            "No.",
            "Um, no.",
            "I'm sorry, not now.",
            f"No thanks, {Girl.player_petname}.",
            "Yeah, sorry.",
            f"Not today, {Girl.player_petname}.",
            "Nah.",
            "Ha! Good one.",
            "No way.",
            "I'd rather not.",
            "Not interested.",
            "No thanks."]

        if Action_type in passive_Action_types:
            $ lines.append("You haven't earned it yet.")

            if Action_type == "handjob":
                $ lines.append("I'd really prefer not touching that.")

        elif Action_type in dildo_Action_types:
            $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
    elif Girl.tag == "Storm":
        $ lines = [
            "Hmm, no.",
            "I do not think so.",
            "No. Thank you.",
            "I would be uncomfortable with that. . .",
            "I would rather not. . .",
            f"Not now, {Girl.player_petname}.",
            "I would rather not right now though.",
            f"Perhaps later, {Girl.player_petname}. . .",
            f"Perhaps later, {Girl.player_petname}.",
            f"I do not think so, {Girl.player_petname}.",
            f"Not now, {Girl.player_petname}. . .",
            "Perhaps another time? . .",
            "I do not believe that would be appropriate. . .",
            "No, I do not think so.",
            f"No, I do not think so, {Girl.player_petname}.",
            f"I would rather not, {Girl.player_petname}.",
            "No way.",
            "No, thank you.",
            "I must refuse.",
            "Thank you, but no."]

        if Action_type in passive_Action_types:
            $ lines.append("I do not think you have earned that yet.")
            $ lines.append("I do not think that I will.")

            if Action_type == "footjob":
                $ lines.append("I am truly in no mood for footplay today. . .")

        elif Action_type in dildo_Action_types:
            $ lines.append(f"I don't think we need any toys, {Girl.player_petname}.")
            $ lines.append(f"We don't need any toys, do we, {Girl.player_petname}?")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Cute, but no.",
            "No thanks. . .",
            "You wish.",
            "Nope.",
            "I'm really not cool with that. . .",
            f"Let's not, ok {Girl.player_petname}?",
            "I'd rather not today. . .",
            f"Not now, {Girl.player_petname}.",
            "Nah.",
            "Um. . . no.",
            "No.",
            f"No thank you, {Girl.player_petname}.",
            "Yeah, sorry.",
            f"Not today, {Girl.player_petname}.",
            "I'm sorry, not now."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label previous_Action_rejected_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Fresh!",
            f"Not right now, {Girl.player_petname}. . .",
            f"Eh-eh, not anymore, {Girl.player_petname}.",]

        if Action_type in mouth_Action_types:
            $ lines.append("Sorry, keep your tongue in your mouth.")

            if Action_type == "suck_breasts":
                $ lines.append(f"Sorry, {Girl.player_petname} you aren't getting these in your mouth.")

        if Action_type in ass_Action_types:
            $ lines.append("The only thing you can do with my ass is kiss it," + Girl.player_petname + ".{p}. . .Don't get any ideas.")

        if Action_type in hand_Action_types:
            $ lines.append("Sorry, keep your hands out of there.")

            if Action_type == "fondle_breasts":
                $ lines.append(f"Sorry, {Girl.player_petname} you aren't touching these again.")
                $ lines.append("I think I'll let you know when I want you touching these again.")
            elif Action_type == "fondle_ass":
                $ lines.append("Sorry, hands off the booty.")
            elif Action_type in finger_Action_types:
                $ lines.append("I think you should keep your fingers to yourself.")

        if Action_type in ["sex", "anal"]:
            $ lines.append("Maybe you could go fuck yourself instead.")
        elif Action_type == "blowjob":
            $ lines.append("I think I've got the taste out of my mouth, thanks.")
        elif Action_type == "handjob":
            $ lines.append("Nope, not anymore, you'll have to go back to Internet porn.")
            $ lines.append("I think you can manage it yourself this time. . .")
        elif Action_type in dildo_Action_types:
            $ lines.append("Sorry, you can keep your toys to yourself.")
            $ lines.append("Sorry, you can keep your toys out of there.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "You had your shot.",
            f"Sorry, {Girl.player_petname}, maybe later?",
            "Fresh!",
            "I don't feel like it.",
            "Sorry, no more of that.",
            "I'm not feeling it today. . .",
            "No, not this time.",
            "Yeah, not again."]

        if Action_type in hand_Action_types:
            $ lines.append("Sorry, keep your hands out of there.")
            $ lines.append("Sorry, hands to yourself.")

            if Action_type == "fondle_breasts":
                $ lines.append("I think I'll let you know when I want you touching these again.")

        if Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("Keep your head out of there.")

        if Action_type == "handjob":
            $ lines.append("Sorry, maybe try a porn game or something.")

        if Action_type in ["sex", "anal"]:
            $ lines.append(f"Maybe just{Girl.like}fuck yourself, huh?")

        if Action_type in kinky_Action_types:
            $ lines.append(f"That's{Girl.like}totally off the table.")

            if Action_type in dildo_Action_types:
                $ lines.append("Sorry, you can keep your toys to yourself.")
                $ lines.append("Sorry, you can keep your toys out of there.")
    elif Girl.tag == "Emma":
        $ lines = [
            "I'm afraid you haven't earned back my good graces.",
            "I am sorry about that, but perhaps later?",
            "I don't feel like it.",
            "Sorry, no more of that.",
            "I'd really rather not. . .",
            "I'm afraid you'll just have to remember the last time.",
            f"I'm just not in the mood, {Girl.player_petname}.",
            f"I'm not in the mood, {Girl.player_petname}. . .",
            "You'll have to show me you're worth it again.",
            "Not under the circumstances."]

        if Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("Keep your head out of there.")
        elif Action_type in hand_Action_types:
            $ lines.append("I'm sorry, keep your hands to yourself.")
            $ lines.append("Keep your head out of there.")
            $ lines.append("Hands.")
        elif Action_type == "masturbation":
            $ lines.append("I'm sure you can find something else to watch.")
        elif Action_type == "handjob":
            $ lines.append("I'm sure you can figure out how to take care of that yourself.")
        elif Action_type in dildo_Action_types:
            $ lines.append("Sorry, you can keep your toys to yourself.")
            $ lines.append("Sorry, you can keep your toys out of there.")
    elif Girl.tag == "Laura":
        $ lines = [
            "You'll have to earn that back.",
            "I don't feel like it.",
            "Sorry, no more of that.",
            "I'm not into it today. . .",
            "I'm not into it right now.",
            "You'll know when it's time for that.",
            "Nah, not this time.",
            "Not right now.",
            "Not anymore."]

        if Action_type in passive_Action_types:
            $ lines.append("You'll have to earn it.")

            if Action_type == "handjob":
                $ lines.append("Just jack it or something.")
        elif Action_type in hand_Action_types:
            $ lines.append("Keep your hands to yourself.")
            $ lines.append("Sorry, keep your hands to yourself.")

            if Action_type in finger_Action_types:
                $ lines.append("Sorry, fingers outside.")
        elif Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("Keep your head out of there.")
        elif Action_type in dildo_Action_types:
            $ lines.append("Sorry, you can keep your toys to yourself.")
            $ lines.append("Sorry, you can keep your toys out of there.")
    elif Girl.tag == "Jean":
        $ lines = [
            "We've had enough of that.",
            "Eh, I think I'm ok for now. . .",
            "I don't feel like it.",
            "I'm not into it today. . .",
            "You'll know when it's time for that.",
            "Nah, not this time.",
            "Not right now.",
            "Not anymore."]

        if Action_type in passive_Action_types:
            $ lines.append("You'll have to earn that one. . .")
        elif Action_type in hand_Action_types:
            $ lines.append("Keep your hands to yourself.")
            $ lines.append("Sorry, keep your hands to yourself.")

            if Action_type in finger_Action_types:
                $ lines.append("You can keep those to yourself.")
        elif Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("Keep your tongue to yourself.")
        elif Action_type in dildo_Action_types:
            $ lines.append("Sorry, you can keep your toys to yourself.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Maybe just fuck one of the others.")
    elif Girl.tag == "Storm":
        $ lines = [
            "No, I do not think so.",
            ". . . I would rather not.",
            "Our time together was a memory.",
            f"I am just not in the mood, {Girl.player_petname}.",
            f"I am in no mood, {Girl.player_petname}. . .",
            "You shall have to display your worth to me again.",
            "Not under the circumstances."]

        if Action_type in dildo_Action_types:
            $ lines.append("Sorry, you can keep your toys to yourself.")
            $ lines.append("Sorry, you can keep your toys out of there.")

        if Action_type == "handjob":
            $ lines.append("I am certain you can take care of that yourself.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "I'm not into it right now.",
            "Sorry, no more of that.",
            "I'm not into it."]

        if Action_type in passive_Action_types:
            $ lines.append("You'll have to earn that.")
            $ lines.append("You'll have to earn that back.")

        if Action_type in hand_Action_types:
            $ lines.append("Keep your hands to yourself.")
            $ lines.append("Sorry, keep your hands to yourself.")

            if Action_type in finger_Action_types:
                $ lines.append("Sorry, keep your fingers outside.")

        if Action_type in ["eat_pussy", "eat_ass"]:
            $ lines.append("Keep your head out of there.")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label taboo_and_said_no_today_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I told you that wasn't appropriate!",
            "You already got your answer!",
            "I told you we can't do that in public!",
            "This is just way too exposed!",
            "Not in public!",
            "I already told you that I wouldn't do that out here!"]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type == "handjob":
            $ lines.append("I already told you that I wouldn't jerk you off in public!")
        elif Action_type == "blowjob":
            $ lines.append("I already told you that I wouldn't suck you off in public!")
        elif Action_type == "hotdog":
            $ lines.append("I told you that I didn't want you rubb'in up on me in public!")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("I already told you that I wouldn't bang you in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Kitty":
        $ lines = [
            "I told you not here!",
            f"I told you this was{Girl.like}too public!",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I said not in public!",
            "This is just way too exposed!",
            "I told you, not in public!",
            "I already told you. . . not in public!",
            "I{i}just{/i}" + Girl.like + "said, not in public!"]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Emma":
        $ lines = [
            "You've been warned.",
            "I told you I couldn't be seen like that.",
            "I told you that wasn't appropriate!",
            "I told you, this is too public!",
            "This is not an appropriate location for that. !",
            "I told you, this is too public!",
            "I refuse to do this in public.",
            "I already told you this is too public!",
            "I just told you. . . not in such an exposed location."]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop showing that thing around in public!")
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Laura":
        $ lines = [
            "I've had enough of this today.",
            "I told you, I couldn't be caught like that.",
            "I told you that wasn't appropriate!",
            "I said not in public.",
            "This is just way too exposed!",
            "Like I told you, not in public.",
            "I said not in public.",
            "I told you. . . this place is too exposed.",
            "I just told you. . . not in such an exposed location."]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
    elif Girl.tag == "Jean":
        $ lines = [
            "I've had enough of this today.",
            "I told you, I'm not comfortable in public.",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I told you I wasn't comfortable in public. . .",
            "Like I said, not in public.",
            "I'm not comfortable with that. . .",
            "I just told you. . . not in such an exposed location."]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
        elif Action_type == "masturbation":
            $ lines.append("I don't want to show off the goods like that!")
    elif Girl.tag == "Storm":
        $ lines = [
            f"This area is too public, {Girl.player_petname}.",
            "You already got your answer!",
            "This is not an appropriate location for that. !",
            "I told you, this is too public!",
            "I refuse to do this in public.",
            "I have already informed you. . . not in such an exposed location.",
            "I just informed you. . . not in such an exposed location."]

        if Action_type in hand_Action_types:
            $ lines.append("I told you not to touch me like that in public!")
        elif Action_type in dildo_Action_types:
            $ lines.append("Stop swinging that thing around in public!")
            $ lines.append("Stop showing that thing around in public!")
    elif Girl.tag == "Jubes":
        $ lines = [
            "I've had enough of this today.",
            "I told you, I couldn't be caught like that.",
            "You already got your answer!",
            "I told you that wasn't appropriate!",
            "I said not in public."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label trying_to_convince_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Ok, you're probably right. . .",
            "Well. . . ok.",
            "I guess.",
            "Heh, ok, alright.",
            "I suppose. . .",
            "You've got me there."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("I guess, whip it out.")

            if Action_type == "hotdog":
                $ lines.append("Well, sure, give it a rub.")
            elif Action_type == "titjob":
                $ lines.append("Fine. . . [She drools a bit into her cleavage].")
            elif Action_type == "hotdog":
                $ lines.append("Well, ok, put it here.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Oh. . . you're probably right. . .",
            "Ok, you're probably right. . .",
            "That's. . . true. . .",
            "You've got me there.",
            "Well, sure, ok.",
            "I suppose. . .",
            "That's. . . that's a good point. . .",
            "Well. . . ok.",
            "I guess.",
            "Heh, ok."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("I guess, whip it out.")

            if Action_type == "titjob":
                $ lines.append("Fine. . . [She drools a bit into her cleavage].")
            elif Action_type == "hotdog":
                $ lines.append("Well, ok, put it here.")
    elif Girl.tag == "Emma":
        $ lines = [
            "You present a compelling case. . .",
            "Ok, you're probably right. . .",
            "You're probably right. . .",
            "I can't exactly argue with that. . .",
            "I suppose. . .",
            "You raise a good point. . .",
            "You make a compelling argument.",
            "Oh, very well.",
            "Mmmmm.",
            "Oh, all right."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")
            $ lines.append("Very well, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("Fine, whip it out.")
            $ lines.append("Well, sure, come over here.")

            if Action_type == "titjob":
                $ lines.append("Fine. . . [She drools a bit into her cleavage].")

    elif Girl.tag == "Laura":
        $ lines = [
            "You make a good point. . .",
            "Ok, you're probably right. . .",
            "I suppose. . .",
            "You've got me there.",
            "You're probably right. . .",
            "I guess. . .",
            "Good point. . .",
            "Yeah, probably. . .",
            "Well. . . ok.",
            "I guess.",
            "Heh, ok."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("I guess, whip it out.")

            if Action_type == "titjob":
                $ lines.append("Fine. . . [She drools a bit into her cleavage].")
            elif Action_type == "hotdog":
                $ lines.append("Well, ok, put it here.")
    elif Girl.tag == "Jean":
        $ lines = [
            "You make a good point. . .",
            "Ok, you're probably right. . .",
            "I suppose. . .",
            "You've got me there.",
            "You're probably right. . .",
            "Yeah, sure. . .",
            "Yeah, probably. . .",
            "I guess. . .",
            "Good point. . .",
            "Well. . . ok.",
            "I guess.",
            "Heh, ok."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("I guess, whip it out.")

            if Action_type == "hotdog":
                $ lines.append("Well, ok, put it here.")
    elif Girl.tag == "Storm":
        $ lines = [
            "I. . . would. . .",
            "Well. . . I might at that. . .",
            "You may be correct. . .",
            "I cannot argue with that. . .",
            "I suppose you have a point. . .",
            "You do raise a worthy point. . .",
            "I suppose. . .",
            "You make a compelling argument.",
            "I cannot exactly argue with that. . .",
            "I suppose. . .",
            "You do raise a good point. . .",
            "Oh, very well.",
            "Mmmmm.",
            "Oh, all right."]

        if Action_type in insertion_Action_types:
            $ lines.append("Well, sure, stick it in.")
            $ lines.append("Very well, stick it in.")

        if Action_type in cock_Action_types:
            $ lines.append("Fine, come over here.")
            $ lines.append("Fine, show me.")

            if Action_type == "titjob":
                $ lines.append("Fine. . . [She drools a bit into her cleavage].")
    elif Girl.tag == "Jubes":
        $ lines = [
            "You make a good point. . .",
            "Um. . . maybe? . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label unconvinced_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"Tsk, not this time, {Girl.player_petname} that just seems. . . dirty.",
            "I really don't think that I would."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Um, not this time, {Girl.player_petname}, that's too. . .",
            "I really don't think so.",
            "I really don't think that I would."]
    elif Girl.tag == "Emma":
        $ lines = [
            f"I would, but still no, {Girl.player_petname}.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl.tag == "Laura":
        $ lines = [
            f"I would, but still no, {Girl.player_petname}.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl.tag == "Jean":
        $ lines = [
            f"I would, but still no, {Girl.player_petname}.",
            "I really don't think so.",
            "I don't think that I would."]
    elif Girl.tag == "Storm":
        $ lines = [
            f"I would, but still no, {Girl.player_petname}.",
            "I really do not think so.",
            "I do not think that I would."]
    elif Girl.tag == "Jubes":
        $ lines = [
            f"I would, but still no, {Girl.player_petname}.",
            "Doubt.",
            "I really doubt that. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label unsatisfied_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I didn't exactly get off there. . .",
            "That didn't really do it for me. . .",
            "Hmm, you seemed to get more out of that than me. . ."]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Could you have maybe paid more attention? . .",
            "Hmm, you seemed to get more out of that than me. . .",
            "I didn't get much out of that. . ."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Forgetting someone? . .",
            "That didn't do much for me. . ."]
    elif Girl.tag == "Emma":
        $ lines = [
            "Could you have perhaps been more attentive? . .",
            "Hmm, you seemed to get more out of that than I did. . .",
            "I'm afraid that didn't do much for me. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["I think you need to get back down there."]
    elif Girl.tag == "Storm":
        $ lines = [
            "I could have used some more attention to my needs. . .",
            "I am afraid that you got more out of that than I. . .",
            "I am afraid that did not do much for me. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label starting_to_get_bored_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Uh, that's nice, but. . ."]

        if Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
        elif Action_type in sex_Action_types:
            $ lines.append("Are you getting close here? I'm getting a little sore.")
        elif Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("Are you getting close here?")
            $ lines.append("You like it down there?")
            $ lines.append("You like how that feels, huh?")

            if Action_type == "titjob":
                $ lines.append("You like how those feel, huh?")
                $ lines.append("You're just going at them, huh?")
            elif Action_type == "blowjob":
                $ lines.append("Are you getting close here? My jaw's getting pretty sore.")
    elif Girl.tag == "Kitty":
        $ lines = ["Uh, that's nice, but. . ."]

        if Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("You like how that feels, huh?")
            $ lines.append("You like it down there?")
            $ lines.append(f"So are we{Girl.like}getting close here?")
            $ lines.append("Are you getting close here?")

            if Action_type == "titjob":
                $ lines.append("You're just going at them, huh?")
                $ lines.append("Are they keeping you satisfied?")
                $ lines.append("You like how those feel, huh?")
        elif Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
            $ lines.append("What are you even?")
        elif Action_type in sex_Action_types:
            $ lines.append("Are you getting close here? I'm getting a little sore.")
            $ lines.append(f"So are we{Girl.like}getting close here? This is not super pleasant. . .")
    elif Girl.tag == "Emma":
        $ lines = ["Mmmm I do enjoy that. . ."]

        if Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("You like how that feels, huh?")
            $ lines.append("So are we getting close?")
            $ lines.append("So are we getting close here?")
            $ lines.append("Are we getting close here?")

            if Action_type == "titjob":
                $ lines.append("They really are magnificent, aren't they?")
                $ lines.append("Lovely, aren't they?")
                $ lines.append("Luxurious, yes?")
        elif Action_type in sex_Action_types:
            $ lines.append("Are you getting close here? I'm getting a bit sore.")
            $ lines.append("You certainly are enthusiastic. . .")
        elif Action_type in ["suck_breasts", "eat_pussy", "eat_ass"]:
            $ lines.append("Isn't it just delicious?")

        if Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
            $ lines.append("Ungh, You're getting going there. . .")
    elif Girl.tag == "Laura":
        $ lines = [
            "This is kinda nice. . .",
            "Kinda nice, but. . .",
            "Mmmm. . ."]

        if Action_type in ["suck_breasts", "eat_pussy", "eat_ass"]:
            $ lines.append("Isn't it just delicious?")
        elif Action_type in sex_Action_types:
            $ lines.append("Are you getting close here? I'm getting bored.")
        elif Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("Are we getting close here?")
            $ lines.append("We getting close here?")
            $ lines.append("So are we getting close?")
            $ lines.append("Mmmm, you're enjoying that, huh?")
            $ lines.append("You seem to be enjoying yourself. . .")
            $ lines.append("Enjoying yourself?")

        if Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
            $ lines.append("Ungh, you're really getting in there. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            "This is kinda nice. . .",
            "Kinda nice, but. . .",
            "Mmmm. . ."]

        if Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("Mmmm, you're enjoying that, huh?")
            $ lines.append("Having fun there?")
            $ lines.append("You seem to be enjoying yourself. . .")
            $ lines.append("Ok, that good enough?")
            $ lines.append("Ok, had enough yet?")

            if Action_type == "blowjob":
                $ lines.append("Hey, how you doing up there? About done?")
        elif Action_type in ["suck_breasts", "eat_pussy", "eat_ass"]:
            $ lines.append("Isn't it just delicious?")

        if Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
            $ lines.append("'bout done there?")
            $ lines.append("Ungh, you're really getting in there. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "Oh, that is delightful. . .",
            "Mmmm. . ."]

        if Action_type in hand_Action_types:
            $ lines.append("Your hands are so warm. . .")

        if Action_type in finger_Action_types or Action_type in dildo_Action_types or Action_type in sex_Action_types:
            $ lines.append("Mmmm, yes. . . deeper. . .")

        if Action_type in below_Action_types:
            $ lines.append("What are you even doing down there?")
            $ lines.append("Ooh, watch it, watch it. . .")

        if Action_type in sex_Action_types:
            $ lines.append("Are you getting close? This is making me a bit sore. . .")
        elif Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("Are you nearly satisfied?")
            $ lines.append("So are you nearly finished?")
            $ lines.append("Are you nearly finished?")
            $ lines.append("You are quite enthusiastic. . .")

            if Action_type == "titjob":
                $ lines.append("You really seem to enjoy those. . .")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Ok, but, uh. . .",
            "Yeah, I like that too. . .",
            "Mmmm. . ."]

        if Action_type in ["handjob", "blowjob", "titjob", "footjob"]:
            $ lines.append("Having fun?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label definitely_bored_now_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"I'm getting rug-burn here {Girl.player_petname}. Can we do something else?",
            f"I'm getting a little tired, {Girl.player_petname}. Can we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            "Ow, i'm not used to this. Mind if we take a break?",
            "Can we be done with this now? I'm getting sore.",
            f"I'm . . .getting . . .worn out. . . here, . . {Girl.player_petname}.",
            f"I'm kinda done with this, {Girl.player_petname}.",
            "Can we. . . do something. . . else?"]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"Maybe we could try something else here {Girl.player_petname}?",
            f"You look like you're having fun there, but maybe we could{Girl.like}try something else?",
            f"{Girl.player_petname}, I know you're having fun down there, but maybe we could try something else.",
            f"{Girl.player_petname}, this is nice, but could we do something else?",
            f"{Girl.player_petname}, this is getting kind sore, maybe we could try something else.",
            f"{Girl.player_petname}, this is getting weird, maybe we could try something else.",
            f"Can we{Girl.Like}be done with this now? I'm getting sore.",
            "Are you getting close here? I'm cramping up.",
            f"Can we{Girl.Like}be done with this now? I'm getting sore.",
            f"Ouch, hand cramp, can we{Girl.like}take a break?",
            f"I'm getting rug-burn here {Girl.player_petname}. Can we do something else?",
            f"I'm{Girl.like}totally worn out here. Can we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            f"Ouch, foot cramp, can we{Girl.like}take a break?",
            "I'm . . .getting . . kinda tired. . . here. . .",
            "I'm . . .getting . . kinda tired. . . of this. . .",
            "Can we. . . do something. . . else?",
            "This is getting a bit dull."]
    elif Girl.tag == "Emma":
        $ lines = [
            f"Perhaps we could try something else, {Girl.player_petname}?",
            "You certainly seem to be enjoying yourself, but perhaps we could add some variety?",
            f"{Girl.player_petname}, I know you're having fun down there, but maybe we could try something else.",
            f"{Girl.player_petname}, this is nice, but could we do something else?",
            f"{Girl.player_petname}, this is getting kind sore, maybe we could try something else.",
            f"{Girl.player_petname}, this is getting weird, maybe we could try something else.",
            "Are you certain you didn't have anything else in mind?",
            "Are you about done? I'm a little tired of this.",
            "Could we be done here, my feet are getting sore.",
            "Hmm, I'm getting a bit of a cramp here.",
            "Mind if we take a break?",
            "I'm getting a bit worn out, could we settle this some other way?",
            "I'm getting a bit worn out here, could we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, foot cramp, could we take a short break?",
            "I'm . . .getting . . a bit. . . tired. . . here. . .",
            "I'm . . .getting . . a bit. . . tired. . . of this. . .",
            "Could we. . . do something. . . else?",
            "Can we. . . do something. . . else?",
            "I'm a bit bored by this."]
    elif Girl.tag == "Laura":
        $ lines = [
            f"Maybe it's time for something else, {Girl.player_petname}?",
            "Maybe change things up a little?",
            f"{Girl.player_petname}, could we try something different?",
            "This working for you?",
            "Are you getting close here? I'm bored.",
            "Ok, seriously, let's try something different.",
            "Hmm, this is boring, can we take a break?",
            "Seriously, can we do something else?",
            "I'm getting kinda bored. Can we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, this is getting a bit boring.",
            "Hey. . . could we. . . try something. . . else?",
            "Can we. . . do something. . . else?",
            "I'm kinda bored by this."]
    elif Girl.tag == "Jean":
        $ lines = [
            f"Maybe it's time for something else, {Girl.player_petname}?",
            "Maybe try something else?",
            f"{Girl.player_petname}, could we try something different?",
            "Nice, right?",
            "Hey, you about done up there?",
            "Ok, seriously, let's try something different.",
            "Ok, I'm bored now. Can we try something else?",
            "Ok, seriously, can't we do something else?",
            "Ok, that's enough of that. Can we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, my feet are cramping up here. . .",
            "Hey. . . you. . . about done. . . there?",
            "Can we. . . do something. . . else?",
            "Well this is not fun."]
    elif Girl.tag == "Storm":
        $ lines = [
            "I am sure that is fun, but could we try something different?",
            "Are you certain you didn't have anything else in mind?",
            "Are you about finished? I am growing tired of this.",
            "Could we be done here, my feet are getting sore.",
            "Hmm, I am developing a hand cramp here.",
            "Mind if we take a break?",
            "This is becoming uncomfortable, is there some way I could finish you off?",
            "My jaw is becoming uncomfortable, could we do something else?",
            f"{Girl.player_petname}, this is getting uncomfortable, maybe we could try something else.",
            "Hmm, foot cramp. Could we take a short break?",
            "I am . . .becoming . . a bit. . . worn out. . . here. . .",
            "This is . . .becoming . . rather. . . uncomfortable. . .",
            "Would you mind. . . a different. . . option?",
            "Could we. . . do something. . . else?",
            "I am getting rather tired of this."]
    elif Girl.tag == "Jubes":
        $ lines = ["Could we maybe try. . . something else?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label no_ass_to_mouth_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [f"No thanks, {Girl.player_petname}. Maybe a Handy instead?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label said_no_recently_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
            f"What part of \"no,\" did you not get, {Girl.player_petname}?"]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"{Girl.Like}no way, {Girl.player_petname}.",
            "I" + Girl.like + "{i}just{/i} told you \"no\"!"
            f"You don't{Girl.like}listen do you, {Girl.player_petname}.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
            "What did I" + Girl.like + "{i}just{/i} tell you " + Girl.player_petname + ".",
            f"You don't{Girl.like}listen do you, {Girl.player_petname}.",
            "I{i}just{/i}" + Girl.like + "told you \"no\"!"]
    elif Girl.tag == "Emma":
        $ lines = [
            f"Your persistence is doing you no favors, {Girl.player_petname}.",
            f"You need to learn to take\"no\" for an answer, {Girl.player_petname}.",
            "I {i}just{/i} refused, " + Girl.player_petname + ".",
            "I believe I just told you, \"no\"."
            f"What part of \"no,\" did you not get, {Girl.player_petname}?",
            f"Pay attention, {Girl.player_petname}.",
            f"I'm afraid that \"no\" is my final answer, {Girl.player_petname}."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Take a breath here, before you regret it.",
            f"I just told you no, {Girl.player_petname}.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
            f"Just told you I wouldn't, {Girl.player_petname}.",
            f"What part of \"no,\" did you not get, {Girl.player_petname}?",
            f"You should listen better, {Girl.player_petname}.",
            f"Sorry, {Girl.player_petname} \"no\"."]
    elif Girl.tag == "Jean":
        $ lines = [
            "I'm not used to repeating myself.",
            f"I just told you no, {Girl.player_petname}.",
            "I {i}just{/i} told you \"no,\" " + Girl.player_petname + ".",
            f"Just told you I wouldn't, {Girl.player_petname}.",
            f"What part of \"no,\" did you not get, {Girl.player_petname}?",
            f"Don't make me repeat myself again, {Girl.player_petname}.",
            "I don't repeat myself."]
    elif Girl.tag == "Storm":
        $ lines = [
            f"Do not persist in this, {Girl.player_petname}.",
            f"Your persistance is doing you no favors, {Girl.player_petname}.",
            f"You will need to accept a \"no\", {Girl.player_petname}.",
            f"What part of \"no,\" did you not get, {Girl.player_petname}?",
            f"I have made myself clear, {Girl.player_petname}.",
            f"I am afraid that \"no\" is my final answer, {Girl.player_petname}."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "I already told you, \"no\".",
            f"I just told you no, {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label said_no_today_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"I already told you \"no,\" {Girl.player_petname}.",
            "I already told you no, take a hint.",
            "What part of \"no\" don't you understand?",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"I told you \"no\" earlier {Girl.player_petname}."]
    elif Girl.tag == "Kitty":
        $ lines = [
            f"I{Girl.like}already told you \"no\"."
            f"{Girl.Like}take a lesson, {Girl.player_petname}.",
            f"I told you \"no,\" {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"I already{Girl.like}told you \"no\"."
            "I{i}just{/i}" + Girl.like + "told you \"no\" earlier!"]
    elif Girl.tag == "Emma":
        $ lines = [
            "I believe you know my answer on this matter.",
            f"I told you \"no,\" {Girl.player_petname}.",
            f"I already refused, {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"I said \"no,\" {Girl.player_petname}.",
            f"I believe I just told you \"no,\" {Girl.player_petname}."]
    elif Girl.tag == "Laura":
        $ lines = [
            "Don't make me tell you again today.",
            f"I told you \"no,\" {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"Told you \"no,\" {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            "I just told you \"no\"."
            f"I'm believe I just told you \"no,\" {Girl.player_petname}."]
    elif Girl.tag == "Jean":
        $ lines = [
            "Don't ask me again today.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"Told you \"no,\" {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"I told you \"no,\" {Girl.player_petname}.",
            "Not today.",
            f"I believe I just told you \"no,\" {Girl.player_petname}."]
    elif Girl.tag == "Storm":
        $ lines = [
            "I have already told you my answer.",
            "I believe you know my answer on this matter.",
            f"You will need to accept a \"no\", {Girl.player_petname}.",
            f"I already refused, {Girl.player_petname}.",
            f"I told you \"no,\" {Girl.player_petname}.",
            f"I already told you \"no,\" {Girl.player_petname}.",
            f"I said \"no,\" {Girl.player_petname}.",
            f"I believe that I just told you \"no,\" {Girl.player_petname}."]
    elif Girl.tag == "Jubes":
        $ lines = [
            "Don't make me tell you again today.",
            f"I told you \"no,\" {Girl.player_petname}."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label try_something_else_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            f"I know you're having fun, but maybe we could try something else {Girl.player_petname}.",
            f"{Girl.player_petname} this is getting uncomfortable, maybe we could try something else.",
            f"{Girl.player_petname} this is nice, but could we do something else?",
            f"{Girl.player_petname} I know you're having fun down there, but maybe we could try something else."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label used_to_action_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "You want some of this action?",
            "So you'd like another go?",
            "You can't stay away from this. . ."]

        if Action_type == "masturbation":
            $ lines.append("You sure do like to watch.")
            $ lines.append("So you'd like me to go again?")
            $ lines.append("You want to watch some more?")
            $ lines.append("You want me ta diddle myself?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("A little. . . [fist pumping hand gestures]?")
            $ lines.append("A little tender loving care?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another foot rub?")
            $ lines.append("So you'd like me to. . . [she rubs her foot along your leg]?")
            $ lines.append("So you'd like another foot rub?")
        elif Action_type == "titjob":
            $ lines.append("A little soft embrace?")
            $ lines.append("You want some of this action [jiggles her tits]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("You want me to pillow your crank?")
        elif Action_type == "blowjob":
            $ lines.append("You want some of this action [mimes blowing]?")
            $ lines.append("So you'd like another blowjob?")
            $ lines.append("A little. . . lick?")
            $ lines.append("You want me to wet your willy?")
            $ lines.append("You want me to slick your pole?")
            $ lines.append("You want me to grease your skids?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want me to ride your pole?")
            $ lines.append("You wanna dip your wick?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("You can't stay away from this booty.")
            $ lines.append("You want me to ride your pole?")
            $ lines.append("You wanna dip your wick?")
        elif Action_type == "hotdog":
            $ lines.append("A little. . . bounce?")
    elif Girl.tag == "Kitty":
        $ lines = [
            "You want some of this?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oooh, you want some of this?",
            "You can't stay away from this. . .",
            "So you'd like another round?",
            "You're really digging this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You like to watch me.")
            $ lines.append("You want me to get myself off?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("A little. . . [fist pumping hand gestures]?")
            $ lines.append("A little TLC?")
            $ lines.append("You want another rub?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another foot sesh?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
            $ lines.append("You want another rub?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("A little. . . puffpuff?")
            $ lines.append("A little soft embrace?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you wanna 'nother blowjob?")
            $ lines.append("A little. . . lick?")
            $ lines.append("You want me to suck you off?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You wanna slide into me?")
            $ lines.append("You gonna make me purr?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("I do have booty for days. . .")
            $ lines.append("You wanna slide into me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl.tag == "Emma":
        $ lines = [
            "You want more?",
            "So you'd like another?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I knew you enjoyed it. . .",
            "I suppose I am irresistible. . .",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Once more?"]

        if Action_type == "masturbation":
            $ lines.append("You really do like to watch.")
            $ lines.append("You enjoy watching me.")
            $ lines.append("You want me to take care of myself?")
        elif Action_type == "handjob":
            $ lines.append("More of this? [fist pumping hand gestures]")
            $ lines.append("Oh, did you want some attention?")
        elif Action_type == "footjob":
            $ lines.append("You'd like me to use my feet again?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("Mmmm, some. . . [she rubs her foot along your leg]?")
            $ lines.append("A little foot rub?")
        elif Action_type == "titjob":
            $ lines.append("You want some of these? [jiggles her tits]")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("A little. . . [bounces tits]?")
            $ lines.append("A little warm embrace?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("Are you asking if I'm hungry?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You'd like me to lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("Do you intend to make me melt?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "anal":
            $ lines.append("You'd like to stick it in my ass again?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl.tag == "Laura":
        $ lines = [
            "You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I must be better than I thought.",
            "I hope you don't plan on wearing me out.",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "I knew you enjoyed it. . .",
            "You're really into this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You like to watch.")
            $ lines.append("You really like to watch me.")
            $ lines.append("You want me to masturbate again?")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handy?")
            $ lines.append("You want a. . . [fist pumping hand gestures]?")
            $ lines.append("Another handjob?")
            $ lines.append("A little TLC?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("Another titjob?")
            $ lines.append("A little [points at her chest]?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to lick you?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("A little bj?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want to plow me?")
        elif Action_type == "anal":
            $ lines.append("You want to stick it in my ass again?")
            $ lines.append("You want to plow me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl.tag == "Jean":
        $ lines = [
            "You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, you want some of this?",
            "You'd like another round?",
            "I must be better than I thought.",
            "I knew you enjoyed it. . .",
            "I hope you don't plan on wearing me out.",
            "Oooh, you want some of this?",
            "So you'd like another round?",
            "You're really into this. . .",
            "Again?"]

        if Action_type == "masturbation":
            $ lines.append("You do like to watch.")
            $ lines.append("You'd like me to masturbate again?")
            $ lines.append("You like to watch me.")
        elif Action_type == "handjob":
            $ lines.append("So you'd like another handjob?")
            $ lines.append("You want a. . . [fist pumping hand gestures]?")
            $ lines.append("Another handjob?")
        elif Action_type == "footjob":
            $ lines.append("You want me to use my feet?")
            $ lines.append("So you'd like another footjob?")
            $ lines.append("A little foot rub?")
            $ lines.append("A little. . . [she rubs her foot along your leg]?")
        elif Action_type == "titjob":
            $ lines.append("You want some of this action [rubs her chest]?")
            $ lines.append("So you'd like another titjob?")
            $ lines.append("Another titjob?")
            $ lines.append("A little [points at her chest]?")
        elif Action_type == "blowjob":
            $ lines.append("You want me to [mimes blowing]?")
            $ lines.append("So you want another blowjob?")
            $ lines.append("You want me to lick you?")
            $ lines.append("You want me to suck you off?")
            $ lines.append("A BJ?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("You want to fuck me?")
            $ lines.append("You want to plow me?")
        elif Action_type == "anal":
            $ lines.append("You want to fuck me?")
            $ lines.append("You want to plow me?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl.tag == "Storm":
        $ lines = [
            "You want more?",
            "So you would like another?",
            "You want some more?",
            "You want some of this action?",
            "So you'd like another go?",
            "Oh, did you want some of this?",
            "You would like another round?",
            "I suppose that I can be irresistible. . .",
            "I could get used to this. . .",
            "Oooh, you wanted some of this?",
            "So you would like another round?",
            "I knew you would enjoy it. . .",
            "You really are into this. . .",
            "Once more?"]

        if Action_type == "masturbation":
            $ lines.append("You really do like to watch.")
            $ lines.append("You enjoy watching me do that?")
            $ lines.append("You want me to take care of myself?")
        elif Action_type == "handjob":
            $ lines.append("More of this? [fist pumping hand gestures]")
            $ lines.append("Oh, did you want some attention?")
            $ lines.append("So you'd like another handy?")
            $ lines.append("Another handjob?")
        elif Action_type == "footjob":
            $ lines.append("You would like me to use my feet again?")
            $ lines.append("So you would like another footjob?")
            $ lines.append("Mmmm, some. . . [she rubs her foot along your leg]?")
            $ lines.append("A little foot rub?")
        elif Action_type == "titjob":
            $ lines.append("You wish to use these? [jiggles her tits]")
            $ lines.append("So you would like another titjob?")
            $ lines.append(". . . [bounces tits]?")
            $ lines.append("You would like to give it a hug?")
        elif Action_type == "blowjob":
            $ lines.append(". . . [mimes blowing]?")
            $ lines.append("So you would like another blowjob?")
            $ lines.append("You wish for me to suck you off?")
            $ lines.append("Are you asking if I am hungry?")
        elif Action_type in dildo_Action_types:
            $ lines.append("You want me ta lube up your toy?")
        elif Action_type == "sex":
            $ lines.append("You want to stick it in my pussy again?")
            $ lines.append("Did you want me to ride you?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "anal":
            $ lines.append("You'd like to stick it in my ass again?")
            $ lines.append("Did you want me to ride you?")
            $ lines.append("You want me to ride you?")
        elif Action_type == "hotdog":
            $ lines.append("You want another rub?")
    elif Girl.tag == "Jubes":
        $ lines = ["Again?"]

        if Action_type == "masturbation":
            $ lines.append("You do enjoy watching.")
            $ lines.append("You really enjoy watching me.")
        elif Action_type == "blowjob":
            $ lines.append("You want me to shlick again?")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label switching_Action_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Mmm, so what else did you have in mind?"]
    elif Girl.tag == "Kitty":
        $ lines = [
            "Mmm, so what else did you have in mind?",
            "Ok, so what were you thinking?"]
    elif Girl.tag == "Emma":
        $ lines = [
            "Very well, what did you want to do?",
            "Mmm, so what else did you have in mind?",
            "Ok then, what were you thinking?"]
    elif Girl.tag == "Laura":
        $ lines = [
            "Ok, so what did you have in mind?",
            "Mmm, so what else did you have in mind?"]
    elif Girl.tag == "Jean":
        $ lines = [
            "Mmm, so what else did you have in mind?",
            "Ok, so what did you have in mind?"]
    elif Girl.tag == "Storm":
        $ lines = [
            "Very well, what did you want to do?",
            "Mmm, so what else did you have in mind?",
            "Ok then, what were you thinking?"]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label accepted_without_question_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = [
            "Well. . . ok.",
            "Sure, I guess.",
            "Sure!",
            "Heh, ok, alright.",
            "Okay.",
            "Hells yeah.",
            "I guess. . .",
            "Fine. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Well. . . ok.",
            "I suppose it would help to have something nice to look at. . .",
            "I've kind of needed this anyways. . .",
            "Sure!",
            "I guess I could. . . give it a go.",
            "Heh, ok, ok."]

        if Action_type == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")
        elif Action_type == "blowjob":
            $ lines.append("Fine. . . [She licks her lips].")
            $ lines.append("Well, sure, ahhhhhh.")
            $ lines.append("Yum.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in hand_Action_types:
            $ lines.append("Well, sure, give it a rub.")
        elif Action_type in dildo_Action_types:
            $ lines.append("Well, sure, stick it in.")
            $ lines.append("I guess I could. . . stick it in.")
        elif Action_type in cock_Action_types:
            $ lines.append("I guess I could. . . whip it out.")
            $ lines.append("Ok, lemme see it.")
            $ lines.append("I suppose, drop trou.")
            $ lines.append("Sure, whip it out.")
            $ lines.append("Well, sure, put'im here.")
    elif Girl.tag == "Kitty":
        $ lines = [
            "Sure, I guess.",
            "Ooooookay    .",
            "Ok. . . [She gestures for you to come over].",
            "Heh, ok, ok.",
            "Well. . . ok.",
            "Heh, ok.",
            "Sure!",
            "Um, yeah.",
            "Hells yeah.",
            "I guess we could do that.",
            "Ooooookay.",
            "Lol, ok, alright.",
            "Huh. Ok.",
            "Couldn't hurt having you around. . .",
            "Two birds with one stone. . .",
            "K.",
            "Sure, why not?",
            "Lol, ok."]

        if Action_type == "titjob":
            $ lines.append("Fine. . . [She drools a bit into her cleavage].")
        elif Action_type == "blowjob":
            $ lines.append("Yum.")
            $ lines.append("Ok. . . [She licks her lips].")
            $ lines.append("Well, sure, ahhhhhh.")
        elif Action_type in ["sex", "anal"]:
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in hand_Action_types:
            $ lines.append("Well, sure, give it a rub.")
        elif Action_type in active_Action_types:
            $ lines.append("You could, I guess.")
        elif Action_type in passive_Action_types:
            $ lines.append("I guess I could. . .")
        elif Action_type in dildo_Action_types:
            $ lines.append("I guess I could. . . stick it in.")
            $ lines.append("Well, sure, stick it in.")
        elif Action_type in cock_Action_types:
            $ lines.append("Cool, lemme see it.")
            $ lines.append("Well, sure, put it here.")
            $ lines.append("Sure, whip it out.")
    elif Girl.tag == "Emma":
        $ lines = [
            "Oh, I suppose.",
            "Fine. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Well, sure, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right.",
            "Well, ok.",
            "Well. . . ok.",
            "Mmmm.",
            "Sure, let me have it.",
            "Mmmm. . . [She licks her lips].",
            "Ok, fine.",
            "Well, sure, stick it in.",
            "Hmm. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok.",
            "Sure, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok.",
            "Well. . . fine, I accept.",
            "Sure!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I suppose we could do that.",
            "Allow me. . .",
            "Heh, ok, ok.",
            "Ok.",
            "It couldn't hurt having you around. . .",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
            $ lines.append("I'll do it.")

        if Action_type in cock_Action_types:
            $ lines.append("Well, give it here.")
    elif Girl.tag == "Laura":
        $ lines = [
            "Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Well, sure, put it here.",
            "Well. . . ok.",
            "Yum.",
            "Sure, whip it out.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Heh, ok.",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "Well. . . ok.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Well, sure, stick it in.",
            "Well. . . ok.",
            "Sure, I guess.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Well. . . fine, let's do it.",
            "Sure.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun.",
            "Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
    elif Girl.tag == "Jean":
        $ lines = [
            "Sure, I guess.",
            "Okay. . .   ",
            "Fine.",
            "Ok. . . Get over here. . .",
            "Ok, ok.",
            "Well, sure, put it here.",
            "Well. . . ok.",
            "Heh, ok.",
            "Sure. Ahhhhhh.",
            "Well. . . alright.",
            "Yum.",
            "Sure, whip it out.",
            "Ok. . . [She licks her lips].",
            "Alright, let's see it.",
            "Well, sure, stick it in.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Hells yeah.",
            "Sure, I guess.",
            "OK.",
            "Fine, lemme see it.",
            "I guess I could. . .",
            "Ok. . . [She gestures for you to come over].",
            "Well. . . fine, let's do it.",
            "We could, I guess.",
            "Hmmm, sure.",
            "Sounds fun.",
            "Well. . . ok.",
            "Sure.",
            "You could, I guess.",
            "Um, yeah.",
            "Well, sure, let me give it a rub.",
            "Very well.",
            "Nice!",
            "I guess we could do that.",
            "Ok, let me. . .",
            "Heh, ok, ok.",
            "Sure. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Sure, why not. . ."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")
    elif Girl.tag == "Storm":
        $ lines = [
            "Oh, I suppose we might.",
            ". . . Fine. [She gestures for you to come over]",
            "Ok, ok.",
            "Fine, come over here.",
            "Oh, very well.",
            "Mmmmm.",
            "Fine, show me.",
            "Fine. . . [She drools a bit into her cleavage].",
            "Oh, all right.",
            ". . . ok.",
            "Well. . . ok.",
            "Mmmm.",
            "Sure, let me have it.",
            "Mmmm. . . [She licks her lips].",
            "Ok, fine.",
            "Well, sure, stick it in.",
            "Sure!",
            "I guess I could. . . stick it in.",
            "Delightful.",
            "Hmm, ok, ok.",
            "Hmm, I suppose.",
            "Fine.",
            "Very well, bring it out.",
            "I suppose that I could. . .",
            "Fine. . . [She gestures for you to come over].",
            "Hmm, ok.",
            "Well. . . fine, I accept.",
            "Of course!",
            "We could, I suppose.",
            "Hmmm, yes.",
            "How could I refuse?",
            "Well. . . I suppose.",
            "Hmm, yes. Fine.",
            "Heh. Ok, ok.",
            "Very well then, let me give it a rub.",
            "Very well.",
            "I suppose that we could do that.",
            "Allow me. . .",
            "Fine.",
            "It could not hurt having you around. . .",
            "Very well.",
            "Sure, why not?",
            "[chuckles]. . . Fine."]

        if Action_type in passive_Action_types:
            $ lines.append("I would do this.")
            $ lines.append("I suppose that I could. . .")

        if Action_type in cock_Action_types:
            $ lines.append("Very well, give it here.")
    elif Girl.tag == "Jubes":
        $ lines = [
            "Sure, I guess.",
            "O-kay.",
            "Fine.",
            "Ok. . . [She gestures for you to come over].",
            "Ok, ok.",
            "Huh. Ok.",
            "Couldn't hurt. . .",
            "Alright.",
            "Sure.",
            "Heh, ok."]

        if Action_type in passive_Action_types:
            $ lines.append("I suppose I could. . .")

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_first_kiss_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["I've never really been able to do this, so I'm a bit excited to try. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["You are kinda cute. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["Well, I suppose it couldn't hurt. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["Worth a shot. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["Why not?"]
    elif Girl.tag == "Storm":
        $ lines = ["I would like that."]
    elif Girl.tag == "Jubes":
        $ lines = ["I guess we did get off to a poor start. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label less_excited_for_first_kiss_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["I guess it's worth a shot. . ."]
    elif Girl.tag == "Kitty":
        $ lines = ["I'll give it a go. . ."]
    elif Girl.tag == "Emma":
        $ lines = ["We could. . ."]
    elif Girl.tag == "Laura":
        $ lines = ["If you insist. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["I mean, whatever. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["I suppose."]
    elif Girl.tag == "Jubes":
        $ lines = ["I suppose we could. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_kiss_love_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Sure, why not?"]
    elif Girl.tag == "Kitty":
        $ lines = ["Smooches!"]
    elif Girl.tag == "Emma":
        $ lines = ["Mwa."]
    elif Girl.tag == "Laura":
        $ lines = ["Mmmmm. . ."]
    elif Girl.tag == "Jean":
        $ lines = ["MmMmmmm. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Hrm. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Mmmm. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label excited_for_kiss_devotion_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["If you wish."]
    elif Girl.tag == "Kitty":
        $ lines = ["Sure, ok."]
    elif Girl.tag == "Emma":
        $ lines = ["Of course."]
    elif Girl.tag == "Laura":
        $ lines = ["If you want."]
    elif Girl.tag == "Jean":
        $ lines = ["Ok. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Very well. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Sure. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label kiss_addicted_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Hm. . . ok, let's do this."]
    elif Girl.tag == "Kitty":
        $ lines = ["I kinda have to."]
    elif Girl.tag == "Emma":
        $ lines = [". . . yes."]
    elif Girl.tag == "Laura":
        $ lines = ["I have to."]
    elif Girl.tag == "Jean":
        $ lines = ["Um. . . yeah. . ."]
    elif Girl.tag == "Storm":
        $ lines = [". . . yes. . ."]
    elif Girl.tag == "Jubes":
        $ lines = ["Oh yes. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label kiss_accepted_lines(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = ["Hmm, ok."]
    elif Girl.tag == "Kitty":
        $ lines = ["Yeah, whatever."]
    elif Girl.tag == "Emma":
        $ lines = ["Very well."]
    elif Girl.tag == "Laura":
        $ lines = ["Sure."]
    elif Girl.tag == "Jean":
        $ lines = ["Whatever. . ."]
    elif Girl.tag == "Storm":
        $ lines = ["Fine."]
    elif Girl.tag == "Jubes":
        $ lines = ["Sure, ok. . ."]

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return

label template(Girl, Action_type):
    if Girl.tag == "Rogue":
        $ lines = []
    elif Girl.tag == "Kitty":
        $ lines = []
    elif Girl.tag == "Emma":
        $ lines = []
    elif Girl.tag == "Laura":
        $ lines = []
    elif Girl.tag == "Jean":
        $ lines = []
    elif Girl.tag == "Storm":
        $ lines = []
    elif Girl.tag == "Jubes":
        $ lines = []

    $ line = renpy.random.choice(lines)

    Girl.voice "[line]"

    return
