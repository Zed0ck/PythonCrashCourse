#with open('pi_digits.txt') as file_object:
#    contents = file_object.read()
#print(contents.rstrip())

with open('text_files/text_file.txt') as file_object_two:
    contents_two = file_object_two.read()
print(contents_two)

filename = 'pi_digits.txt'

#with open(filename) as file_object_three:
#    for line in file_object_three:
#        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))