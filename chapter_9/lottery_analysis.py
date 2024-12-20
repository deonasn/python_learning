# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-15

from random import choice

# stores 10 numbers and 5 alphabets to be chosen for the lottery series
choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
# a list to store the winning series
result = []

# using choice() to create a random series, append them to a list, and outputting the result
print("\t\t\t\tLottery!!! \nThe Winning Series for this Week's Lottery is: ")
# for loop to get 4 alphabets/digits to create the series
for i in range(4):
    series = choice(choices)
    result.append(series)
print(f"\t\t\t{result}")

# flag for continuous lottery attempts - True means picking lottery continues since we haven't won it
lottery_status = True
# initiating variable to store the number of attempts
lottery_attempts = 0

print("\n\nYour Lottery Picks:")
# while loop to run until we win the lottery
while lottery_status:
    # a list to store my lottery pulls
    my_ticket = []
    for i in range(4):
        my_pull = choice(choices)
        my_ticket.append(my_pull)
    print(f"\t\t\t{my_ticket}")
    # increments attempts by 1 every time it loops
    lottery_attempts += 1

    # if-statement to show the result and to set the flag to false since we have won the ticket and doesn't need to continue
    if my_ticket == result:
        print("----------------------------------------")
        print("- You have finally Won the Ticket!!!!!!!")
        print("----------------------------------------")
        lottery_status = False

# output the number of attempts
print(f"\n-> It took {lottery_attempts} attempts to win!")