"""
CP1404/CP5632 - Practical
Create a new file called files.py and do all the following separate questions in it.
"""

# Question 1

out_file = open("names.txt", "w")
name = input("What is your name: ")
print(name, file=out_file)
out_file.close()

# Question 2

in_file = open("names.txt", "r")
name = in_file.read().strip()
in_file.close()
print(f"Hello {name}")

# Question 3
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())
print(first_number + second_number)
