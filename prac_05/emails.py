def main():
    # Get email from the user and receive confirmation.
    email_dict = {}

    input_active = True

    while input_active:
        email = input("Email: ").strip()

        if not email:
            input_active = False
            break

        name = extract_name(email)

        confirmation = input(f'Is your name {name}? (Y/n): ').strip().lower()
        if confirmation not in ['y', 'yes', '']:
            name = input("Name: ").strip()
        email_dict[email] = name

    for email, name in email_dict.items():
        print(f'{name} ({email})')


def extract_name(email):
    "Extracts the name from the email address."
    name_part = email.split("@")[0]
    name = name_part.replace(".", " ").title()
    return name


main()
