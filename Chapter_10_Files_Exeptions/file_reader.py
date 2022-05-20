file_path = 'txt_files/pi_digits.txt'

# with open(file_path) as file_object:
#     contents = file_object.read()

#print(contents.rstrip()) 

# with open(file_path) as file_object:
#     #contents = file_object.read()
#     for line in file_object:
#         print(line.rstrip())

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


