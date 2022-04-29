def send_messages(messages: list, sent_messages: list) -> None:
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)

def sandwich_sumarize(*toppings):
    """This funtion acepts an arbitrary number of arguments 
    (toppings) for a sandwinch
    """
    print("Your sandwich has:")
    for topping in toppings:
        print(f"-{topping}")
