# Deon Anoth
# 06-21-2024
# Python Crash Course: Try it yourself: 8-10

# defining function 'send_messages' to pop from the 'short_messages' list and append them to 'sent_messages' list
def send_messages(messages):
    while messages:
        message = messages.pop()
        print(f'Sending message: "{message}"')
        sent_messages.append(message)

# defining function 'show_messages' to store messages, and prints them
def show_messages(messages):
    for message in messages:
        print(message)

# list of short messages and sent messages
short_messages = ['Hello there!', 'Welcome to Ooty!', "Haven't seen you around here!"]
sent_messages = []

# calling 'show_messages' function with short_messages as its argument
show_messages(short_messages)
print('\n')
# calling 'send_messages' function
send_messages(short_messages)
print('\n')
# to print the lists to check them
print(f"Messages: {short_messages}")
print(f"Sent: {sent_messages}")