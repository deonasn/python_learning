# Deon Anoth
# 06-19-2024
# Python Crash Course: Try it yourself: 8-6

# defining function 'city_country' to take city and country as its parameters, and returns the information
def city_country(city, country):
    city_info = f'"{city.title()}, {country.title()}"'
    return city_info

# calls 'city_country' function while printing it
print(city_country("san francisco", "united states"))
print(city_country('Mecca','saudi arabia'))
print(city_country('kyoto','japan'))