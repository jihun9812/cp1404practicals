import datetime
from project import Project

def load_projects(filename):
    """Load projects from a file and return a list of Project objects."""
    projects = []
    try:
        with open(filename, 'r') as file:
            file.readline()  # Skip header
            for line in file:
                parts = line.strip().split('\t')
                if len(parts) == 5:  # Ensure we have all required fields
                    project = Project(parts[0], parts[1], int(parts[2]), float(parts[3]), int(parts[4]))
                    projects.append(project)
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
    except ValueError as e:
        print(f"Error: Invalid data in the file. {str(e)}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return projects

def save_projects(filename, projects):
    """Save a list of Project objects to a file."""
    try:
        with open(filename, 'w') as file:
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            for project in projects:
                file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                           f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
        print(f"Projects saved to {filename}")
    except Exception as e:
        print(f"Error saving projects: {str(e)}")

def display_projects(projects):
    """Display projects grouped by completion status and sorted by priority."""
    incomplete = [project for project in projects if not project.is_completed()]
    complete = [project for project in projects if project.is_completed()]
    
    print("Incomplete projects:")
    for project in sorted(incomplete):
        print(f"  {project}")
    print("Completed projects:")
    for project in sorted(complete):
        print(f"  {project}")

def filter_projects_by_date(projects):
    """Filter and display projects that start after a specified date."""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = [project for project in projects if project.start_date > date]
        for project in sorted(filtered_projects, key=lambda p: p.start_date):
            print(project)
    except ValueError:
        print("Invalid date format. Please use dd/mm/yyyy.")

def add_new_project(projects):
    """Add a new project based on user input."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost_estimate = input("Cost estimate: $")
    percent_complete = input("Percent complete: ")
    try:
        new_project = Project(name, start_date, int(priority), float(cost_estimate), int(percent_complete))
        projects.append(new_project)
        print("Project added successfully.")
    except ValueError as e:
        print(f"Error adding project: {str(e)}")

def update_project(projects):
    """Update an existing project's completion percentage and priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        choice = int(input("Project choice: "))
        project = projects[choice]
        print(project)
        new_percentage = input("New Percentage: ")
        if new_percentage:
            project.completion_percentage = int(new_percentage)
        new_priority = input("New Priority: ")
        if new_priority:
            project.priority = int(new_priority)
        print("Project updated successfully.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")

def main():
    """Main program for project management."""
    filename = 'projects.txt'
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")
    
    while True:
        print("\n- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")
        
        choice = input(">>> ").lower()
        
        if choice == 'l':
            filename = input("Enter filename to load projects from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save projects to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save = input("Would you like to save to projects.txt? ").lower()
            if save.startswith('y'):
                save_projects('projects.txt', projects)
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
