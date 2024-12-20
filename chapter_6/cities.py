# Deon Anoth
# 06-12-2024
# Python Crash Course: Try it yourself: 6-11

# did - to store information about specific cities and their respecitve country, population, and a fact
cities = {'mecca': {'country': 'saudi arabia','population': '2,427,924', 'fact': 'It is the holiest city in Islam'},
          'medina': {'country': 'saudi arabia', 'population': '1,411,599',
                     'fact': 'It is the second holiest city in Islam'},
          'tokyo': {'country': 'japan', 'population': '14,094,034',
                    'fact': 'It is the capital city of Japan and used to be called Edo during the ancient times'},
          }

# for loop to print information stored in the dictionary above
for city, info in cities.items():
    print(f"Information about {city.title()}: ")
    for key, value in info.items():
        # if block to print the value in title() only if the key is 'country'
        if key == 'country':
            print(f"\t - {key.title()}: \t{value.title()}.")
        # elif block to print only if the key is 'population'
        elif key == 'population':
            print(f"\t - {key.title()}:  {value}.")
        # elif block to print only if the key is 'fact'
        elif key == 'fact':
            print(f"\t - {key.title()}: \t\t{value}.")