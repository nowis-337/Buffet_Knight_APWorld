

from collections.abc import Mapping
from typing import Any, Callable, Optional

# Imports base Archipelago autoworld.
from worlds.AutoWorld import World

from BaseClasses import Entrance, Region, CollectionState, Item, Location

# Imports our files. We use capitals for the paths.
from . import items, locations, options, regions, rules, Web_World
import logging
logger = logging.getLogger("Silver Daze")
logger.setLevel(logging.WARNING)






class SDWorld(World):
    """
    Silver Daze is a 2025 Coming-of-Age RPG where you collect cards and battle monsters to save a fractured world.
    The game includes a comprehensive randomizer mode in which the player collects keys and party members to access
    new locations.
    """
    game = "Silver Daze"

    #Sawyer: Webworld will be important eventually so we might as well add that now.
    web = Web_World.SilverDazeWebWorld()

    options_dataclass = options.SilverDazeOptions
    options: options.SilverDazeOptions

    #Sawyer: We used to define these here, but we'll do it in Regions and Items instead.
    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = {key: item.code for (key, item) in items.item_table.items()}

    item_name_groups = items.sd_item_name_groups

    #Sawyer: These are iterative values we can check later.
    partyMembers = 0

    @staticmethod
    def connect_2way(r1: Region, r2: Region, rule: Callable[[CollectionState], bool]):
        #Credit Emily, thank you!
        r1.connect(connecting_region=r2, rule=rule)
        r2.connect(connecting_region=r1, rule=rule)

    #Sawyer: You start in Geo's Room, after all.
    origin_region_name = "GeoRoom"

    #Sawyer: These are important rules, check APQuest for an explanation.
    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    #Sawyer: Time to make items, of course!
    def create_item(self, name: str) -> items.SDItem:
        return items.create_item(self, name)

    # def pre_fill(self):
    #     state = CollectionState(self.multiworld)
    #     state.sweep_for_advancements()  # breakpoint here, step through the function to see what it's doing
    #     print(state.prog_items)

    #Sawyer: We should make sure we have filler items too.
    #Sawyer: ATM these will just be Heal Tokens but honestly most Tokens work, maybe even some weak cards.
    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        emblempool = self.options.emblempool
        if (emblempool < self.options.emblemcount and self.options.goal == 2):
            logger.warning(
                f"Silver Daze ({self.player_name}): "
                f"There are fewer emblems in the pool than required to beat the game. "
                f"The difference will be added to the pool."
            )

        if (self.options.chippool < self.options.chipcount and self.options.goal == 3):
            logger.warning(
                f"Silver Daze ({self.player_name}): "
                f"There are fewer Chaos Chips in the pool than required to beat the game. "
                f"The difference will be added to the pool."
            )
        if self.options.hintchips == 1 and self.options.goal == 3:
            self.options.start_hints.value.add("Chaos Chip")


    # #Sawyer: Slotdata currently contains Goal.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # This is just options.
        return self.options.as_dict(
            "minibosses","wardens","chaoswardens","omni","shops","recollections","starstuds","goal",
            "omniscaling","emblemcount","chipcount","disableenemylevelslider"
        )

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

        # Iterate Collectibles
        if name == "Starstud":
            state.prog_items[self.player]["Starstuds"] += num
        if name == "Memory Emblem":
            state.prog_items[self.player]["Memory Emblems"] += num
        if name == "Chaos Chip":
            state.prog_items[self.player]["Chaos Chip"] += num

        # Iterate Keys
        if name == "Red Key":
            state.prog_items[self.player]["Red"] += num
        if name == "Orange Key":
            state.prog_items[self.player]["Orange"] += num
        if name == "Yellow Key":
            state.prog_items[self.player]["Yellow"] += num
        if name == "Green Key":
            state.prog_items[self.player]["Green"] += num
        if name == "Blue Key":
            state.prog_items[self.player]["Blue"] += num
        if name == "Purple Key":
            state.prog_items[self.player]["Purple"] += num
        if name == "Black Key":
            state.prog_items[self.player]["Black"] += num
