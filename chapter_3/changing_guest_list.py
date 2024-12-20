# Deon Anoth
# 05-23-2024
# Python Crash Course: Try it yourself: 3-5

guest_list = ['Shahana', 'Rahath', 'Zyer', 'Bashir', 'Basheer']             # guest list

for i in guest_list:                        # for-loop to output invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)

print('\n')
print("Basheer can't make it tonight")
print('\n')

guest_list[4] = 'Sanjana'                   # modified list by replacing Basheer with Sanjana
for i in guest_list:                        # for-loop to output the second set of invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)