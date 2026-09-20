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
    create_events(world)


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
    

def create_events(world: TAWorld) -> None:
    #End of Game Event
    world.get_region("Final Boss Room").add_event("Final Boss Defeated", "Victory", location_type = TALocation, item_type = items.TAItem)

