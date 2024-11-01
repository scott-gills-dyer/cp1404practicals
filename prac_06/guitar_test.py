from guitar import Guitar


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other_guitar = Guitar("Another Guitar", 2013, 1512.9)

    print(f"{guitar.name} get_age() - Expected {102}. Got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected {11}. Got {other_guitar.get_age()}")
    print(f"{guitar.name} get_age() - Expected {True}. Got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected {False}. Got {other_guitar.is_vintage()}")


run_test()
