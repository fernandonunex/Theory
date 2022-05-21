file = 'programming_poll.txt'

with open(file, 'a') as file_object:
    while True:
        user = input("Why do you like programming?('q' to quit):").capitalize()
        if user == 'Q':
            break
        else:
            file_object.write(f'{user}\n')