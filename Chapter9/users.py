# User
class User:
    """Class for users"""
    def __init__(self, first_name, last_name, role):
        self.first_name = first_name
        self.last_name = last_name
        self.role = role
        self.login_attempts = 0

    def describe_user(self):
        """Describes user"""
        print(f"\n\nFirst name: {self.first_name.title()}\nLast name: {self.last_name.title()}\nRole: {self.role}")
    
    def greet_user(self):
        """Print greetings."""
        print(f"\nHello {self.first_name.title()} {self.last_name.title()}!")
    
    def increment_login_attempts(self):
        """Add one to login attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0."""
        self.login_attempts = 0

user_one = User('albert', 'einstein', 'scientist')
user_two = User('teemu', 'selanne', 'hockey player')
user_three = User('kimi', 'raikkonen', 'race driver')
user_one.describe_user()
user_one.greet_user()
user_two.describe_user()
user_two.greet_user()
user_three.describe_user()
user_three.greet_user()

print(user_one.login_attempts)
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.increment_login_attempts()
print(user_one.login_attempts)
user_one.reset_login_attempts()
print(user_one.login_attempts)