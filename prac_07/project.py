# project.py

from datetime import datetime


class Project:
    COMPLETE_PERCENTAGE = 100
    """A class to represent a project with its details."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialize a new Project instance."""
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)

    def __str__(self):
        """Return a formatted string representation of the project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority: {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion}%")

    def is_complete(self):
        """Check if the project is complete"""
        return self.completion == self.COMPLETE_PERCENTAGE

    def update(self, completion=None, priority=None):
        """Update the project's completion and priority if provided."""
        if completion is not None:
            self.completion = completion
        if priority is not None:
            self.priority = priority

    def __lt__(self, other):
        """Compare projects based on priority for sorting."""
        return self.priority < other.priority
