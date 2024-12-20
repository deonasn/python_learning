# Deon Anoth
# 05-23-2024
# Python Crash Course: Try it yourself: 3-7

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
for i in guest_list:                            # for-loop to output the third set of invitation message for everyone
    message = f'Hi {i}, I am inviting you to dinner tonight!'
    print(message)

print('\n')
print('Hi guests, I apologize to let you know that the dinner table I have order will not arrive on time. As well as I only have seats for two guests.')
print('\n')

for l in range(3,len(guest_list)+1):        # for-loop to pop and save guests ranging from index-2 to the last
    if guest_list:
        pop_guest = guest_list.pop()
        message = f'Hi {pop_guest}, I am inviting you to dinner tonight!'
        print(message)

print('\n')
for i in guest_list:                        # for-loop to output the third set of invitation message for everyone
    message = f'Hi {i}, you are still invited to dinner tonight!'
    print(message)

for x in range(len(guest_list)):            # for-loop to delete the remaining guests
    del guest_list[0]

print('\n')
print(guest_list)                           # output to check if the list is empty