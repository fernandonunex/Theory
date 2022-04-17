alien_0 = {'color':'green','points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points =alien_0['points']
print(f"You have earnead {new_points} points.")

print("**"*50)

alien_0['coordinates_x'] = 0
alien_0['coordinates_y'] = 25

print(alien_0)

print("**"*50)

print(f"The alien color is {alien_0['color']}.")
alien_0['color'] = 'black'
print(f"The alien color is now {alien_0['color']}.")
