alien_0 = {'x_coordinates': 0, 'y_coordinates': 25, 'speed': 'medium','color':'green'}

print(f"The original position is {alien_0['x_coordinates']},{alien_0['y_coordinates']}")
#Move the alien to the right

if alien_0['speed'] == 'low':
	increment  = 1
elif alien_0['speed'] == 'medium':
	increment = 2
else:
	increment = 3

alien_0['x_coordinates'] = alien_0['x_coordinates'] + increment

print(f"The new position is {alien_0['x_coordinates']},{alien_0['y_coordinates']}")

print(alien_0)
del alien_0['color']
print(alien_0)
