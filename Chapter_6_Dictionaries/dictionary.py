users = {	
		'aeinstein':{
			'first':'albert',
			'last':'einstein',
			'location':'princenton',		
			},
		'mcurie':{
			'first':'marie',
			'last':'curie',
			'location':'paris',
			},

		}

for username, user_ifo in users.items():
	print(f"Username: {username}")
	full_name = f"{user_ifo['first']} {user_ifo['last']}"
	location = user_ifo['location']

	print(f"\tFull name: {full_name.title()}")
	print(f"\tLocation: {location.title()}")

