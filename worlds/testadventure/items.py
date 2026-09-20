from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import TAWorld

ITEM_NAME_TO_ID = {
    "Red Key": 1,
    "Pink Key": 2,
    "Yellow Key": 3,
    "Blue Key": 4,
    "Crystal 1": 5,
    "Crystal 2": 6,
    "Crystal 3": 7,
    "Crystal 4": 8,
    "Crystal 5": 9,
    "Dungeon Key 1": 10,
    "Dungeon Key 2": 11,
    "Dungeon Key 3": 12,
    "Filler Loot": 30,
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    "Red Key": ItemClassification.progression,
    "Pink Key": ItemClassification.progression,
    "Yellow Key": ItemClassification.progression,
    "Blue Key": ItemClassification.progression,
    "Crystal 1": ItemClassification.progression,
    "Crystal 2": ItemClassification.progression,
    "Crystal 3": ItemClassification.progression,
    "Crystal 4": ItemClassification.progression,
    "Crystal 5": ItemClassification.progression,
    "Dungeon Key 1": ItemClassification.progression,
    "Dungeon Key 2": ItemClassification.progression,
    "Dungeon Key 3": ItemClassification.progression,
    "Filler Loot": ItemClassification.filler,

}

class TAItem(Item):
    game = "Test Adventure"



def get_random_filler_item_name(world: TAWorld) -> str:
    return "Filler Loot"


def create_item_with_correct_classification(world: TAWorld, name: str) -> TAItem:
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]
    return TAItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: TAWorld) -> None:
    itempool: list[Item] = [
        world.create_item("Red Key"),
        world.create_item("Pink Key"),
        world.create_item("Yellow Key"),
        world.create_item("Blue Key"),

        world.create_item("Crystal 1"),
        world.create_item("Crystal 2"),
        world.create_item("Crystal 3"),
        world.create_item("Crystal 4"),
        world.create_item("Crystal 5"),

        world.create_item("Dungeon Key 1"),
        world.create_item("Dungeon Key 2"),
        world.create_item("Dungeon Key 3"),
    ]


    #Fillers
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]
    world.multiworld.itempool += itempool

