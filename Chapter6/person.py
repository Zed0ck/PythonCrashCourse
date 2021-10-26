person_0 = {'first_name' : 'sanni', 'last_name' : 'vallin', 'age': 5, 'city' : 'tampere'}
print(person_0['age'])
print(person_0['city'])
print(person_0['first_name'])
print(person_0['last_name'])

people = {
    'sanni': {
        'age': 5,
        'city': 'tampere',
    },
    'mika': {
        'age': 35,
        'city': 'tampere',
    },
    'sara': {
        'age': 40,
        'city': 'helsinki',
    }
}

for person, person_info in people.items():
    print(f"\n\tName: {person.title()}")
    age = person_info['age']
    location = person_info['city']

    print(f"\tAge: {age}")
    print(f"\tLocation: {location.title()}")
