"""

"""

from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = []
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input("Choose a menu option: ").lower()
    while choice != "q":
        if choice == "c":
            pass
        elif choice == "d":
            if current_taxi:
                pass
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("invalid option.")
    print("Thank you, goodbye!")


main()
