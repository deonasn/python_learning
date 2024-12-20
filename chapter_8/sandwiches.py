# Deon Anoth
# 06-24-2024
# Python Crash Course: Try it yourself: 8-12

# defining a function 'sandwich_order' using an arbitrary argument to store as many items as possible
def sandwich_order(*ingrediants):
    print('\nYour sandwich order contains:')
    # for loop to print the items
    for ingrediant in ingrediants:
        print(f"\t- {ingrediant.title()}")

# calling function , each with different number of arguments
sandwich_order('chicken','olives','bell pepper','buffalo sauce')
sandwich_order('beef','banana pepper','teriyaki sauce')
sandwich_order('turkey','olives','jalapenoes','banana pepper','buffalo sauce')