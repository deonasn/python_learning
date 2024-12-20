# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-11

# list of number from 1 to 9
numbers = [x for x in range(1, 10)]

# for loop through the list of numbers to print out proper ordinal ending
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')