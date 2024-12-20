# Deon Anoth
# 06-01-2024
# Python Crash Course: Try it yourself: 4-8

cubes = []                  # empty list
for value in range(1,11):       # for loop to append cube values of numbers ranging from 1 to 10, while printing them
    cubes.append(value**3)
    print(cubes[value-1])