# Deon Anoth
# 06-01-2024
# Python Crash Course: Try it yourself: 4-10

odd_numbers = list(range(1, 21, 2))         # list of odd numbers
for odd_number in odd_numbers:              # for loop to print each odd number
    print(odd_number)

print(f"The first three items in the list are: {odd_numbers[:3]}")              # prints the first three items in the list
print(f"Three items from the middle of the list are: {odd_numbers[3:-4]}")      # prints three items from the middle of the list
print(f"The last three items in the list are: {odd_numbers[-3:]}")              # prints the last three items in the list