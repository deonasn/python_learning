# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-7

favorite_fruits = ['apple', 'mango', 'banana']          # list of favorite fruits

if 'apple' in favorite_fruits:                          # independant if statements for output
    print('You really like apple!')
if 'orange' in favorite_fruits:
    print('You really like orange!')
if 'mango' in favorite_fruits:
    print('You really like mango!')
if 'kiwi' in favorite_fruits:
    print('You really like kiwi!')
if 'banana' in favorite_fruits:
    print('You really like banana!')

print('\n')

for favorite_fruit in favorite_fruits:              # for loop with the same purpose as the above block
    if favorite_fruit in favorite_fruits:
        print(f'You really like {favorite_fruit}!')