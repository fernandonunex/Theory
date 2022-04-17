#Store information about pizza
pizza = {
		'crust':'thick',
		'toppings':['mushrooms','peperoni','extra cheese'],
		}

#Sumarize the order

print(f"The pizza's crust is {pizza['crust']}" 
	" with the following toppings: ")

for topping in pizza['toppings']:
	print(topping)
	