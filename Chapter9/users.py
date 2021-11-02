class User:
    """Class for users"""
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role

    def describe_user(self):
        """Describes user"""
        print(f"\n\nFirst name: {self.first_name.title()}\nLast name: {self.last_name.title()}\nRole: {self.role}")
    
    def greet_user(self):
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")

user_one = User('albert', 'einstein', 'scientist')
user_two = User('teemu', 'selanne', 'hockey player')
user_three = User('kimi', 'raikkonen', 'race driver')
user_one.describe_user()
user_one.greet_user()
user_two.describe_user()
user_two.greet_user()
user_three.describe_user()
user_three.greet_user()