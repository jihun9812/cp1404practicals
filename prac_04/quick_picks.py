import random

NUM_MIN = 1
NUM_MAX = 45
NUM_PICKS_PROMPT = "How many quick picks? "

def generate_quick_pick():
    numbers = set()
    while len(numbers) < 6:
        numbers.add(random.randint(NUM_MIN, NUM_MAX))
    return sorted(numbers)

def main():
    num_picks = int(input(NUM_PICKS_PROMPT))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        print(" ", end="")
        for num in quick_pick:
            print("{:>3}".format(num), end="")
        print()

if __name__ == "__main__":
    main()