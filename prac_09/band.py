class Band:
    """Represents a band with a name and a list of musicians."""

    def __init__(self, name):
        """Initializes the band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Returns a string representation of the band, including its name and musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Adds a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Iterates through the musicians and prints a message for each one playing their instrument."""
        for musician in self.musicians:
            print(musician.play())
