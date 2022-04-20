
def make_shirt(size, message):
    """This function make a T shirt

    Args:
        size (str): Small, M, L, XL
        message (str): Any message to be write in the shirt
    """
    print(f"Size: {size}")
    print(f"Sentence on the shirt: {message}\n")


def run():
    # Call function using positional arguments
    make_shirt("M", "Positional Arguments")
    make_shirt(size="XL", message="I'm super big")


if __name__ == "__main__":
    run()
