prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when you are ready to stop. "

age = ""

while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Ticket is free")
        elif age <= 12:
            print("Ticket is $10")
        else:
            print("Ticket is $15")