file_path = 'txt_files/pi_digits.txt'
with open(file_path) as file_object:
    #contents = file_object.read()
    for line in file_object:
        print(line.rstrip())


#print(contents.rstrip()) 