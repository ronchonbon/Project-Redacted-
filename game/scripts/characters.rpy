init python:

    import copy

    class PlayerClass(object):
        def __init__(self, name, **properties):
            self.name = name

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.skin_color = properties.get("skin_color", "green")

            self.level = 1
            self.XP = 0

            self.naked = False
            self.cock_out = False

            self.destination = "bg_entrance"
            self.location = "bg_entrance"

            self.focused_Girl = None
            self.Phonebook = []
            self.Party = []
            self.Keys = []
            self.Harem = []

            self.income = 12
            self.cash = 20

            self.inventory = []

            self.primary_Action = ActionClass(None, None)
            self.secondary_Action = ActionClass(None, None)

            self.History = HistoryClass(default = False)
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

    class GirlClass(object):
        def __init__(self, name, **properties):
            self.name = name
            self.tag = name
            self.names = [name]

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.level = 1
            self.XP = 0

            self.love = properties.get("love", 0)
            self.devotion = properties.get("devotion", 0)
            self.trust = properties.get("trust", 0)
            self.desire = properties.get("desire", 0)

            self.brows = "normal"
            self.eyes = "normal"
            self.mouth = "normal"
            self.blushing = ""

            # sprite_layer = [background_characters (eg. teachers), midground (eg. pool mask), midground_characters (eg. students), foreground (eg. desks), foreground_characters (eg. Present), Player.focused_Girl, cover (eg. fog)]
            self.sprite_location = stage_center
            self.sprite_layer = 6

            self.destination = "hold"
            self.location = "hold"
            self.home = f"bg_{name.lower()}"

            self.History = HistoryClass()
            self.recent_History = self.History.recent
            self.daily_History = self.History.daily
            self.permanent_History = self.History.permanent

            self.Wardrobe = WardrobeClass()
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            self.primary_Action = ActionClass(None, None)
            self.secondary_Action = ActionClass(None, None)

            self.petname = self.name
            self.petnames = [self.name]

            if self.tag == "Rogue":
                self.player_petname = "Sugar"
                self.player_petnames = [self.player_petname, Player.name]

            all_Girls.append(self)

            self.default_Outfits()

        def travel(self):
            possible_locations = []

            possible_locations.append(self.home)

            if time_index < 3:
                possible_locations.append("bg_campus")

            if time_index < 3 and weekday > 4:
                possible_locations.append("bg_pool")
            elif time_index in [1, 2]:
                possible_locations.append("bg_pool")

            renpy.random.shuffle(possible_locations)

            self.destination = possible_locations[0]

            return

        def try_on(self, Clothing):
            self.Outfit.change_into(Clothing)

            return

        def take_off(self, type):
            self.Outfit.change_out_of(type)

            return

        def give(self, Clothing):
            self.Wardrobe.add_Clothing(Clothing)

            return

        def change_into(self, Clothing_name):
            if Clothing_name not in self.Wardrobe.Clothes.keys():
                self.voice("I don't have a piece of clothing named [Clothing_name].")

                return

            self.Outfit.change_into(self.Wardrobe.Clothes[Clothing_name])

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def change_out_of(self, type):
            self.Outfit.change_out_of(type)

            self.Wardrobe.temp_Outfit = copy.deepcopy(self.Outfit)

            return

        def undress(self, instant = False):
            self.Outfit.undress(instant = instant)

            return

        def expose_breasts(self):
            for type in reversed(self.Outfit.hide_breasts):
                if self.Clothes[type].number_of_states > 2:
                    self.Clothes[type].state += 2

                    renpy.pause(0.1)
                elif self.Clothes[type].number_of_states == 1:
                    self.Clothes[type].take_off()
                else:
                    self.Outfit.remove_Clothing(type)

                    renpy.pause(0.1)

            return

        def expose_underwear(self):
            for type in reversed(self.Outfit.hide_underwear):
                self.Clothes[type].take_off()

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def expose_pussy(self):
            for type in reversed(self.Outfit.hide_pussy):
                self.Clothes[type].take_off()

                if self.Clothes[type].state < 1:
                    self.Outfit.remove_Clothing(type)

            return

        def fix_clothing(self):
            for type in removable_Clothing_types:
                if self.Wardrobe.temp_Outfit.Clothes[type] and not self.Clothes[type]:
                    self.Wardrobe.temp_Outfit.Clothes[type].state = self.Wardrobe.temp_Outfit.Clothes[type].undressed_state

                    self.Outfit.add_Clothing(self.Wardrobe.temp_Outfit.Clothes[type])

                    renpy.pause(0.2)

                if self.Clothes[type] and self.Clothes[type].state > 0:
                    self.Clothes[type].put_on()

            return

        def add_Outfit(self, Outfit):
            self.Wardrobe.add_Outfit(Outfit)

            return

        def remove_Outfit(self, name):
            self.Wardrobe.remove_Outfit(name)

            return

        def change_Outfit(self, name = None, instant = False):
            if not name:
                name = self.Wardrobe.public_Outfit.name

            if name not in self.Wardrobe.Outfits.keys():
                self.voice("I don't have an outfit named [name].")

                return

            self.Wardrobe.change_Outfit(self.Wardrobe.Outfits[name], instant = instant)
            self.Outfit = self.Wardrobe.current_Outfit
            self.Clothes = self.Outfit.Clothes

            return

        def choose_Outfits(self):
            self.Wardrobe.choose_Outfits()

            return

        def default_Outfits(self):
            default = OutfitClass("default", wear_in_public = True, wear_in_private = True)
            alternate = OutfitClass("alternate", wear_in_public = True, wear_in_private = True)

            if self.tag == "Rogue":
                default.update_Clothes({"hair": Evolutions_hair(self)})
                alternate.update_Clothes({"hair": Evolutions_hair(self)})

            for Outfit in [default, alternate]:
                self.Wardrobe.Outfits.update({Outfit.name: Outfit})

            for Outfit in self.Wardrobe.Outfits.values():
                for Clothing in Outfit.Clothes.values():
                    if Clothing.name:
                        self.Wardrobe.add_Clothing(Clothing)

            self.Wardrobe.choose_Outfits()
            self.change_Outfit(self.Wardrobe.public_Outfit.name, instant = True)

            return

    class NPCClass(object):
        def __init__(self, name, **properties):
            self.name = name

            self.voice = properties.get("voice", None)
            self.text = properties.get("text", None)

            self.sprite_location = stage_center
