aliens = []

for alien_number in range(30):

	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)

for alien in aliens[:5]:
	print(alien) 

print(f"The total float of aliens are: {len(aliens)}")

for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'red'
		alien['points'] = 20
		alien['speed'] = 'medium'

for alien in aliens[:5]:
	print(alien)

