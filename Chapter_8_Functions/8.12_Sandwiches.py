def sandwich_sumarize(*toppings):
    """This funtion acepts an arbitrary number of arguments 
    (toppings) for a sandwinch
    """
    print("Your sandwich has:")
    for topping in toppings:
        print(f"-{topping}")


def run():
    sandwich_sumarize("Pepperoni","Cheese")
    sandwich_sumarize("Tomato", "Pineaple", "Mushrooms", "Tuna")
    sandwich_sumarize("Lemon")


if __name__ == "__main__":
    run()
