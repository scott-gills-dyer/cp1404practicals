"""
CP1404 - Practical 02
write a program that asks the user for a password, with error-checking to repeat if the password doesn't meet a minimum length set by a variable.
"""

MINIMUM_LENGTH = 6


def main():
    """Program to get valid password and print asterisks."""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """Print asterisks equal to the length of password."""
    print("*" * len(password))


def get_password():
    """Get valid password length greater than minimum."""
    password = input("Enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Please enter a password of length {MINIMUM_LENGTH} or greater")
        password = input("Enter a password: ")
    return password


main()
