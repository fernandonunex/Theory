favorite_places = {'elon': ['califas','mars'],
				   'reeve': ['londres'],
				   'ezekiel':['pensylvania','los angeles','south central']
				  }

for person,places in favorite_places.items():
	print(f"\nThe {person.title()}'s favorite places are")

	for place in places:
		print(f"\t{place.title()}")