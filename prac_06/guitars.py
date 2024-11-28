"""
CP1404

Estimate: 15 minutes
Actual:   25 minutes
"""

from guitar import Guitar


def main():
    """Program that gets guitar information, appends a list and prints the formatted list."""
    guitars = []
    name = input("Enter a guitar name: ")
    while name != "":
        year = int(input("Enter a year: "))
        cost = float(input("Enter a cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:.2f} added.")
        name = input("Enter a guitar name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        max_name_length = max(len(guitar.name) for guitar in guitars)
        print("These are my guitars:")

        for i, guitar in enumerate(guitars, 1):
            vintage_string = "(Vintage)" if guitar.is_vintage() else ""
            print(
                f"Guitar {i}: {guitar.name:>{max_name_length}} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

    else:
        print("There are no guitars.")


main()
