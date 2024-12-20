# Deon Anoth
# 08-09-2024
# Python Crash Course: Try it yourself: 9-4

class Restaurant:
    """A class to represent a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0              # additional attribute with default value of 0

    def describe_restaurant(self):
        """prints the restaurant name, cuisine type, and customers served."""
        print(f"\nThe restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")
        print(f"The number of customers served is {self.number_served}")

    def open_restaurant(self):
        """prints the restaurant is open."""
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


# creating an instance using Restaurant class and storing it into my_restaurant
restaurant = Restaurant('Mr.Currys','Indian')

# calling method from the class - default value
restaurant.describe_restaurant()

# creating instance to change the number served and calling method to describe the restaurant
restaurant.number_served = 32
restaurant.describe_restaurant()

# calling method to change the number served and to describe the restaurant
restaurant.set_number_served(33)
restaurant.describe_restaurant()

# calling method to increment the number served and to describe the restaurant
restaurant.increment_number_served(5)
restaurant.describe_restaurant()