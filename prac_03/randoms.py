import random

# Line 1

# This function generates a random integer between 5 and 20 inclusive.
# Example output: 15, 8, 20, etc.
# Smallest possible number: 5
# Largest possible number: 20
print(random.randint(5, 20))

# Line 2:

# This function generates a random integer starting from 3 up to, but not including, 10, with a step of 2.
# Possible outputs: 3, 5, 7, 9
# Smallest possible number: 3
# Largest possible number: 9
# Line 2 cannot produce a 4 because of the step of 2.
print(random.randrange(3, 10, 2))

# Line 3: random.uniform(2.5, 5.5)
# This function generates a random floating-point number between 2.5 and 5.5.
# Example output: 3.9842, 4.123, 5.004, etc.
# Smallest possible number: 2.5
# Largest possible number: 5.5
print(random.uniform(2.5, 5.5))

# Code to produce a random number between 1 and 100 inclusive:
print(random.randint(1, 100))
