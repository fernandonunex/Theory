favorite_languages = {'fernando':'python', 
					'velverosa':'c', 
					'malori': 'c', 
					'john wick':'ruby', 
					'cerik': 'java',
					}
friends = ['velverosa','cerik']


for name in favorite_languages.keys():
	print(f"Hi {name.title()}!")

	if name in friends:
		language = favorite_languages[name]
		print(f"{name.title()}, I see you realy like {language.upper()}")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

print("*"*50)

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}")

print("*"*50)
print("Languages mentioned:")
for language in favorite_languages.values():
	print(f"{language.title()}")

print("*"*50)
print("Languages without repetition:")
for language in set(favorite_languages.values()):
	print(f"{language.title()}")


