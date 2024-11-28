"""
CP1404/CP5632 Practical - Band.py.
"""


class Band:
    """Represent class Band."""

    def __init__(self, name):
        """Initialize Band with name."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Represent a string of Band object."""
        musician_info = ''.join([str(musician) for musician in self.musicians])
        return f"Band: {self.name}\n{musician_info}"

    def add(self, musician):
        """Add musician to musicians list."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing the instrument playing"""
        return '\n'.join([musician.play() for musician in self.musicians])
