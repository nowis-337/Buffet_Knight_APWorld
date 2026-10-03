from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class HardMode(Toggle):
    """
    Option to toggle advanced logic that may include sequence-breaks in item placement.
    """
    display_name = "Advanced Logic"


class Goal(Choice):
    """
    Selects the victory condition of the game.
    Default: Requires the collection of all ingredients and at least achieving the "Insatiable Black Hole" Ending.
    Full Course: Requires reaching the end of the Casino Bonus Dungeon and achieving the "More Than You Can Chew" Ending.
    """
    display_name = "Victory Condition"

    option_default = 0
    option_fullcourse = 1

    default = option_default

class ExludeSecret(Toggle):
    """
    Option to exclude Secret Dungeon for progresion items in the multiworld.
    """
    display_name = "Exclude Secret Dungeon"


@dataclass
class BKOptions(PerGameCommonOptions):
    hard_mode: HardMode
    goal: Goal
    exclude_secret: ExludeSecret


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [Goal, ExludeSecret, HardMode],
    ),
]

option_presets = {
    "Default Adventure": {
        "hard_mode": False,
        "goal": 0,
        "exclude_secret": 1,
    },
    "Decadent Full Course": {
        "hard_mode": False,
        "goal": 1,
        "exclude_secret": 0,
    },
}
