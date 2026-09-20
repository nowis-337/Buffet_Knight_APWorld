from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

import Options
from .items import (party_members, equips,keys,skills)

if TYPE_CHECKING:
    from .world import CTBWorld


def set_all_rules(world: CTBWorld) -> None:

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


#Battle
def ctb_has_fire_extinguisher(state: CollectionState, world: CTBWorld) -> bool:
    return state.has("Fire Extinguisher", world.player)
def ctb_has_soak(state: CollectionState, world: CTBWorld) -> bool:
    return state.has("Soak", world.player)
def ctb_has_ventilate(state: CollectionState, world: CTBWorld) -> bool:
    return state.has("Ventilate", world.player)

#Item
def ctb_has_locker_key(state: CollectionState, world: CTBWorld) -> bool:
    return state.has("Locker Key", world.player)
def ctb_has_broom_and_dustpan(state: CollectionState, world: CTBWorld) -> bool:
    return state.has("Broom and Dustpan", world.player)


#End of helpers


#Sawyer: Entrance time!
def set_all_entrance_rules(world: CTBWorld) -> None:
    player = world.player
    multiworld = world.multiworld
    #Sawyer: Below is a var to make it so we don't have to type CollectionState every time we wanna check a function.
    mystate = CollectionState

    #begin_new_game = world.get_entrance("Begin_New_Game")


#Sawyer: These are the location rules! Hoo boy there are many haha
def set_all_location_rules(world: CTBWorld) -> None:
    player = world.player
    multiworld = world.multiworld





#Sawyer: Time for the wincon!
def set_completion_condition(world: CTBWorld) -> None:
    player = world.player

    world.multiworld.completion_condition[world.player] = (lambda mystate: ctb_has_fire_extinguisher( mystate, world) and
        ctb_has_soak(mystate, world) and ctb_has_ventilate(mystate, world))
