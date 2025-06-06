# Deon Anoth
# 06-03-2024
# Python Crash Course: Try it yourself: 5-2

car = 'toyota'
print(f"Is car == 'toyota'? I predict True")
print(car == 'toyota')
print(f"Is car != 'hyundai'? I predict False")
print(car == 'hyundai')

motorcycle = 'ducati'
print(f"\nIs motorcycle == 'ducati'? I predict True")
print(motorcycle == 'ducati')
print(f"Is motorcycle == 'bmw'? I predict False")
print(motorcycle == 'bmw')

pizza = 'cheese pizza'
print(f"\nIs pizza == 'cheese pizza'? I predict True")
print(pizza == 'cheese pizza')
print(f"Is pizza == 'buffalo pizza'? I predict False")
print(pizza == 'buffalo pizza')

age = 28
print(f"\nIs age == '{age}'? I predict True")
print(age == 28)
print(f"Is age == '19'? I predict False")
print(age == 19)

age_1 = 28
age_2 = 19
print('\n',age_1 >= 19 and age_2 <= 19)
print('\n',age_1 <= 19 or age_2 >= 28)

requested_toppings = 'mushrooms'
if requested_toppings == 'mushrooms':
    print('\nTopping you chose: Mushrooms')
if requested_toppings != 'anchovies':
    print('Hold the Anchovies!\n')

name = 'Deon'
print(name == 'deon')
print(name.lower() == 'deon')

foods = ['ramen', 'sushi', 'rice curry', 'omelet', 'bullseye egg']
if 'ramen' in foods:
    print('\nramen is available!')
if 'tikka masala' not in foods:
    print('tikka masala is not available!')
