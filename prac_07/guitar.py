# guitar.py

class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost"""
    def __init__(self, name="", year=0, cost=0):
        "Initialize a Guitar instance with name, year, and cost attributes "
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        "Return a formatted string representation of the guitar."
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        "Calculate and return the age of the guitar based on the current year."
        current_year = 2024
        return current_year - self.year

    def is_vintage(self):
        "Determine if the guitar is considered vintage (50 or more years old)."
        return self.get_age() >= 50

    def __lt__(self,other):
        """Define the less-than operator for sorting guitars by year."""
        return self.year < other.year

