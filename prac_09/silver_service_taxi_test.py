from silver_service_taxi import SilverServiceTaxi

silver_taxi = SilverServiceTaxi("Hummer", 200, 2)

silver_taxi.drive(18)

print(silver_taxi)
print("Total fare: $", silver_taxi.get_fare())
