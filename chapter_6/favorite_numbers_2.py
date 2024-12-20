# Deon Anoth
# 06-12-2024
# Python Crash Course: Try it yourself: 6-10

# lid - dictionary consisting of person's name and list of their favorite numbers
favorite_numbers = {'zyer': [3, 2, 5], 'deon': [1, 5, 9], 'shahana': [9, 3, 4], 'basheer': [8, 4, 2],
                    'rahath': [4, 3, 7], 'bashir': [2, 5, 7],
                    }

# for loop to print information stored in the dictionary above
for name, numbers in favorite_numbers.items():
    print(f"{name.title()}'s favorite numbers are: ")
    for number in numbers:
        print(f' - {number}')
