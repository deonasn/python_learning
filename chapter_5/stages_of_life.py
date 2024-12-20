# Deon Anoth
# 06-04-2024
# Python Crash Course: Try it yourself: 5-6

age = 65
stage = ''

if age < 2:
    print('The person is a baby.')
elif age < 4:
    print('The person is a toddler.')
elif age < 13:
    print('The person is a kid.')
elif age < 20:
    print('The person is a teenager.')
elif age < 65:
    print('The person is an adult.')
elif age >= 65:
    print('The person is an elder.')

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
elif age >= 65:
    stage = 'elder'

print(f'The person is {stage}')