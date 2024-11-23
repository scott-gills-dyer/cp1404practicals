
from prac_09.taxi import Taxi

class SilverServiceTaxi(Taxi):
    """"""

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= self.fanciness

    def __str__(self):
        return f"{self.fanciness} {self.price_per_km}"


