from __future__ import annotations

from typing import TYPE_CHECKING
import typing

from BaseClasses import Item, ItemClassification

from worlds.AutoWorld import World, WebWorld
import logging

from ..stardew_valley.stardew_rule import true_

logger = logging.getLogger("Silver Daze")
logger.setLevel(logging.WARNING)

if TYPE_CHECKING:
    from .world import SDWorld

#Sawyer: This time I said screwit and went with the old system we already had, hopefully it works.
#Sawyer: The APQuest version looked mean and scary but we can do it if we must.

class SDItem(Item):
    game = "Silver Daze"




class ItemData(typing.NamedTuple):
    code: int
    classification: ItemClassification = ItemClassification.filler
    category: str = 'Card'
    max_quantity: int = 1
    weight: int = 1

def decide_omni_progression_status(world: SDWorld) -> ItemClassification:
    if world.options.goal == 1 or world.options.omni:
        return ItemClassification.progression
    else:
        return ItemClassification.useful

# Item groups for easy management

party_members = {
    "Pinn": ItemData(3001, ItemClassification.progression, "Party"),
    "Geo": ItemData(3002, ItemClassification.progression, "Party"),
    "Kani": ItemData(3003, ItemClassification.progression, "Party"),
    "Shane": ItemData(3004, ItemClassification.progression, "Party"),
    "Jeff": ItemData(3005, ItemClassification.progression, "Party"),
    #"Wink": ItemData(3006, ItemClassification.progression, "Party"),
    "Progressive Wink": ItemData(4247, ItemClassification.progression, "Party", 2),
    "Liza": ItemData(3007, ItemClassification.progression, "Party"),
}

