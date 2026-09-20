#Sawyer: Okay we have a whole lotta locations, here's hoping for the best!


#Snagging all the below from APQuest again
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import CTBWorld
from .Location_Table import location_table

#Okay, looks like everything needs an ID. Blehhh it is what it is, I'll just go in order from the default thingy.


#LOCATION_NAME_TO_ID = json.load(open("./worlds/silverdaze/Location_Table.json"))
LOCATION_NAME_TO_ID = location_table

class CTBLocation(Location):
    game = "Silver Daze"

#Sawyer: NGL I don't really get this but APQuest said to do it.
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: CTBWorld) -> None:
    create_regular_locations(world)

def create_regular_locations(world: CTBWorld) -> None:
    #Sawyer: Now we add stuff to regions!
#Here's the main story non optional stuff.
    world.get_region("Hallway").add_locations(get_location_names_with_ids([
        "HallShelf1","HallShelf2","HallShelf3","HallShelf4","HallShelf5","HallShelf6","HallEnemy1"
    ]),CTBLocation)
    world.get_region("Hallway Dust Piles").add_locations(get_location_names_with_ids([
        "HallDust1","HallDust2","HallDust3","HallDust4",
    ]),CTBLocation)
    world.get_region("Hallway Lockers").add_locations(get_location_names_with_ids([
        "HallLocker",
    ]),CTBLocation)
    world.get_region("Hallway Boss").add_locations(get_location_names_with_ids([
        "HallBoss",
    ]),CTBLocation)
#
    world.get_region("BreakRoom").add_locations(get_location_names_with_ids([
        "BreakRoomFridge","BreakRoomTrash","BreakRoomEnemy1","BreakRoomEnemy2",
    ]),CTBLocation)
    world.get_region("BreakRoom Dust Piles").add_locations(get_location_names_with_ids([
        "BreakRoomDust1","BreakRoomDust2","BreakRoomDust3",
    ]),CTBLocation)
    world.get_region("BreakRoom Lockers").add_locations(get_location_names_with_ids([
        "BreakRoomLocker",
    ]),CTBLocation)
    world.get_region("BreakRoom Boss").add_locations(get_location_names_with_ids([
        "BreakRoomBoss",
    ]),CTBLocation)
#
    world.get_region("Closet").add_locations(get_location_names_with_ids([
        "ClosetEnemy1",
    ]),CTBLocation)
    world.get_region("Closet Dust Piles").add_locations(get_location_names_with_ids([
        "ClosetDust1","ClosetDust2"
    ]),CTBLocation)
    world.get_region("Closet Lockers").add_locations(get_location_names_with_ids([
        "ClosetLocker1","ClosetLocker2"
    ]),CTBLocation)
    world.get_region("Closet Boss").add_locations(get_location_names_with_ids([
        "ClosetBoss",
    ]),CTBLocation)
#
    world.get_region("Office").add_locations(get_location_names_with_ids([
        "OfficeTrash","OfficeEnemy1","OfficeEnemy2",
    ]),CTBLocation)
    world.get_region("Office Dust Piles").add_locations(get_location_names_with_ids([
        "OfficeDust1","OfficeDust2","OfficeDust3",
    ]),CTBLocation)
    world.get_region("Office Lockers").add_locations(get_location_names_with_ids([
        "OfficeLocker",
    ]),CTBLocation)
#
    world.get_region("Lobby").add_locations(get_location_names_with_ids([
        "LobbyTrash",
    ]),CTBLocation)
    world.get_region("Lobby Dust Piles").add_locations(get_location_names_with_ids([
        "LobbyDust1","LobbyDust2",
    ]),CTBLocation)

    #LOCATION_NAME_TO_ID.close()







