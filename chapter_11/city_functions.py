# Deon Anoth
# 06-01-2025
# Python Crash Course: Try it yourself: 11-1 -> 11-2

def get_formatted_city_country(city, country, population=None):
    """Generate a neatly formatted city and country."""
    if population:
        city_information = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_information = f"{city.title()}, {country.title()}"
    return city_information