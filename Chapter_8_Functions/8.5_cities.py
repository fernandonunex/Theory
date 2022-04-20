def describe_city(city, country="Mexico"):
    print(f"{city} is in {country}\n")


def run():
    describe_city("Nuevo Leon")
    describe_city("Bangkok", "Thailand")
    describe_city("Guadalajara")
    describe_city("Sao Paulo", "Brazil")


if __name__ == "__main__":
    run()
