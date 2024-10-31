"""
CP1404/CP5632 Practical

Predicted: 10 mins
Actual: 20 mins

"""


class ProgrammingLanguage:
    """Programming Language class, has name, typing, reflection, year"""
    def __init__(self, name, typing, reflection, year):
        """Initialise a language instance"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if language is dynamic."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return string of the language object."""
        return f"{self.name}, {self.typing}, {self.reflection}, {self.year}"
