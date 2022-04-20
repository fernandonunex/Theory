from urllib import response


def run():
    places = {}
    active = True
    prompt = "If you could visit one place in the world,"
    prompt += "\nwhere would you go? "

    while active == True:
        name = input("What is your name? ")
        response = input(prompt)

        places[name] = response

        repeat = input(
            "Would you like to let another person respond?(yes/no) ")
        if repeat == 'no':
            active = False

    for name, place in places.items():
        print(f"{name} would like to go {place}.")


if __name__ == "__main__":
    run()
