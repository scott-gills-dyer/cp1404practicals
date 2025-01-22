"""
CP1404/CP5632 Practical - Silver service taxi test.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Program to test Silver Service Taxi class."""
    taxi = SilverServiceTaxi('Lux Taxi', 100, 1.5)
    taxi.drive(50)
    print(taxi)
    print(f" Fare: ${taxi.get_fare():.2f}")

    other_taxi = SilverServiceTaxi('Super Lux', 100, 2)
    assert other_taxi.drive(18)
    assert other_taxi.get_fare() == 48.80
    print(other_taxi)
    print(f" Fare: ${other_taxi.get_fare():.2f}")

main()
