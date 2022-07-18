init -1:

    default stack_depth = 0

    default day = 1
    default round = 100
    default time_options = ["morning", "midday", "evening", "night", "late night"]
    default time_index = 2
    default current_time = time_options[time_index]
    default week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    default weekday = 6
    default day_of_week = week[weekday]

    default Present = []
    default Nearby = []
    default Students = []
    default Staff = []
    default Professor = []
    default active_Girls = []
    default all_Girls = []

    define stage_far_far_left = 0.15
    define stage_far_left = 0.25
    define stage_left = 0.35
    define stage_center = 0.5
    define stage_right = 0.65
    define stage_far_right = 0.75
    define stage_far_far_right = 0.85

    define location_names = {
        "bg_campus": "Campus",
        "bg_dangerroom": "Danger Room",
        "bg_entrance": "Main Entrance",
        "bg_jean": "[Jean.name]'s Bedroom",
        "bg_kitty": "[Kitty.name]'s Bedroom",
        "bg_laura": "[Laura.name]'s Bedroom",
        "bg_movies": "Movie Theater",
        "bg_player": "[Player.name]'s Bedroom",
        "bg_pool": "Pool",
        "bg_rogue": "[Rogue.name]'s Bedroom",
        "bg_shower": "Showers"}

    define all_Clothing_types = ["face_tattoos", "face_piercings", "makeup", "gag",
        "face_inner_accessory", "hair", "face_outer_accessory",
        "body_tattoos", "body_piercings", "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define intrinsic_Clothing_types = ["face_tattoos", "face_piercings",
        "body_tattoos", "body_piercings"]

    define removable_Clothing_types = ["makeup", "gag",
        "face_inner_accessory", "face_outer_accessory",
        "buttplug",
        "nipple_accessories", "underwear", "hose",
        "bodysuit", "rope",
        "socks", "pants", "skirt", "boots",
        "bra", "dress", "top",
        "neck", "gloves", "sleeves", "belt", "suspenders",
        "jacket", "cloak"]

    define breast_hiding_Clothing_types = ["bodysuit", "bra", "dress", "top", "jacket"]
    define underwear_hiding_Clothing_types = ["bodysuit", "pants", "skirt", "dress", "top", "jacket"]
    define pussy_hiding_Clothing_types = ["underwear", "bodysuit", "pants", "skirt", "dress"]
    define thigh_covering_Clothing_types = ["bodysuit", "hose", "pants", "skirt", "boots", "dress"]
    define feet_covering_Clothing_types = ["hose", "socks", "boots"]

    define Clothing_coverage = {"face_tattoos": [],
        "face_piercings": [],
        "makeup": [],
        "gag": [],
        "face_inner_accessory": [],
        "hair": [],
        "face_outer_accessory": [],
        "body_tattoos": [],
        "body_piercings": [],
        "buttplug": ["underwear"],
        "nipple_accessories": ["bodysuit", "bra", "dress", "top"],
        "underwear": ["hose", "bodysuit", "pants", "suspenders", "boots"],
        "hose": ["bodysuit", "pants", "socks", "boots"],
        "bodysuit": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "rope": ["bra", "dress", "top", "jacket", "cloak", "socks", "pants", "skirt", "boots"],
        "socks": ["boots"],
        "pants": ["boots", "suspenders"],
        "skirt": ["boots", "suspenders"],
        "boots": [],
        "bra": ["dress", "top", "suspenders", "jacket", "cloak"],
        "dress": ["top", "belt", "suspenders", "jacket", "cloak", "boots"],
        "top": ["belt", "suspenders", "jacket", "cloak"],
        "neck": [],
        "gloves": [],
        "sleeves": ["jacket"],
        "belt": ["suspenders"],
        "suspenders": ["jacket", "cloak"],
        "jacket": ["cloak"],
        "cloak": []}

    define job_Action_types = ["blowjob"]
    define sex_Action_types = ["sex", "anal"]

    define cock_Action_types = ["blowjob", "sex", "anal"]

    define active_Action_types = ["sex", "anal"]
    define passive_Action_types = ["blowjob"]

    define primary_Action_types = [
        "blowjob",
        "sex", "anal"]
    define secondary_Action_types = []

    define all_Action_types = [
        "blowjob",
        "sex", "anal"]

    define Emma_harden = ImageDissolve("images/wipes/Emma_harden.jpg", 0.5, 8)
    define Mystique_dissolve = ImageDissolve("images/wipes/Mystique_dissolve.jpg", 1.0, 8)

    define ch_p = Character("[Player.name]", who_color = "#87CEEB")
    define ch_p_nvl = Character("[Player.name]", kind = nvl)

    define ch_r = Character("[Rogue.name]", who_color = "#85BB65", image = "Rogue_sprite")
    define ch_r_nvl = Character("[Rogue.name]", kind = nvl)