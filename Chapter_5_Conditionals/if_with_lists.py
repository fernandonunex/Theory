avaible_toppings = ['mushroooms', 'olives','green peppers'
					'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushroooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in avaible_toppings:
		print(f"Adding {requested_topping}.")
	else: 
		print(f"Sorry we don't have {requested_topping}.")
print("\n Finished making your pizza!")

