#guest list
name = input("Give your name to the list: ")

filename = 'guest.txt'

with open(filename, 'a') as file_object:
    file_object.write(name)