from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import BKWorld

LOCATION_NAME_TO_ID = {

    #Gourmet Castle
    "Castle_Grounds": 1,
    "Castle_Vault_1": 2,
    "Castle_Vault_2": 3,
    "Castle_Shooting_Range_1": 4,
    "Castle_Shooting_Range_2": 5,

    #Gourmet Town
    "Town_Shop_1": 6,
    "Town_Shop_2": 7,
    "Town_Shop_3": 8,
    "Town_Blacksmith_Weapon_Upgrade_1": 9,
    "Town_Blacksmith_Weapon_Upgrade_2": 10,
    "Town_Blacksmith_Helmet_Upgrade_1": 11,
    "Town_Blacksmith_Helmet_Upgrade_2": 12,
    "Chef_Town_Crossroads": 13,

    "Forest_Field_Crossroads": 14,

    #Swamp and Witch
    "Swamp_Ingredients_Gathered": 15,
    "Swamp_Witch_Intoduction": 16,
    #"Swamp_Witch_Relics_Gathered": 17,
    #"Swamp_Witch_End_Game": 18,

    "Swamp_Potion_Upgrade_1": 19,
    "Swamp_Potion_Upgrade_2": 20,
    "Swamp_Potion_Upgrade_3": 21,
    "Swamp_Potion_Upgrade_4": 22,
    "Swamp_Potion_Upgrade_5": 23,

    "Town_Field_1_Goblins": 24,
    "Town_Field_2_Ledge": 25,
    "Town_Cave": 26,

    #Wasteland
    "Wasteland_Field_1_North": 27,
    "Wasteland_Gold_Pond": 28,
    "Wasteland_Field_2_South": 29,

    #Vegetable Valley
    "Forest_Village_Garden": 30,
    "Forest_Village_Hut_Basement": 31,

    #Leafy-Greens Forest Dungeon
    "Forest_Dungeon_Hub": 32,
    "Forest_Dungeon_1_Pond": 33,
    "Forest_Dungeon_2_Spider": 34,
    "Forest_Dungeon_3_Hive": 35,
    "Forest_Dungeon_Cave": 36,

    "Forest_Dungeon_Ingredient": 37,
    "Forest_Dungeon_Ability": 38,

    #Forest Fields
    "Forest_Field_Pond": 39,
    "Forest_Field_Tree": 40,
    "Forest_Field_Cave": 41,
    "Forest_Field_Civet": 42,
    "Forest_Field_Beach": 43,

    "Forest_Field_Poison_Cave_Essence": 44,
    "Forest_Field_Poison_Cave_Relic": 45,

    #Desert Fields
    "Desert_Field_Pond": 46,
    "Chef_Desert_Cave": 47,
    "Desert_Field_Ledge": 48,
    "Desert_Field_Centre_Buried": 49,
    "Desert_Underground_Essence": 50,
    "Desert_Underground_Relic": 51,

    #Desert Camp
    "Desert_Camp_Ingredient": 52,
    "Desert_Camp_Leader": 53,

    "Desert_Tunnel": 54,
    "Desert_Challenge_Cave": 55,

    #Mt Broil Dungeon
    "Desert_Dungeon_Vent_1": 56,
    "Desert_Dungeon_Vent_2": 57,
    "Desert_Dungeon_Key_1": 58,
    "Desert_Dungeon_Cave": 59,
    "Desert_Dungeon_Key_2": 60,
    "Desert_Dungeon_Rubble": 61,
    "Desert_Dungeon_Basement": 62,
    "Desert_Dungeon_Ability": 63,

    #Mountain Fields
    "Mountain_Field_1_Tree": 64,
    "Mountain_Field_2_Ledge": 65,
    "Sky_Nest_Essence": 66,
    "Sky_Nest_Relic": 67,
    "Mountain_Field_Cave": 68,
    "Mountain_Challenge_Cave": 69,
    "Chef_Graveyard": 70,

    #Flosstopia
    "Sky_Town_Cafe": 71,
    "Sky_House": 72,

    #Sky Dungeon
    "Sky_Dungeon_1_Chamber": 73,
    "Sky_Dungeon_2_East": 74,
    "Sky_Dungeon_3_West": 75,
    "Sky_Dungeon_4_Seraphim": 76,
    "Sky_Dungeon_Ability": 77,
    "Sky_Dungeon_Ingredient": 78,


    #City Fields
    "City_Field_1_Waterfall": 79,
    "City_Field_2_Goblins": 80,
    "City_Restaurant": 81,
    "City_Hermit_Helmet_Upgrade": 82,
    "City_Hermit_Weapon_Upgrade": 83,
    "City_Field_3_Lighthouse": 84,
    "City_Sewers_North": 85,
    "City_Sewers_Lab": 86,
    "City_Sewers_Rat_Essence": 87,
    "City_Sewers_Rat_Relic": 88,

    #Bistropolis
    "City_Vending_Machine": 89,
    "City_Fast_Food_Purchase": 90,
    "City_Fast_Food_Quest": 91,
    "City_Arcade": 92,
    "City_Factory_Cleaner": 93,

    #Bistroland Factory
    "Factory_Dungeon_1_Floor": 94,
    "Factory_Dungeon_2_Elevator": 95,
    "Factory_Dungeon_3_Mimic": 96,
    "Factory_Dungeon_4_Generator": 97,
    "Factory_Dungeon_5_Upper_Floor": 98,
    "Factory_Dungeon_6_Vent": 127,
    "Factory_Dungeon_Ability": 99,
    "Factory_Dungeon_Ingredient": 100,

    "Beach_Field_Crossroads": 101,
    "Beach_Field_1": 102,
    "Beach_Field_2_Campfire": 103,
    "Beach_Field_3_Secretary": 104,
    "Beach_Cave_1": 105,
    "Beach_Clam_Cave_Essence": 106,
    "Beach_Clam_Cave_Relic": 107,

    "Beach_Dungeon_Cave": 108,
    "Beach_Dungeon_Starfish": 109,

    "Stomach_Dungeon_Cave": 110,
    "Stomach_Dungeon_Intestines": 111,
    "Stomach_Dungeon_Ability": 112,
    "Stomach_Dungeon_Ingredient": 113,


    #Tower
    "Tower_Ground_Centre": 114,
    "Tower_Ground_Boss_Key": 115,

    "Tower_Basement_Garbage": 116,
    "Tower_Basement_Centre": 117,
    #"Tower_Basement_Jail": 118,

    "Tower_Top_Storeroom": 119,
    "Tower_Top_Bar": 120,
    "Tower_Top_Bathroom": 121,
    "Tower_Boss_Essence": 122,
    "Tower_Relic": 123,

    #Extras
    "Fishing_Prize": 124,
    "Secret_Gallery": 125,
    "Secret_End": 126,
    "Death_Item": 127,

}   

