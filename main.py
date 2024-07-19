class GymMembership:
    def __init__(self):
        self.membership_plans = {
            "Basic": 100,
            "Premium": 150,
            "Family": 200
        }
        self.additional_features = {
            "Personal Training": 50,
            "Group Classes": 30
        }
        self.premium_features = 0.15
        self.selected_plan = None
        self.selected_features = []
        self.group_members = 1
        self.base_cost = 0
        self.additional_cost = 0
        self.total_cost = 0

    def display_membership_plans(self):
        print("Available Membership Plans:")
        for plan, cost in self.membership_plans.items():
            print(f"{plan}: ${cost}")
    
    def select_membership_plan(self):
        self.display_membership_plans()
        plan = input("Select a membership plan: ")
        if plan in self.membership_plans:
            self.selected_plan = plan
            self.base_cost = self.membership_plans[plan]
        else:
            print("Invalid membership plan selected.")
            self.select_membership_plan()
    
    def display_additional_features(self):
        print("Available Additional Features:")
        for feature, cost in self.additional_features.items():
            print(f"{feature}: ${cost}")

    def select_additional_features(self):
        self.display_additional_features()
        features = input("Select additional features (comma separated): ").split(',')
        for feature in features:
            feature = feature.strip()
            if feature in self.additional_features:
                self.selected_features.append(feature)
                self.additional_cost += self.additional_features[feature]
            else:
                print(f"Invalid feature selected: {feature}")
    
    def calculate_total_cost(self):
        self.total_cost = self.base_cost + self.additional_cost
        if self.group_members > 1:
            self.total_cost -= self.total_cost*0.1
        if self.total_cost > 200:
            self.total_cost -= 20
        if self.total_cost > 400:
            self.total_cost -= 50
        if "Premium" in self.selected_plan:
            self.total_cost += self.total_cost * self.premium_features
    
    def confirm_membership(self):
        print(f"Selected Plan: {self.selected_plan}")
        print(f"Selected Features: {', '.join(self.selected_features)}")
        print(f"Total Cost: ${self.total_cost}")
        confirm = input("Confirm membership? (yes/no): ").lower()
        if confirm == 'yes':
            return self.total_cost
        else:
            return -1

    def handle_group_memberships(self):
        members = input("Number of members signing up together: ")
        try:
            self.group_members = int(members)
        except ValueError:
            print("Invalid number of members. Please enter a valid number.")
            self.handle_group_memberships()
    
    def run(self):
        self.select_membership_plan()
        self.select_additional_features()
        self.handle_group_memberships()
        self.calculate_total_cost()
        return self.confirm_membership()


if __name__ == "__main__":
    gym_membership = GymMembership()
    total_cost = gym_membership.run()
    if total_cost != -1:
        print(f"Membership confirmed. Total cost: ${total_cost}")
    else:
        print("Membership not confirmed or invalid input.")