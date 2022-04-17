squares = [value**2 for value in range(1,11)]

print("The first three items in the list are:")
for x in squares[:3]:
	print(x)

print("\nThree items in the middle of the list are:")
for x in squares[3:7]:
	print(x)

print("The last three items in the list are:")
for x in squares[-3:]:
	print(x)