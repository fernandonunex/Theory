favorites_pizzas = ['pepperoni','chorizo','doritos']
friend_pizzas = favorites_pizzas[:]

favorites_pizzas.append('super cheese')
friend_pizzas.append('sarten')

print("My favorite pizzas are: ")
for pizza in favorites_pizzas:
	print(pizza.title())

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza.title())