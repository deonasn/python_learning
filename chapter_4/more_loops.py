# Deon Anoth
# 06-01-2024
# Python Crash Course: Try it yourself: 4-12

my_foods = ['pizza', 'falafel', 'carrot cake']      # list of my favorite foods
friend_foods = my_foods[:]                  # made friend_foods a copy of my_foods

my_foods.append('cannoli')                  # appended a new item in the list my_foods
friend_foods.append('ice cream')            # appended a new item in the list friends_foods

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)