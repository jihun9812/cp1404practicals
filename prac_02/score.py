import random


MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_SCORE = 90
PASSABLE_SCORE = 50



def main():
    # Get the score from the user
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(result)

    # Generate a random score and print the result
    random_score = random.randint(0, 100)
    random_result = determine_score_result(random_score)
    print(f"Random score: {random_score}, Result: {random_result}")



def determine_score_result(score):
    # Function to determine the result based on the score
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_SCORE:
       return  "Excellent"
    elif score >= PASSABLE_SCORE:
        return "Passable"
    else:
        return "Bad"




main()

