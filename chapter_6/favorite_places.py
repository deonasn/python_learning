# Deon Anoth
# 06-12-2024
# Python Crash Course: Try it yourself: 6-9

# lid - to store information about specific people and their favorite places
favorite_places = {'deon': ['japan', 'mecca', 'madina'],
                   'zyer': ['korea', 'finland', 'south africa'],
                   'shahanas': ['mecca', 'madina', 'u.s.a.'],
                   }

# for loop to print information stored in the dictionary above
for name, places in favorite_places.items():
    print(f"{name.title()}'s favorite places are: ")
    for place in places:
        print(f' - {place.title()}')