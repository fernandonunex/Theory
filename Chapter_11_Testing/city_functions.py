
def fortmated_city(city, country, population=''):
    """A function that return a formatted string like City, Country"""
    if population:
        formatted_city = f"{city.capitalize()}, {country.capitalize()} - population {population}."
    else:
        formatted_city = f"{city.capitalize()}, {country.capitalize()}."
    return formatted_city
