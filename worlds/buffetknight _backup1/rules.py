from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import BKWorld


def set_all_rules(world: BKWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_all_event_rules(world)
    set_completion_condition(world)

def set_all_entrance_rules(world: BKWorld) -> None:
    
    #====== Skills ========
    def skill_bomb(state: CollectionState) -> bool:
        return state.has("Chilli Bomb", world.player)

    def skill_heal(state: CollectionState) -> bool:
        return state.has("Heartful Fruit", world.player)

    def skill_shock(state: CollectionState) -> bool:
        return state.has("Lemon Shock", world.player)
    
    def skill_bounce(state: CollectionState) -> bool:
        return state.has("Bouncy Gum", world.player)
    
    def skill_shell(state: CollectionState) -> bool:
        return state.has("Chitin Shell", world.player)

    def all_skills_base(state: CollectionState) -> bool:
        return skill_bomb(state) and skill_heal(state) and skill_shock(state) and skill_bounce(state) and skill_shell(state)

    def all_skill_upgrades(state: CollectionState) -> bool:
        return state.has_all(("Fruitful Potion", "Molten Potion", "Bubble Gum Potion", "Voltaic Potion", "Oceanic Potion"), world.player)

    #====== Game Progression =======
    def all_ingredients_collected(state: CollectionState) -> bool:
        return state.has_all(("Ambrosial Herb", "Fiery Pepper", "Celestial Sugar", "M.S.G.", "Abyssal Salt"), world.player)

    def reached_pre_end_game(state: CollectionState) -> bool:
       return state.has("Demon_Chef_Defeated", world.player) 
    
    #====== Area Access ========
    def can_access_overworld_2(state: CollectionState) -> bool:
        return state.has_any(("Chilli Bomb", "Chitin Shell", "Bouncy Gum", "Reaper's Meal Ticket"), world.player)

    def can_access_overworld_3(state: CollectionState) -> bool:
        return skill_bomb(state)

    def can_access_casino_dungeon(state: CollectionState) -> bool:
        return skill_bomb(state)

    def can_access_secret_dungeon(state: CollectionState) -> bool:
        return can_access_overworld_2(state) and skill_bomb(state) and skill_shock(state)

    #===== Reaching the End ========
    def swamp_endgame_access(state: CollectionState) -> bool:
           #if world.options.goal == 1: return False
           if not reached_pre_end_game(state): return False
           if not state.has("Gastronomancy Essence", world.player): return False
           return False

    def casino_endgame_access(state: CollectionState) -> bool:
            #Accesible in Advanced Mode
            #if world.options.goal == 0: return False
            if not all_ingredients_collected(state): return False
            if not all_skills_base(state): return False #Progress through Casino Dungeon
            if not all_skill_upgrades(state): return False #Progress through Casino Dungeon
            if not state.has("Gastronomancy_Potion_Get", world.player): return False #Witch End 
            if not state.has("Forbidden_Insight_Get", world.player): return False #All Relics
            return True

    set_rule(world.get_entrance("Overworld_2_Connection"), can_access_overworld_2)
    set_rule(world.get_entrance("Overworld_3_Connection"), can_access_overworld_3)

    set_rule(world.get_entrance("Desert_Dungeon_Entrance"), lambda state: state.has("Desert_Dungeon_Entry_Permission", world.player))
    set_rule(world.get_entrance("Desert_Dungeon_Gate"), lambda state: state.has_all(("Temple Key 1", "Temple Key 2"), world.player))
    set_rule(world.get_entrance("Desert_Boss_Gate"), lambda state: state.has("Meat Effigy", world.player))

    set_rule(world.get_entrance("Factory_Dungeon_Entrance"), lambda state: state.has("Factory Key", world.player))
    set_rule(world.get_entrance("Ocean_Dungeon_Entrance"), lambda state: state.has("Note in a Bottle", world.player))

    set_rule(world.get_entrance("Tower_Dungeon_Entrance"), lambda state: state.has("Mysterious Fried Chicken", world.player))
    set_rule(world.get_entrance("Tower_Dungeon_Boss_Door"), lambda state: state.has("Tower Master Key", world.player))

    set_rule(world.get_entrance("Casino_Dungeon_Entrance"), can_access_casino_dungeon)
    set_rule(world.get_entrance("Secret_Dungeon_Entrance"), can_access_secret_dungeon)

    set_rule(world.get_entrance("Castle_Vault_Entrance"), skill_bomb)
    set_rule(world.get_entrance("Hermit_Cave_Entrance"), lambda state: state.has_any(("Stainless Steel Knife", "Ultimaxcalibur(TM)"), world.player))

    set_rule(world.get_entrance("Poison_Cave_Entrance"), lambda state: state.has_all(("Chilli Bomb", "Heartful Fruit"), world.player))
    set_rule(world.get_entrance("Desert_Pit_Entrance"), skill_bomb)
    set_rule(world.get_entrance("Sky_Nest_Entrance"), lambda state: state.has_all(("Chilli Bomb", "Bouncy Gum"), world.player))
    set_rule(world.get_entrance("Sewer_Den_Entrance"), skill_shock)
    set_rule(world.get_entrance("Sea_Clam_Cave_Entrance"), skill_shell)

    set_rule(world.get_entrance("Swamp_Endgame_Entrance"), swamp_endgame_access)
    set_rule(world.get_entrance("Casino_Endgame_Entrance"), casino_endgame_access)


def set_all_location_rules(world: BKWorld) -> None:
    
     #====== Skills ========
    def skill_bomb(state: CollectionState) -> bool:
        return state.has("Chilli Bomb", world.player)

    def skill_heal(state: CollectionState) -> bool:
        return state.has("Heartful Fruit", world.player)

    def skill_shock(state: CollectionState) -> bool:
        return state.has("Lemon Shock", world.player)
    
    def skill_bounce(state: CollectionState) -> bool:
        return state.has("Bouncy Gum", world.player)
    
    def skill_shell(state: CollectionState) -> bool:
        return state.has("Chitin Shell", world.player)

    ore_array = ["Mineral Ore 1","Mineral Ore 2","Mineral Ore 3","Mineral Ore 4","Mineral Ore 5","Mineral Ore 6","Mineral Ore 7","Mineral Ore 8","Mineral Ore 9"]

    def blacksmith_ore_2(state: CollectionState) -> bool:
        ore_count = 0
        for item in ore_array:
            if state.has(item, world.player): ore_count += 1
        return ore_count >= 2

    def blacksmith_ore_5(state: CollectionState) -> bool:
        ore_count = 0
        for item in ore_array:
            if state.has(item, world.player): ore_count += 1
        return ore_count >= 5

    def blacksmith_ore_9(state: CollectionState) -> bool:
        ore_count = 0
        for item in ore_array:
            if state.has(item, world.player): ore_count += 1
        return ore_count >= 9

    def all_ingredients_collected(state: CollectionState) -> bool:
        return skill_bomb(state) and skill_heal(state) and skill_shock(state) and skill_bounce(state) and skill_shell(state)

    set_rule(world.get_location("Town_Blacksmith_Weapon_Upgrade_1"), blacksmith_ore_2)
    set_rule(world.get_location("Town_Blacksmith_Weapon_Upgrade_2"), blacksmith_ore_5)
    set_rule(world.get_location("Town_Cave"), skill_bomb)

    set_rule(world.get_location("Swamp_Ingredients_Gathered"), all_ingredients_collected)

    set_rule(world.get_location("Swamp_Potion_Upgrade_1"), lambda state: state.has("Fruitful Essence", world.player))
    set_rule(world.get_location("Swamp_Potion_Upgrade_2"), lambda state: state.has("Molten Essence", world.player))
    set_rule(world.get_location("Swamp_Potion_Upgrade_3"), lambda state: state.has("Bubble Gum Essence", world.player))
    set_rule(world.get_location("Swamp_Potion_Upgrade_4"), lambda state: state.has("Voltaic Essence", world.player))
    set_rule(world.get_location("Swamp_Potion_Upgrade_5"), lambda state: state.has("Ocean Essence", world.player))

    set_rule(world.get_location("Wasteland_Field_1_North"), lambda state: state.has_any(("Witch's Brew", "Bouncy Gum"), world.player))
    set_rule(world.get_location("Wasteland_Field_2_South"), skill_bomb)

    set_rule(world.get_location("Forest_Field_Pond"), skill_shock)
    set_rule(world.get_location("Forest_Field_Tree"), lambda state: state.has_any(("Chilli Bomb", "Bouncy Gum"), world.player))
    set_rule(world.get_location("Forest_Field_Cave"), skill_bomb)
    set_rule(world.get_location("Forest_Field_Civet"), skill_bomb)
    set_rule(world.get_location("Forest_Field_Beach"), skill_bomb)

    set_rule(world.get_location("Desert_Field_Pond"), lambda state: state.has_any(("Chilli Bomb", "Witch's Brew"), world.player))
    set_rule(world.get_location("Desert_Field_Ledge"), lambda state: state.has_any(("Chilli Bomb", "Bouncy Gum"), world.player))
    set_rule(world.get_location("Desert_Field_Centre_Buried"), skill_bomb)
    set_rule(world.get_location("Desert_Tunnel"), skill_bomb)
    set_rule(world.get_location("Desert_Challenge_Cave"), lambda state: state.has_all(("Chilli Bomb", "Molten Potion"), world.player))

    set_rule(world.get_location("Desert_Camp_Leader"), lambda state: state.has("Red Juicy Tomato", world.player))

    set_rule(world.get_location("Mountain_Field_1_Tree"), lambda state: state.has_any(("Chilli Bomb", "Bouncy Gum"), world.player))
    set_rule(world.get_location("Mountain_Field_2_Ledge"), lambda state: state.has_all(("Chilli Bomb", "Bouncy Gum"), world.player))

    set_rule(world.get_location("Mountain_Field_Cave"), skill_bomb)
    set_rule(world.get_location("Mountain_Challenge_Cave"), lambda state: state.has_all(("Bubble Gum Potion", "Bouncy Gum"), world.player))

    set_rule(world.get_location("Sky_Town_Cafe"), lambda state: state.has("Stinky Berry", world.player))
    set_rule(world.get_location("Sky_House"), lambda state: state.has("Bag of Crunchy Chips", world.player))

    set_rule(world.get_location("City_Field_1_Waterfall"), lambda state: state.has_all(("Chilli Bomb", "Chitin Shell"), world.player))
    set_rule(world.get_location("City_Hermit_Weapon_Upgrade"), blacksmith_ore_9)
    #set_rule(world.get_location("City_Field_3_Lighthouse"), skill_shock)

    set_rule(world.get_location("City_Sewers_North"), skill_shock)
    set_rule(world.get_location("City_Sewers_Lab"), lambda state: state.has("Witch's Brew", world.player))
    set_rule(world.get_location("Factory_Dungeon_5_Upper_Floor"), skill_bomb)

    set_rule(world.get_location("Beach_Field_Crossroads"), skill_bomb)
    set_rule(world.get_location("Beach_Field_1"), skill_bounce)
    set_rule(world.get_location("Beach_Field_3_Secretary"), lambda state: state.has("Jolly Meal Delivery", world.player))
    set_rule(world.get_location("Beach_Cave_1"), skill_bomb)
    set_rule(world.get_location("Fishing_Prize"), skill_shock)

    set_rule(world.get_location("Stomach_Dungeon_Cave"), skill_bomb)

    set_rule(world.get_location("Tower_Ground_Boss_Key"), lambda state: state.has("Storage Key", world.player))


def set_all_event_rules(world: BKWorld) -> None:

    set_rule(world.get_location("Event_Desert_Dungeon_Entry_Permission"), lambda state: state.has("Red Juicy Tomato", world.player))
    set_rule(world.get_location("Event_Gastronomancy_Potion_Get"), lambda state: state.has_all(("Demon_Chef_Defeated", "Gastronomancy Essence"), world.player))
    set_rule(world.get_location("Event_Forbidden_Insight_Get"), lambda state: state.has_all(("Relic Fragment 1","Relic Fragment 2","Relic Fragment 3","Relic Fragment 4","Relic Fragment 5"), world.player))


def set_completion_condition(world: BKWorld) -> None:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Endgame_Reached", world.player)
