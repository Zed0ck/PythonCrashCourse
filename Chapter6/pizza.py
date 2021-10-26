pizza = {
    'crust': 'paksu',
    'toppings': ['herkkusieni', 'ekstra juusto'],
}

print(f"Tilasit {pizza['crust']}-crust pizzan"
    "\nseuraavilla täytteillä:")

for topping in pizza['toppings']:
    print(f"\t{topping}")