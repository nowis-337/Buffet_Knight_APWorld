#Sawyer: Okay we have a whole lotta locations, here's hoping for the best!


#Snagging all the below from APQuest again
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import SDWorld
from .Location_Table import location_table

#Okay, looks like everything needs an ID. Blehhh it is what it is, I'll just go in order from the default thingy.


#LOCATION_NAME_TO_ID = json.load(open("./worlds/silverdaze/Location_Table.json"))
LOCATION_NAME_TO_ID = location_table

#with open(os.path.join(os.path.dirname(__file__), 'Location_Table.json'), 'r') as file:
#    LOCATION_NAME_TO_ID = json.loads(file.read())

# Sawyer: Locations are now stored inside the Location_Table.json file.
# This is so they can easily be transferred to Silver Daze and given the location data.
#Sawyer: PHEW! That covers the demo stuff. It'll be fun adding more haha

class SDLocation(Location):
    game = "Silver Daze"

#Sawyer: NGL I don't really get this but APQuest said to do it.
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def create_all_locations(world: SDWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: SDWorld) -> None:
    #Sawyer: Now we add stuff to regions!
#Here's the main story non optional stuff.
    world.get_region("GeoRoom").add_locations(get_location_names_with_ids([
        "Geo's Room Reward 1","Geo's Room Reward 2","Geo's Room Reward 3","Geo's Room Reward 4","Geo's Room Reward 5",
    ]),SDLocation)
#
    world.get_region("Hub1").add_locations(get_location_names_with_ids([
        "Grey Zone - Yellow Key Pickup","Cotton Street - Geo Join Reward 1","Cotton Street - Geo Join Reward 2",
        "Cotton Street - Geo Join Reward 3","Cotton Street Green Chest","Cotton Street Silver Chest",
    ]),SDLocation)
#
    world.get_region("Hub2").add_locations(get_location_names_with_ids([
        "Grey Zone - ReCollection 08 Unlock","Grey Zone - Silver Chest in Hub 2",
    ]),SDLocation)
#
    world.get_region("QuoDefenderRoom").add_locations(get_location_names_with_ids([
        "Quo Defender Memo 1", "Quo Defender Memo 2",
    ]),SDLocation)
#
    world.get_region("Red1").add_locations(get_location_names_with_ids([
        "Red Zone - Green Chest Behind Key Bridge", "Red Zone - Green Chest Before Kingoose",
    ]),SDLocation)
#
    world.get_region("KingooseRoom").add_locations(get_location_names_with_ids([
        "Kingoose Memo 1","Kingoose Memo 2","Red Zone - Kani Join Reward 1","Red Zone - Kani Join Reward 2",
        "Red Zone - Kani Join Reward 3","Red Zone - Kani Join Reward 4","Red Zone - Kani Join Reward 5",
    ]),SDLocation)
#
    world.get_region("Red2").add_locations(get_location_names_with_ids([
        "Red Zone - Green Chest 1 After Kingoose","Red Zone - Green Chest 2 After Kingoose","Red Zone - Silver Chest",
        "Red Tower - Silver Chest","Red Tower - Gold Chest","Red Zone Chasm - Silver Chest Near Bridge",
        "Red Zone Chasm - Gold Chest",
        "Red Zone Chasm - Silver Chest Behind Key Bridge","Red Zone Chasm - Green Chest",
        "Red Zone - ReCollection 02 Unlock"
    ]),SDLocation)
#
    if not (world.options.easylogic):
        world.get_region("GreyIslandGreenDoor").add_locations(get_location_names_with_ids([
            "Grey Zone - Silver Chest From Green Door"
        ]),SDLocation)
#
        world.get_region("YellowBackdoorIsland").add_locations(get_location_names_with_ids([
            "Yellow Zone - Chaos Enri Silver Chest"
        ]),SDLocation)
#
        world.get_region("GreyIslandBlueDoor").add_locations(get_location_names_with_ids([
            "Grey Zone - Gold Chest From Blue Door"
        ]),SDLocation)
#
        world.get_region("GreyIslandRedDoor").add_locations(get_location_names_with_ids([
            "Grey Zone - Gold Chest From Red Door",
        ]),SDLocation)
#
        world.get_region("RedBackdoorIsland").add_locations(get_location_names_with_ids([
            "Red Zone - Chaos Rot Chest"
        ]),SDLocation)

