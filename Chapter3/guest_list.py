guests = ['Jessica Alba', 'Sanna Marin', 'Kate Beckinsale']
print(f"Hi, {guests[0]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[1]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[2]} I would like to invite you to dinner with me.")
print(str(len(guests)))

# Changing guest list
print(f"\n{guests[1]} couldn't join.")
guests.remove('Sanna Marin')
guests.append('Natalie Portman')
print(f"Hi {guests[2]} would you like to join our dinner party?")
print(str(len(guests)))

# Adding some more guests
print("\nI found a bigger table so I add some more guests.")
guests.insert(0, 'Kiera Knightly')
guests.insert(2, 'Natalie Dormer')
guests.append('Zara Larsson')
print(str(len(guests)))

print(f"Hi, {guests[0]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[1]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[2]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[3]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[4]} I would like to invite you to dinner with me.")
print(f"Hi, {guests[5]} I would like to invite you to dinner with me.")

# Shrinking guest list
print("\nSorry I have to change my plans and I can't host party for all of you. Dinner party is cancelled at this point.")
first = guests.pop()
print(f"Sorry {first} I can't invite you to the party.")
second = guests.pop()
print(f"Sorry {second} I can't invite you to the party.")
third = guests.pop(1)
print(f"Sorry {third} I can't invite you to the party.")
fourth = guests.pop(1)
print(f"Sorry {fourth} I can't invite you to the party.")
print(f"\nHi {guests[0]} and {guests[1]} you are still invited to our dinner party.")
print(guests)
print(str(len(guests)))
guests.remove('Kiera Knightly')
last = 'Kate Beckinsale'
guests.remove(last)
print(guests)