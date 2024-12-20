# Deon Anoth
# 08-15-2024
# Python Crash Course: Try it yourself: 9-8

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


# creating an instance of Admin class while storing privileges in a list and calling method to display said privileges
admin = Admin("Deon", "Anoth", "dafb9", "dafb9@umsystem.edu", "Iwantabetterfuture1")
admin.privileges.privileges = ["can add post", "can delete post", "can ban user"]
admin.privileges.show_privileges()