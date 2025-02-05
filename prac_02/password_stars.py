
PASSWORD_LENGTH = 8

def main():
    # Receive a password from the user and output it as '*'.
    password = get_password()
    print_star(password)


def get_password():
    # get password from users
    password = input("Enter your password: ")
    while len(password) < PASSWORD_LENGTH:
        print("Password is too short, please enter at least 8 characters.")
        password = input("Enter your password: ")
    return password


def print_star(password):
    # print asterisks
    print('*' * len(password))





main()