mp3s = {
    "Vengeance": ItemData(1002, ItemClassification.useful, "MP3"),
    "Big Shot": ItemData(1003, ItemClassification.useful, "MP3"),
    "Contact": ItemData(1004, ItemClassification.useful, "MP3"),
    "The Distance": ItemData(1005, ItemClassification.useful, "MP3"),
    "After Pain": ItemData(1006, ItemClassification.useful, "MP3"),
    "Aerodynamic": ItemData(1008, ItemClassification.useful, "MP3"),
    "Flow": ItemData(1009, ItemClassification.useful, "MP3"),

    "Answers": ItemData(1011, ItemClassification.useful, "MP3"),
    "Instant Crush": ItemData(1012, ItemClassification.useful, "MP3"),
    "The One Star": ItemData(1013, ItemClassification.useful, "MP3"),
    "Elevation": ItemData(1014, ItemClassification.useful, "MP3"),
    "Deja Vu": ItemData(1016, ItemClassification.useful, "MP3"),
    "The Good Doctor": ItemData(1017, ItemClassification.useful, "MP3"),
    "Rewrite": ItemData(1018, ItemClassification.useful, "MP3"),
    "Freedom": ItemData(1019, ItemClassification.useful, "MP3"),
    "The Will of One": ItemData(1020, ItemClassification.useful, "MP3"),

    "Dramaturgy": ItemData(1021, ItemClassification.useful, "MP3"),
    "Something About Us": ItemData(1022, ItemClassification.useful, "MP3"),
    "Death By Glamour": ItemData(1023, ItemClassification.useful, "MP3"),
    "Long Dream": ItemData(1024, ItemClassification.useful, "MP3"),
    "Light Up The Night": ItemData(1026, ItemClassification.useful, "MP3"),
    "Stand By Me": ItemData(1027, ItemClassification.useful, "MP3"),
    "Hanabi": ItemData(1028, ItemClassification.useful, "MP3"),

    "Fragments Of Time": ItemData(1031, ItemClassification.useful, "MP3"),
    "Too Good Too Bad": ItemData(1032, ItemClassification.useful, "MP3"),
    "Don't Bother None": ItemData(1033, ItemClassification.useful, "MP3"),
    "Anything": ItemData(1034, ItemClassification.useful, "MP3"),
    "Gigalomania": ItemData(1035, ItemClassification.useful, "MP3"),
    "High Life": ItemData(1036, ItemClassification.useful, "MP3"),
    "Don'tStopMeNow": ItemData(1037, ItemClassification.useful, "MP3"),
    "RTRT": ItemData(1039, ItemClassification.useful, "MP3"),
    "Your Reality": ItemData(1040, ItemClassification.useful, "MP3"),

    "Watercolour": ItemData(1041, ItemClassification.useful, "MP3"),
    "Low Ride": ItemData(1042, ItemClassification.useful, "MP3"),
    "Technician": ItemData(1043, ItemClassification.useful, "MP3"),
    "Flossophy": ItemData(1044, ItemClassification.useful, "MP3"),
    "The Sign": ItemData(1045, ItemClassification.useful, "MP3"),
    "Clear Mind": ItemData(1046, ItemClassification.useful, "MP3"),
    "All Blues": ItemData(1048, ItemClassification.useful, "MP3"),
    "Dry Hands": ItemData(1050, ItemClassification.useful, "MP3"),

    "History Repeating": ItemData(1051, ItemClassification.useful, "MP3"),
    "Motherboard": ItemData(1052, ItemClassification.useful, "MP3"),
    "Oblivion": ItemData(1053, ItemClassification.useful, "MP3"),
    "Gymnopedie": ItemData(1054, ItemClassification.useful, "MP3"),
    "Synthetic": ItemData(1057, ItemClassification.useful, "MP3"),
    "Keep Quiet": ItemData(1058, ItemClassification.useful, "MP3"),
    "What Is Love": ItemData(1059, ItemClassification.useful, "MP3"),
    "Undercover": ItemData(1060, ItemClassification.useful, "MP3"),

    "Strides": ItemData(1061, ItemClassification.useful, "MP3"),
    "Lost In Thought": ItemData(1062, ItemClassification.useful, "MP3"),
    "QuaternionicManifold": ItemData(1064, ItemClassification.useful, "MP3"),
    "Triage": ItemData(1065, ItemClassification.useful, "MP3"),
    "Re:Re": ItemData(1067, ItemClassification.useful, "MP3"),
    "To The Edge": ItemData(1068, ItemClassification.useful, "MP3"),
    "Resistance": ItemData(1069, ItemClassification.useful, "MP3"),
    "imprinting": ItemData(1070, ItemClassification.useful, "MP3"),

    "Glass Onion": ItemData(1071, ItemClassification.useful, "MP3"),
    "Blackbird": ItemData(1072, ItemClassification.useful, "MP3"),
    "I Will": ItemData(1075, ItemClassification.useful, "MP3"),
    "Julia": ItemData(1076, ItemClassification.useful, "MP3"),

}

