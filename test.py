import unittest
import main as gym

class TestGymMembership(unittest.TestCase):

    def setUp(self):
        self.gym = gym.GymMembership()
        self.gym.selected_plan = "Basic"
        self.gym.base_cost = self.gym.membership_plans["Basic"]
    
    def test_base_membership_cost(self):
        self.gym.calculate_total_cost()
        self.assertEqual(self.gym.total_cost, 100)
    
    def test_additional_features_cost(self):
        self.gym.selected_features = ["Personal Training"]
        self.gym.additional_cost = self.gym.additional_features["Personal Training"]
        self.gym.calculate_total_cost()
        self.assertEqual(self.gym.total_cost, 150)

    def test_group_discount(self):
        self.gym.group_members = 3
        self.gym.calculate_total_cost()
        self.assertEqual(self.gym.total_cost, 90)
    
    def test_special_offer_discount(self):
        self.gym.base_cost = 250
        self.gym.calculate_total_cost()
        self.assertEqual(self.gym.total_cost, 230)

    def test_premium_membership_surcharge(self):
        self.gym.selected_plan = "Premium"
        self.gym.base_cost = self.gym.membership_plans["Premium"]
        self.gym.calculate_total_cost()
        self.assertEqual(self.gym.total_cost, 172.5)

if __name__ == "__main__":
    unittest.main()
