# Deon Anoth
# 06-18-2024
# Python Crash Course: Try it yourself: 8-5

# defining function 'describe_city' to take city and country as its parameters, and print a sentence
def describe_city(city='mecca', country='saudi arabia'):
    print(f"{city.title()} is in {country.title()}.")

# calling function describe_city with specific arguments
describe_city('medina', 'saudi arabia')
describe_city('kochi','india')
describe_city('kyoto','japan')
describe_city('beijing','china')
describe_city()

#print(describe_city())