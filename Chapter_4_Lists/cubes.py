cubes = []

for x in range(11):
	cubes.append(x**3)

print(cubes)

print("*"*20)

cubes_v2 = [x**3 for x in range(11)]
print(cubes_v2)