"""
Emails
Estimate: 20 minutes
Actual:   30 minutes
"""

def extract_name(email):
    username = email.split('@')[0]
    parts = username.split('.')
    name = ' '.join(parts).title()
    return name

def main():
    user_data = {}

    while True:
        email = input("Email: ")
        if not email:
            break

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation == 'n':
            name = input("Name: ").title()

        user_data[email] = name

    print("\nResults:")
    for email, name in user_data.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
