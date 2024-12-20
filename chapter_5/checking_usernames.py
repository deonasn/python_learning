# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-10

# list of current users and new users, as well as a lowercase version of the current users
current_users = ['admin','danoth','zanoth','shahana','bash','Bashir','rahath']
new_users = ['bashir','rahath','shafique','neenu','ayra','ayza']
lowercase_current_users = [user.lower() for user in current_users]

# if-else to check if new_users list is empty
if new_users:
    # for loop to print whether a username already exists or not between the current users and new users
    for user in new_users:
        if user.lower() in lowercase_current_users:
            print(f'{user} already exists, enter a new username.')
        else:
            print(f'{user} is available.')
else:
    print('There are no new users!')