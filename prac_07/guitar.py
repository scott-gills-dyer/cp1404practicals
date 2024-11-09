"""
CP1404 Practical

guitar
"""

CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Guitar class has name, year and cost."""

    def __init__(self, name="", year=0, cost=0.0):
        """Initialise a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of the guitar object."""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def __lt__(self, other):
        """Return if guitar object is older than other guitar."""
        return self.year < other.year

    def get_age(self):
        """Determine the age of the guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE
