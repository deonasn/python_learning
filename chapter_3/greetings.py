# Deon Anoth
# 05-22-2024
# Python Crash Course: Try it yourself: 3-2

names = ['Deon','Zyer','Shahana','Basheer','Rahath','Bashir']       # names of people close to me
message = 'Hello, how are you?'                                     # message
print(message, names[0])                                            # message for a specific person - first to last
print(message, names[1])
print(message, names[2])
print(message, names[3])
print(message, names[4])
print(message, names[5])
print('\n')

for n in names:                 # for loop to print the message above
    print(message, n)