# Deon Anoth
# 06-01-2025
# Python Crash Course: Try it yourself: 11-1 -> 11-2

from city_functions import get_formatted_city_country

def test_city_country():
    """Test the get_formatted_city_country function."""
    formatted_city_country = get_formatted_city_country('santiago', 'chile')
    assert formatted_city_country == "Santiago, Chile"

def test_city_country_population():
    """Test the get_formatted_city_country function with a population."""
    formatted_city_country = get_formatted_city_country('santiago', 'chile', 5000000)
    assert formatted_city_country == "Santiago, Chile - population 5000000"