# Deon Anoth
# 06-12-2024
# Python Crash Course: Try it yourself: 6-8

# did - dictionary of pet information inside another dictionary named pets
pets = {'chiku': {'kind': 'squirrel', 'owner': 'zyer anoth'},
        'shiro': {'kind': 'cat', 'owner': 'deon anoth'},
        'kuro': {'kind': 'dog', 'owner': 'weismann cheondoyoon'}
        }

# for loop to print information about pets stored in the dictionary above
for pet_name, pet_info in pets.items():
        print(f'{pet_name.title()} is a {pet_info['kind'].title()} and is owned by {pet_info['owner'].title()}')