"""
CP1404 Practical

Project Management Program
Estimate: 4 Hours
Actual:
"""

from project import Project

FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter by date\n(A)dd new project\n(U)pdate project")

def main():
    projects = []
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "L":
            load_project(projects)
            pass
        elif choice == "S":
            pass
        elif choice == "D":
            for project in projects:
                print(project)
        elif choice == "F":
            pass
        elif choice == "U":
            pass
        elif choice == "A":
            pass
        elif choice == "U":
            pass
        else:
            print("Invalid choice")
            print(MENU)
        choice = input("Enter your choice: ").upper()


def load_project(projects):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
