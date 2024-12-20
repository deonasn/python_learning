# Deon Anoth
# 06-01-2024
# Python Crash Course: Try it yourself: 4-11

pizzas = ['mushroom pizza', 'cheese pizza', 'olive pizza']          # list of my favorite pizzas
friend_pizzas = pizzas[:]                           # made friend_pizzas a copy of pizzas

pizzas.append("buffalo pizza")                  # appended a new item in the list pizzas
friend_pizzas.append("jalapenos pizza")         # appended a new item in the list friend_pizzas

print(pizzas)                   # prints the list pizzas
print(friend_pizzas)            # prints the list friends_pizzas

print("My favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are: ")
for friend_pizza in friend_pizzas:
    print(friend_pizza)