#
#       world.get_region("Blue1").add_locations(get_location_names_with_ids([
#   I don't think Blue1 has any locations atm
#    ]),SDLocation)
#
    world.get_region("Blue2").add_locations(get_location_names_with_ids([
        "Blue Zone - Glitch Bridge 1 Silver Chest", "Blue Zone - Glitch Bridge 1 Green Chest 1"
    ]),SDLocation)
#
    world.get_region("Griffin1Room").add_locations(get_location_names_with_ids([
        "Griffin (Blue Zone) Memo 1","Griffin (Blue Zone) Memo 2"
    ]),SDLocation)
#
    world.get_region("BlueShaneArea").add_locations(get_location_names_with_ids([
        "Blue Zone - Glitch Bridge 1 Green Chest 2"
    ]),SDLocation)
#
    world.get_region("DiggerRoom").add_locations(get_location_names_with_ids([
        "Blue Zone - Digger Room Chest","Digger Memo 1","Digger Memo 2","Blue Zone - Shane Join Reward 1",
        "Blue Zone - Shane Join Reward 2","Blue Zone - Shane Join Reward 4","Blue Zone - Shane Join Reward 3",
    ]),SDLocation)
#
    world.get_region("Blue3").add_locations(get_location_names_with_ids([
        "Blue Zone - Glitch Bridge 2 Green Chest"
    ]),SDLocation)
#
    world.get_region("Blue4").add_locations(get_location_names_with_ids([
        "Blue Zone - Wink Area Silver Chest","Blue Zone - ReCollection 05 Unlock",
        "Blue Zone - Wink Area Green Chest 1","Blue Zone - Wink Area Green Chest 2",
        "Blue Zone - Wink Join Reward 4","Blue Zone - Wink Join Reward 3","Blue Zone - Wink Join Reward 2",
        "Blue Zone - Wink Join Reward 1"
    ]),SDLocation)
#
    world.get_region("Blue5").add_locations(get_location_names_with_ids([
        "Blue Cavern - Left Side Glitch Chest","Blue Cavern - Left Side Silver Chest",
        "Blue Cavern - Right Side Glitch Chest","Blue Cavern - Right Side Gold Chest",
    ]),SDLocation)
#
#    world.get_region("Scatter").add_locations(get_location_names_with_ids([
#       Scatter lacks locations as well.
#    ]),SDLocation)
#
#
    world.get_region("PurpleHippoRoom").add_locations(get_location_names_with_ids([
        "Blue Zone - Purple Hippo Chest",
    ]), SDLocation)
#
    if not (world.options.easylogic):
        world.get_region("PurpleBackdoorIsland").add_locations(get_location_names_with_ids([
            "Purple Zone - Chaos Ruda Chest",
        ]),SDLocation)

#
        world.get_region("BlueBackdoorIsland").add_locations(get_location_names_with_ids([
            "Blue Zone - Chaos Nyx Chest",
        ]),SDLocation)

#
    world.get_region("Green1").add_locations(get_location_names_with_ids([
        "Grey Zone - Path To Green Zone Chest","Green Zone - ReCollection 03 Unlock","Green Zone - Jeff Join Reward 5",
        "Green Zone - Jeff Join Reward 4","Green Zone - Jeff Join Reward 3","Green Zone - Jeff Join Reward 2",
        "Green Zone - Jeff Join Reward 1","Green Zone - Cyphon's Debut Silver Chest",
        "Green Zone - First Room Silver Chest",
    ]),SDLocation)
#
    world.get_region("DesmodusRoom").add_locations(get_location_names_with_ids([
        "Desmodus Memo 1","Desmodus Memo 2",
    ]),SDLocation)
#
    world.get_region("Green2").add_locations(get_location_names_with_ids([
        "Green Chessboard - Silver Chest","Green Zone - Left Path Silver Chest","Green Zone - Right Path Gold Chest",
    ]),SDLocation)
#
    world.get_region("SquailArea").add_locations(get_location_names_with_ids([
        "Squail Memo 1","Squail Memo 2","Green Zone - Squail Theatre Chest",
    ]),SDLocation)
#
    world.get_region("Purple1").add_locations(get_location_names_with_ids([
        "Purple Zone - First Room Green Chest","Purple Zone - First Room Silver Chest",
    ]),SDLocation)
