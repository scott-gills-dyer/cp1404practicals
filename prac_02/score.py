"""
CP1404/CP5632 - Practical
Program to determine score status
"""


def main():
    """Program to display score status by getting input."""
    score = float(input("Enter score: "))
    print(determine_score(score))


def determine_score(score):
    """Determine the status of given score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    return "Excellent"


main()
