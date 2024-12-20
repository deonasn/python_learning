# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-9

# list of usernames
usernames = []

# if-else statement to check if the usernames list is empty, and to act on specific conditions
if usernames:
    # for loop to print a unique greeting to admin and generic greetings to others
    for username in usernames:
        if username == 'admin':
            print(f'\nHello {username}, would you like to see a status report?')
        else:
            print(f'Hello {username}, thank you for logging in again!')
else:
    print('\nWe need to find some users!')