from __future__ import annotations

from typing import TYPE_CHECKING
import typing

from BaseClasses import Item, ItemClassification

from worlds.AutoWorld import World, WebWorld
import logging

logger = logging.getLogger("Check The Back ")
logger.setLevel(logging.WARNING)

if TYPE_CHECKING:
    from .world import CTBWorld

class CTBItem(Item):
    game = "Check The Back "




class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler
    category: str = 'Item'
    max_quantity: int = 1
    weight: int = 1


# Item groups for easy management

party_members = {
    "Amy": ItemData(3002, ItemClassification.progression, "Party"),
    "Mel": ItemData(3003, ItemClassification.progression, "Party"),

}

skills = {
    "Soak": ItemData(5002, ItemClassification.progression, "Skill"),
    "Ventilate": ItemData(5003, ItemClassification.progression, "Skill"),
    "Fire Extinguisher": ItemData(5004, ItemClassification.progression, "Skill"),
    "Deep Clean": ItemData(5005, ItemClassification.useful, "Skill"),
    "Restock": ItemData(5006, ItemClassification.useful, "Skill"),
    "Spot Sweep": ItemData(5008, ItemClassification.useful, "Skill"),
}

equips = {
    "Latex Gloves": ItemData(2001, ItemClassification.useful, "Equipment"),
    "Abrasive Sponge": ItemData(2002, ItemClassification.useful, "Equipment"),
}

keys = {
    "Locker Key": ItemData(2003, ItemClassification.progression, "Key"),
    "Broom and Dustpan": ItemData(2004, ItemClassification.progression, "Key"),
}

ctb_item_name_groups = {
    "Party": {key for key, val in party_members.items()},
    "Skills": {key for key, val in skills.items()},
    "Equips": {key for key, val in equips.items()},
    "Keys": {key for key, val in keys.items()},
}

filler = {
    "Useless Filler Trash": ItemData(2005, ItemClassification.filler, "Key"),
}

item_table = {
    # This includes all entries in those other dicts in this one
    **party_members,
    **skills,
    **equips,
    **keys,
    **filler,
}


#Sawyer: This should give us some random fillers. Let's look into adding traps later.
def get_random_filler_item_name(world: CTBWorld) -> str:
    fillers = [
        "Useless Filler Trash"
    ]

    randomResult = world.random.randint(0, len(fillers) - 1)
    return fillers[randomResult]





def create_all_items(world: CTBWorld):
    itempool = []


    # for name in item_table:
    #     itempool.append(world.create_item(name))
    for name in party_members:
        for x in range(0, party_members[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in skills:
        for x in range(0, skills[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in equips:
        for x in range(0, equips[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in keys:
        for x in range(0, keys[name].max_quantity):
            itempool.append(world.create_item(name))

    #If we still need more filler after that, add filler.
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def create_item(self, name: str) -> CTBItem:
    item_data = item_table[name]
    item = CTBItem(name, item_data.classification, item_data.code, self.player)
    return item


