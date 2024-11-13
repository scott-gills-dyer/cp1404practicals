"""
CP1404 Practical

Project Management Program
Estimate: 4 Hours
Actual: 5 Hours
"""
from project import Project
from datetime import datetime

FILENAME = "projects.txt"
MENU = ("(L)oad projects\n(S)ave projects\n(D)isplay projects\n"
        "(F)ilter by date\n(A)dd new project\n(U)pdate project")


def main():
    """Program that loads data from a file to a list, allows adding and amending projects,
    and saves updates back to the file."""
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
            date = get_valid_date("Show projects that start after date (dd/mm/yy): ")
            filter_project_date = filter_projects_by_date(date, projects)
            display_incomplete_projects(filter_project_date)

        elif choice == "A":
            name = get_valid_input("Enter the project name: ").title()
            start_date = get_valid_date("Start date (dd/mm/yyyy): ")
            priority = get_valid_number("Priority: ")
            cost_estimate = get_valid_cost("Cost estimate: ")
            completion_percentage = get_valid_percentage("Percent complete: ")
            projects.append(Project(name, start_date, priority, cost_estimate, completion_percentage))
        elif choice == "U":
            if projects:
                project_choice = get_project_choice(projects)
                selected_project = projects[project_choice]
                print(selected_project)
                update_project(selected_project)
            else:
                print("There are no projects loaded")
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


def get_valid_index(projects, prompt):
    """Get a valid index below the length of the list."""
    valid_index = get_valid_number(prompt)
    while valid_index > len(projects):
        print("Invalid input")
        valid_index = int(input())
    return valid_index


def get_valid_number(prompt):
    """Get a valid number above 0."""
    is_valid_input = False
    while not is_valid_input:
        try:
            valid_number = int(input(prompt))
            if valid_number < 0:
                print("Number must not be negative")
            else:
                is_valid_input = True
        except ValueError:
            print("Invalid Input")
    # Will never be referenced before assignment
    return valid_number


def get_valid_input(prompt):
    """Get a valid input that is empty."""
    valid_input = input(prompt).strip()
    while not valid_input:
        print("Input cannot be empty")
        valid_input = input(prompt).strip()
    return valid_input


def get_valid_date(prompt):
    """Get a valid date format."""
    is_valid_date = False
    while not is_valid_date:
        date_string = input(prompt).strip()
        try:
            valid_date = datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date format. Please use dd/mm/yyyy.")
    # Will never be referenced before assignment
    return valid_date


def get_valid_cost(prompt):
    """Get valid float above 0."""
    is_valid_input = False
    while not is_valid_input:
        try:
            valid_cost = float(input(prompt))
            if valid_cost >= 0:
                is_valid_input = True
            else:
                print("Cost estimate must not be negative.")
        except ValueError:
            print("Invalid input.")
    # Will never be referenced before assignment
    return valid_cost


def get_valid_percentage(prompt):
    """Get a valid percentage between 0 and 100"""
    is_valid_input = False
    while not is_valid_input:
        try:
            percentage = float(input(prompt))
            if 0 <= percentage <= 100:
                is_valid_input = True
            else:
                print("Completion percentage must be between 0 and 100.")
        except ValueError:
            print("Invalid percentage.")
    # Will never be referenced before assignment
    return percentage


def filter_projects_by_date(date, projects):
    """Filter projects by date."""
    filter_project_date = [project for project in projects if project.start_date > date]
    return filter_project_date


def update_project(selected_project):
    """Update a project with a new percentage and priority."""
    new_percentage = get_valid_percentage("New percentage: ")
    new_priority = get_valid_number("New priority: ")
    selected_project.completion_percentage = new_percentage
    selected_project.priority = new_priority


def save_projects(projects):
    """Save a projects list to projects.txt."""
    with open(FILENAME, "w", encoding="utf-8-sig") as out_file:
        for project in projects:
            out_file.write(f"{project}\n")


def get_project_choice(projects):
    """Get a valid project choice from list of projects."""
    for i, project in enumerate(projects):
        print(i, project)
    project_choice = get_valid_index(projects, "Project choice: ")
    return project_choice


def display_complete_projects(projects):
    """Display complete projects list."""
    print("completed projects:")
    for project in projects:
        if project.is_complete():
            print(project)


def display_incomplete_projects(projects):
    """Display incomplete projects list."""
    print("Incomplete projects:")
    for project in projects:
        if not project.is_complete():
            print(project)


def load_projects(projects):
    """Load projects from projects.txt."""
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            start_date = datetime.strptime(parts[1], "%d/%m/%Y").date()
            project = Project(parts[0], start_date, int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
