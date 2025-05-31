# just for practicing 'pytest' while reading
# imports functions from practicing.py
# mostly in-text examples

from practicing import get_formatted_name

def test_get_formatted_name():
    """Test the get_formatted_name function."""
    formatted_name = get_formatted_name('deon', 'anoth')
    assert formatted_name == "Deon Anoth"

def test_get_formatted_name_with_middle():
    """Test the get_formatted_name function with a middle name."""
    formatted_name = get_formatted_name('deon', 'anoth', 'basheer')
    assert formatted_name == "Deon Basheer Anoth"