"""
CP1404 Practical

Project Management Program
Estimate: 4 Hours
Actual:
"""

from project import Project

FILENAME = "projects.txt"


def main():
    projects = []
    load_project(projects)
    for project in projects:
        print(project)


def load_project(projects):
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split("\t")
            project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4]))
            projects.append(project)


main()