class BKLocation(Location):
    game = "Buffet Knight"

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: BKWorld) -> None:
    create_regular_locations(world)
    create_events(world)


def create_regular_locations(world: BKWorld) -> None:

    #Main
    world.get_region("Overworld_1").add_locations(get_location_names_with_ids([
        #Castle
        "Castle_Grounds","Castle_Shooting_Range_1","Castle_Shooting_Range_2",
        
        #Town
        "Town_Shop_1", "Town_Shop_2", "Town_Shop_3", "Town_Blacksmith_Weapon_Upgrade_1", "Town_Blacksmith_Weapon_Upgrade_2",
        "Town_Blacksmith_Helmet_Upgrade_1", "Town_Blacksmith_Helmet_Upgrade_2", "Chef_Town_Crossroads",
        "Town_Field_1_Goblins", "Town_Field_2_Ledge", "Town_Cave"

        #Swamp
        "Swamp_Ingredients_Gathered", "Swamp_Witch_Intoduction", #"Swamp_Witch_Relics_Gathered", "Swamp_Witch_End_Game",
        "Swamp_Potion_Upgrade_1", "Swamp_Potion_Upgrade_2", "Swamp_Potion_Upgrade_3", "Swamp_Potion_Upgrade_4", "Swamp_Potion_Upgrade_5",

        #Wasteland
        "Wasteland_Field_1_North", "Wasteland_Gold_Pond", "Wasteland_Field_2_South",

        #Forest
        "Forest_Village_Garden", "Forest_Village_Hut_Basement",
        "Forest_Field_Crossroads", "Forest_Field_Pond", "Forest_Field_Tree", "Forest_Field_Cave", "Forest_Field_Civet", "Forest_Field_Beach",

        #Desert
        "Desert_Field_Pond", "Chef_Desert_Cave", "Desert_Field_Ledge", "Desert_Field_Centre_Buried",
        "Desert_Camp_Leader", "Desert_Tunnel", "Desert_Challenge_Cave",

        #Misc
        "Death_Item",

        ]), BKLocation)
    
    world.get_region("Overworld_2").add_locations(get_location_names_with_ids([
        #Mountains
        "Mountain_Field_1_Tree", "Mountain_Field_2_Ledge", "Mountain_Field_Cave", "Mountain_Challenge_Cave", "Chef_Graveyard",

        #City
        "City_Field_1_Waterfall", "City_Field_2_Goblins", "City_Restaurant", "City_Field_3_Lighthouse", "City_Sewers_North", "City_Sewers_Lab",
        "City_Vending_Machine", "City_Fast_Food_Purchase", "City_Fast_Food_Quest", "City_Arcade", "City_Factory_Cleaner",

        #Beach
        "Beach_Field_Crossroads", "Beach_Field_1", "Beach_Field_2_Campfire", "Beach_Field_3_Secretary", "Beach_Cave_1",
        "Fishing_Prize"



        ]), BKLocation)
    
    world.get_region("Overworld_3").add_locations(get_location_names_with_ids([
        "Sky_Town_Cafe", "Sky_House",
        ]), BKLocation)

    #Dungeons
    #---- Forest -----
    world.get_region("Dungeon_Forest").add_locations(get_location_names_with_ids([
        "Forest_Dungeon_Hub", "Forest_Dungeon_1_Pond", "Forest_Dungeon_2_Spider", "Forest_Dungeon_3_Hive", "Forest_Dungeon_Cave",
        "Forest_Dungeon_Ingredient", "Forest_Dungeon_Ability",
        ]), BKLocation)

    #---- Desert -----
    world.get_region("Dungeon_Desert").add_locations(get_location_names_with_ids([
        "Desert_Dungeon_Vent_1", "Desert_Dungeon_Vent_2", "Desert_Dungeon_Key_1", "Desert_Dungeon_Cave", "Desert_Dungeon_Key_2"
        ]), BKLocation)
    world.get_region("Dungeon_Desert_2").add_locations(get_location_names_with_ids([
        "Desert_Dungeon_Rubble", "Desert_Dungeon_Basement",
        ]), BKLocation)
    world.get_region("Dungeon_Desert_Boss").add_locations(get_location_names_with_ids([
        "Desert_Dungeon_Ability", "Desert_Camp_Ingredient", 
        ]), BKLocation)
    
    #---- Sky -----
    world.get_region("Dungeon_Sky").add_locations(get_location_names_with_ids([
        "Sky_Dungeon_1_Chamber", "Sky_Dungeon_2_East", "Sky_Dungeon_3_West", "Sky_Dungeon_4_Seraphim", "Sky_Dungeon_Ability", "Sky_Dungeon_Ingredient",
        ]), BKLocation)
    
    #---- Factory -----
    world.get_region("Dungeon_Factory").add_locations(get_location_names_with_ids([
        "Factory_Dungeon_1_Floor", "Factory_Dungeon_2_Elevator", "Factory_Dungeon_3_Mimic", "Factory_Dungeon_4_Generator", "Factory_Dungeon_5_Upper_Floor",
        "Factory_Dungeon_6_Vent", "Factory_Dungeon_Ability", "Factory_Dungeon_Ingredient",
        ]), BKLocation)
    
    #---- Ocean -----
    world.get_region("Dungeon_Ocean").add_locations(get_location_names_with_ids([
        "Beach_Dungeon_Cave", "Beach_Dungeon_Starfish",
        ]), BKLocation)

    #---- Stomach -----
    world.get_region("Dungeon_Stomach").add_locations(get_location_names_with_ids([
        "Stomach_Dungeon_Cave", "Stomach_Dungeon_Intestines",
        "Stomach_Dungeon_Ability", "Stomach_Dungeon_Ingredient",
        ]), BKLocation)

    #---- Tower -----
    world.get_region("Dungeon_Tower").add_locations(get_location_names_with_ids([
        "Tower_Ground_Centre", "Tower_Ground_Boss_Key",
        "Tower_Basement_Garbage", "Tower_Basement_Centre", #"Tower_Basement_Jail",
        "Tower_Top_Storeroom", "Tower_Top_Bar", "Tower_Top_Bathroom",
        ]), BKLocation)
    world.get_region("Dungeon_Tower_Boss").add_locations(get_location_names_with_ids([
        "Tower_Boss_Essence", "Tower_Relic",
        ]), BKLocation)

    #---- Secret -----
    world.get_region("Secret_Dungeon").add_locations(get_location_names_with_ids([
        "Secret_Gallery", "Secret_End",
        ]), BKLocation)
    
    #Extras
    world.get_region("Castle_Vault").add_locations(get_location_names_with_ids([
        "Castle_Vault_1", "Castle_Vault_2",
        ]), BKLocation)
    world.get_region("Hermit_Cave").add_locations(get_location_names_with_ids([
        "City_Hermit_Helmet_Upgrade", "City_Hermit_Weapon_Upgrade",
        ]), BKLocation)

    world.get_region("Forest_Poison_Cave").add_locations(get_location_names_with_ids([
        "Forest_Field_Poison_Cave_Essence", "Forest_Field_Poison_Cave_Relic",
        ]), BKLocation)
    world.get_region("Desert_Pit").add_locations(get_location_names_with_ids([
        "Desert_Underground_Essence", "Desert_Underground_Relic",
        ]), BKLocation)
    world.get_region("Sky_Nest").add_locations(get_location_names_with_ids([
        "Sky_Nest_Essence", "Sky_Nest_Relic",
        ]), BKLocation)
    world.get_region("Sewer_Den").add_locations(get_location_names_with_ids([
        "City_Sewers_Rat_Essence", "City_Sewers_Rat_Relic",
        ]), BKLocation)
    world.get_region("Sea_Clam_Cave").add_locations(get_location_names_with_ids([
        "Beach_Clam_Cave_Essence", "Beach_Clam_Cave_Relic",
        ]), BKLocation)

    
def create_events(world: BKWorld) -> None:
    world.get_region("Overworld_1").add_event("Desert_Dungeon_Entry_Permission", "Desert_Dungeon_Entry_Permission", location_type = BKLocation, item_type = items.BKItem)

    world.get_region("Dungeon_Tower_Boss").add_event("Demon_Chef_Defeated", "Demon_Chef_Defeated", location_type = BKLocation, item_type = items.BKItem)
    world.get_region("Overworld_1").add_event("Gastronomancy_Potion_Get", "Gastronomancy_Potion_Get", location_type = BKLocation, item_type = items.BKItem)
    world.get_region("Overworld_1").add_event("Forbidden_Insight_Get", "Forbidden_Insight_Get", location_type = BKLocation, item_type = items.BKItem)

    
    
    
    world.get_region("Endgame").add_event("Endgame_Reached", "Endgame_Reached", location_type = BKLocation, item_type = items.BKItem)