#
    world.get_region("SwordmoleRoom").add_locations(get_location_names_with_ids([
        "Swordmole Memo 2","Swordmole Memo 1",
    ]),SDLocation)
#
    world.get_region("Purple2").add_locations(get_location_names_with_ids([
        "Purple Zone - After Swordmole Gold Chest","Purple Zone - After Swordmole Green Chest",
        "Purple Zone - Sniper Long Bridge Chest","Purple Zone - Before Scaventure Gold Chest",
        "Purple Zone - Before Scaventure Silver Chest","Purple Zone - Liza Join Reward 1",
        "Purple Zone - Liza Join Reward 2","Purple Zone - Liza Join Reward 3",
        "Purple Zone - Liza Join Reward 4","Purple Zone - Liza Join Reward 5",
    ]),SDLocation)
#
    world.get_region("ScaventureRoom").add_locations(get_location_names_with_ids([
        "Scaventure Memo 1","Scaventure Memo 2",
    ]),SDLocation)
#
    world.get_region("PurpleTower").add_locations(get_location_names_with_ids([
        "Purple Zone - Tower Entrance Gold Chest","Purple Zone - Left Path Silver Chest",
        "Purple Zone - ReCollection 04 Unlock","Purple Tower - Silver Chest Before Enri",
    ]),SDLocation)

#
    if not (world.options.easylogic):
        world.get_region("GreyIslandBlackDoor").add_locations(get_location_names_with_ids([
            "Grey Zone - Silver Chest From Black Door"
        ]),SDLocation)
#
        world.get_region("BlackBackdoorIsland").add_locations(get_location_names_with_ids([
            "Black Zone - Chaos Scatter Chest"
        ]),SDLocation)


#
    world.get_region("OngardRoom").add_locations(get_location_names_with_ids([
        "Ongard Memo 1","Ongard Memo 2",
    ]),SDLocation)
#
    world.get_region("Hub3GreenSide").add_locations(get_location_names_with_ids([

    ]),SDLocation)
#
    world.get_region("Orange1").add_locations(get_location_names_with_ids([
        "Orange Zone - Right Room 1","Orange Zone - Left Room Chest","Orange Zone - Center Room Silver Chest",
        "Orange Zone - Center Room Green Chest"
    ]),SDLocation)
#
    world.get_region("DualistsRoom").add_locations(get_location_names_with_ids([
        "Dualists Memo 1","Dualists Memo 2",
    ]),SDLocation)
#
    world.get_region("Hub3PurpleSide").add_locations(get_location_names_with_ids([
        "Grey Zone - Path To Orange Zone Chest",
    ]),SDLocation)
#
    world.get_region("Orange2").add_locations(get_location_names_with_ids([
        "Orange Zone - ReCollection Room Gold Chest","Orange Zone - ReCollection Room Silver Chest",
        "Orange Zone - ReCollection 07 Unlock",
    ]),SDLocation)
#
    if not (world.options.easylogic):
        world.get_region("OrangeBackdoorIsland").add_locations(get_location_names_with_ids([
            "Orange Zone - Chaos Cyphon Chest",
        ]),SDLocation)
#
        world.get_region("GreenBackdoorIsland").add_locations(get_location_names_with_ids([
            "Green Zone - Chaos Wink Chest"
        ]),SDLocation)
#
    world.get_region("Black1").add_locations(get_location_names_with_ids([
        "Black Zone - First Room Chest Behind Key Bridge","Black Zone - Rot Passageway 1 Gold Chest",
        "Black Zone - Silver Chest Next To First Elevator","Black Zone - Green Chest Past First Elevator",
    ]),SDLocation)
#
    world.get_region("KisaijuRoom").add_locations(get_location_names_with_ids([
        "Kisaiju Memo 1","Kisaiju Memo 2",
    ]),SDLocation)
#
    world.get_region("Black2").add_locations(get_location_names_with_ids([
        "Black Zone - Second Elevator Room Behind Key Bridge","Black Zone - Rot Passageway 2 Gold Chest",
    ]),SDLocation)
#
    world.get_region("Griffin2Room").add_locations(get_location_names_with_ids([
        "Griffin (Black Zone) Memo 1","Griffin (Black Zone) Memo 2","Black Zone - ReCollection 01 Unlock",
    ]),SDLocation)
