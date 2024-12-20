# Deon Anoth
# 06-13-2024
# Python Crash Course: Try it yourself: 7-2

# input asking for the number of people a dinner group have
no_dinner_people = int(input("How many people do you have? "))

# if-else block to print a specific message if there are more than 8 people in the group and otherwise
if no_dinner_people > 8:
    print("Sorry, you will have to wait for a table. Thank you.")
else:
    print("Hi, your table is ready.")