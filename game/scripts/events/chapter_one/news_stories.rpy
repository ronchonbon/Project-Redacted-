init python:

    def chapter_one_news_story_A():
        label = "chapter_one_news_story_A"

        conditions = [
            "chapter == 1",
            "Player.destination != Player.location"]

        conversation = False

        priority = False

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_news_story_A:
    "You pass by a TV tuned to the news."
    ch_reporter ". . . a widespread epidemic of anti-mutant hysteria has swept the country following the reappearance of the notorious mutant-hunting Sentinels. . ."

    return

init python:

    def chapter_one_news_story_B():
        label = "chapter_one_news_story_B"

        conditions = [
            "chapter == 1",
            "Player.destination != Player.location"]

        conversation = False

        priority = False

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_news_story_B:
    "You overhear another student watching a news clip on their phone."
    ch_reporter ". . . among the confirmed dead is Colonel Michael Rossi. Government officials insist the crash was the result of a tragic onboard computer malfunction. . ."

    return

init python:

    def chapter_one_news_story_C():
        label = "chapter_one_news_story_C"

        conditions = [
            "chapter == 1",
            "Player.destination != Player.location"]

        conversation = False

        priority = False

        repeatable = False

        return EventClass(label, conditions, conversation = conversation, priority = priority, repeatable = repeatable)

label chapter_one_news_story_C:
    "You scroll past headlines as you walk."
    "Pandemonium at Kennedy International Airport:{p}Dozens Injured and Two 747s Damaged in Apparent Mutant Conflict."

    return
