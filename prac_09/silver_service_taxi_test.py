"""

"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """"""
    taxi = SilverServiceTaxi('Lux Taxi', 100, 1.5)
    taxi.drive(50)
    print(taxi)
    print(taxi.get_fare())

    other_taxi = SilverServiceTaxi('Super Lux', 100, 2)
    assert other_taxi.drive(18)
    print(other_taxi.fuel)
    assert other_taxi.get_fare() == 48.78
    print(other_taxi.get_fare())

main()
