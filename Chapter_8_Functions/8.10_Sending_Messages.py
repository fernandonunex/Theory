def send_messages(messages: list, sent_messages: list) -> None:
    while messages:
        message = messages.pop()
        print(f"Sending message: {message}")
        sent_messages.append(message)


def run():
    list_of_messages: list = ["I love u",
                              "You are so beautiful", "I'm proud of u'"]
    sent_messages: list = []
    # Exercise 8.10 Using the original list -> list_of_messages
    send_messages(list_of_messages, sent_messages)
    print(list_of_messages)
    print(sent_messages)

    # Exercise 8.11
    list_of_messages: list = ["I love u",
                              "You are so beautiful", "I'm proud of u'"]
    sent_messages: list = []
    send_messages(list_of_messages[:], sent_messages)
    print(list_of_messages)
    print(sent_messages)


if __name__ == "__main__":
    run()
