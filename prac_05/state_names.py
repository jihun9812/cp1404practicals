"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {
    "qld": "Queensland",
    "nsw": "New South Wales",
    "nt": "Northern Territory",
    "wa": "Western Australia",
    "act": "Australian Capital Territory",
    "vic": "Victoria",
    "tas": "Tasmania",
}

for code, name in CODE_TO_NAME.items():
    print(f"{code} is {name}")

while True:
    try:
        state_code = input("Enter short state: ").lower()
        if not state_code:
            break
        print(f"{state_code} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
