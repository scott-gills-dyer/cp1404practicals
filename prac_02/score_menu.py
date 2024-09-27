"""
CP1404/CP5632 - Practical
Score menu program
"""

MENU = "(G)et a valid score \n(P)rint result \n(S)how stars \n(Q)uit"
MINIMUM = 0
MAXIMUM = 100


def main():
    """Program display score status and stars after getting a score."""
    score = get_valid_score()
    print(MENU)
    choice = input("Please select an option above: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score(score))
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice.")
            print(MENU)
        choice = input("Please choose an option above: ").upper()
    print("Goodbye Good Friend!")


def determine_score(score):
    """Determine the status of given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    return "Excellent"


def get_valid_score():
    """Get a valid score."""
    valid_score = int(input("Please enter your score: "))
    while valid_score < MINIMUM or valid_score > MAXIMUM:
        print("Invalid score")
        valid_score = int(input("Please enter your score: "))
    return valid_score


main()
