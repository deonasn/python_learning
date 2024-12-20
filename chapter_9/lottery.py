# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-14

from random import choice

choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E']
result = []

# using choice() to create a random series, append them to a list, and outputting the result
print("\t\t\t\tLottery!!! \nThe Winning Series for this Week's Lottery is: ")
# for loop to get 4 alphabets/digits to create the series
for i in range(4):
    series = choice(choices)
    result.append(series)
print(f"\t\t\t{result}")