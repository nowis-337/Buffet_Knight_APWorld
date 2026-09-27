from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class HardMode(Toggle):
    """
    Hard mode text
    """
    display_name = "Hard Mode"


@dataclass
class TAOptions(PerGameCommonOptions):
    hard_mode: HardMode


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [HardMode],
    ),
]

option_presets = {
    "Option Preset A": {
        "hard_mode": False,
    },
    "Option Preset B": {
        "hard_mode": True,
    },
}
