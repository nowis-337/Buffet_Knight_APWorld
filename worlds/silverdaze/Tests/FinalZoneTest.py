from .bases import SDTestBase
from worlds.silverdaze import SDWorld

options = {
    "goal": "Entropy",
}

class TestFinalZone(SDTestBase):

    def test_final_zone_chest(self) -> None:
        """Test access to Final Zone first chest"""
        print('Testing to ensure that Wink only counts as a party member once')
        locations = "Final Zone - Silver Chest"
        party = ["Progressive Wink", "Geo", "Kani", "Liza", "Jeff", "Shane"]


        self.collect_by_name(party)
        self.collect_by_name("Black Key")

        print('We only have six party members')
        self.assertFalse(self.can_reach_location(locations))
        self.collect_by_name("Pinn")

        print('Now we have seven party members')
        self.assertTrue(self.can_reach_location(locations))