# In Visual Studio Code or another IDE you can collapse the dict to hide the cards
redcards = {
    "RATD": ItemData(4, ItemClassification.filler, "Card", 0),
    "Cold As Ice": ItemData(5, ItemClassification.filler, "Card", 0),
    "Strife": ItemData(6, ItemClassification.filler, "Card", 0),
    "Morning Ray": ItemData(7, ItemClassification.filler, "Card", 0),
    "Spitfire": ItemData(10),
    "Seru": ItemData(11, ItemClassification.filler, "Card", 0),
    "All You Got": ItemData(12),
    "All You Got (Foil)": ItemData(512),
    "Slug Shot": ItemData(13, ItemClassification.filler, "Card", 0),
    "Drag It Out": ItemData(14),
    "InfernRay": ItemData(15),
    "BlazEdge": ItemData(16),
    "Seeing Red": ItemData(17),
    "Flatten": ItemData(18),
    "Projector": ItemData(19),
    "Off Wave": ItemData(23),
    "ValorDrive": ItemData(25),
    "FirstBurst": ItemData(26),
    "Initiative": ItemData(28),
    "Sonic Boom": ItemData(29),
    "VariaCut": ItemData(30),
    "Blaze": ItemData(34, ItemClassification.filler, "Card", 0),
    "Parry": ItemData(39),
    "FRAGSLASH": ItemData(40),
    "FastestFist": ItemData(41),
    "Finish Touch": ItemData(42),
    "En Passant": ItemData(44),
    "Dragon+": ItemData(48),
}
orangecards = {
    "Motivate": ItemData(52, ItemClassification.filler, "Card", 0),
    "Gyro": ItemData(53, ItemClassification.filler, "Card", 0),
    "Field Guard": ItemData(57),
    "Straight Shot": ItemData(58),
    "NthngRhyms": ItemData(60),
    "The Right Time": ItemData(61),
    "Unleash (Foil)": ItemData(562),
    "Jewell": ItemData(64),
    "My Turn": ItemData(65),
    "Not Dead Yet": ItemData(66),
    "Flexibility": ItemData(68),
    "Warm Glow": ItemData(69, ItemClassification.filler, "Card", 0),
    "ManaShield": ItemData(70),
    "ThiefBolt": ItemData(71),
    "PowerNap": ItemData(72),
    "Bubble": ItemData(73),
    "NovaBurst": ItemData(75),
    "MasterDrive": ItemData(76),
    "Pilfer": ItemData(77, ItemClassification.filler, "Card", 0),
    "VariaJab": ItemData(78),
    "FireSmash": ItemData(79),
    "FRAGHEAL": ItemData(83),
    "Brightslice": ItemData(84, ItemClassification.filler, "Card", 0),
    "OmniGuard": ItemData(85),
    "ScorchEarth": ItemData(87),
    "Dancer": ItemData(88),
    "SpecialWall": ItemData(89),
    "Lost Void": ItemData(90),
    "Phoenix Mira": ItemData(91),
    "Capitalism": ItemData(92),
    "Consume": ItemData(93),
    "Phoenix+": ItemData(98),
}
yellowcards = {
    "Flash": ItemData(102, ItemClassification.filler, "Card", 0),
    "Soft Glow": ItemData(103),
    "Synchlite": ItemData(106, ItemClassification.filler, "Card", 0),
    "Disarm": ItemData(108),
    "Overwhelm": ItemData(112),
    "Execute": ItemData(114),
    "Cremation": ItemData(115),
    "High Kick": ItemData(116),
    "Blacklight": ItemData(118),
    "Screen": ItemData(119, ItemClassification.filler, "Card", 0),
    "Overcharge": ItemData(120),
    "You'll See": ItemData(121),
    "You'll See (Foil)": ItemData(621),
    "WhaleEarly": ItemData(122),
    "Hold It!": ItemData(123, ItemClassification.filler, "Card", 0),
    "PainSplit": ItemData(124),
    "YellowJacket": ItemData(126),
    "Streetlight": ItemData(129),
    "Next Step": ItemData(130),
    "Beat Step": ItemData(133),
    "FRAGSTUN": ItemData(134),
    "Setback": ItemData(135, ItemClassification.filler, "Card", 0),
    "Beatdown": ItemData(139),
    "Shoot Star": ItemData(140),
    "EggnogGuard": ItemData(141),
    "Glass Cannon": ItemData(142),
}
greencards = {
    "Somewhen": ItemData(156, ItemClassification.filler, "Card", 0),
    "Somewhen (Foil)": ItemData(656),
    "3's A Crowd": ItemData(158),
    "Dutch Angle": ItemData(160),
    "Mudsling": ItemData(161, ItemClassification.filler, "Card", 0),
    "Phalanx": ItemData(162),
    "Look Alive": ItemData(163),
    "Helion": ItemData(164),
    "Drift": ItemData(166),
    "This Just In": ItemData(168),
    "Meat Shield": ItemData(169),
    "Once More": ItemData(170),
    "Why Lie?": ItemData(172),
    "GuardBreak": ItemData(173),
    "Wall": ItemData(174),
    "UngaBunga": ItemData(175),
    "GuardiaDrive": ItemData(177),
    "Forcefield": ItemData(178),
    "VariaDrive": ItemData(179),
    "Storage": ItemData(180),
    "Deep Breath": ItemData(182, ItemClassification.filler, "Card", 0),
    "Gamble Beam": ItemData(183),
    "BargainBin": ItemData(185, ItemClassification.filler, "Card", 0),
    "Emerald": ItemData(188),
    "FRAGSHIELD": ItemData(189),
    "Robo Punch": ItemData(192),
    "Simple Playing": ItemData(193, ItemClassification.filler, "Card"),
    "Unicorn+": ItemData(198),
}
bluecards = {
    "Drive Bit": ItemData(206, ItemClassification.filler, "Card", 0),
    "Schema": ItemData(209, ItemClassification.filler, "Card", 0),
    "Rushdown": ItemData(210, ItemClassification.filler, "Card", 0),
    "Be The One": ItemData(212),
    "Light Form": ItemData(213),
    "Vizio": ItemData(215),
    "G.D.Break": ItemData(216),
    "D-Buster": ItemData(219),
    "JstDessrts": ItemData(223),
    "LimitDrive": ItemData(225),
    "VariaDive": ItemData(227),
    "Progress": ItemData(229),
    "Grapevine": ItemData(231),
    "FRAGDRIVE": ItemData(234),
    "Wishful": ItemData(236),
    "Wishful (Foil)": ItemData(736),
    "Multiguard": ItemData(237),
    "Pointblank": ItemData(238),
    "Defender": ItemData(241, ItemClassification.filler, "Card", 0),
    "Vorpal": ItemData(242),
    "Kappa+": ItemData(248),
}
purplecards = {
    "Curiosity": ItemData(254),
    "Speed Mode": ItemData(255, ItemClassification.filler, "Card", 0),
    "Fine Tune": ItemData(256),
    "Ampersand": ItemData(260),
    "Lydian Scale": ItemData(261, ItemClassification.filler, "Card", 0),
    "Brainwave": ItemData(263),
    "Lavender": ItemData(266),
    "ChronoShot": ItemData(268),
    "ZettaBeam": ItemData(269),
    "ColorPoint": ItemData(271),
    "Suprvulcan": ItemData(272),
    "Suprvulcan (Foil)": ItemData(772),
    "Steamroll": ItemData(274),
    "ChargeBolt": ItemData(275),
    "CloudDitto": ItemData(278),
    "LSDJ": ItemData(279, ItemClassification.filler, "Card", 0),
    "Contrarian": ItemData(281),
    "WisdomDrive": ItemData(284),
    "Patience": ItemData(286),
    "VariaBeam": ItemData(288),
    "Voidskipper": ItemData(290),
    "FRAGBOOST": ItemData(291),
    "Floodgate": ItemData(293, ItemClassification.filler, "Card", 0),
    "JumperJet": ItemData(296),
    "Tranche-Voix": ItemData(297),
    "Cyclops+": ItemData(298),
}
blackcards = {
    "CRT": ItemData(303, ItemClassification.filler, "Card", 0),
    "Zoner": ItemData(304, ItemClassification.filler, "Card", 0),
    "Play It Loud": ItemData(307, ItemClassification.filler, "Card", 0),
    "Switchblade": ItemData(310, ItemClassification.filler, "Card", 0),
    "PaintItBlck": ItemData(312),
    "Wasting Time": ItemData(314),
    "PitchShift": ItemData(315),
    "Thrashmetl": ItemData(317),
    "Ace": ItemData(318),
    "Heavyweight": ItemData(319),
    "Disruption": ItemData(321, ItemClassification.filler, "Card", 0),
    "SaltInWound": ItemData(322),
    "ShadowPulse": ItemData(324),
    "AntiDrive": ItemData(329),
    "Begrudge": ItemData(331),
    "Counter": ItemData(333, ItemClassification.filler, "Card", 0),
    "VariaSlice": ItemData(334),
    "Mesmer Eyes": ItemData(337),
    "Mesmer Eyes (Foil)": ItemData(837),
    "CraftyCoyote": ItemData(339),
    "FRAGBLAST": ItemData(340),
    "Backup": ItemData(342, ItemClassification.filler, "Card", 0),
    "CursedSword": ItemData(343),
    "ChaoticDance": ItemData(344, ItemClassification.filler, "Card", 0),
    "GeoRomancey": ItemData(347),
    "Pulgasari+": ItemData(348),
}

