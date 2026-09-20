#Sawyer: Don't know what a lot of this is but we'll get there!
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, CollectionState

from .rules import ctb_has_fire_extinguisher, ctb_has_soak, ctb_has_ventilate, ctb_has_locker_key, ctb_has_broom_and_dustpan

if TYPE_CHECKING:
    from .world import CTBWorld

def create_and_connect_regions(world: CTBWorld) -> None:
    state = CollectionState
    create_all_regions(world)
    connect_regions(state,world)

 # Sawyer: Okay, we had some regions defined in our last attempts.
def create_all_regions(world: CTBWorld) -> None:

    #Sawyer: Putting them all together now! Don't forget to add the full game's regions when you're done!
    regions = [
        Region("Hallway", world.player, world.multiworld),
        Region("Hallway Dust Piles", world.player, world.multiworld),
        Region("Hallway Lockers", world.player, world.multiworld),
        Region("Hallway Boss", world.player, world.multiworld),

        Region("BreakRoom", world.player, world.multiworld),
        Region("BreakRoom Dust Piles", world.player, world.multiworld),
        Region("BreakRoom Lockers", world.player, world.multiworld),
        Region("BreakRoom Boss", world.player, world.multiworld),

        Region("Closet", world.player, world.multiworld),
        Region("Closet Dust Piles", world.player, world.multiworld),
        Region("Closet Lockers", world.player, world.multiworld),
        Region("Closet Boss", world.player, world.multiworld),

        Region("Office", world.player, world.multiworld),
        Region("Office Dust Piles", world.player, world.multiworld),
        Region("Office Lockers", world.player, world.multiworld),

        Region("Lobby", world.player, world.multiworld),
        Region("Lobby Dust Piles", world.player, world.multiworld),
    ]


    #Sawyer: Add it all together now!
    world.multiworld.regions += regions




#Sawyer: Next part has me nervous. This is entrances, right?
def connect_regions(state: CollectionState, world: CTBWorld) -> None:
    world.connect_2way(world.get_region("Hallway"), world.get_region("Closet"),
                       lambda state: True)
    world.connect_2way(world.get_region("Hallway"), world.get_region("BreakRoom"),
                       lambda state: True)
    world.connect_2way(world.get_region("Hallway"), world.get_region("Lobby"),
                       lambda state: True)
    world.connect_2way(world.get_region("Hallway"), world.get_region("Office"),
                       lambda state: ctb_has_fire_extinguisher(state, world))
    world.connect_2way(world.get_region("Hallway"), world.get_region("Hallway Dust Piles"),
                       lambda state: ctb_has_broom_and_dustpan(state, world))
    world.connect_2way(world.get_region("Hallway"), world.get_region("Hallway Lockers"),
                       lambda state: ctb_has_locker_key(state, world))
    world.connect_2way(world.get_region("Hallway"), world.get_region("Hallway Boss"),
                       lambda state: ctb_has_fire_extinguisher(state, world))

    world.connect_2way(world.get_region("BreakRoom"), world.get_region("BreakRoom Dust Piles"),
                       lambda state: ctb_has_broom_and_dustpan(state, world))
    world.connect_2way(world.get_region("BreakRoom"), world.get_region("BreakRoom Lockers"),
                       lambda state: ctb_has_locker_key(state, world))
    world.connect_2way(world.get_region("BreakRoom"), world.get_region("BreakRoom Boss"),
                       lambda state: ctb_has_ventilate(state, world))

    world.connect_2way(world.get_region("Closet"), world.get_region("Closet Dust Piles"),
                       lambda state: ctb_has_broom_and_dustpan(state, world))
    world.connect_2way(world.get_region("Closet"), world.get_region("Closet Lockers"),
                       lambda state: ctb_has_locker_key(state, world))
    world.connect_2way(world.get_region("Closet"), world.get_region("Closet Boss"),
                       lambda state: ctb_has_soak(state, world))

    world.connect_2way(world.get_region("Office"), world.get_region("Office Dust Piles"),
                       lambda state: ctb_has_broom_and_dustpan(state, world))
    world.connect_2way(world.get_region("Office"), world.get_region("Office Lockers"),
                       lambda state: ctb_has_locker_key(state, world))

    world.connect_2way(world.get_region("Lobby"), world.get_region("Lobby Dust Piles"),
                       lambda state: ctb_has_broom_and_dustpan(state, world))