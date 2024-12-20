# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-10

import restaurant_class_module as rcm

# creating three instances using Restaurant class and storing it into my_restaurant
restaurant_one = rcm.Restaurant('Mr.Currys','Indian')
restaurant_two = rcm.Restaurant('88 China','Chinese')
restaurant_three = rcm.Restaurant('Oriental Spoon','Korean')

# calling describe_restaurant method from the class for all three instances
restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()