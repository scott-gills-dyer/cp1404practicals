"""
CP1404/CP5632 - Practical
Create a new file called files.py and do all the following separate questions in it.
"""

# Question 1.

out_file = open("names.txt", "w")
name = input("What is your name: ")
print(name, file=out_file)
out_file.close()
