# Deon Anoth
# 06-01-2025
# Python Crash Course: Try it yourself: 11-3
# test_ file for employee.py

from employee import Employee

def test_give_default_raise():
    """Test the default raise amount."""
    employee = Employee('Deon', 'Anoth', 10000)
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise():
    """Test a custom raise amount."""
    employee = Employee('Deon', 'Anoth', 10000)
    employee.give_raise(2000)
    assert employee.annual_salary == 12000