keys = {
    "Yellow Key": ItemData(2010, ItemClassification.progression, "Key"),
    "Green Key": ItemData(2011, ItemClassification.progression, "Key"),
    "Blue Key": ItemData(2012, ItemClassification.progression, "Key"),
    "Purple Key": ItemData(2013, ItemClassification.progression, "Key"),
    "Red Key": ItemData(2014, ItemClassification.progression, "Key"),
    "Orange Key": ItemData(2015, ItemClassification.progression, "Key"),
    "Black Key": ItemData(2016, ItemClassification.progression, "Key"),
}

special_keys = {
    "Blue_Zone()": ItemData(2018, ItemClassification.progression, "Glitch"),
    "._locale": ItemData(2019, ItemClassification.progression, "Glitch"),

    "Memfinder": ItemData(2009, ItemClassification.progression, "Memfinder"),

    "Red Fragment": ItemData(2022, ItemClassification.progression, "Fragment"),
    "Orange Fragment": ItemData(2023, ItemClassification.progression, "Fragment"),
    "Yellow Fragment": ItemData(2024, ItemClassification.progression, "Fragment"),
    "Green Fragment": ItemData(2025, ItemClassification.progression, "Fragment"),
    "Blue Fragment": ItemData(2026, ItemClassification.progression, "Fragment"),
    "Purple Fragment": ItemData(2027, ItemClassification.progression, "Fragment"),
    "Black Fragment": ItemData(2028, ItemClassification.progression, "Fragment"),

    #"Exander": ItemData(4247, ItemClassification.useful, "Party"),
}

