# Deon Anoth
# 05-29-2024
# Python Crash Course: Try it yourself: 3-10

countries = ['united kingdom', 'united states', 'canada', 'japan', 'china', 'united arab emirates', 'saudi arabia', 'yemen', 'south korea', 'scotland', 'norway', 'finland']

print(countries[3])
print(f'I would like to visit {countries[3].title()}')      # using .title()
countries[0] = 'qatar'
print(countries)
countries.append('qatar')           # using append()
print(countries)
country = []                        # initializing list with no value/index
print(country)
country.append('qatar')             # using append() to add object into an empty list
country.append('united arab emirates')
country.append('saudi arabia')
country.append('yemen')
print(country)
country.insert(1, 'south korea')    # using insert() to insert a value to a specific index
print(country)
del country[1]                                  # using del to delete an object
print(country)
country.insert(1, 'south korea')
popped_country = country.pop()                  # using pop() to pop the last object in the list while assigning it to a variable
print(popped_country)
print(country)
popped_country = country.pop(1)                 # using pop() on a specfic index while assigning it a variable
print(popped_country)
print(country)
country.remove('saudi arabia')                  # using remove() to remove an ojbect whose value is known
print(country)
print(countries)
countries.sort()                    # using sort() to sort list in alphabetical order
print(countries)
countries.sort(reverse=True)        # using sort(reverse=True) to sort list in reverse alphabetical order
print(countries)
print(sorted(countries))            # using print(sorted(x)) to sort the list temporarily while printing it
print(countries)
countries.reverse()                 # using reverse() to sort the list in reverse order - not alphabetical order
print(countries)
print(len(countries))               # using len(x) to show the number of objects in the list