#
#    world.get_region("BlackDungeon").add_locations(get_location_names_with_ids([
#Doesn't seem to have any items.
#    ]),SDLocation)
#
    world.get_region("Yellow1").add_locations(get_location_names_with_ids([
        "Yellow Zone - Green Chest Before Esquire","Yellow Zone - Green Chest Behind Early Key Bridge",
    ]),SDLocation)
#
    world.get_region("EsquireRoom").add_locations(get_location_names_with_ids([
        "Esquire Memo 1","Esquire Memo 2"
    ]),SDLocation)
#
    world.get_region("Yellow2").add_locations(get_location_names_with_ids([
        "Yellow Zone - Silver Chest Atop Waterfall","Yellow Zone - Green Chest Approaching Mothership",
        "Yellow Zone - Gold Chest At Bottom of Waterfall",
    ]),SDLocation)
#
    world.get_region("MothershipRoom").add_locations(get_location_names_with_ids([
        "Mothership Memo 1","Mothership Memo 2"
    ]),SDLocation)
#
    world.get_region("YellowLighthouse").add_locations(get_location_names_with_ids([
        "Yellow Zone - ReCollection Room Chest","Yellow Zone - East of Tower Gold Chest",
        "Yellow Zone - East of Tower Green Chest","Yellow Zone - East of Tower Silver Chest",
        "Yellow Tower - Green Chest","Yellow Tower - Gold Chest","Yellow Zone - ReCollection 06 Unlock",
    ]),SDLocation)
#
    world.get_region("FinalLobby").add_locations(get_location_names_with_ids([
        "Forge Chaotic Dance","White Zone - ReCollection 10 Unlock","White Zone - MemFinder Unlock",
    ]),SDLocation)
#
    world.get_region("ExanderZone").add_locations(get_location_names_with_ids([
        "Final Zone - Silver Chest","Final Zone - Green Chest","Final Zone - Gold Chest",
        "Final Zone Festival - Green Chest","Final Zone Festival - Silver Chest","Final Zone Festival - Gold Chest",
        "Final Zone - ReCollection 09 Unlock",
        "Final Zone - Gold Chest Before Exander","Final Zone - Exander Location",
    ]),SDLocation)
