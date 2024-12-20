# Deon Anoth
# 05-23-2024
# Python Crash Course: Try it yourself: 3-4

guest_list = ['Shahana', 'Rahath', 'Zyer', 'Bashir', 'Basheer']             # guest list
message = f'Hi {guest_list[1]}, I am inviting you to dinner tonight!'       # invitation message for only one person
print(message)                                                              # message output
print('\n')

for i in guest_list:                        # for-loop to output invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)