reco_keys = {
    "ReCollection01": ItemData(4175, ItemClassification.progression, "Fragment"),
    "ReCollection02": ItemData(4166, ItemClassification.progression, "Fragment"),
    "ReCollection03": ItemData(4169, ItemClassification.progression, "Fragment"),
    "ReCollection04": ItemData(4173, ItemClassification.progression, "Fragment"),
    "ReCollection05": ItemData(4168, ItemClassification.progression, "Fragment"),
    "ReCollection06": ItemData(4176, ItemClassification.progression, "Fragment"),
    "ReCollection07": ItemData(4180, ItemClassification.progression, "Fragment"),
    "ReCollection08": ItemData(4182, ItemClassification.progression, "Fragment"),
    "ReCollection09": ItemData(4184, ItemClassification.progression, "Fragment"),
    "ReCollection10": ItemData(4186, ItemClassification.progression, "Fragment"),
}

card_keys = {
    "Ultima": ItemData(352),
#These are cards but we shall treat them as progression.
    "Dragon": ItemData(31, ItemClassification.progression, "Card"),
    "Kappa": ItemData(230, ItemClassification.progression, "Card"),
    "Unicorn": ItemData(187, ItemClassification.progression, "Card"),
    "Cyclops": ItemData(292, ItemClassification.progression, "Card"),
    "Phoenix": ItemData(86, ItemClassification.progression, "Card"),
    "Pulgasari": ItemData(345, ItemClassification.progression, "Card"),
    "Pixie": ItemData(137, ItemClassification.progression, "Card"),
#Irritate is progressive to ensure you can enter the Purple Reco
    "Irritate": ItemData(228, ItemClassification.progression, "Card"),
}

