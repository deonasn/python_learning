# Deon Anoth
# 06-01-2025
# Python Crash Course: Try it yourself: 11-3
# test_ file for employee.py

import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Fixture to create an instance of Employee."""
    employee = Employee('Deon', 'Anoth', 10000)
    return employee

def test_give_default_raise(employee):
    """Test the default raise amount."""
    employee.give_raise()
    assert employee.annual_salary == 15000

def test_give_custom_raise(employee):
    """Test a custom raise amount."""
    employee.give_raise(2000)
    assert employee.annual_salary == 12000