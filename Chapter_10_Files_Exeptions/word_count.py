file_name = 'txt_files/alice.txt'

try:
    with open(file_name, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_name} does not exist")

else:
    words = contents.split()
    count_words = len(words)
    print(f"The file {file_name} has about {count_words} words")

