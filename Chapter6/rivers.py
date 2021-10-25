rivers = {
    'nile' : 'egypt',
    'thames' : 'england',
    'vantaa' : 'finland'
}

for key, value in rivers.items():
    print(f"The {key.title()} runs through {value.title()}")

print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for country in rivers.values():
    print(country.title())