# Deon Anoth
# 06-03-2024
# Python Crash Course: Try it yourself: 5-4

alien_color = 'yellow'                  # block that fails if test
if alien_color == 'green':
    print('The player just earned 5 points for shooting the alien')
else:
    print('The player just earned 10 points')

alien_color = 'green'                   # block that passes if test
if alien_color == 'green':
    print('\nThe player just earned 5 points for shooting the alien')
else:
    print('The player just earned 10 points')