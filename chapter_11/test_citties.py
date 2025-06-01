# Deon Anoth
# 01-10-2025
# Python Crash Course: Try it yourself: 10-1 -> 10-2

from city_functions import get_formatted_city_country

def test_city_country():
    """Test the get_formatted_city_country function."""
    formatted_city_country = get_formatted_city_country('santiago', 'chile')
    assert formatted_city_country == "Santiago, Chile"