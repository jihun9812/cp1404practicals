# project_management.py

import datetime
from operator import attrgetter
from project import Project

FILENAME = "project.txt"

MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
"""


def load_projects(filename=FILENAME):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    with open(filename, "r") as file:
        next(file)
        for line in file:
            name, start_date, priority, cost_estimate, completion = line.strip().split("\t")
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


def save_projects(projects, filename=FILENAME):
    """Save a list of Project objects to a file."""
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.completion}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete_projects = sorted([p for p in projects if not p.is_complete()])
    completed_projects = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(" ", project)

    print("Completed projects:")
    for project in completed_projects:
        print(" ", project)


def filter_projects_by_date(projects):
    """Filter and display projects that start after a given date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()


    filtered_projects = sorted(
        [p for p in projects if p.start_date > filter_date],
        key=attrgetter('start_date')
    )

    for project in filtered_projects:
        print(project)


def add_project():
    """Prompt the user to add a new project."""
    print("Let's add a new project")

    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion = int(input("Percent complete: "))
    return Project(name, start_date, priority, cost_estimate, completion)


def update_project(projects):
    """Allow the user to update an existing project's completion and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    project_choice = int(input("Project choice: "))
    project = projects[project_choice]

    print(project)
    new_completion = input("New percentage: ")
    new_priority = input("New priority: ")

    project.update(
        completion=int(new_completion) if new_completion else None,
        priority=int(new_priority) if new_priority else None
    )


def main():
    """Run the project management program."""
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    choice = ""
    while choice != "q":
        print(MENU)
        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(projects, filename)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            new_project = add_project()
            projects.append(new_project)
            print(f"Added project: {new_project}")
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_confirm = input(f"Would you like to save to {FILENAME}? (y/n): ").lower()
            if save_confirm == 'y':
                save_projects(projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
