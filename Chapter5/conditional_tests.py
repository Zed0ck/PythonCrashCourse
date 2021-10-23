car = 'ford'
print("Is car == 'ford'? I predict True")
print(car == 'ford')

print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

print("\nIs car.upper() == 'ford'? I predict False")
print(car.upper() == 'ford')

number = 2
print("\nIs number 4? I predict not")
print(number == 4)

print("\nIs number 2? I predict yes")
print(number == 2)

print("\nIs number smaller than 5? I predict yes")
print(number < 5)

print("\nIs number larger than 5? I predict no")
print(number > 5)

my_list = ['audi', 'bmw', 'ford']
print('audi' in my_list)
print('tesla' in my_list)

if 'tesla' not in my_list:
    print("Add Tesla to my list")
