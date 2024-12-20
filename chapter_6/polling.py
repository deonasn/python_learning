# Deon Anoth
# 06-08-2024
# Python Crash Course: Try it yourself: 6-6

# dictionary containing favorite languages of some coders
favorite_languages = {'jen': 'c++',
                      'sarah': 'c',
                      'edward': 'ruby',
                      'miller': 'java',
                      'deon': 'python'}

# for loop to print out who participated the poll and their favorite languages
for name in favorite_languages.keys():
    print(f"{name.title()}'s favorite language is {favorite_languages[name].title()}")

print('\n')

# list of coders including those who participated in the poll and of those who did not
coders = ['deon','zyer','jen','sarah','shahana','rahath']
# for loop to print messages to those who participated in the poll and of those who did not
for coder in coders:
    # if statement to print message for those who did not participate in the poll
    if coder not in favorite_languages.keys():
        print(f'{coder.title()}, please take our poll. Thank you.')
    # elif statement to print message for those who participated in the poll
    elif coder in favorite_languages.keys():
        print(f'{coder.title()}, Thank you very much for participating in our poll.')