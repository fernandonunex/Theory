favorite_numbers = {'fernando':[6, 11], 
					'velverosa':[14, 15], 
					'malori': [5, 7], 
					'john wick':[1, 0], 
					'cerik': [4, 100],
					}

for name, numbers in favorite_numbers.items():
	print(f"\nThe {name.title()}'s favorite numbers are:")

	for number in numbers:
		print(f"\t{number}")
	