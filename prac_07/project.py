import datetime

class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize a Project."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return a string representation of a Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare two projects based on priority."""
        return self.priority < other.priority

    def is_completed(self):
        """Check if the project is completed."""
        return self.completion_percentage == 100
