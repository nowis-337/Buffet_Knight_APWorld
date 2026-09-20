from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import TAWorld

LOCATION_NAME_TO_ID = {

    #Dungeon 1
    "Dungeon 1 Chest 1": 1,
    "Dungeon 1 Chest 2": 2,

    #Dungeon 2
    "Dungeon 2_1 Chest 1": 3,
    "Dungeon 2_2 Chest 1": 4,
    "Dungeon 2_2 Chest 2": 5,

    #Dungeon 3
    "Dungeon 3 Chest 1": 6,
    "Dungeon 3 Chest 2": 7,

    #Dungeon 4
    "Dungeon 4 Chest 1": 8,
    "Dungeon 4 Chest 2": 9,

    #Dungeon 5
    "Dungeon 5_1 Chest 1": 10,
    "Dungeon 5_2 Boss Drop": 11,
    "Dungeon 5_3 Missable Chest": 12,

    #Misc Treasures
    "Treasure Red": 13,
    "Treasure Pink": 14,
    "Treasure Yellow": 15,
    "Treasrue Blue": 16,

    "Overworld 2 Chest 1": 17,
    "Overworld 2 Chest 2": 18
}

class TALocation(Location):
    game = "Test Adventure"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: TAWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: TAWorld) -> None:
    #Dungeon 1
    world.get_region("Dungeon 1").add_locations(get_location_names_with_ids([
        "Dungeon 1 Chest 1",
        "Dungeon 1 Chest 2",
        ]), TALocation)

    #Dungeon 2
    world.get_region("Dungeon 2_1").add_locations(get_location_names_with_ids([
        "Dungeon 2_1 Chest 1",
        ]), TALocation)   

    world.get_region("Dungeon 2_2").add_locations(get_location_names_with_ids([
        "Dungeon 2_2 Chest 1",
        "Dungeon 2_2 Chest 2",
        ]), TALocation)   

    #Dungeon 3
    world.get_region("Dungeon 3").add_locations(get_location_names_with_ids([
        "Dungeon 3 Chest 1",
        "Dungeon 3 Chest 2",
        ]), TALocation)       
    
    #Dungeon 4
    world.get_region("Dungeon 4").add_locations(get_location_names_with_ids([
        "Dungeon 4 Chest 1",
        "Dungeon 4 Chest 2",
        ]), TALocation)       

    #Dungeon 5
    world.get_region("Dungeon 5_1").add_locations(get_location_names_with_ids([
        "Dungeon 5_1 Chest 1",
        ]), TALocation)       

    world.get_region("Dungeon 5_2").add_locations(get_location_names_with_ids([
        "Dungeon 5_2 Boss Drop",
        ]), TALocation)    

    world.get_region("Dungeon 5_3").add_locations(get_location_names_with_ids([
        "Dungeon 5_3 Missable Chest",
        ]), TALocation)    

    #Treasures
    world.get_region("Treasure Red Room").add_locations(get_location_names_with_ids(["Treasure Red"]), TALocation)
    world.get_region("Treasure Pink Room").add_locations(get_location_names_with_ids(["Treasure Pink"]), TALocation)
    world.get_region("Treasure Yellow Room").add_locations(get_location_names_with_ids(["Treasure Pink"]), TALocation)
    world.get_region("Treasure Blue Room").add_locations(get_location_names_with_ids(["Treasure Blue"]), TALocation)

    #Misc Overworld Treasures
    world.get_region("Overworld 2").add_locations(get_location_names_with_ids([
        "Overworld 2 Chest 1",
        "Overworld 2 Chest 2",
        ]), TALocation)    
    

#NOT USED
def create_events(world: APQuestWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = APQuestLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.APQuestItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=APQuestLocation, item_type=items.APQuestItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
