# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-12.2

"""Module to store classes to manage Admin information and privileges."""

from user_class_module import User

class Admin(User):
    """A child class of User, for Admin class"""
    def __init__(self, first_name, last_name, username, email, password):
        super().__init__(first_name, last_name, username, email, password)      # super-class call: necessary for child class
        self.privileges = Privileges()


class Privileges:
    """A class to store privileges"""
    def __init__(self, privileges = ''):
        self.privileges = privileges

    def show_privileges(self):
        """method to display privileges of the Admin class"""
        print("\nThe Admin privileges are:")
        for privilege in self.privileges:
            print(f"\t{privilege.capitalize()}")