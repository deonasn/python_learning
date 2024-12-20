# Deon Anoth
# 05-23-2024
# Python Crash Course: Try it yourself: 3-6

guest_list = ['Shahana', 'Rahath', 'Zyer', 'Bashir', 'Basheer']             # guest list

for i in guest_list:                        # for-loop to output invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)

print('\n')
print("Basheer can't make it tonight")
print('\n')

guest_list[4] = 'Shafique'                  # modified list by replacing Basheer with Sanjana
for i in guest_list:                        # for-loop to output the second set of invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)

print('\n')
print('Hi guests, I found a bigger table.')
print('\n')

guest_list.insert(0, 'Ayra')    # inserting Ayra at the beginning of the list
guest_list.insert(3, 'Ayza')    # inserting Ayza at the middle of the list
guest_list.insert(7, 'Neenu')   # inserting Neenu at the end of the list
for i in guest_list:                        # for-loop to output the third set of invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)