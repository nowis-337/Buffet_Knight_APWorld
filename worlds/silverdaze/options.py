from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


#Win Condition (Entropy, Omni, Bounty Hunt, Memo Hunt, ChaoticDance)

#Number of Memos (1-14)

#Number of Bounties (1-9)
#Bounties could be any Chaos Warden, Omni, or Purple Hippo

class goal(Choice):
    """
    This selects the victory condition from the following:
    Entropy - Collect seven party members and beat Entropy.
    Omni - Reach Omni and defeat them using any strategy.
    Memory Emblem - Find and collect enough Memory Emblems.
    Chaos Emblem - Defeat bosses holding Chaos Emblems.
    """
    display_name = "Victory Condition"
    option_entropy = 0
    option_omni = 1
    option_memory_emblem = 2
    option_chaos_chip = 3

    default = option_entropy

class minibosses(Toggle):
    """
    This toggles whether minibosses drops are included in the multiworld.
    NOTE: You may still need to defeat minibosses if they are blocking your path to progression
    """
    display_name = "Enable Miniboss Drops"
    default = 1

class wardens(Toggle):
    """
    This toggles whether Wardens drops are included in the multiworld.
    NOTE: This only includes normal Wardens, Chaos Wardens are a different option
    """
    display_name = "Enable Warden Drops"
    default = 1

class chaoswardens(Toggle):
    """
    This toggles whether Chaos Wardens drops are included in the multiworld.
    NOTE: This only includes Chaos Wardens, normal Wardens are a different option
    """
    display_name = "Chaos Warden Drops"
    default = 1

class omni(Toggle):
    """
    This toggles whether Omni drops are included in the multiworld.
    Note! Disabling this could prevent Omni from being beatable.
    """
    display_name = "Omni Drops"
    default = 0

class shops(Toggle):
    """
    This toggles whether shops are included in the multiworld.
    """
    display_name = "Enable Shops"
    default = 1

class recollections(Toggle):
    """
    This toggles whether ReCollections are included in the multiworld.
    """
    display_name = "Enable ReCollections"
    default = 1

class starstuds(Toggle):
    """
    This toggles whether Starstuds are included in the multiworld.
    """
    display_name = "Enable Starstuds"
    default = 1

class easylogic(Toggle):
    """
    This creates an easier path for the player which prevents logic requiring the use of the multicolored doors found
    in other zones.
    """
    display_name = "Easy Logic"
    default = 0

class omniscaling(Toggle):
    """
    This toggles whether Omni scales the party's level down to 50 when fought.
    """
    display_name = "Omni Level Scaling"
    default = 1

class disableenemylevelslider(Toggle):
    """
    This toggles whether the Enemy Levels slider in the options is available to be edited.
    WARNING: This could cause required grinding for some seeds.
    """
    display_name = "Disable Enemy Level Slider"
    default = 0


class emblemcount(Range):
    """
    How many Memory Emblems are required to beat the game?
    (Only affected if your goal is Memory Emblems)
    """
    display_name = "Memory Emblem Requirement"
    range_start = 1
    range_end = 100
    default = 25

class emblempool(Range):
    """
    How many Memory Emblems are added to the item pool?
    (Only affected if your goal is Memory Emblems)
    """
    display_name = "Memory Emblem Pool"
    range_start = 1
    range_end = 100
    default = 25

class chipcount(Range):
    """
    How many Chaos Chips are required to beat the game?
    (Only affected if your goal is Chaos Chips)

    Chaos Chips will only spawn on bosses dictated by your
    settings.
    """
    display_name = "Chaos Chip Requirement"
    range_start = 1
    range_end = 15
    default = 4

class chippool(Range):
    """
    How many Chaos Chips are added to the item pool?
    (Only affected if your goal is Chaos Chips)
    """
    display_name = "Chaos Chip Pool"
    range_start = 1
    range_end = 15
    default = 4

class hintchips(Toggle):
    """
    Toggle on to hint the location of Chaos Chips at the beginning.
    """
    display_name = "Hint Chaos Chips"
    default = 0


@dataclass
class SilverDazeOptions(PerGameCommonOptions):
         #starting_party_member: starting_party_member
         goal: goal
         emblemcount: emblemcount
         emblempool: emblempool
         chipcount: chipcount
         chippool: chippool
         hintchips: hintchips

         easylogic: easylogic
         omniscaling: omniscaling
         disableenemylevelslider: disableenemylevelslider

         minibosses: minibosses
         wardens: wardens
         chaoswardens: chaoswardens
         omni: omni
         shops: shops
         recollections: recollections
         starstuds: starstuds



option_groups = [
    OptionGroup(
        "Goals",
        [goal,emblemcount,emblempool,chipcount,chippool,hintchips]
    ),
    OptionGroup(
        "Gameplay",
        [omniscaling,easylogic,disableenemylevelslider]
    ),
    OptionGroup(
        "Excluded Locations",
        [starstuds,omni,minibosses,wardens,chaoswardens,shops,recollections]
    ),
]

option_presets = {
    "Spinel": {
        "goal": 1,
        "minibosses": True,
        "wardens": True,
        "chaoswardens": True,
        "omni": True,
        "shops": True,
        "recollections": True,
        "starstuds": True,
        "omniscaling": True,
        "disableenemylevelslider": True,
        "easylogic": False,
    },
    "Breezy": {
        "goal": 2,
        "minibosses": False,
        "wardens": False,
        "chaoswardens": False,
        "omni": False,
        "shops": False,
        "recollections": False,
        "starstuds": False,
        "easylogic": True,
        "disableenemylevelslider": False,
        "emblemcount": 25,
        "emblempool": 50,

    }
}