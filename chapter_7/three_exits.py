# Deon Anoth
# 06-15-2024
# Python Crash Course: Try it yourself: 7-6

# Welcome Message
print("Welcome to the Special Movie Theater!\n"
      "Enter 'quit' to quit the program.\n")
# prompt message for the user
prompt = "Please enter your age: "
# flag for the while loop - initialized as true
active = True

# while loop asking for the user age and to print the cost in regard to it
while active:
    # input and prompt for the user
    age = input(prompt)

    # if block to run only if input is a number
    if age.isnumeric():
        age = int(age)
        if age < 3:
            print('\t- The ticket is free!')
        elif age <= 12:
            print('\t- The ticket is $10.')
        elif age > 12:
            print('\t- The ticket is $15.')

    # if block to break from the loop incase the input is 'quit'
    if age == 'quit':
        print("\nThank you for your time!")
        break