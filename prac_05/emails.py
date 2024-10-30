"""
CP1404
Email to name dictionary
"""


def main():
    """Program to get user email and add to a dictionary after separating name."""
    email_to_name = {}
    email = input("Please enter your email: ")
    while email != "":
        name = get_name_from_email(email)
        choice = input(f" Is your name {name}? (Y/n)")

        if choice.upper() != "Y" and choice != "":
            name = input("What is your name: ")

        email_to_name[email] = name
        email = input("Please enter your email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Extract name from email address, separate multiple names if given."""
    prefix = email.split('@')[0]
    split_name = prefix.split('.')
    return " ".join(split_name).title()


main()
