MINIMUM_LENGTH = 6


def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Please enter a password of length {MINIMUM_LENGTH} or greater")
        password = input("Enter a password: ")
    return password


main()
