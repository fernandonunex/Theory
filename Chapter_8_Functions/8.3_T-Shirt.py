def make_shirt(size="Large", message="I love Python"):
    """This function make a T shirt

    Args:
        size (str): Small, Medium, Large, XL
        message (str): Any message to be write in the shirt
    """
    print(f"Size: {size}")
    print(f"Sentence on the shirt: {message}\n")


def run():
    # Call function using positional arguments
    # make_shirt("M", "Positional Arguments")

    # Call function using positional arguments
    # make_shirt(size="XL", message="I'm super big")

    # Exercise 8.4
    make_shirt("Large")
    make_shirt("Medium")
    make_shirt("XL", "Never stop learning")


if __name__ == "__main__":
    run()
