"""
CP1404/CP5632 - Practical
Menus.py

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
MENU = " (H)ello \n (G)oodbye \n (Q)uit "

name = input("Enter your name: ")
print(MENU)
choice = input("Please choose an option above: ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello, {name}")
    elif choice == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input("Please choose an option above: ").upper()
print(f"Finished")
