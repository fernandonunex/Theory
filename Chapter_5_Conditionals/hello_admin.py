users = ['admin','fernando','tom','sombra','pepe tovar']

if users:
	for user in users:
		if user == 'admin':
			print(f"Hello {user} would you like to see a status report?")
		else:
			print(f"Hello {user.title()}, thank you for logging in again!")
else:
	print("The list of users is empty")