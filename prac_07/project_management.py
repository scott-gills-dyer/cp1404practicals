"""
CP1404 Practical

Project Management Program
Estimate: 4 Hours
Actual:
"""
from project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter by date\n(A)dd new project\n(U)pdate project")


def main():
    projects = []
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":
        if choice == "L":
            load_projects(projects)
            print(f"Loaded {len(projects)} from projects.txt")
        elif choice == "S":
            save_projects(projects)
            print(f"Saved {len(projects)} to projects.txt")
        elif choice == "D":
            if projects:
                display_incomplete_projects(projects)
                display_complete_projects(projects)
            else:
                print("There are no projects loaded")
        elif choice == "F":
            date = get_date()
            filter_project_date = filter_projects_by_date(date, projects)
            display_incomplete_projects(filter_project_date)

        elif choice == "A":
            name = input("Enter the project name: ").title()
            start_date = input("Start date (dd/mm/yy): ")
            priority = int(input("Priority: "))
            cost_estimate = float(input("Cost estimate: "))
            completion_percentage = float(input("Percent complete: "))
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            project_choice = get_project_choice(projects)
            selected_project = projects[project_choice]
            print(selected_project)
            update_project(selected_project)
        else:
            print("Invalid choice")
            print(MENU)
        print(MENU)
        choice = input("Enter your choice: ").upper()
    save_option = input("Would you like to save to projects.txt? (Y/n): ")
    if save_option != "n":
        save_projects(projects)
        print("projects saved")
    print("Thank you for using custom-built project management software.")


def filter_projects_by_date(date, projects):
    """"""
    filter_project_date = [project for project in projects if project.start_date > date]
    return filter_project_date


def get_date():
    """"""
    date_string = input("Show projects that start after date (dd/mm/yy): ")
    date = datetime.strptime(date_string, "%d/%m/%Y").date()
    return date


def update_project(selected_project):
    """"""
    new_percentage = float(input("New percentage: "))
    new_priority = int(input("New priority: "))
    selected_project.completion_percentage = float(new_percentage)
    selected_project.priority = int(new_priority)


def save_projects(projects):
    """"""
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for project in projects:
            out_file.write(f"{project}\n")


def get_project_choice(projects):
    """"""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = int(input("Project choice: "))
    return project_choice


def display_complete_projects(projects):
    """"""
    print("completed projects:")
    for project in projects:
        if project.is_complete():
            print(project)


def display_incomplete_projects(projects):
    """"""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(project)


def load_projects(projects):
    """"""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
