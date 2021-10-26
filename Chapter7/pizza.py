prompt = "\nPlease tell me what you want in your pizza."
prompt += "\nEnter 'quit' when you tell all your pizza toppings to me. "

topping = ""
all_toppings = []
active = True

while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        all_toppings.append(topping)
        print("Topping added to the list")

print("I added these toppings to your pizza:")
for incredient in all_toppings:
    print(f"\t{incredient}")