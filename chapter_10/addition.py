# Deon Anoth
# 01-04-2025
# Python Crash Course: Try it yourself: 10-6

try:
    first_number = int(input('\nEnter first number: '))
except ValueError:
    print("Invalid Entry! Please enter an integer.")
else:
    try:
        second_number = int(input('Enter second number: '))
    except ValueError:
        print("Invalid Entry! Please enter a number.")
    else:
        result = first_number + second_number
        print(f'\n->  {first_number} + {second_number} = {result}')