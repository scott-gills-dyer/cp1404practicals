"""

"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        """"""
        return f"{super().__str__()} plus flagfall of ${self.price_per_km:.2f}"

    def get_fare(self):
        """"""
        return round(self.flagfall + super().get_fare(), 1)
