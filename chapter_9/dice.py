# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-13

import random

class Die:
    """class to represent a die"""
    def __init__(self, sides=6):
        """default method with an attribute 'sides' with a default value of 6"""
        self.sides = sides

    def roll_die(self):
        """method to roll the die and get a random number within the range [0, sides]"""
        die = random.randint(1, self.sides)
        return die



# creating an instance of 6-sided die and outputs the results
six_sided_die = Die()
results = []
# for loop to roll the die 10 times
for roll in range(10):
    six_sided_die_roll = six_sided_die.roll_die()
    results.append(six_sided_die_roll)
print("\nThe Result of rolling 6-sided die for 10 times:")
print(f"\t{results}")


# creating an instance of 10-sided die and outputs the results
ten_sided_die = Die(10)
results = []
# for loop to roll the die 10 times
for roll in range(10):
    ten_sided_die_roll = ten_sided_die.roll_die()
    results.append(ten_sided_die_roll)
print("\nThe Result of rolling 10-sided die for 10 times:")
print(f"\t{results}")


# creating an instance of 20-sided die and outputs the results
twenty_sided_die = Die(20)
results = []
# for loop to roll the die 10 times
for roll in range(10):
    twenty_sided_die_roll = twenty_sided_die.roll_die()
    results.append(twenty_sided_die_roll)
print("\nThe Result of rolling 20-sided die for 10 times:")
print(f"\t{results}")