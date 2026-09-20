from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import TAWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: TAWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: TAWorld) -> None:
    overworld1 = Region("Overworld 1", world.player, world.multiworld)
    overworld2 = Region("Overworld 2", world.player, world.multiworld)

    dungeon1 = Region("Dungeon 1", world.player, world.multiworld)
    dungeon2_1 = Region("Dungeon 2_1", world.player, world.multiworld)
    dungeon2_2 = Region("Dungeon 2_2", world.player, world.multiworld)
    dungeon3 = Region("Dungeon 3", world.player, world.multiworld)
    dungeon4 = Region("Dungeon 4", world.player, world.multiworld)
    dungeon5_1 = Region("Dungeon 5_1", world.player, world.multiworld)
    dungeon5_2 = Region("Dungeon 5_2", world.player, world.multiworld)
    dungeon5_3 = Region("Dungeon 5_3", world.player, world.multiworld) #Missable Location

    treasure_red = Region("Treasure Red Room", world.player, world.multiworld)
    treasure_pink = Region("Treasure Pink Room", world.player, world.multiworld)
    treasure_yellow = Region("Treasure Yellow Room", world.player, world.multiworld)
    treasure_blue = Region("Treasure Blue Room", world.player, world.multiworld)

    final_boss_room = Region("Final Boss Room", world.player, world.multiworld)

    # Let's put all these regions in a list.
    regions = [overworld1, overworld2, dungeon1, dungeon2_1, dungeon2_2, dungeon3, dungeon4, dungeon5_1, dungeon5_2, dungeon5_3, treasure_red,
               treasure_pink, treasure_yellow, treasure_blue, final_boss_room]

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: TAWorld) -> None:
    # An even easier way is to use the region.connect helper.
    #overworld.connect(right_room, "Overworld to Right Room")
    #right_room.connect(final_boss_room, "Right Room to Final Boss Room")

    # The region.connect helper even allows adding a rule immediately.
    # We'll talk more about rule creation in the set_all_rules() function in rules.py.
    #overworld.connect(top_left_room, "Overworld to Top Left Room", lambda state: state.has("Key", world.player))

    #Overworld 1
    world.get_region("Overworld 1").connect(world.get_region("Overworld 2"), "Overworld Bridge 1")
    world.get_region("Overworld 1").connect(world.get_region("Overworld 2"), "Overworld Bridge 2")
    world.get_region("Overworld 1").connect(world.get_region("Dungeon 1"), "Dungeon 1 Entrance")
    world.get_region("Overworld 1").connect(world.get_region("Dungeon 2_1"), "Dungeon 2 Entrance")
    world.get_region("Overworld 1").connect(world.get_region("Final Boss Room"), "Final Boss Gate")

    world.get_region("Overworld 2").connect(world.get_region("Dungeon 3"), "Dungeon 3 Entrance")
    world.get_region("Overworld 2").connect(world.get_region("Dungeon 4"), "Dungeon 4 Entrance")
    world.get_region("Overworld 2").connect(world.get_region("Dungeon 5_1"), "Dungeon 5 Entrance")

    #Overworld 2
    world.get_region("Overworld 2").connect(world.get_region("Treasure Red Room"), "Treasure Red Entrance")
    world.get_region("Overworld 2").connect(world.get_region("Treasure Pink Room"), "Treasure Pink Entrance")
    world.get_region("Overworld 2").connect(world.get_region("Treasure Yellow Room"), "Treasure Yellow Entrance")
    world.get_region("Overworld 2").connect(world.get_region("Treasure Blue Room"), "Treasure Blue Entrance")

    #Additional Dungeon Connections
    world.get_region("Dungeon 2_1").connect(world.get_region("Dungeon 2_2"), "Dungeon 2 Gate")
    world.get_region("Dungeon 5_1").connect(world.get_region("Dungeon 5_2"), "Dungeon 5 Warp")
    world.get_region("Dungeon 5_2").connect(world.get_region("Dungeon 5_3"), "Dungeon 5 Missable")

