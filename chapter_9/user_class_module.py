# Deon Anoth
# 08-18-2024
# Python Crash Course: Try it yourself: 9-12.1

"""Module to store class to manage User information"""
class User:
    """A class for user profile"""
    def __init__(self, first_name, last_name, username, email, password):
        """default method"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

    def describe_user(self):
        """Defining a method to describe user"""
        print(f"\nFirst Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")

    def greet_user(self):
        """Defining a method to greet user"""
        print(f"\nGreetings {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """increments login attempts"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """resets login attempts"""
        self.login_attempts = 0
        print(f"\nLogin attempts have been reset!")