favorite_languages = {'fernando':'python', 
					'velverosa':'c', 
					'malori': 'c', 
					'john wick':'ruby', 
					'cerik': 'java',
					}
polling_friends = ['velverosa','padilla','cerik','chisco','devil','christ','fernando']

for friend in polling_friends:
	if friend not in favorite_languages.keys():
		print(f"Hi {friend.title()}, I am inviting you to take the poll")
	else:
		print(f"Thank {friend.title()} for taking the poll")