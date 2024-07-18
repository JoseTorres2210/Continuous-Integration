class GymMembership:
    def __init__(self, name, base_cost, additional_features=None):
        self.name = name
        self.base_cost = base_cost
        self.additional_features = additional_features if additional_features else {}
        self.selected_features = []

    def add_feature(self, feature_name):
        if feature_name in self.additional_features:
            self.selected_features.append(feature_name)
            print("\n-----------------------------------------------------\n" +
                f"Adding {feature_name} feature to your membership...\n" +
                "-----------------------------------------------------\n ")
        else:
            raise ValueError(f"Feature {feature_name} is not available for {self.name} membership.")

    def calculate_cost(self):
        total_cost = self.base_cost
        for feature in self.selected_features:
            total_cost += self.additional_features[feature]
        return total_cost
    
class Gym:
    def __init__(self):
        self.memberships = {}
        self.group_discount = 0.10
        self.special_discounts = [
            (400, 50),
            (200, 20)      
        ]
        self.premium_surcharge = 0.15
        
        
        
        
   def add_membership(self, membership):
        self.memberships[membership.name] = membership

    def display_memberships(self):
        for membership in self.memberships.values():
            print(f"Membership: {membership.name}, Base Cost: ${membership.base_cost}")
            for feature, cost in membership.additional_features.items():
                print(f"  - Feature: {feature}, Cost: ${cost}")

    def select_membership(self, membership_name):
        if membership_name in self.memberships:
            return self.memberships[membership_name]
        else:
            raise ValueError(f"Membership {membership_name} is not available.")

    def calculate_total_cost(self, membership, num_members=1):
        base_cost = membership.calculate_cost()
        total_cost = base_cost * num_members
       

        if membership.name == "Premium" and len(membership.selected_features) >= 1:
            surcharge = total_cost * 0.15
            total_cost += surcharge
            print(f"15% surcharge applied for being a Premium plan with at least 1 feature: ${surcharge}")

        if num_members >= 2:
            total_cost -= total_cost * self.group_discount
            print(f"Group discount applied: {self.group_discount * 100}%")

        sorted_special_discounts = sorted(self.special_discounts, key=lambda x: x[0], reverse=True)
        for threshold, discount in sorted_special_discounts:
            if total_cost > threshold:
                total_cost -= discount
                print(f"Special discount of ${discount} applied for total cost over ${threshold}")
                break  # Rompe después de aplicar el primer descuento válido

        return total_cost