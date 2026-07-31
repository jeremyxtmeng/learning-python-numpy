"""A class that can be used to represent a car."""
class Car:
    """Representing a car"""
    def __init__(self, make, year):
        self.odometer=0
        self.year=year
        self.make=make
        pass

    def read_odometer(self):
        """Print odometer"""
        print(f"This case has {self.odometer} miles")

    def get_name(self):
        """Pring car make"""
        print(f"The make is {self.make}")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer += miles

