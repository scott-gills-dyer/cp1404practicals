"""
CP1404 Practical

Estimate: 4 hours
Actual:
"""


class Project:
    """"""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0, completion_percentage=0.0):
        """"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


    def __str__(self):
        """"""
        return (f"{self.name}, Start: {self.start_date}, Priority: {self.priority}, "
                f"Estimate: ${self.cost_estimate:.2f}, Completion: {self.completion_percentage}")
