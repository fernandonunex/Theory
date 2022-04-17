current_users = ['admin','fernando','tom','sombra','pepe tovar']

new_users = ['juan','james','TOM','abraham','pePe tovaR']

for user in new_users:
	if user.lower() in current_users:
		print(f"The user {user} is already taken. Pleas try another")
	else:
		print(f"The user {user} is available")