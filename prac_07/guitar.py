class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialize a Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of a Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the current year."""
        return 2023 - self.year

    def is_vintage(self):
        """Determine if a guitar is vintage or not based on age."""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Compare two guitars based on their year."""
        return self.year < other.year
