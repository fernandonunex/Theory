import re


def city_country(city, country):
    formated_city = f"{city.capitalize()}, {country.capitalize()}"
    return formated_city



def run():
    print(city_country("Guadalajara", "Mexico"))
    print(city_country("Zacatecas", "Mexico"))
    print(city_country("Tokio", "Japan"))
    


if __name__ == "__main__":
    run()
