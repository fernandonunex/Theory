def run():
    number = int(
        input("Please enter a number to check if is multiple of 10: "))
    if number % 10 == 0:
        print(f"The number {number} is multiple of 10")
    else:
        print(f"The number {number} is not multiple of 10")


if __name__ == "__main__":
    run()
