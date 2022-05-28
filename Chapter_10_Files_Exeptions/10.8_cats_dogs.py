files_names = ['cat.txt','dog.txt']

for file in files_names:
    try:
        with open(file) as f:
            content = f.readlines()
    except FileNotFoundError:
        print(f"Sorry, the file {file} was not found")
    else:    
        print(f"Names stored in {file}")
        for name in content:
            print(name.strip())
