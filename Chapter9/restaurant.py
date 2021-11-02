class Restaurant:
    """Class for restaurants"""
    def __init__(self, restaurant_name, restaurant_type):
        self.restaurant_name = restaurant_name
        self.restaurant_type = restaurant_type


my_restaurant = Restaurant('mc donalds', 'fast food')
your_restaurant = Restaurant('dennis', 'pizza')
moms_restaurant = Restaurant('plevna', 'fine dinning')
print(f"{my_restaurant.restaurant_name.title()} is a {my_restaurant.restaurant_type} restaurant.")
print(f"{your_restaurant.restaurant_name.title()} is a {your_restaurant.restaurant_type} restaurant.")
print(f"{moms_restaurant.restaurant_name.title()} is a {moms_restaurant.restaurant_type} restaurant.")
