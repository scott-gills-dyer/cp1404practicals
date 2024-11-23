"""

"""

from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    total_bill = 0
    taxis = [Taxi('Prius', 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer" , 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU)
    choice = input("Choose a menu option: ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxis available")
            for i, taxi in enumerate(taxis):
                print(f"{i} - {taxi}")
            taxi_choice = int(input("Choose a taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid taxi")

        elif choice == "d":
            if current_taxi:
                pass
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("invalid option.")
        print(f"Bill to date: ${total_bill:.2f}")
        choice = input("Choose a menu option: ").lower()
    print("Thank you, goodbye!")


main()
