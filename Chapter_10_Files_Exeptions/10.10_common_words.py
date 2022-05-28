file_path = "txt_files/frankenstein.txt"

try:
    with open(file_path, encoding='utf-8') as f:
        content = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {file_path} does not exist")

else:
    print(
        f"The word 'the' appears {content.lower().count('the ')} times in the file {file_path}")
