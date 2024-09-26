PASSWORD_LENGTH = 6

password = input("Enter a password: ")
while len(password) < PASSWORD_LENGTH:
    print("Please enter a password of length 6 or greater")
    password = input("Enter a password: ")
print("*" * len(password))
