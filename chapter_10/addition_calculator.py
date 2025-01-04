# Deon Anoth
# 01-04-2025
# Python Crash Course: Try it yourself: 10-7

print("\nWelcome to Addition Calculator!")
print("Enter 'q' anytime to quit.")
while True:
    first_number = input('\nEnter first number: ')
    if first_number == 'q':
        print('\nThank you for using the Addition Calculator!.')
        break
    second_number = input('Enter second number: ')
    if second_number == 'q':
        print('\nThank you for using the Addition Calculator!.')
        break
    try:
        first_number = int(first_number)
        second_number = int(second_number)
    except ValueError:
        print("Invalid Entry! Please enter an integer.")
    else:
        result = int(first_number + second_number)
        print(f'\n->  {first_number} + {second_number} = {result}')