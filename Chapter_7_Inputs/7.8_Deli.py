def run():
    ordered_sandwiches = ['Avocado', 'pastrami',
                          'Pepperoni', 'pastrami', 'Salad', 'Beef', 'pastrami']
    finished_sandwiches = []

    print("The Deli Store has run out of 'pastrami'")

    while 'pastrami' in ordered_sandwiches:
        ordered_sandwiches.remove('pastrami')

    while ordered_sandwiches:
        made_sandwich = ordered_sandwiches.pop()
        print(f"I made your {made_sandwich} sandwich.")

        finished_sandwiches.append(made_sandwich)

    print("Sandwiches made:")
    for sandwich in finished_sandwiches:
        print(sandwich)


if __name__ == "__main__":
    run()
