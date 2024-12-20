# Deon Anoth
# 06-14-2024
# Python Crash Course: Try it yourself: 7-4

# Welcome Message
print("Welcome to Deon's Pizzeria!\n"
      "Choose the toppings you would like to have on you pizza!\n"
      "Enter 'quit' to quit the program.\n")
# list for adding toppings
toppings = []
# flag for the while loop - initialized as true
active = True

number_of_toppings = 1

# while loop for adding toppings
while active:
    # if-elif blocks to choose prompt based on what number of toppings the user is at
    if number_of_toppings == 1:
        prompt = f"Enter your {number_of_toppings}st toppings: "
    elif number_of_toppings == 2:
        prompt = f"Enter your {number_of_toppings}nd toppings: "
    elif number_of_toppings == 3:
        prompt = f"Enter your {number_of_toppings}rd toppings: "
    else:
        prompt = f"Enter your {number_of_toppings}th toppings: "

    # input and prompt for the user
    topping = input(prompt)

    # if block to flag active as false incase the input is 'quit' to exit the program
    if topping == 'quit':
        active = False
    # elif block to continue if the input is not 'quit', appends the topping to the list
    elif topping != 'quit':
        print(f"\tI will add {topping} to your pizza.")
        toppings.append(topping)
        number_of_toppings += 1

    # if block to flag active as false if the number of toppings reach 5
    if number_of_toppings > 5:
        active = False
        print("You can only have 5 toppings!")

# prints the toppings entered by the user at the end, after the user chooses to quit.
print("\nYour pizza toppings are: ")
for topping in toppings:
    print(f"\t\t - {topping}")