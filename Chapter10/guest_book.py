filename = 'guest_book.txt'
name = ''

print("You can stop adding name by giving 'e' to the program.")

while name != 'e':
    name = input("Give your name to the guest book: ")
    
    with open(filename, 'a') as file_object:
        if name != 'e':
            print(f"Hello {name}\n")
            file_object.write(f"{name}\n")