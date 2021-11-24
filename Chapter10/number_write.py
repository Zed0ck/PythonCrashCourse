# number writer
import json

numbers = [2, 3, 5, 7, 11, 13, 15, 17]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
