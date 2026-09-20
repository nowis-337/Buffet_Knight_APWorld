from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import TAWorld


def set_all_rules(world: TAWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: TAWorld) -> None:
    def has_red_key(state: CollectionState) -> bool:
        return state.has("Red Key", world.player)
    
    def has_pink_key(state: CollectionState) -> bool:
        return state.has("Pink Key", world.player)

    def has_blue_key(state: CollectionState) -> bool:
        return state.has("Blue Key", world.player)
    
    def has_yellow_key(state: CollectionState) -> bool:
        return state.has("Yellow Key", world.player)

    def has_all_crystals(state: CollectionState) -> bool:
        return state.has_all(("Crystal 1", "Crystal 2", "Crystal 3", "Crystal 4", "Crystal 5"), world.player)

    #Overworld 1
    set_rule(world.get_entrance("Overworld Bridge 1"), has_red_key)
    set_rule(world.get_entrance("Overworld Bridge 2"), has_blue_key)
    set_rule(world.get_entrance("Final Boss Gate"), has_all_crystals)
    set_rule(world.get_entrance("Dungeon 2 Entrance"), lambda state: state.has("Dungeon Key 1"), world.player)

    #Overworld 2
    set_rule(world.get_entrance("Dungeon 3 Entrance"), has_red_key)
    set_rule(world.get_entrance("Dungeon 4 Entrance"), lambda state: state.has("Dungeon Key 3"), world.player)
    set_rule(world.get_entrance("Treasure Red Entrance"), has_red_key)
    set_rule(world.get_entrance("Treasure Pink Entrance"), has_pink_key)
    set_rule(world.get_entrance("Treasure Yellow Entrance"), has_yellow_key)
    set_rule(world.get_entrance("Treasure Blue Entrance"), has_blue_key)

    #Dungeon Connections
    set_rule(world.get_entrance("Dungeon 2 Gate"), lambda state: state.has("Dungeon Key 2"), world.player)
    set_rule(world.get_entrance("Dungeon 5 Missable"), has_red_key)



def set_all_location_rules(world: TAWorld) -> None:
    pass


def set_completion_condition(world: TAWorld) -> None:
    #Obtained when final boss defeated:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
