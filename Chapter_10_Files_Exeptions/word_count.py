def count_word(filname):
    """Count the approximate number of words in a file."""
    try:
        with open(filname, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filname} does not exist")

    else:
        words = contents.split()
        count_words = len(words)
        print(f"The file {filname} has about {count_words} words")


filnames = ['txt_files/alice.txt', 'txt_files/siddhartha.txt',
            'txt_files/moby_dick.txt', 'txt_files/little_women.txt']

for filname in filnames:
    count_word(filname)
