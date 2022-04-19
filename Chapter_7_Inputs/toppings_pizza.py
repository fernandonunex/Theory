def run():
    toppings = ""
    prompt = "Enter 'quit' to send the order"
    prompt += "\nHello, what topping would you like? : "

    # Version 1
    while toppings != "quit":
        toppings = input(prompt)
        if toppings != "quit":
            print(f"The topping you have selected is {toppings}")
            print("--"*20)
    print("Thanks, we will prepare your pizza.")

    # Version 2
    active = True
    while active:
        toppings = input(prompt)
        if toppings != "quit":
            print(f"The topping you have selected is {toppings}")
            print("--"*20)
            continue
        break

    # Version 3
    while True:
        toppings = input(prompt)
        if toppings == "quit":
            break
        print(f"The topping you have selected is {toppings}")
        print("--"*20)
    print("Thanks, we will prepare your pizza.")

    print("Thanks, we will prepare your pizza.")


if __name__ == "__main__":
    run()
