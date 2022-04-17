favorite_language = {
					'jen' : ['python','c'],
					'sarah' : ['c'],
					'edward' : ['ruby','go','java'],
					'phil' : ['python','haskell'], 
					}

for person in favorite_language.keys():
	print(f"\n{person.title()} favorite languages are:")
	for language in favorite_language[person]:
		print(language)
		
print("***"*15)

for name, languages in favorite_language.items():
	if len(languages) == 1:
		print(f"\n{name.title()}'s favorite languages is:")
	else:
		print(f"\n{name.title()}'s favorite languages are:")

	for language in languages:
		print(language)