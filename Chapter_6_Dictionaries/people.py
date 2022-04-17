person_1 = {'first_name':'fernando',
 			'last_name':'nunez',
 			'age':19,
 			'city':'pozoyork'
 			}
person_2 = {'first_name':'cesar',
			 'last_name':'nunez',
			 'age':26,
			 'city':'zacatecas'
			 }
person_3 = {'first_name':'vel',
			 'last_name':'drake',
			 'age':254,
			 'city':'demon kingdom'
			 }

people = [person_1, person_2, person_3]

for person in people:
	for key, info in person.items():
		print(f"{key.title()}: {info}")
	print("\n")