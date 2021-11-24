# Addition
print("Give me two numbers and I add them together.")
print("Enter 'q' to quit")

while True:
    number_one = input("\nFirst number: ")
    if number_one == 'q':
        break
    number_two = input("Second number: ")
    if number_two == 'q':
        break
    try:
        answer = number_one + number_two
    except ValueError:
        print("You should give me two numbers.")
    else:
        print(answer)