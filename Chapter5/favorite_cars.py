favorite_cars = ['mercedes benz', 'tesla', 'bmw']
guess = 'audi'
print(f"Is {guess.title()} in favorite cars list?")
if guess in favorite_cars:
    print(f"{guess.title()} is in favorite cars list")
else:
    print(f"{guess.title()} is not in favorite cars list")

guess = 'tesla'
print(f"\nIs {guess.title()} in favorite cars list?")
if guess in favorite_cars:
    print(f"{guess.title()} is in favorite cars list")
else:
    print(f"{guess.title()} is not in favorite cars list")