"""
CP1404 Practical

Estimate: 4 hours
Actual: 5 Hours
"""
from datetime import datetime

class Project:
    """Project class that has name, start_date, priority, cost_estimate, completion_percentage."""

    def __init__(self, name, start_date, priority=0, cost_estimate=0, completion_percentage=0.0):
        """Initialises a project instance with name, start_date, priority, cost_estimate, completion_percentage."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage


    def __str__(self):
        """Return string of the project object."""
        return (f"{self.name}, Start: {self.start_date}, Priority: {self.priority}, "
                f"Estimate: ${self.cost_estimate:.2f}, Completion: %{self.completion_percentage}")

    def is_complete(self):
        """Determines if the project has been completed."""
        return self.completion_percentage == 100