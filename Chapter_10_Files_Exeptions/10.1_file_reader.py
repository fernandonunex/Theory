file = 'learning_python.txt'

# Reading the entire file
with open(file) as file_object:
    content = file_object.read()

print(content.strip().replace('Python', 'C'))
print("--"*20)


# Reading line by line
with open(file) as file_object:
    for line in file_object:
        print(line.strip().replace('Python', 'C'))

print("--"*20)



# Storing in a list
with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))