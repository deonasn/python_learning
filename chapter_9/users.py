# Deon Anoth
# 08-09-2024
# Python Crash Course: Try it yourself: 9-3

class User:
    """A class for user profile"""
    def __init__(self, first_name, last_name, username, email, password):
        """default method"""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password

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

# creating user1 instance and calling methods from the class 'User'
user1 = User('Deon','Anoth','danoth','dafb9@umsl.edu','Iwantabetterfuture1')
user1.describe_user()
user1.greet_user()

# creating user2 instance and calling methods from the class 'User'
user2 = User('Zyer','Anoth','zanoth','zyeranoth@gmail.com','brsdzbaans')
user2.describe_user()
user2.greet_user()

# creating user3 instance and calling methods from the class 'User'
user3 = User('Shahana','Bashir','shahanabashir','shahanabashir@gmail.com',
             'brsdzbaans')
user3.describe_user()
user3.greet_user()