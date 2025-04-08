from unreliable_car import UnreliableCar

# Create an unreliable car with a 50% chance of starting
unreliable_car = UnreliableCar("Unreliable Car", 100, 50)

# Attempt to drive the car 3 times
for _ in range(3):
    unreliable_car.drive(40)
