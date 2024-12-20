# Deon Anoth
# 06-08-2024
# Python Crash Course: Try it yourself: 6-5

# dictionary containing three major rivers and the country each river runs through
rivers = {'nile': 'egypt', 'amazon river': 'peru', 'yangtze river': 'china', }

# for loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

# for loop to print the name of each river in the dictionary
print('\n')
for river in rivers.keys():
    print(river.title())

# for loop to print the name of each country included in the dictionary
print('\n')
for country in rivers.values():
    print(country.title())
