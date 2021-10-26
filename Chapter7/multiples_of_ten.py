number = input("Tell me a number, and I tell you is it multiple of 10. ")
number = int(number)

if number % 10:
    print(f"\nThe number {number} is multiple of 10")
else:
    print(f"\nThe number {number} is not multiple of 10")