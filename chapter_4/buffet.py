# Deon Anoth
# 06-01-2024
# Python Crash Course: Try it yourself: 4-13

basic_foods = ('ramen','sushi','rice curry','omelet','bullseye egg')        # list of five basic foods offered in a restaurant
for food in basic_foods:                # for loop to output items in the list
    print(food)

#basic_foods[1] = 'karage'          # made to show the typeError for tuple item assignment

print('\n')
basic_foods = ('ramen','karage','macaroni','omelet','bullseye egg')         # modified list of five basic foods offered in a restaurant
for food in basic_foods:                # for loop to output items in the modified list
    print(food)