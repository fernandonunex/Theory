motorcycles = ['Honda', 'Yamaha', 'Suzuki'] 
print(motorcycles)

#USING append method
motorcycles.append('Ducati')
print(motorcycles)

#USING insert method
motorcycles.insert(1, 'Mortalika')
print(motorcycles)


#USING del statment
del motorcycles[3]
print(motorcycles)

#USING pop method
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#USING pop method with index
first_owned = motorcycles.pop(1)
print(f"The first motorcycle I owned was a {first_owned}")
print(motorcycles)



#USING remove() by value
too_awful = 'Honda'
motorcycles.remove(too_awful)
print(motorcycles)
print(f" \nThe {too_awful.title()} is too awful for me.")

