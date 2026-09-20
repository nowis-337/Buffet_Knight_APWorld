

from collections.abc import Mapping
from typing import Any, Callable, Optional

# Imports base Archipelago autoworld.
from worlds.AutoWorld import World

from BaseClasses import Entrance, Region, CollectionState, Item, Location

# Imports our files. We use capitals for the paths.
from . import items, locations, options, regions, rules, Web_World
import logging
logger = logging.getLogger("Check The Back")
logger.setLevel(logging.WARNING)






class CTBWorld(World):
    """
    Desc coming soon
    """
    game = "Check The Back"

    #Sawyer: Webworld will be important eventually so we might as well add that now.
    web = Web_World.CheckTheBackWebWorld()

    #options_dataclass = options.CheckTheBackOptions
    #options: options.CheckTheBackOptions

    #Sawyer: We used to define these here, but we'll do it in Regions and Items instead.
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = {key: item.code for (key, item) in items.item_table.items()}

    item_name_groups = items.ctb_item_name_groups

    #Sawyer: These are iterative values we can check later.
    partyMembers = 0

    @staticmethod
    def connect_2way(r1: Region, r2: Region, rule: Callable[[CollectionState], bool]):
        #Credit Emily, thank you!
        r1.connect(connecting_region=r2, rule=rule)
        r2.connect(connecting_region=r1, rule=rule)

    origin_region_name = "Hallway"

    #Sawyer: These are important rules, check APQuest for an explanation.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    #Sawyer: Time to make items, of course!
    def create_item(self, name: str) -> items.CTBItem:
        return items.create_item(self, name)

    #Sawyer: We should make sure we have filler items too.
    #Sawyer: ATM these will just be Heal Tokens but honestly most Tokens work, maybe even some weak cards.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        name = self.collect_item(state, item)
        num = 1
        if name:
            state.add_item(name, self.player)
            self.iterate_collectibles(state, name, num)

            return True
        return False

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        name = self.collect_item(state, item, True)
        num = -1
        if name:
            state.remove_item(name, self.player)
            self.iterate_collectibles(state, name, num)


            return True
        return False

    def iterate_collectibles(self, state:CollectionState, name, num) -> None:
        # Iterate Party Members
        if name in items.party_members:
            if state.count(name, self.player) < 2:
                state.prog_items[self.player]["Party"] += num
                if state.prog_items[self.player]["Party"] > 7:
                    state.prog_items[self.player]["Party"] = 7

        # Iterate Keys
        if name == "Locker Key":
            state.prog_items[self.player]["Locker"] += num
        if name == "Broom and Dustpan":
            state.prog_items[self.player]["Broom"] += num
        if name == "Soak":
            state.prog_items[self.player]["Soak"] += num
        if name == "Fire Extinguisher":
            state.prog_items[self.player]["Fire"] += num
        if name == "Ventilate":
            state.prog_items[self.player]["Vent"] += num
