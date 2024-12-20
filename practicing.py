# just for practicing while reading
# mostly in-text examples

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kWh battery.")

    def get_range(self):
        if self.battery_size == 40:
            battery_range = 150
        elif self.battery_size == 65:
            battery_range = 225
        elif self.battery_size == 110:
            battery_range = 380

        print(f"This car can go about {battery_range} miles on a full charge")


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


my_x = ElectricCar('Tesla', 'X', 2024)
print(my_x.get_descriptive_name())
my_x.battery.battery_size = 110
my_x.battery.describe_battery()
my_x.battery.get_range()


# my_new_car = Car("audi", 'a4', 2024)
# my_new_car.get_descriptive_name()
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()
# my_new_car.update_odometer(34)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(20)
# my_new_car.read_odometer()