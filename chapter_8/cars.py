# Deon Anoth
# 06-24-2024
# Python Crash Course: Try it yourself: 8-14

# defining function 'build_car' using arbitrary keyword arguments
def build_car(manufacturer, model, **car_info):
    """Build a dictionary containing everything we kow about the car."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# function call and prints the dictionary
car = build_car('subaru', 'outback', color = 'blue', tow_package = True)
print(car)