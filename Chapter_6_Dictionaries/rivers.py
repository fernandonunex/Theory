biggest_rivers = {'egypt':'nile river',
				  'amazon':'amazon river',
				  'china':'yangtze river'	
				}

for country, river in biggest_rivers.items():
	print(f"{river.title()} runs through {country.title()}")

print("\nCountrys included")
for country in biggest_rivers.keys():
	print(country.title())

print("\nRivers included")
for river in biggest_rivers.values():
	print(river.title())