omni_keys = {
#These are progression because they can be used to defeat Omni.
    "Shoto": ItemData(9, ItemClassification.useful, "Card"),
    "Team Player": ItemData(346, ItemClassification.useful, "Card"),
    "Reflect": ItemData(287, ItemClassification.useful, "Card"),
    "Bubble (Foil)": ItemData(573, ItemClassification.useful, "Card", 2),
    "Microwave": ItemData(214, ItemClassification.useful, "Card"),
    "Momentum": ItemData(22, ItemClassification.useful, "Card"),
    "Re:Move": ItemData(43, ItemClassification.useful, "Card"),
    "Bloody Heck": ItemData(38, ItemClassification.useful, "Card", 2),
    "FirstCut": ItemData(27, ItemClassification.useful, "Card"),
    "Mono No Aware": ItemData(244, ItemClassification.useful, "Card"),
    "Storm": ItemData(217, ItemClassification.useful, "Card"),
    "Pep Talk": ItemData(204, ItemClassification.useful, "Card"),
    "SmokeBreak": ItemData(311, ItemClassification.useful, "Card"),
    "GoMode": ItemData(194, ItemClassification.useful, "Card"),
    "Exception": ItemData(221, ItemClassification.useful, "Card"),
    "Wall (Foil)": ItemData(674, ItemClassification.useful, "Card"),
    "Footstool": ItemData(138, ItemClassification.useful, "Card"),
    "Amp Up": ItemData(105, ItemClassification.useful, "Card", 2),
    "NoU": ItemData(323, ItemClassification.useful, "Card"),
    "Exploit": ItemData(239, ItemClassification.useful, "Card"),
    "ZoneSlice": ItemData(224, ItemClassification.useful, "Card"),
    "Pushbie": ItemData(24, ItemClassification.useful, "Card"),
    "MOTS": ItemData(8, ItemClassification.useful, "Card"),
    "FeelingBlue": ItemData(211, ItemClassification.useful, "Card"),
    "Pullbie": ItemData(222, ItemClassification.useful, "Card"),
    "WeirdSig": ItemData(341, ItemClassification.useful, "Card"),
    "TobiasMoor": ItemData(35, ItemClassification.useful, "Card"),
    "Quick Strike": ItemData(109, ItemClassification.useful, "Card"),
    "BlitzDrive": ItemData(125, ItemClassification.useful, "Card"),
    "Underhand": ItemData(113, ItemClassification.useful, "Card"),
    "Re:PUNCH": ItemData(208, ItemClassification.useful, "Card", 2),
    "Softlock": ItemData(59, ItemClassification.useful, "Card"),
    "Chain Bolt": ItemData(128, ItemClassification.useful, "Card"),
    "Hear Me Out": ItemData(56, ItemClassification.useful, "Card"),
    "Save4thBase": ItemData(243, ItemClassification.useful, "Card"),
    "TeaTime": ItemData(157, ItemClassification.useful, "Card"),
    "Cellik": ItemData(308, ItemClassification.useful, "Card"),
    "Setplay": ItemData(253, ItemClassification.useful, "Card"),
    "Improvise": ItemData(282, ItemClassification.filler, "Card"),
    "GoMode (Foil)": ItemData(694, ItemClassification.useful, "Card"),
    "Edison": ItemData(107, ItemClassification.useful, "Card"),
    "VariaBolt": ItemData(127, ItemClassification.useful, "Card"),
    "ItAin'tEasy": ItemData(167, ItemClassification.useful, "Card"),

    "I'm So Tired": ItemData(1074, ItemClassification.useful, "MP3"),
    "Someday": ItemData(1047, ItemClassification.useful, "MP3"),
    "Second Chance": ItemData(1056, ItemClassification.useful, "MP3"),
    "Nightvision": ItemData(1029, ItemClassification.useful, "MP3"),
    "Revolution 1": ItemData(1073, ItemClassification.useful, "MP3"),
    "Voxel Generation": ItemData(1007, ItemClassification.useful, "MP3"),
    "Move Along": ItemData(1049, ItemClassification.useful, "MP3"),
    "Freddie Freeloader": ItemData(1063, ItemClassification.useful, "MP3"),
    "Wet Hands": ItemData(1010, ItemClassification.useful, "MP3"),
    "Move": ItemData(1001, ItemClassification.useful, "MP3"),
    "Due Vendetta": ItemData(1025, ItemClassification.useful, "MP3"),
    "Break Free": ItemData(1015, ItemClassification.useful, "MP3"),
    "Sound of Silence": ItemData(1066, ItemClassification.useful, "MP3"),
    "Handsome People": ItemData(1038, ItemClassification.useful, "MP3"),
    "Short Circuit": ItemData(1030, ItemClassification.useful, "MP3"),
}

consumables = {
    "Heal Token": ItemData(2002, ItemClassification.filler, "Filler", 0),
    "Evade Token": ItemData(2003, ItemClassification.filler, "Filler", 0),
    "Hi-Heal Token": ItemData(2004, ItemClassification.filler, "Filler", 0),
    "Tent Token": ItemData(2005, ItemClassification.filler, "Filler", 0),
    # Tent Token Here
    "Sneak Token": ItemData(2006, ItemClassification.filler, "Filler", 0),
}

#starstuds = {
#    "Starstud": ItemData(None, ItemClassification.progression, "Event", 25),
#}

