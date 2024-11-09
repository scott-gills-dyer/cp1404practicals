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
            print(f"Loaded {len(projects)} from projects.txt")
        elif choice == "S":
            pass
        elif choice == "D":
            if projects:
                display_incomplete_projects(projects)
                display_complete_projects(projects)
            else:
                print("There are no projects loaded")
        elif choice == "F":
            pass
        elif choice == "A":
            name = input("Enter the project name: ").title()
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: "))
            completion_percentage = float(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            for i, project in enumerate(projects):
                print(i, project)
        else:
            print("Invalid choice")
            print(MENU)
        print(MENU)
        choice = input("Enter your choice: ").upper()


def display_complete_projects(projects):
    """"""
    print("completed projects")
    for project in projects:
        if project.is_complete():
            print(project)


def display_incomplete_projects(projects):
    """"""
    print("Incomplete projects")
    for project in projects:
        if not project.is_complete():
            print(project)


def load_project(projects):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
