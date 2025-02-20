DISCOUNT_RATE = 0.1
DISCOUNT_THRESHOLD = 100

total_price = 0

items_number = int(input("Number of items: "))
while items_number <= 0:
    print("Invalid number of items!")
    items_number = int(input("Please enter a valid number of items: "))

for i in range(items_number):
    price = float(input(f"Price of item {i + 1}: "))
    total_price += price

if total_price >= DISCOUNT_THRESHOLD:
    total_price -= total_price * DISCOUNT_RATE

print(f"Total price for {items_number} items is ${total_price:.2f}")
