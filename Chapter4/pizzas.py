pizzas = ['pepperoni pizza', 'americana pizza', 'quatro formaggi pizza']
for pizza in pizzas:
    print(f"I like {pizza}.")
print("I really love pizza!")

friends_pizzas = pizzas[:]

pizzas.append('blue cheese special')
friends_pizzas.append('chili special')
print("\nMy pizzas:")
print(pizzas)
print("\nFriend's pizzas:")
print(friends_pizzas)