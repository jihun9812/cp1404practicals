from taxi import Taxi

my_taxi = Taxi("Prius 1", 100)

my_taxi.drive(40)

print(my_taxi)
print("Current fare: $", my_taxi.get_fare())
fare = my_taxi.get_fare()
formatted_fare = f"$ {fare:.2f}"
print("Total fare:", formatted_fare)

my_taxi.start_fare()
my_taxi.drive(100)

print(my_taxi)
print("Current fare: $", my_taxi.get_fare())
fare = my_taxi.get_fare()
formatted_fare = f"$ {fare:.2f}"
print("Total fare:", formatted_fare)