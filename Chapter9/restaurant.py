# Resaurant
"""Classes that can be used as representing restaurants."""

class Restaurant:
    """Class for restaurants"""
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type
        self.number_served = 0

    def read_number_served(self):
        """Print number_served."""
        print(f"\n{self.number_served} numbers served!")

    def set_number_served(self, number):
        """Set given number as number served."""
        self.number_served = number
    
    def increment_number_served(self, increment_number):
        """Add given increment to served number."""
        self.number_served += increment_number

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ['chocolate', 'vanilla', 'banana']
    
    def get_flavors(self):
        print("We have flavors:") 
        for flavor in self.flavors:
            print(f"\t{flavor.title()}")