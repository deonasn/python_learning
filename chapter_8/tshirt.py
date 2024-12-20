# Deon Anoth
# 06-18-2024
# Python Crash Course: Try it yourself: 8-3

# defining function 'make_shirt' to take size and message as its parameters, and print a sentence
def make_shirt(size, message):
    print(f"The size of the shirt is {size}.\n"
          f"The message to be printed is {message}.\n")

# calling functino make_shirt with specific arguments
make_shirt('XL', "Hello World!")
make_shirt(message='Hey World!', size='L')