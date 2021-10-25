alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# print(alien_0['color'])
# print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

del alien_0['points']
print(alien_0)

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)