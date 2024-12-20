# Deon Anoth
# 08-15-2024
# Python Crash Course: Try it yourself: 9-10.1

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
        """sets the number of customers served."""
        self.number_served = number_served

    def increment_number_served(self, number_served):
        """increments the number of customers served."""
        self.number_served += number_served