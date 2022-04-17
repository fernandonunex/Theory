pet_1 = {'owner': 'vel',
		 'kind': 'dragon',
		 'pet_name': 'draki',
		 }

pet_2 = {'owner': 'fer',
		 'kind': 'dog',
		 'pet_name': 'sombra',
		 }

pet_3 = {'owner': 'lippman',
		 'kind': 'horse',
		 'pet_name': 'boone',
		 }

pets = [pet_1,pet_2,pet_3]

for pet in pets:
	for key,info in pet.items():
		print(f"{key.title()} ---> {info.title()}")
		
	print("\n\n")