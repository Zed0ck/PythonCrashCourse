cars = ['tesla', 'bmw', 'volvo']
message_one = f"I would like to own a {cars[0].title()}."
message_two = f"I have dreamed about {cars[1].title()}."
message_three = f"I have owned a {cars[2].title()}."
print(message_one)
print(message_two)
print(message_three)


# Muutama extra harjoitus, listalle lisäämiseen ja poistamiseen
cars.append('ford')
print(cars)

cars.insert(1, 'toyota')
print(cars)

del cars[1]
print(cars)

popped_car = cars.pop()
print(cars)
print(popped_car)

first_car = cars.pop(0)
print(f"The first car in the list was a {first_car.title()}.")

cars.remove('bmw')
print(cars)

cars.append('bmw')
cars.append('tesla')
print(cars)

too_expensive = 'tesla'
cars.remove(too_expensive)
print(cars)
print(f"\nA {too_expensive.title()} is too expensive for me.")
