"""

"""
class Band:
    """"""
    def __init__(self, name):
        self.name = name
        self.musicians = []

    def __str__(self):
        musician_info = ''.join([str(musician) for musician in self.musicians])
        return f"Band: {self.name}\n{musician_info}"


