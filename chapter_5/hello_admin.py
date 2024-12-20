# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-8

# list of usernames
usernames = ['admin','danoth','zanoth','shahana','bash','bashir','rahath','shafique','neenu','ayra','ayza']

# for loop to print a unique greeting to admin and generic greetings to others
for username in usernames:
    if username == 'admin':
        print(f'\nHello {username}, would you like to see a status report?')
    else:
        print(f'Hello {username}, thank you for logging in again!')