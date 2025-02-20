BONUS_THRESHOLD = 1000  # basic sales
LOW_BONUS_RATE = 0.10   # 10% bonus
HIGH_BONUS_RATE = 0.15   #15% bonus

sales = float(input("Enter sales: $"))

while sales >= 0:
    bonus = sales * (LOW_BONUS_RATE if sales < BONUS_THRESHOLD else HIGH_BONUS_RATE)
    print(f"Your bonus is: ${bonus:.2f}")
    sales = float(input("Enter sales: $"))

print("Exiting the program.")
