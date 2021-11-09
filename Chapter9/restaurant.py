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

my_restaurant = Restaurant('mc donalds', 'fast food')
your_restaurant = Restaurant('dennis', 'pizza')
moms_restaurant = Restaurant('plevna', 'fine dinning')
print(f"{my_restaurant.restaurant_name.title()} is a {my_restaurant.restaurant_type} restaurant.")
print(f"{your_restaurant.restaurant_name.title()} is a {your_restaurant.restaurant_type} restaurant.")
print(f"{moms_restaurant.restaurant_name.title()} is a {moms_restaurant.restaurant_type} restaurant.")

my_restaurant.read_number_served()
my_restaurant.set_number_served(6)
my_restaurant.read_number_served()
my_restaurant.increment_number_served(1)
my_restaurant.read_number_served()
ice_cream_restaurant = IceCreamStand('valio', 'dessert bar')
print(ice_cream_restaurant.restaurant_name.title())
ice_cream_restaurant.get_flavors()

