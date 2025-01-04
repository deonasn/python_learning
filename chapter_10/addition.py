# Deon Anoth
# 01-04-2025
# Python Crash Course: Try it yourself: 10-6

first_number = input('\nEnter first number: ')
second_number = input('Enter second number: ')
try:
    first_number = int(first_number)
    second_number = int(second_number)
except ValueError:
    print("Invalid Entry! Please enter an integer.")
else:
    result = int(first_number + second_number)
    print(f'\n->  {first_number} + {second_number} = {result}')