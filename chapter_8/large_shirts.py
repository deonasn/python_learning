# Deon Anoth
# 06-18-2024
# Python Crash Course: Try it yourself: 8-4

# defining function 'make_shirt' to take size and message as its parameters, and print a sentence
def make_shirt(size='L', message='I love Python'):
    print(f"The size of the shirt is {size}.\n"
          f"The message to be printed is '{message}'\n")

# calling function make_shirt with specific arguments
make_shirt('L')
make_shirt('M')
make_shirt('XL', 'Welcome to Pandemonium!')