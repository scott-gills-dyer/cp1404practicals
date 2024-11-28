"""
CP1404/CP5632 Practical - unreliable car.
"""
from prac_09.car import Car
from random import uniform


class UnreliableCar(Car):
    """Represent class unreliable car"""

    def __init__(self, name, fuel, reliability=0.0):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive car if random number is greater than reliability."""
        random_number = uniform(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven
