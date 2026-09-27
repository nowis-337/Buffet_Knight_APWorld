from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle


class goal(Choice):
    """
    Select the winning condition:
    Default - Reach the end through consuming the Gastronomancy Potion from the Witch after defeating the Demon Chef.
    Full Course - Reach the end through defeating the Game Master Boss. Requires consuming the Gastronomancy Potion, collecting all ingredients and relics.
    """
    display_name = "Victory Condition"
    option_default = 0
    option_full_course = 1

    default = option_default


@dataclass
class BKOptions(PerGameCommonOptions):
    Goal: goal


