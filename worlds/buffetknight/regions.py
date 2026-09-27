from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import BKWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: BKWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: BKWorld) -> None:

    #Overworld
    Region1 = Region("Overworld_1", world.player, world.multiworld)
    Region2 = Region("Overworld_2", world.player, world.multiworld)
    Region3 = Region("Overworld_3", world.player, world.multiworld)

    #Others
    CastleVault = Region("Castle_Vault", world.player, world.multiworld)
    HermitCave = Region("Hermit_Cave", world.player, world.multiworld)

    #Dungeons
    Dungeon1 = Region("Dungeon_Forest", world.player, world.multiworld)
    Dungeon2 = Region("Dungeon_Desert", world.player, world.multiworld)
    Dungeon2a = Region("Dungeon_Desert_2", world.player, world.multiworld)
    Dungeon2b = Region("Dungeon_Desert_Boss", world.player, world.multiworld)


    Dungeon3 = Region("Dungeon_Sky", world.player, world.multiworld)
    Dungeon4 = Region("Dungeon_Factory", world.player, world.multiworld)
    Dungeon5 = Region("Dungeon_Ocean", world.player, world.multiworld)
    Dungon5a = Region("Dungeon_Stomach", world.player, world.multiworld)
    Dungeon6 = Region("Dungeon_Tower", world.player, world.multiworld)
    Dungeon6a = Region("Dungeon_Tower_Boss", world.player, world.multiworld)
    Dungeon7 = Region("Casino_Dungeon", world.player, world.multiworld)
    Dungeon8 = Region("Secret_Dungeon", world.player, world.multiworld)

    Extra1 = Region("Forest_Poison_Cave", world.player, world.multiworld)
    Extra2 = Region("Desert_Pit", world.player, world.multiworld)
    Extra3 = Region("Sky_Nest", world.player, world.multiworld)
    Extra4 = Region("Sewer_Den", world.player, world.multiworld)
    Extra5 = Region("Sea_Clam_Cave", world.player, world.multiworld)

    Endgame = Region("Endgame", world.player, world.multiworld)


    regions = [Region1, Region2, Region3,
               Dungeon1, Dungeon2, Dungeon2a, Dungeon2b, Dungeon3, Dungeon4, Dungeon5, Dungon5a, Dungeon6, Dungeon6a, Dungeon7, Dungeon8,
               Extra1, Extra2, Extra3, Extra4, Extra5,
               Endgame, CastleVault, HermitCave
            ]

    world.multiworld.regions += regions
    pass

def connect_regions(world: BKWorld) -> None:

    # Main Regions
    world.get_region("Overworld_1").connect(world.get_region("Overworld_2"), "Overworld_2_Connection")
    world.get_region("Overworld_2").connect(world.get_region("Overworld_3"), "Overworld_3_Connection")

    #Dungeons
    world.get_region("Overworld_1").connect(world.get_region("Dungeon_Forest"), "Forest_Dungeon_Entrance")
    
    world.get_region("Overworld_1").connect(world.get_region("Dungeon_Desert"), "Desert_Dungeon_Entrance")
    world.get_region("Dungeon_Desert").connect(world.get_region("Dungeon_Desert_2"), "Desert_Dungeon_Gate")
    world.get_region("Dungeon_Desert_2").connect(world.get_region("Dungeon_Desert_Boss"), "Desert_Boss_Gate")

    world.get_region("Overworld_3").connect(world.get_region("Dungeon_Sky"), "Sky_Dungeon_Entrance")

    world.get_region("Overworld_2").connect(world.get_region("Dungeon_Factory"), "Factory_Dungeon_Entrance")
    
    world.get_region("Overworld_2").connect(world.get_region("Dungeon_Ocean"), "Ocean_Dungeon_Entrance")
    world.get_region("Dungeon_Ocean").connect(world.get_region("Dungeon_Stomach"), "Stomach_Dungeon_Entrance")

    world.get_region("Overworld_1").connect(world.get_region("Dungeon_Tower"), "Tower_Dungeon_Entrance")
    world.get_region("Dungeon_Tower").connect(world.get_region("Dungeon_Tower_Boss"), "Tower_Dungeon_Boss_Door")

    world.get_region("Overworld_1").connect(world.get_region("Casino_Dungeon"), "Casino_Dungeon_Entrance")
    world.get_region("Overworld_1").connect(world.get_region("Secret_Dungeon"), "Secret_Dungeon_Entrance")


    #Others
    world.get_region("Overworld_1").connect(world.get_region("Castle_Vault"), "Castle_Vault_Entrance")
    world.get_region("Overworld_2").connect(world.get_region("Hermit_Cave"), "Hermit_Cave_Entrance")

    world.get_region("Overworld_1").connect(world.get_region("Forest_Poison_Cave"), "Poison_Cave_Entrance")
    world.get_region("Overworld_1").connect(world.get_region("Desert_Pit"), "Desert_Pit_Entrance")
    world.get_region("Overworld_2").connect(world.get_region("Sky_Nest"), "Sky_Nest_Entrance")
    world.get_region("Overworld_2").connect(world.get_region("Sewer_Den"), "Sewer_Den_Entrance")
    world.get_region("Overworld_2").connect(world.get_region("Sea_Clam_Cave"), "Sea_Clam_Cave_Entrance")

    #End Game
    world.get_region("Overworld_1").connect(world.get_region("Endgame"), "Swamp_Endgame_Entrance")
    world.get_region("Casino_Dungeon").connect(world.get_region("Endgame"), "Casino_Endgame_Entrance")


