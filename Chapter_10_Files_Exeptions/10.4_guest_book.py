file = 'guests_book.txt'

with open(file, 'w') as file_object:
    while True:
        user = input("Enter your name or 'q' to quit:").title()
        if user == 'Q':
            break
        else:
            print(f"Welcome, {user}!")
            file_object.write(f'{user}\n')