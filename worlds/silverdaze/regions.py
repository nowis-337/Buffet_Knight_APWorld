#Sawyer: Don't know what a lot of this is but we'll get there!
from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region, CollectionState

from .rules import sd_has_black, sd_has_blue, sd_has_red, sd_has_green, sd_has_orange, sd_has_purple, sd_has_yellow
from .rules import sd_can_fight_chaos_warden, sd_can_fight_warden, sd_can_fight_miniboss, sd_party_size_meets
from .rules import sd_has_memfinder, sd_has_glitch, sd_can_fight_omni, sd_has_reco, sd_has_reco10, omni_reachable
from .rules import (sd_has_dragon, sd_has_kappa, sd_has_cyclops, sd_has_unicorn, sd_has_phoenix, sd_has_pulgasari,
                    sd_has_pixie)
from .rules import sd_can_use_all_colors, sd_can_status_stun, sd_can_status_depression, sd_has_heal

if TYPE_CHECKING:
    from .world import SDWorld

def create_and_connect_regions(world: SDWorld) -> None:
    state = CollectionState
    create_all_regions(world)
    connect_regions(state,world)

 # Sawyer: Okay, we had some regions defined in our last attempts.
def create_all_regions(world: SDWorld) -> None:

    #Sawyer: Putting them all together now! Don't forget to add the full game's regions when you're done!
    regions = [
        Region("GeoRoom", world.player, world.multiworld),
        Region("Hub1", world.player, world.multiworld),
        Region("Hub2", world.player, world.multiworld),
        Region("QuoDefenderRoom", world.player, world.multiworld),
        Region("Red1", world.player, world.multiworld),
        Region("KingooseRoom", world.player, world.multiworld),
        Region("Red2", world.player, world.multiworld),
        Region("GreyIslandGreenDoor", world.player, world.multiworld),
        Region("YellowBackdoorIsland", world.player, world.multiworld),
        Region("GreyIslandBlueDoor", world.player, world.multiworld),
        Region("GreyIslandRedDoor", world.player, world.multiworld),
        Region("RedBackdoorIsland", world.player, world.multiworld),
        Region("Blue1", world.player, world.multiworld),
        Region("Blue2", world.player, world.multiworld),
        Region("Griffin1Room", world.player, world.multiworld),
        Region("BlueShaneArea", world.player, world.multiworld),
        Region("DiggerRoom", world.player, world.multiworld),
        Region("Blue3", world.player, world.multiworld),
        Region("Blue4", world.player, world.multiworld),
        Region("Blue5", world.player, world.multiworld),
        Region("ScatterRoom", world.player, world.multiworld),
        Region("PurpleBackdoorIsland", world.player, world.multiworld),
        Region("PurpleHippoRoom", world.player, world.multiworld),
        Region("BlueBackdoorIsland", world.player, world.multiworld),
        Region("Green1", world.player, world.multiworld),
        Region("DesmodusRoom", world.player, world.multiworld),
        Region("Green2", world.player, world.multiworld),
        Region("SquailArea", world.player, world.multiworld),
        Region("OrangeBackdoorIsland", world.player, world.multiworld),
        Region("Purple1", world.player, world.multiworld),
        Region("SwordmoleRoom", world.player, world.multiworld),
        Region("Purple2", world.player, world.multiworld),
        Region("ScaventureRoom", world.player, world.multiworld),
        Region("PurpleTower", world.player, world.multiworld),
        Region("GreyIslandBlackDoor", world.player, world.multiworld),
        Region("BlackBackdoorIsland", world.player, world.multiworld),
        Region("OngardRoom", world.player, world.multiworld),
        Region("Hub3GreenSide", world.player, world.multiworld),
        Region("Orange1", world.player, world.multiworld),
        Region("DualistsRoom", world.player, world.multiworld),
        Region("Hub3PurpleSide", world.player, world.multiworld),
        Region("Orange2", world.player, world.multiworld),
        Region("GreenBackdoorIsland", world.player, world.multiworld),
        Region("Black1", world.player, world.multiworld),
        Region("KisaijuRoom", world.player, world.multiworld),
        Region("Black2", world.player, world.multiworld),
        Region("Griffin2Room", world.player, world.multiworld),
        Region("BlackDungeon", world.player, world.multiworld),
        Region("Yellow1", world.player, world.multiworld),
        Region("EsquireRoom", world.player, world.multiworld),
        Region("Yellow2", world.player, world.multiworld),
        Region("MothershipRoom", world.player, world.multiworld),
        Region("YellowLighthouse", world.player, world.multiworld),
        Region("FinalLobby", world.player, world.multiworld),
        Region("ExanderZone", world.player, world.multiworld),
        Region("OmniZone1", world.player, world.multiworld),
        Region("OmniZone2", world.player, world.multiworld),
        Region("OmniZone3", world.player, world.multiworld),
        Region("OmniZone4", world.player, world.multiworld),
        Region("OmniZone5", world.player, world.multiworld),
        Region("OmniZone6", world.player, world.multiworld),
        Region("OmniZone7", world.player, world.multiworld),
        Region("OmniRoom", world.player, world.multiworld),
    ]

    #Below are option regions
    if world.options.shops:
        regions.append(Region("Shop", world.player, world.multiworld))
        # Shop is the hub that contains all other shop checks. It has no locations of its own.
        # The following are all of the shop regions.
        regions.append(Region("Shop1", world.player, world.multiworld))
        regions.append(Region("Shop2", world.player, world.multiworld))
        regions.append(Region("Shop3", world.player, world.multiworld))
        regions.append(Region("Shop4", world.player, world.multiworld))
        regions.append(Region("Shop5", world.player, world.multiworld))
        regions.append(Region("Shop6", world.player, world.multiworld))
        regions.append(Region("Shop7", world.player, world.multiworld))

    if world.options.recollections:
        regions.append(Region("ReCollectionBlue", world.player, world.multiworld))
        regions.append(Region("ReCollectionPurple", world.player, world.multiworld))
        regions.append(Region("ReCollectionBlack", world.player, world.multiworld))
        regions.append(Region("ReCollectionRed", world.player, world.multiworld))
        regions.append(Region("ReCollectionOrange", world.player, world.multiworld))
        regions.append(Region("ReCollectionYellow", world.player, world.multiworld))
        regions.append(Region("ReCollectionGreen", world.player, world.multiworld))
        regions.append(Region("ReCollectionGrey", world.player, world.multiworld))
        regions.append(Region("ReCollectionExander", world.player, world.multiworld))
        regions.append(Region("ReCollectionWhite", world.player, world.multiworld))

    #Sawyer: Bosses are optional so they'll be their own region.
    if world.options.minibosses:
        regions.append(Region("QuoDefenderItems", world.player, world.multiworld))
        regions.append(Region("KingooseItems", world.player, world.multiworld))
        regions.append(Region("Griffin1Items", world.player, world.multiworld))
        regions.append(Region("DiggerItems", world.player, world.multiworld))
        regions.append(Region("DesmodusItems", world.player, world.multiworld))
        regions.append(Region("SquailItems", world.player, world.multiworld))
        regions.append(Region("SwordmoleItems", world.player, world.multiworld))
        regions.append(Region("ScaventureItems", world.player, world.multiworld))
        regions.append(Region("OngardItems", world.player, world.multiworld))
        regions.append(Region("DualistsItems", world.player, world.multiworld))
        regions.append(Region("KisaijuItems", world.player, world.multiworld))
        regions.append(Region("Griffin2Items", world.player, world.multiworld))
        regions.append(Region("EsquireItems", world.player, world.multiworld))
        regions.append(Region("MothershipItems", world.player, world.multiworld))

    if world.options.wardens:
        regions.append(Region("NyxItems", world.player, world.multiworld))
        regions.append(Region("ScatterItems", world.player, world.multiworld))
        regions.append(Region("CyphonItems", world.player, world.multiworld))
        regions.append(Region("EnriItems", world.player, world.multiworld))
        regions.append(Region("RudaItems", world.player, world.multiworld))
        regions.append(Region("RotItems", world.player, world.multiworld))
        regions.append(Region("WinkItems", world.player, world.multiworld))
        regions.append(Region("FinalGriffinItems", world.player, world.multiworld))

    if world.options.chaoswardens:
        regions.append(Region("PurpleHippoItems", world.player, world.multiworld))
        regions.append(Region("ChaosRotItems", world.player, world.multiworld))
        regions.append(Region("ChaosRudaItems", world.player, world.multiworld))
        regions.append(Region("ChaosNyxItems", world.player, world.multiworld))
        regions.append(Region("ChaosEnriItems", world.player, world.multiworld))
        regions.append(Region("ChaosCyphonItems", world.player, world.multiworld))
        regions.append(Region("ChaosWinkItems", world.player, world.multiworld))
        regions.append(Region("ChaosScatterItems", world.player, world.multiworld))

    if world.options.omni or world.options.goal == 1:
        regions.append(Region("OmniItems", world.player, world.multiworld))

    if world.options.starstuds:
        regions.append(Region("Starstuds", world.player, world.multiworld))


    #Sawyer: Add it all together now!
    world.multiworld.regions += regions




