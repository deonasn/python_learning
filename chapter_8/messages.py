# Deon Anoth
# 06-21-2024
# Python Crash Course: Try it yourself: 8-9

# defining function 'show_messages' to store messages, and prints them
def show_messages(messages):
    for message in messages:
        print(message)

# list of short messages
short_messages = ['\n', 'Hello there!', 'Welcome to Ooty!', "Haven't seen you around here!"]

# calling 'show_messages' function with short_messages as its argument
show_messages(short_messages)