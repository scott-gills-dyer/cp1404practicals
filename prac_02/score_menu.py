"""
CP1404/CP5632 - Practical
Score menu program
"""

MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"
MINIMUM = 0
MAXIMUM = 100

def main():
    print(MENU)
    choice = input("Please select an option above: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            pass
        elif choice == "S":
            pass
        else:
            print("Invalid choice.")
            print(MENU)
            choice = input("Please choose an option above: ").upper()


def get_valid_score():
    valid_score = int(input("Please enter your score: "))
    while valid_score < MINIMUM or valid_score > MAXIMUM:
        print("Invalid score")
        valid_score = int(input("Please enter your score: "))
    return valid_score


main()
