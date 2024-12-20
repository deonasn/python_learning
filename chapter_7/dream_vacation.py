# Deon Anoth
# 06-15-2024
# Python Crash Course: Try it yourself: 7-10

# Welcome message
print('Welcome to Dream Vacation Polling!')
# empty dictionary for the polling responses
responses = {}
# flag initially set as true
polling_active = True

# prompt messages for the poll
name_prompt = 'What is your name? '
response_prompt = 'If you could visit one place in the world, where would you go? '
repeat_prompt = 'Would you like to let another person respond? (yes/no) '

# while loop for taking the poll
while polling_active:
    # inputs for name and their response
    name = input(f'\n{name_prompt}')
    response = input(response_prompt)

    # storing the name and their respones to the 'responses' dictionary
    responses[name.lower()] = response.lower()
    # prompt for repeating the poll
    repeat = input(f'{repeat_prompt}')

    # if block to set polling_active flag as false in case the user wants to quit
    if repeat == 'no':
        polling_active = False

# prints results of the poll
print('\n----- Poll Results -----')
for name, response in responses.items():
    print(f'{name.title()} would like to visit {response.title()} as his dream vacation.')