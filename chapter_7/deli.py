# Deon Anoth
# 06-15-2024
# Python Crash Course: Try it yourself: 7-8

# list of sandwiches
sandwich_orders = ['buffalo sandwich', 'rotissary sandwich', 'meatball sandwich', 'cold-cut-combo sandwich']
# empty list to store finished sandwiches
finished_sandwiches = []

# while loop to pop and append sandwiches from sandwich_orders to finished_sandwiches
while sandwich_orders:
    # popping the sandwich order from sandwich_orders and storing it to a variable
    current_order = sandwich_orders.pop()
    print(f'Your {current_order.title()} has been made!')
    # appends the popped sandwich order to the finished_order
    finished_sandwiches.append(current_order)

# for loop to print the finished and ready to go sandwiches
print("\nThe sandwiches ready are: ")
for sandwich_order in finished_sandwiches:
    print(f"\t- {sandwich_order.title()}")