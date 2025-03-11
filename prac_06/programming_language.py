class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""
    def __init__(self,name,typing,reflection,year):
        """Initialise a Programming Language instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        "checks if the object's typing attribute is dynamic."
        return self.typing.lower() == "dynamic"


    def __str__(self):
        """Return a string representation of the state."""
        return f'{self.name},{self.typing} Typing, Reflection={self.reflection}, First appear in {self.year}'
