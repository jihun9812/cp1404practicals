"""CP1404/CP5632 Practical - Guitar class."""

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar object."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the current year."""
        return 2024 - self.year

    def is_vintage(self):
        """Determine if a guitar is considered vintage or not."""
        return self.get_age() >= 50
