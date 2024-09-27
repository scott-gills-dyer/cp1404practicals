"""
CP1404/CP5632 - Practical
Score menu program
"""

MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"


def main():
    print(MENU)
    choice = input("Please select an option above: ").upper()
    while choice != "Q":
        if choice == "G":
            pass
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice.")
            print(MENU)
            choice = input("Please choose an option above: ").upper()


main()
