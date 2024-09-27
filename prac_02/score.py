"""
CP1404/CP5632 - Practical
Program to determine score status
"""

from random import randint

MINIMUM = 0
MAXIMUM = 100


def main():
    """Program to display score status by getting input."""
    score = float(input("Enter score: "))
    print(determine_score(score))
    print(determine_score(randint(MINIMUM, MAXIMUM)))


def determine_score(score):
    """Determine the status of given score."""
    if score < MINIMUM or score > MAXIMUM:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    return "Excellent"


main()