#
    world.get_region("OmniZone1").add_locations(get_location_names_with_ids([
        "White Zone - First Room Green Chest","White Zone - Dragon Room Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone2").add_locations(get_location_names_with_ids([
        "White Zone - Kappa Room Green Chest","White Zone - Kappa Room Gold Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone3").add_locations(get_location_names_with_ids([
        "White Zone - Cyclops Room Gold Chest", "White Zone - Cyclops Room Green Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone4").add_locations(get_location_names_with_ids([
        "White Zone - Unicorn Room Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone5").add_locations(get_location_names_with_ids([
        "White Zone - Phoenix Room Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone6").add_locations(get_location_names_with_ids([
        "White Zone - Pulgasari Room Chest"
    ]),SDLocation)
#
    world.get_region("OmniZone7").add_locations(get_location_names_with_ids([
        "White Zone - Pixie Room Chest"
    ]),SDLocation)
#
    world.get_region("OmniRoom").add_locations(get_location_names_with_ids([
        "White Zone - Omni Chest"
    ]),SDLocation)

#Here are the optional ones.

#Minibosses
    if world.options.minibosses:
#
        world.get_region("QuoDefenderItems").add_locations(get_location_names_with_ids([
            "Quo Defender Reward 1","Quo Defender Reward 2","Quo Defender Reward 3",
        ]), SDLocation)
#
        world.get_region("KingooseItems").add_locations(get_location_names_with_ids([
            "Kingoose Reward 1","Kingoose Reward 2","Kingoose Reward 3",
        ]), SDLocation)
#
        world.get_region("Griffin1Items").add_locations(get_location_names_with_ids([
            "Griffin (Blue Zone) Reward 1","Griffin (Blue Zone) Reward 2","Griffin (Blue Zone) Reward 3",
        ]), SDLocation)
#
        world.get_region("DiggerItems").add_locations(get_location_names_with_ids([
            "Digger Reward 1","Digger Reward 2","Digger Reward 3",
        ]), SDLocation)
#
        world.get_region("DesmodusItems").add_locations(get_location_names_with_ids([
            "Desmodus Reward 1","Desmodus Reward 2","Desmodus Reward 3",
        ]), SDLocation)
#
        world.get_region("SquailItems").add_locations(get_location_names_with_ids([
            "Squail Reward 1","Squail Reward 2","Squail Reward 3",
        ]), SDLocation)
#
        world.get_region("SwordmoleItems").add_locations(get_location_names_with_ids([
            "Swordmole Reward 1","Swordmole Reward 2","Swordmole Reward 3"
        ]), SDLocation)
#
        world.get_region("ScaventureItems").add_locations(get_location_names_with_ids([
            "Scaventure Reward 1","Scaventure Reward 2","Scaventure Reward 3"
        ]), SDLocation)
#
        world.get_region("OngardItems").add_locations(get_location_names_with_ids([
            "Ongard Reward 1","Ongard Reward 2","Ongard Reward 3",
        ]), SDLocation)
#
        world.get_region("DualistsItems").add_locations(get_location_names_with_ids([
            "Dualists Reward 1","Dualists Reward 2","Dualists Reward 3",
        ]), SDLocation)
#
        world.get_region("KisaijuItems").add_locations(get_location_names_with_ids([
            "Kisaiju Reward 1","Kisaiju Reward 2","Kisaiju Reward 3",
        ]), SDLocation)
#
        world.get_region("Griffin2Items").add_locations(get_location_names_with_ids([
            "Griffin (Black Zone) Reward 1","Griffin (Black Zone) Reward 2","Griffin (Black Zone) Reward 3"
        ]), SDLocation)
#
        world.get_region("EsquireItems").add_locations(get_location_names_with_ids([
            "Esquire Reward 1","Esquire Reward 2","Esquire Reward 3"
        ]), SDLocation)
#
        world.get_region("MothershipItems").add_locations(get_location_names_with_ids([
            "Mothership Reward 1","Mothership Reward 2","Mothership Reward 3"
        ]), SDLocation)

#Wardens
    if world.options.wardens:
#
        world.get_region("NyxItems").add_locations(get_location_names_with_ids([
            "Nyx Reward 1","Nyx Reward 2","Nyx Reward 3","Nyx Reward Key"
        ]), SDLocation)
#
        world.get_region("ScatterItems").add_locations(get_location_names_with_ids([
            "Scatter Reward 1","Scatter Reward 2","Scatter Reward 3","Scatter Reward Key"
        ]), SDLocation)
#
        world.get_region("CyphonItems").add_locations(get_location_names_with_ids([
            "Cyphon Reward 1","Cyphon Reward 2","Cyphon Reward 3","Cyphon Reward Key"
        ]), SDLocation)
#
        world.get_region("EnriItems").add_locations(get_location_names_with_ids([
            "Enri Reward 1","Enri Reward 2","Enri Reward 3","Enri Reward Key",
        ]), SDLocation)
#
        world.get_region("RudaItems").add_locations(get_location_names_with_ids([
            "Ruda Reward 1","Ruda Reward 2","Ruda Reward 3","Ruda Reward Key"
        ]), SDLocation)
#
        world.get_region("RotItems").add_locations(get_location_names_with_ids([
            "Rot Reward 1","Rot Reward 2","Rot Reward 3","Rot Reward Key"
        ]), SDLocation)
#
        world.get_region("WinkItems").add_locations(get_location_names_with_ids([
            "Wink Reward 1","Wink Reward 2","Wink Reward 3"
        ]), SDLocation)
#
        world.get_region("FinalGriffinItems").add_locations(get_location_names_with_ids([
            "Griffin (Final) Reward 1","Griffin (Final) Reward 2","Griffin (Final) Reward 3","Griffin (Final) Reward 4"
        ]), SDLocation)

#Chaos Wardens
    if world.options.chaoswardens:
#
        world.get_region("ChaosNyxItems").add_locations(get_location_names_with_ids([
            "Chaos Nyx Reward Fragment","Chaos Nyx Reward 1","Chaos Nyx Reward 2","Chaos Nyx Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosScatterItems").add_locations(get_location_names_with_ids([
            "Chaos Scatter Reward Fragment","Chaos Scatter Reward 1","Chaos Scatter Reward 2","Chaos Scatter Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosCyphonItems").add_locations(get_location_names_with_ids([
            "Chaos Cyphon Reward Fragment","Chaos Cyphon Reward 1","Chaos Cyphon Reward 2","Chaos Cyphon Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosEnriItems").add_locations(get_location_names_with_ids([
            "Chaos Enri Reward Fragment","Chaos Enri Reward 1","Chaos Enri Reward 2","Chaos Enri Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosRudaItems").add_locations(get_location_names_with_ids([
            "Chaos Ruda Reward Fragment","Chaos Ruda Reward 1","Chaos Ruda Reward 2","Chaos Ruda Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosRotItems").add_locations(get_location_names_with_ids([
            "Chaos Rot Reward Fragment","Chaos Rot Reward 1","Chaos Rot Reward 2","Chaos Rot Reward 3"
        ]), SDLocation)
#
        world.get_region("ChaosWinkItems").add_locations(get_location_names_with_ids([
            "Chaos Wink Reward Fragment","Chaos Wink Reward 1","Chaos Wink Reward 2","Chaos Wink Reward 3"
        ]), SDLocation)
#
        world.get_region("PurpleHippoItems").add_locations(get_location_names_with_ids([
            "Purple Hippo Reward 1","Purple Hippo Reward 2","Purple Hippo Reward 3"
        ]), SDLocation)

    if world.options.omni or world.options.goal == 1:
        world.get_region("OmniItems").add_locations(get_location_names_with_ids([
            "Omni Reward 1","Omni Reward 2","Omni Reward 3",
        ]), SDLocation)

    if world.options.starstuds:
        world.get_region("Starstuds").add_locations(get_location_names_with_ids([
            "Starstud 1","Starstud 2","Starstud 3","Starstud 4","Starstud 5","Starstud 6","Starstud 7","Starstud 8",
            "Starstud 9",
            "Starstud 10","Starstud 11","Starstud 12","Starstud 13","Starstud 14","Starstud 15","Starstud 16",
            "Starstud 17",
            "Starstud 18","Starstud 19",
            "Starstud 20","Starstud 21","Starstud 22","Starstud 23","Starstud 24","Starstud 25",
        ]), SDLocation)


    if world.options.shops:
# #
#         world.get_region("Shop").add_locations(get_location_names_with_ids([
# #No items here.
#
#         ]), SDLocation)
#
        world.get_region("Shop1").add_locations(get_location_names_with_ids([
            "Shop 1 (Req 1 Party Member)", "Shop 2 (Req 1 Party Member)","Shop 3 (Req 1 Party Member)",
            "Shop 4 (Req 1 Party Member)",
            "Shop 5 (Req 1 Party Member)", "Shop 6 (Req 1 Party Member)", "Shop 7 (Req 1 Party Member)",
            "Shop 8 (Req 1 Party Member)",
            "Shop 9 (Req 1 Party Member)", "Shop 10 (Req 1 Party Member)", "Shop 11 (Req 1 Party Member)",
            "Shop 12 (Req 1 Party Member)",
            "Shop 13 (Req 1 Party Member)","Shop 14 (Req 1 Party Member)", "Shop 15 (Req 1 Party Member)",
            "Shop 16 (Req 1 Party Member)",
            "Shop 17 (Req 1 Party Member)",
        ]), SDLocation)
#
        world.get_region("Shop2").add_locations(get_location_names_with_ids([
            "Shop 18 (Req 2 Party Members)","Shop 19 (Req 2 Party Members)","Shop 20 (Req 2 Party Members)",
            "Shop 21 (Req 2 Party Members)","Shop 22 (Req 2 Party Members)",
        ]), SDLocation)
#
        world.get_region("Shop3").add_locations(get_location_names_with_ids([
            "Shop 23 (Req 3 Party Members)","Shop 24 (Req 3 Party Members)","Shop 25 (Req 3 Party Members)",
            "Shop 26 (Req 3 Party Members)","Shop 27 (Req 3 Party Members)","Shop 28 (Req 3 Party Members)",
        ]), SDLocation)
#
        world.get_region("Shop4").add_locations(get_location_names_with_ids([
            "Shop 29 (Req 4 Party Members)","Shop 30 (Req 4 Party Members)","Shop 31 (Req 4 Party Members)",
            "Shop 32 (Req 4 Party Members)","Shop 33 (Req 4 Party Members)",
        ]), SDLocation)
#
        world.get_region("Shop5").add_locations(get_location_names_with_ids([
            "Shop 34 (Req 5 Party Members)","Shop 35 (Req 5 Party Members)","Shop 36 (Req 5 Party Members)",
            "Shop 37 (Req 5 Party Members)","Shop 38 (Req 5 Party Members)","Shop 39 (Req 5 Party Members)",
        ]), SDLocation)
#
        world.get_region("Shop6").add_locations(get_location_names_with_ids([
            "Shop 40 (Req 6 Party Members)","Shop 41 (Req 6 Party Members)", "Shop 42 (Req 6 Party Members)",
            "Shop 43 (Req 6 Party Members)", "Shop 44 (Req 6 Party Members)", "Shop 45 (Req 6 Party Members)",
        ]), SDLocation)
#
        world.get_region("Shop7").add_locations(get_location_names_with_ids([
            "Shop 46 (Req 7 Party Members)","Shop 47 (Req 7 Party Members)","Shop 48 (Req 7 Party Members)",
            "Shop 49 (Req 7 Party Members)",
            "Shop 50 (Req 7 Party Members)","Shop 51 (Req 7 Party Members)","Shop 52 (Req 7 Party Members)",
            "Shop 53 (Req 7 Party Members)",
            "Shop 54 (Req 7 Party Members)","Shop 55 (Req 7 Party Members)","Shop 56 (Req 7 Party Members)",
            "Shop 57 (Req 7 Party Members)",
            "Shop 58 (Req 7 Party Members)","Shop 59 (Req 7 Party Members)",
        ]), SDLocation)

    if world.options.recollections:
#
        world.get_region("ReCollectionRed").add_locations(get_location_names_with_ids([
            "ReCollection 2 (Red) Reward 1", "ReCollection 2 (Red) Reward 2", "ReCollection 2 (Red) Reward 3",
            "ReCollection 2 (Red) Reward 4", "ReCollection 2 (Red) Reward 5", "ReCollection 2 (Red) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionBlue").add_locations(get_location_names_with_ids([
            "ReCollection 5 (Blue) Reward 1", "ReCollection 5 (Blue) Reward 2", "ReCollection 5 (Blue) Reward 3",
            "ReCollection 5 (Blue) Reward 4", "ReCollection 5 (Blue) Reward 5", "ReCollection 5 (Blue) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionGreen").add_locations(get_location_names_with_ids([
            "ReCollection 3 (Green) Reward 1", "ReCollection 3 (Green) Reward 2", "ReCollection 3 (Green) Reward 3",
            "ReCollection 3 (Green) Reward 4","ReCollection 3 (Green) Reward 5", "ReCollection 3 (Green) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionPurple").add_locations(get_location_names_with_ids([
            "ReCollection 4 (Purple) Reward 1", "ReCollection 4 (Purple) Reward 2", "ReCollection 4 (Purple) Reward 3",
            "ReCollection 4 (Purple) Reward 4", "ReCollection 4 (Purple) Reward 5", "ReCollection 4 (Purple) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionOrange").add_locations(get_location_names_with_ids([
            "ReCollection 7 (Orange) Reward 1", "ReCollection 7 (Orange) Reward 2", "ReCollection 7 (Orange) Reward 3",
            "ReCollection 7 (Orange) Reward 4", "ReCollection 7 (Orange) Reward 5", "ReCollection 7 (Orange) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionBlack").add_locations(get_location_names_with_ids([
            "ReCollection 1 (Black) Reward 1","ReCollection 1 (Black) Reward 2","ReCollection 1 (Black) Reward 3",
            "ReCollection 1 (Black) Reward 4","ReCollection 1 (Black) Reward 5","ReCollection 1 (Black) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionYellow").add_locations(get_location_names_with_ids([
            "ReCollection 6 (Yellow) Reward 1", "ReCollection 6 (Yellow) Reward 2", "ReCollection 6 (Yellow) Reward 3",
            "ReCollection 6 (Yellow) Reward 4", "ReCollection 6 (Yellow) Reward 5", "ReCollection 6 (Yellow) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionGrey").add_locations(get_location_names_with_ids([
            "ReCollection 8 (Grey) Reward 1", "ReCollection 8 (Grey) Reward 2", "ReCollection 8 (Grey) Reward 3",
            "ReCollection 8 (Grey) Reward 4", "ReCollection 8 (Grey) Reward 5", "ReCollection 8 (Grey) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionExander").add_locations(get_location_names_with_ids([
            "ReCollection 9 (Exander) Reward 1", "ReCollection 9 (Exander) Reward 2",
            "ReCollection 9 (Exander) Reward 3",
            "ReCollection 9 (Exander) Reward 4", "ReCollection 9 (Exander) Reward 5",
            "ReCollection 9 (Exander) Reward 6",
        ]), SDLocation)
#
        world.get_region("ReCollectionWhite").add_locations(get_location_names_with_ids([
            "ReCollection 10 (Tefka) Reward 1", "ReCollection 10 (Tefka) Reward 2", "ReCollection 10 (Tefka) Reward 3",
            "ReCollection 10 (Tefka) Reward 4", "ReCollection 10 (Tefka) Reward 5", "ReCollection 10 (Tefka) Reward 6",
        ]), SDLocation)


def create_events(world: SDWorld) -> None:
    world.get_region("Hub1").locations.append(
        SDLocation(world.player, "Starstud1Empty", None, world.get_region("Hub1")))
    world.get_region("Hub2").locations.append(
        SDLocation(world.player, "Starstud2Empty", None, world.get_region("Hub2")))
    world.get_region("Red1").locations.append(
        SDLocation(world.player, "Starstud3Empty", None, world.get_region("Red1")))
    world.get_region("Red2").locations.append(
        SDLocation(world.player, "Starstud4Empty", None, world.get_region("Red2")))
    world.get_region("Red2").locations.append(
        SDLocation(world.player, "Starstud5Empty", None, world.get_region("Red2")))
    world.get_region("Orange1").locations.append(
        SDLocation(world.player, "Starstud6Empty", None, world.get_region("Orange1")))
    world.get_region("Orange1").locations.append(
        SDLocation(world.player, "Starstud24Empty", None, world.get_region("Orange1")))
    world.get_region("Orange2").locations.append(
        SDLocation(world.player, "Starstud7Empty", None, world.get_region("Orange2")))
    world.get_region("Hub3GreenSide").locations.append(
        SDLocation(world.player, "Starstud8Empty", None, world.get_region("Hub3GreenSide")))
    world.get_region("EsquireRoom").locations.append(
        SDLocation(world.player, "Starstud9Empty", None, world.get_region("EsquireRoom")))
    world.get_region("Yellow2").locations.append(
        SDLocation(world.player, "Starstud10Empty", None, world.get_region("Yellow2")))
    world.get_region("YellowLighthouse").locations.append(
        SDLocation(world.player, "Starstud11Empty", None, world.get_region("YellowLighthouse")))
    world.get_region("Green1").locations.append(
        SDLocation(world.player, "Starstud12Empty", None, world.get_region("Green1")))
    world.get_region("Green2").locations.append(
        SDLocation(world.player, "Starstud13Empty", None, world.get_region("Green2")))
    world.get_region("Green2").locations.append(
        SDLocation(world.player, "Starstud14Empty", None, world.get_region("Green2")))
    world.get_region("Blue1").locations.append(
        SDLocation(world.player, "Starstud15Empty", None, world.get_region("Blue1")))
    world.get_region("Blue4").locations.append(
        SDLocation(world.player, "Starstud16Empty", None, world.get_region("Blue4")))
    world.get_region("Blue5").locations.append(
        SDLocation(world.player, "Starstud17Empty", None, world.get_region("Blue5")))
    world.get_region("Purple1").locations.append(
        SDLocation(world.player, "Starstud18Empty", None, world.get_region("Purple1")))
    world.get_region("PurpleTower").locations.append(
        SDLocation(world.player, "Starstud19Empty", None, world.get_region("PurpleTower")))
    world.get_region("PurpleTower").locations.append(
        SDLocation(world.player, "Starstud20Empty", None, world.get_region("PurpleTower")))
    world.get_region("Black1").locations.append(
        SDLocation(world.player, "Starstud21Empty", None, world.get_region("Black1")))
    world.get_region("Black2").locations.append(
        SDLocation(world.player, "Starstud22Empty", None, world.get_region("Black2")))
    world.get_region("BlackDungeon").locations.append(
        SDLocation(world.player, "Starstud23Empty", None, world.get_region("BlackDungeon")))
    world.get_region("OmniZone1").locations.append(
        SDLocation(world.player, "Starstud25Empty", None, world.get_region("FinalLobby")))

    for i in range(25):
        location_name = f"Starstud{i + 1}Empty"
        location = world.get_location(location_name)
        starstud = items.SDItem("Starstud", ItemClassification.progression, None, world.player)
        location.place_locked_item(starstud)

    #LOCATION_NAME_TO_ID.close()







