# Deon Anoth
# 06-01-2025
# Python Crash Course: Try it yourself: 11-3

class Employee:
    """A class to represent an employee."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee's attributes."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_salary = annual_salary

    def give_raise(self, raise_amount=5000):
        """Add the raise amount to the annual salary."""
        self.annual_salary += raise_amount
        