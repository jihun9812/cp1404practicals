COLOR_CODES = {
    "AliceBlue": "#f0f8ff",
    "Red": "#ff0000",
    "Orange": "#ffa500",
    "Yellow": "#ffff00",
    "Green": "#00ff00",
    "Blue": "#0000ff",
    "Indigo": "#4b0082",
    "Purple": "#9b30ff",
    "White": "#ffffff",
    "Black": "#000000",
}

user_input = input("Enter a color name (or blank to quit): ").lower()

while user_input:
    if user_input in COLOR_CODES:
        print(f"The hex code for {user_input} is: {COLOR_CODES[user_input]}")
    else:
        print(f"Sorry, I don't know the hex code for '{user_input}'.")

    user_input = input("Enter a color name (or blank to quit): ").lower()

print("Thank you for using the color code lookup program!")
