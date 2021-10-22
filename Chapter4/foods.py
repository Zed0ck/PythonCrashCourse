my_foods = ['pizza', 'burgeri', 'pasta']
friend_foods = my_foods[:]

my_foods.append('jätski')
my_foods.append('pihvi')
friend_foods.append('karkki')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\nFirst three items in my foods list are:")
print(my_foods[:3])

print("\nThree items in the middle of the my foods list are:")
print(my_foods[1:4])

print("\nLast three items in my foods list are:")
print(my_foods[2:])