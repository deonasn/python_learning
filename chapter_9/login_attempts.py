# Deon Anoth
# 08-09-2024
# Python Crash Course: Try it yourself: 9-5

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
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"\nLogin attempts have been reset!")

# creating user1 instance and calling methods from the class 'User'
user1 = User('Deon','Anoth','danoth','dafb9@umsl.edu','Iwantabetterfuture1')
user1.describe_user()
user1.greet_user()

# calling methods to increment and reset the values of login_attempts for user1
print("\n")
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Number of login attempts for {user1.first_name} {user1.last_name} : {user1.login_attempts}")
user1.reset_login_attempts()
print(f"Number of login attempts for {user1.first_name} {user1.last_name} : {user1.login_attempts}")