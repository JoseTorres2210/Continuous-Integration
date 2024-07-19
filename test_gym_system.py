import unittest
from main import GymMembership, Gym

class TestGymSystem(unittest.TestCase):
    """Unit tests for the Gym and GymMembership classes."""

    def setUp(self):
        """Set up test fixtures for the Gym system tests."""
        self.basic_features = {"Group Classes": 25, "Crossfit Sessions": 10}
        self.premium_features = {"Personal Trainer": 40, "Sauna": 10, "Nutrition Plan": 20}
        self.family_features = {"Tennis Court": 10, "Group Classes": 15}

        self.basic_membership = GymMembership("Basic", 60, self.basic_features)
        self.premium_membership = GymMembership("Premium", 80, self.premium_features)
        self.family_membership = GymMembership("Family", 100, self.family_features)

        self.gym = Gym()
        self.gym.add_membership(self.basic_membership)
        self.gym.add_membership(self.premium_membership)
        self.gym.add_membership(self.family_membership)

    def test_membership_plan_selection(self):
        """Test selection of membership plans."""
        self.assertIsNotNone(self.gym.select_membership("Basic"))
        self.assertIsNotNone(self.gym.select_membership("Premium"))
        self.assertIsNotNone(self.gym.select_membership("Family"))
        with self.assertRaises(ValueError):
            self.gym.select_membership("Nonexistent")

    def test_additional_features_selection(self):
        """Test selection of additional features."""
        self.basic_membership.add_feature("Group Classes")
        self.assertIn("Group Classes", self.basic_membership.selected_features)

        with self.assertRaises(ValueError):
            self.basic_membership.add_feature("Nonexistent Feature")

        self.premium_membership.add_feature("Personal Trainer")
        self.premium_membership.add_feature("Sauna")
        self.assertIn("Personal Trainer", self.premium_membership.selected_features)
        self.assertIn("Sauna", self.premium_membership.selected_features)

    def test_cost_calculation(self):
        """Test calculation of membership costs."""
        self.assertEqual(self.basic_membership.calculate_cost(), 60)

        self.basic_membership.add_feature("Group Classes")
        self.assertEqual(self.basic_membership.calculate_cost(), 85)

        self.premium_membership.add_feature("Personal Trainer")
        self.premium_membership.add_feature("Sauna")
        self.assertEqual(self.premium_membership.calculate_cost(), 130)

    def test_discounts_for_group_memberships(self):
        """Test application of group discounts."""
        self.basic_membership.add_feature("Group Classes")
        total_cost = self.gym.calculate_total_cost(self.basic_membership, 2)
        self.assertAlmostEqual(total_cost, 153, places=0)

        total_cost = self.gym.calculate_total_cost(self.basic_membership, 1)
        self.assertEqual(total_cost, 85)

    def test_special_offer_discounts(self):
        """Test application of special offer discounts."""
        self.premium_membership.add_feature("Personal Trainer")
        self.premium_membership.add_feature("Sauna")
        total_cost = self.gym.calculate_total_cost(self.premium_membership, 5)
        expected_cost = 622.75
        self.assertAlmostEqual(total_cost, expected_cost, places=0)

        self.basic_membership.add_feature("Group Classes")
        total_cost = self.gym.calculate_total_cost(self.basic_membership, 4)
        expected_cost = 286
        self.assertAlmostEqual(total_cost, expected_cost, places=0)

    def test_premium_membership_features(self):
        """Test additional cost calculation for premium memberships."""
        self.premium_membership.add_feature("Personal Trainer")
        total_cost = self.gym.calculate_total_cost(self.premium_membership, 1)
        self.assertEqual(total_cost, 138)

    def test_error_handling(self):
        """Test error handling for invalid feature selection."""
        with self.assertRaises(ValueError):
            self.basic_membership.add_feature("Nonexistent Feature")

if __name__ == "__main__":
    unittest.main()
