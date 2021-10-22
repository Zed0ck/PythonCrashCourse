cubes = []
for value in range(1, 11):
    cube = value**3
    cubes.append(cube)
    print(cube)

cubes_two = [value**3 for value in range(1,11)]
print(cubes_two)