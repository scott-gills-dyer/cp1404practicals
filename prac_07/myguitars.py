"""
CP1404 Practical

Guitars
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Project that reads from file, adds to list to and prints guitars."""
    guitars = []
    read_file(FILENAME, guitars)
    guitars.sort()
    for guitar in guitars:
        print(guitar)


def read_file(filename, guitars):
    """Read guitars from a CSV file."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


main()
