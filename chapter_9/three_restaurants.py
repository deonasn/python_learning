# Deon Anoth
# 08-03-2024
# Python Crash Course: Try it yourself: 9-2

class Restaurant:
    """A class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type."""
        print("\n")
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """prints the restaurant is open."""
        print(f"{self.restaurant_name} is open")


# creating three instances using Restaurant class and storing it into my_restaurant
restaurant_one = Restaurant('Mr.Currys','Indian')
restaurant_two = Restaurant('88 China','Chinese')
restaurant_three = Restaurant('Oriental Spoon','Korean')

# calling describe_restaurant method from the class for all three instances
restaurant_one.describe_restaurant()
restaurant_two.describe_restaurant()
restaurant_three.describe_restaurant()