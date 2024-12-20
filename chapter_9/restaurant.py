# Deon Anoth
# 08-03-2024
# Python Crash Course: Try it yourself: 9-1

class Restaurant:
    """A class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """prints the restaurant name and cuisine type."""
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        """prints the restaurant is open."""
        print(f"{self.restaurant_name} is open")


# creating an instance using Restaurant class and storing it into my_restaurant
restaurant = Restaurant('Mr.Currys','Indian')

# calling methods from the class
print('\n')
restaurant.describe_restaurant()
restaurant.open_restaurant()