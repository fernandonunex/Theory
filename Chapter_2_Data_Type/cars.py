cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)


print("This is the original list")
print(cars)
print("This is the sorted list")
print(sorted(cars))
print("This is the original list again")
print(cars)

cars.reverse()
print(cars)