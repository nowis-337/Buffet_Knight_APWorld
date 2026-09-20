from BaseClasses import Tutorial
#from scripts.regsetup import description
from worlds.AutoWorld import WebWorld

#from .options import option_groups, option_presets



class CheckTheBackWebWorld(WebWorld):
    game = "Check The Back"

    theme = "ice"

    setup_en = Tutorial(
        tutorial_name = "Setup Guide",
        description = "A guide to setting up Check The Back for MultiWorld.",
        language = "English",
        file_name = "setup_en.md",
        link = "setup/en",
        authors = ["Sawyer Friend"],
    )


    tutorials = [setup_en]

    #option_groups = option_groups
    #options_presets = option_presets
