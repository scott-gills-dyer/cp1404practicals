"""
CP1404/CP5632 Practical - Silver service taxi.
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent silver service taxi object."""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialize silver service taxi object."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """Represent a string of SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.price_per_km:.2f}"

    def get_fare(self):
        """Return flagfall plus fare rounded to nearest 10 cent."""
        return round(self.flagfall + super().get_fare(), 1)