emblems = {
    "Memory Emblem": ItemData(2040, ItemClassification.progression, "Progression", 0),
    "Chaos Chip": ItemData(2041, ItemClassification.progression, "Progression", 0),
}


cards = {
    **redcards,
    **orangecards,
    **yellowcards,
    **greencards,
    **bluecards,
    **purplecards,
    **blackcards
}

item_table = {
    # This includes all entries in those other dicts in this one
    **party_members,
    **mp3s,
    **keys,
    **special_keys,
    **reco_keys,
    **card_keys,
    **omni_keys,
    **consumables,
    **redcards,
    **orangecards,
    **yellowcards,
    **greencards,
    **bluecards,
    **purplecards,
    **blackcards,
    **emblems,

    # Events - Note that these are items!

    # Other Items
    #  "Sneak Token":          ItemData(2006,       ItemClassification.filler, "Filler",   1),
}

fillercards = list(cards.keys())

sd_item_name_groups = {
    # Sawyer: These aren't working right, I'll fix it later.
    # Pulled the basic code concept from Outer Wilds, probably just a syntax issue with different formats.

    # "progression": set(entry["name"] for entry in item_table if entry["category"] == "progression"),
    # "useful": set(entry["name"] for entry in item_table if entry["category"] == "useful"),
    # "filler": set(entry["name"] for entry in item_table if entry["category"] == "filler"),
    # "trap": set(entry["name"] for entry in item_table if entry["category"] == "trap"),

    "Party": {key for key, val in party_members.items()},
    "Keys": {key for key, val in keys.items()},
    # "Zone Keys": {"Red Key", "Yellow Key", "Blue Key", "Green Key", "Purple Key", "Orange Key", "Black Key"},
}


#Sawyer: This should give us some random fillers. Let's look into adding traps later.
def get_random_filler_item_name(world: SDWorld) -> str:
    fillers = [
        "Evade Token", "Tent Token","Sneak Token","Heal Token","Hi-Heal Token",
        "ChaoticDance", "Backup", "Counter", "Disruption", "Switchblade", "Play It Loud",
        "Zoner", "CRT", "Floodgate", "LSDJ", "Lydian Scale", "Speed Mode", "Defender",
        "Rushdown",
        "Drive Bit", "Schema", "BargainBin", "Deep Breath", "Mudsling", "Somewhen", "Setback", "Hold It!", "Screen",
        "Synchlite", "Flash", "Brightslice", "Pilfer", "Warm Glow", "Gyro", "Motivate", "Blaze",
        "Slug Shot",
        "RATD", "Morning Ray", "Cold As Ice", "Strife",
    ]

    randomResult = world.random.randint(0, len(fillers) - 1)
    return fillers[randomResult]


#Sawyer: Make a random starting member.
def get_random_member(world: SDWorld) -> SDItem:
    #Sawyer: First we get the keys (names of the values) from the party member list.
    members = [key for key, val in party_members.items()]
    #Sawyer: Then we get a random number from the length of that list.
    randomResult = world.random.randint(0, len(members) - 1)
    #Sawyer: Then we get the member belonging to that random number we picked.
    member_name = members[randomResult]
    starty_member = world.create_item(member_name)
    #Next we grab the PinnJoin location which is where the first party member is always given.
    location = world.multiworld.get_location("Geo's Room Reward 1", world.player)
    #Finally, add it to the location.
    location.place_locked_item(starty_member)
    return starty_member
    #members.remove(starty_member)



def initialize_chaos_chips(world: SDWorld) -> list[str]:
    chaos_pool = []
    if world.options.chaoswardens:
        chaos_pool.extend(
            [
                "Chaos Nyx Reward Fragment","Chaos Scatter Reward Fragment","Chaos Enri Reward Fragment",
                "Chaos Cyphon Reward Fragment","Chaos Ruda Reward Fragment","Chaos Rot Reward Fragment",
                "Chaos Wink Reward Fragment","Purple Hippo Reward 1",
            ]
        )

    if world.options.wardens:
        chaos_pool.extend(
            [
                "Nyx Reward Key", "Scatter Reward Key", "Enri Reward Key", "Cyphon Reward Key", "Ruda Reward Key",
                "Rot Reward Key", "Wink Reward 1", "Griffin (Final) Reward 4",
            ]
        )

    if world.options.minibosses:
        chaos_pool.extend(
            [
                "Quo Defender Reward 1", "Kingoose Reward 1", "Griffin (Blue Zone) Reward 1", "Digger Reward 1",
                "Desmodus Reward 1", "Squail Reward 1", "Swordmole Reward 1", "Scaventure Reward 1", "Ongard Reward 1",
                "Dualists Reward 1","Kisaiju Reward 1", "Griffin (Black Zone) Reward 1", "Esquire Reward 1",
                "Mothership Reward 1",
            ]
        )

    if world.options.omni:
        chaos_pool.extend(
            [
                "Omni Reward 1", "White Zone - Omni Chest"
            ]
        )

    world.random.shuffle(chaos_pool)
    world.chaos_pool = chaos_pool
    return chaos_pool

def get_random_chaos_chips(world: SDWorld):
    #Sawyer: Shuffle the pool of eligible places we can put Chaos Chips.
    initialize_chaos_chips(world)
    pool = world.options.chippool
    chaos_chip = world.create_item("Chaos Chip")

    #Sawyer: If chippool is less than required chips, make required chips the pool.
    if world.options.chippool < world.options.chipcount:
        pool = world.options.chipcount

    #If they don't have enough bosses due to settings, this will set their max chips to the number of bosses.
    if pool > len(world.chaos_pool):
        pool = len(world.chaos_pool)
        logger.warning(
            f"Silver Daze ({world.player_name}): "
            f"There are fewer bosses in your settings than Chaos Chips required to beat the game. "
            f"The difference will be subtracted from your Chips."
        )

    #Sawyer: Go through the shuffled Chaos Chip pool, and if we don't have enough chips yet, place a chip.
    chips_added = 0
    for name in world.chaos_pool:
        location = world.multiworld.get_location(name, world.player)
        if chips_added < pool:
            chips_added += 1
            location.place_locked_item(chaos_chip)

        else:
            break

def create_all_items(world: SDWorld):
    itempool = []

    if world.options.goal == 2:
        goal = world.options.emblemcount
        emblems_added = 0
        while emblems_added < world.options.emblempool:
            emblems_added += 1
            itempool.append(world.create_item("Memory Emblem"))
        while emblems_added < goal:
            emblems_added += 1
            itempool.append(world.create_item("Memory Emblem"))
    if world.options.goal == 3:
        get_random_chaos_chips(world)



    # for name in item_table:
    #     itempool.append(world.create_item(name))
    for name in party_members:
        for x in range(0, party_members[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in mp3s:
        for x in range(0, mp3s[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in keys:
        for x in range(0, keys[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in special_keys:
        for x in range(0, special_keys[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in card_keys:
        for x in range(0, card_keys[name].max_quantity):
            itempool.append(world.create_item(name))
    for name in omni_keys:
        for x in range (0, omni_keys[name].max_quantity):
            itempool.append(SDItem(name, decide_omni_progression_status(world), omni_keys[name].code, world.player))
    if world.options.recollections:
        for name in reco_keys:
            for x in range(0, reco_keys[name].max_quantity):
                itempool.append(world.create_item(name))


    # Starting Party Member given at game start
    #if world.options.starting_party_member:
    itempool.remove(get_random_member(world))
    #This adds in the second Wink slot.
    #itempool.append(world.create_item("Progressive Wink"))


    #The following block will give us random cards but will *not* give us duplicate cards.
    #Create a "deck" of cards from the list.
    fillerCards = list(cards)
    #Shuffle the deck of cards.
    world.random.shuffle((fillerCards))
    #Then for each card in the shuffled deck, if we still need filler, add the next card in the deck.
    for name in fillerCards:
        number_of_items = len(itempool)
        number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
        needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
        if needed_number_of_filler_items > 0:
            itempool.append(world.create_item(name))

    #If we still need more filler after that, add filler.
    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


def create_item(self, name: str) -> SDItem:
    item_data = item_table[name]
    item = SDItem(name, item_data.classification, item_data.code, self.player)
    return item


