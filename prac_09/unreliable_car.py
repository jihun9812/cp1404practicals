import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that might not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive like a normal Car, but only sometimes."""
        random_number = random.randint(1, 100)
        if random_number <= self.reliability:
            distance_driven = super().drive(distance)
            print(f"{self.name} drove {distance_driven}km")
            return distance_driven
        else:
            print(f"{self.name} didn't start!")
            return 0