#Sawyer: Next part has me nervous. This is entrances, right?
def connect_regions(state: CollectionState, world: SDWorld) -> None:
    world.connect_2way(world.get_region("GeoRoom"), world.get_region("Hub1"),
                       lambda state: sd_party_size_meets(state, world, 1))
    world.connect_2way(world.get_region("Hub1"), world.get_region("Hub2"), lambda state: sd_has_yellow(state, world))

    #this path continues through Red Zone.
    world.connect_2way(world.get_region("Hub2"), world.get_region("QuoDefenderRoom"),
                       lambda state: sd_has_yellow(state, world))
    world.connect_2way(world.get_region("QuoDefenderRoom"), world.get_region("Red1"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Red1"), world.get_region("KingooseRoom"),
                       lambda state: sd_has_yellow(state, world))
    world.connect_2way(world.get_region("KingooseRoom"), world.get_region("Red2"),
                       lambda state: sd_can_fight_miniboss(state, world))

    if not(world.options.easylogic):
        # This path leads through the green door in red zone 1
        world.connect_2way(world.get_region("Red1"), world.get_region("GreyIslandGreenDoor"),
                           lambda state: sd_has_green(state, world))
        #This path leads through the green door in red zone 2
        world.connect_2way(world.get_region("Red2"), world.get_region("YellowBackdoorIsland"),
                           lambda state: sd_has_green(state, world))
        #This path leads through the blue door in red tower
        world.connect_2way(world.get_region("Red2"), world.get_region("GreyIslandBlueDoor"),
                           lambda state: sd_has_blue(state, world))
    #This path leads through the red door in red zone chasm.
    # For all intents and purposes this belongs to Red Zone 2, but I'm diligent.
    world.connect_2way(world.get_region("Red2"), world.get_region("GreyIslandRedDoor"),
                       lambda state: sd_has_red(state, world))
    #This path leads to the red backdoor island
    world.connect_2way(world.get_region("Red1"), world.get_region("RedBackdoorIsland"),
                       lambda state: sd_has_red(state, world))



    #Blue Zone!
    world.connect_2way(world.get_region("Hub2"), world.get_region("Blue1"),
                       lambda state: sd_has_red(state, world))
    #You need two party members to pass the first Blue Bridge.
    world.connect_2way(world.get_region("Blue1"), world.get_region("Blue2"),
                       lambda state: sd_party_size_meets(state, world, 2))
    world.connect_2way(world.get_region("Blue2"), world.get_region("Griffin1Room"),
                       lambda state: sd_party_size_meets(state, world, 1))
    # Right now miniboss logic is the same as Blue2's entrance but that could change, prepping in advance.
    # ShaneArea is technically in Blue2 but I'm making it its own region to be safe.
    world.connect_2way(world.get_region("Griffin1Room"), world.get_region("BlueShaneArea"),
                       lambda state: sd_can_fight_miniboss(state, world))
    #You can also technically skip Griffin by hopping the 3-long bridge.
    world.connect_2way(world.get_region("Blue2"), world.get_region("BlueShaneArea"),
                       lambda state: sd_party_size_meets(state, world,3))
    #Adding the digger room, but it's not necessary because it blocks no paths.
    world.connect_2way(world.get_region("BlueShaneArea"), world.get_region("DiggerRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    #To proceed, you now need three party members.
    world.connect_2way(world.get_region("BlueShaneArea"), world.get_region("Blue3"),
                       lambda state: sd_party_size_meets(state, world,3))
    #To proceed, you now need four party members already!
    world.connect_2way(world.get_region("Blue3"), world.get_region("Blue4"),
                       lambda state: sd_party_size_meets(state, world,4))
    #Let's start by going through the Wink side in Blue 4.
    #Back on track, confronting Scatter!
    world.connect_2way(world.get_region("Blue3"), world.get_region("Blue5"),
                       lambda state: sd_party_size_meets(state, world,4))
    #Normally I don't connect boss rooms but Scatter is a special case because he demands key items.
    world.connect_2way(world.get_region("Blue5"), world.get_region("ScatterRoom"),
                       (lambda state: sd_party_size_meets(state, world,2) and sd_has_glitch(state, world)))
    if not (world.options.easylogic):
        # This path leads through the blue door in blue zone 1
        world.connect_2way(world.get_region("Blue1"), world.get_region("RedBackdoorIsland"),
                           lambda state: sd_has_blue(state, world))
        #This path leads through the blue door in blue zone 3
        world.connect_2way(world.get_region("Blue3"), world.get_region("GreyIslandBlueDoor"),
                           lambda state: sd_has_blue(state, world))
        #This path leads through the yellow door in blue zone 4
        world.connect_2way(world.get_region("Blue4"), world.get_region("PurpleBackdoorIsland"),
                           lambda state: sd_has_yellow(state, world))
    #This path leads through the long path to Purple Hippo's room
    world.connect_2way(world.get_region("Blue3"), world.get_region("PurpleHippoRoom"),
                       lambda state: sd_party_size_meets(state, world,6))
    #This path leads to the Blue Backdoor Island
    world.connect_2way(world.get_region("Blue3"), world.get_region("BlueBackdoorIsland"),
                       lambda state: sd_has_blue(state, world))


    #Green Zone!
    #Don't forget the chest in Grey Zone on your way to Green1, it should be considered part of Green1
    world.connect_2way(world.get_region("Hub1"), world.get_region("Green1"),
                       lambda state: sd_has_blue(state, world))
    world.connect_2way(world.get_region("Green1"), world.get_region("DesmodusRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("DesmodusRoom"), world.get_region("Green2"),
                       lambda state: sd_can_fight_miniboss(state, world))
    #Calling it "Squail Area" because it includes everything behind the Squail
    world.connect_2way(world.get_region("Green2"), world.get_region("SquailArea"),
                       lambda state: sd_can_fight_miniboss(state, world))


    if not (world.options.easylogic):
        # This path is through the Purple Door in the Cyphon Debut area
        world.connect_2way(world.get_region("Green1"), world.get_region("OrangeBackdoorIsland"),
                           lambda state: sd_has_purple(state, world))
        #This path is through the Green Door in the left area
        world.connect_2way(world.get_region("Green2"), world.get_region("GreyIslandGreenDoor"),
                           lambda state: sd_has_green(state, world))
        #This path is to the Green Backdoor Island
    world.connect_2way(world.get_region("Green2"), world.get_region("GreenBackdoorIsland"),
                       lambda state: sd_has_green(state, world))


    #Time for Purple Zone!
    world.connect_2way(world.get_region("Hub2"), world.get_region("Purple1"), lambda state: sd_has_blue(state, world))
    world.connect_2way(world.get_region("Purple1"), world.get_region("SwordmoleRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("SwordmoleRoom"), world.get_region("Purple2"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Purple2"), world.get_region("ScaventureRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("ScaventureRoom"), world.get_region("PurpleTower"),
                       lambda state: sd_can_fight_miniboss(state, world))

    #this connects to the purple backdoor
    world.connect_2way(world.get_region("Purple1"), world.get_region("PurpleBackdoorIsland"),
                       lambda state: sd_has_purple(state, world))
    if not (world.options.easylogic):
        #this is the path through the black door in purple 2
        world.connect_2way(world.get_region("Purple2"), world.get_region("GreyIslandBlackDoor"),
                           lambda state: sd_has_black(state, world))
        #this is the path through the red door in the tower area
        world.connect_2way(world.get_region("PurpleTower"), world.get_region("BlackBackdoorIsland"),
                           lambda state: sd_has_red(state, world))


    #On to Orange Zone!
    #Green Side First
    world.connect_2way(world.get_region("Hub2"), world.get_region("OngardRoom"),
                       lambda state: sd_has_green(state, world))
    world.connect_2way(world.get_region("OngardRoom"), world.get_region("Hub3GreenSide"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Hub3GreenSide"), world.get_region("Orange1"),
                       lambda state: sd_has_purple(state, world))
    #Sawyer! There is a Starstud on the Hub3GreenSide, don't forget!
    #Now Purple Side
    world.connect_2way(world.get_region("Hub2"), world.get_region("DualistsRoom"),
                       lambda state: sd_has_purple(state, world))
    world.connect_2way(world.get_region("DualistsRoom"), world.get_region("Hub3PurpleSide"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Hub3PurpleSide"), world.get_region("Orange1"),
                       lambda state: sd_has_green(state, world))
    #Now we are in Orange Zone proper!
    world.connect_2way(world.get_region("Orange1"), world.get_region("Orange2"),
                       lambda state: sd_has_orange(state, world))

    # this is the path to the orange backdoor
    world.connect_2way(world.get_region("Orange1"), world.get_region("OrangeBackdoorIsland"),
                       lambda state: sd_has_orange(state, world))

    if not (world.options.easylogic):
        # this is the path through the black door in orange1
        world.connect_2way(world.get_region("Orange1"), world.get_region("GreyIslandBlackDoor"),
                           lambda state: sd_has_black(state, world))
        #this is the path through the orange door in the hub
        world.connect_2way(world.get_region("Orange1"), world.get_region("GreenBackdoorIsland"),
                           lambda state: sd_has_orange(state, world))


    #Now we do Black Zone! I'm getting close, I hope.
    world.connect_2way(world.get_region("Hub1"), world.get_region("Black1"),
                       lambda state: sd_has_orange(state, world))
    world.connect_2way(world.get_region("Black1"), world.get_region("KisaijuRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("KisaijuRoom"), world.get_region("Black2"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Black2"), world.get_region("Griffin2Room"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("Griffin2Room"), world.get_region("BlackDungeon"),
                       lambda state: sd_party_size_meets(state, world,1))

    #Here's the backdoor
    world.connect_2way(world.get_region("Black1"), world.get_region("BlackBackdoorIsland"),
                       lambda state: sd_has_black(state, world))
    #The Rot black doors don't lead to a new region. Treat them as item rules.

    #Huh, okay, Yellow Time I guess!
    world.connect_2way(world.get_region("Hub1"), world.get_region("Yellow1"), lambda state: sd_has_black(state, world))
    world.connect_2way(world.get_region("Yellow1"), world.get_region("EsquireRoom"),
                       lambda state: sd_can_fight_miniboss(state, world))
    world.connect_2way(world.get_region("EsquireRoom"), world.get_region("Yellow2"),
                       lambda state:  sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("Yellow2"), world.get_region("MothershipRoom"),
                       lambda state: sd_party_size_meets(state, world,1))
    world.connect_2way(world.get_region("MothershipRoom"), world.get_region("YellowLighthouse"),
                       lambda state: sd_can_fight_miniboss(state, world))

    #This leads to the backdoor!
    world.connect_2way(world.get_region("Yellow1"), world.get_region("YellowBackdoorIsland"),
                       lambda state: sd_party_size_meets(state, world,1))
    #Here's the black door in Yellow Zone
    if not (world.options.easylogic):
        world.connect_2way(world.get_region("Yellow2"), world.get_region("BlueBackdoorIsland"),
                           lambda state: sd_has_black(state, world))

    #Next up, let's connect the fast travels.
    if not (world.options.easylogic):
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("Red2"),
                           lambda state: sd_has_red(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("ScatterRoom"),
                           lambda state: sd_has_blue(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("Green2"),
                           lambda state: sd_has_green(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("PurpleTower"),
                           lambda state: sd_has_purple(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("Orange1"),
                           lambda state: sd_has_orange(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("BlackDungeon"),
                           lambda state: sd_has_black(state, world) and sd_has_memfinder(state,world))
        world.connect_2way(world.get_region("GeoRoom"), world.get_region("YellowLighthouse"),
                           lambda state: sd_has_yellow(state, world) and sd_has_memfinder(state,world))

    #Next up, we'll do the big Final Area shit.
    world.connect_2way(world.get_region("Hub1"), world.get_region("FinalLobby"),
                       lambda state: sd_has_black(state, world))
    #This is also how we reach our goal.
    world.connect_2way(world.get_region("FinalLobby"), world.get_region("ExanderZone"),
                       lambda state: sd_has_black(state, world) and sd_party_size_meets(state, world, 7))

    world.connect_2way(world.get_region("FinalLobby"), world.get_region("OmniZone1"),
                       lambda state: sd_has_black(state, world))
    world.connect_2way(world.get_region("OmniZone1"), world.get_region("OmniZone2"),
                       lambda state:  sd_has_dragon(state, world))
    world.connect_2way(world.get_region("OmniZone2"), world.get_region("OmniZone3"),
                       lambda state: sd_has_kappa(state, world))
    world.connect_2way(world.get_region("OmniZone3"), world.get_region("OmniZone4"),
                       lambda state: sd_has_cyclops(state, world))
    world.connect_2way(world.get_region("OmniZone4"), world.get_region("OmniZone5"),
                       lambda state: sd_has_unicorn(state, world))
    world.connect_2way(world.get_region("OmniZone5"), world.get_region("OmniZone6"),
                       lambda state: sd_has_phoenix(state, world))
    world.connect_2way(world.get_region("OmniZone6"), world.get_region("OmniZone7"),
                       lambda state: sd_has_pulgasari(state, world))
    world.connect_2way(world.get_region("OmniZone7"), world.get_region("OmniRoom"),
                       lambda state: sd_has_pixie(state, world))


    #Shops require a yellow key and get more stock with party members
    if world.options.shops:
        world.connect_2way(world.get_region("Hub1"), world.get_region("Shop"),lambda state: sd_has_yellow(state, world))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop1"),
                           lambda state: sd_party_size_meets(state, world, 1))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop2"),
                           lambda state: sd_party_size_meets(state, world, 2))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop3"),
                           lambda state: sd_party_size_meets(state, world, 3))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop4"),
                           lambda state: sd_party_size_meets(state, world, 4))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop5"),
                           lambda state: sd_party_size_meets(state, world, 5))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop6"),
                           lambda state: sd_party_size_meets(state, world, 6))
        world.connect_2way(world.get_region("Shop"), world.get_region("Shop7"),
                           lambda state: sd_party_size_meets(state, world, 7))

    if world.options.recollections:
        world.connect_2way(world.get_region("Blue4"), world.get_region("ReCollectionBlue"),
                           lambda state: sd_has_reco(state, world, 5))
        world.connect_2way(world.get_region("Green1"), world.get_region("ReCollectionGreen"),
                           lambda state: sd_has_reco(state, world, 3))
        world.connect_2way(world.get_region("PurpleTower"), world.get_region("ReCollectionPurple"),
                           lambda state: sd_has_reco(state, world, 4) and sd_can_status_stun(state, world))
        world.connect_2way(world.get_region("Orange2"), world.get_region("ReCollectionOrange"),
                           lambda state: sd_has_reco(state, world, 7) and sd_can_status_depression(state, world))
        world.connect_2way(world.get_region("Griffin2Room"), world.get_region("ReCollectionBlack"),
                           lambda state: sd_has_reco(state, world, 1))
        world.connect_2way(world.get_region("YellowLighthouse"), world.get_region("ReCollectionYellow"),
                           lambda state: sd_has_yellow(state, world) and sd_has_reco(state, world, 6))
        world.connect_2way(world.get_region("Red2"), world.get_region("ReCollectionRed"),
                           lambda state: sd_has_reco(state, world, 2))
        world.connect_2way(world.get_region("Hub2"), world.get_region("ReCollectionGrey"),
                           lambda state: sd_has_reco(state, world, 8))
        world.connect_2way(world.get_region("FinalLobby"), world.get_region("ReCollectionWhite"),
                           lambda state: sd_has_reco10(state, world) and sd_can_use_all_colors(state, world))
        world.connect_2way(world.get_region("ExanderZone"), world.get_region("ReCollectionExander"),
                           lambda state: sd_has_reco(state, world, 9))

    if world.options.minibosses:
        world.connect_2way(world.get_region("QuoDefenderRoom"), world.get_region("QuoDefenderItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("KingooseRoom"), world.get_region("KingooseItems"),
                           lambda state:  sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("Griffin1Room"), world.get_region("Griffin1Items"),
                           lambda state:  sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("DiggerRoom"), world.get_region("DiggerItems"),
                           lambda state: sd_can_fight_miniboss(state, world) and sd_has_heal(state, world))
        world.connect_2way(world.get_region("DesmodusRoom"), world.get_region("DesmodusItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("SquailArea"), world.get_region("SquailItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("SwordmoleRoom"), world.get_region("SwordmoleItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("ScaventureRoom"), world.get_region("ScaventureItems"),
                           lambda state:  sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("OngardRoom"), world.get_region("OngardItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("DualistsRoom"), world.get_region("DualistsItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("KisaijuRoom"), world.get_region("KisaijuItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("Griffin2Room"), world.get_region("Griffin2Items"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("EsquireRoom"), world.get_region("EsquireItems"),
                           lambda state: sd_can_fight_miniboss(state, world))
        world.connect_2way(world.get_region("MothershipRoom"), world.get_region("MothershipItems"),
                           lambda state: sd_can_fight_miniboss(state, world))

    if world.options.wardens:
        world.connect_2way(world.get_region("Red2"), world.get_region("NyxItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("ScatterRoom"), world.get_region("ScatterItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("Green2"), world.get_region("CyphonItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("PurpleTower"), world.get_region("EnriItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("Orange1"), world.get_region("RudaItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("BlackDungeon"), world.get_region("RotItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("YellowLighthouse"), world.get_region("WinkItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("ExanderZone"), world.get_region("FinalGriffinItems"),
                           lambda state: sd_can_fight_warden(state, world))

    if world.options.chaoswardens:
        world.connect_2way(world.get_region("PurpleHippoRoom"), world.get_region("PurpleHippoItems"),
                           lambda state: sd_can_fight_warden(state, world))
        world.connect_2way(world.get_region("RedBackdoorIsland"), world.get_region("ChaosRotItems"),
                           lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("PurpleBackdoorIsland"), world.get_region("ChaosRudaItems"),
                           lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("BlueBackdoorIsland"), world.get_region("ChaosNyxItems"),
                           lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("OrangeBackdoorIsland"), world.get_region("ChaosCyphonItems"),
                           lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("YellowBackdoorIsland"), world.get_region("ChaosEnriItems"),
                           lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("GreenBackdoorIsland"), world.get_region("ChaosWinkItems"), lambda state: sd_can_fight_chaos_warden(state, world))
        world.connect_2way(world.get_region("BlackBackdoorIsland"), world.get_region("ChaosScatterItems"), lambda state: sd_can_fight_chaos_warden(state, world))

    if world.options.omni or world.options.goal == 1:
        world.connect_2way(world.get_region("OmniRoom"), world.get_region("OmniItems"), lambda state: sd_can_fight_omni(state, world))

    if world.options.starstuds:
        world.connect_2way(world.get_region("Hub1"), world.get_region("Starstuds"), lambda state: sd_party_size_meets(state, world, 1))