# My cars
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2010)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model x', 2020)
print(my_tesla.get_descriptive_name())