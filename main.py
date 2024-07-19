"""
Module to define the GymMembership and Gym classes for managing gym memberships and features.
"""

class GymMembership:
    """Represents a gym membership with optional additional features."""

    def __init__(self, name, base_cost, additional_features=None):
        self.name = name
        self.base_cost = base_cost
        self.additional_features = additional_features if additional_features else {}
        self.selected_features = []

    def add_feature(self, feature_name):
        """Adds a feature to the membership if available."""
        if feature_name in self.additional_features:
            self.selected_features.append(feature_name)
            print("\n-----------------------------------------------------\n" +
                  f"Adding {feature_name} feature to your membership...\n" +
                  "-----------------------------------------------------\n ")
        else:
            raise ValueError(f"Feature {feature_name} is not available for {self.name} membership.")

    def calculate_cost(self):
        """Calculates the total cost of the membership including selected features."""
        total_cost = self.base_cost
        for feature in self.selected_features:
            total_cost += self.additional_features[feature]
        return total_cost

class Gym:
    """Manages multiple gym memberships and applies discounts."""

    def __init__(self):
        self.memberships = {}
        self.group_discount = 0.10
        self.special_discounts = [
            (400, 50),
            (200, 20)
        ]
        self.premium_surcharge = 0.15

    def add_membership(self, membership):
        """Adds a membership plan to the gym."""
        self.memberships[membership.name] = membership

    def select_membership(self, membership_name):
        """Select a membership plan by name."""
        if membership_name in self.memberships:
            return self.memberships[membership_name]
        else:
            raise ValueError(f"Membership {membership_name} not found.")

    def calculate_total_cost(self, membership, num_members=1, apply_premium=False):
        """Calculates the total cost of a membership including any discounts and surcharges."""
        total_cost = membership.calculate_cost() * num_members
        if num_members > 1:
            total_cost -= total_cost * self.group_discount

        for threshold, discount in self.special_discounts:
            if total_cost > threshold:
                total_cost -= discount

        if apply_premium:
            total_cost += total_cost * self.premium_surcharge

        return total_cost

# Final newline
