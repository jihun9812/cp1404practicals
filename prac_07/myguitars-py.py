from guitar import Guitar

def load_guitars(filename):
    """Load guitars from a file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars

def save_guitars(filename, guitars):
    """Save a list of Guitar objects to a file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

def main():
    """Read file of guitar details, save as objects, display."""
    guitars = load_guitars('guitars.csv')

    # Display guitars
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

    # Sort guitars by year and display
    guitars.sort()
    print("\nGuitars sorted by year:")
    for guitar in guitars:
        print(f"{guitar.name} ({guitar.year})")

    # Get a new guitar from user input
    print("\nAdd a new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)

    # Save all guitars back to the file
    save_guitars('guitars.csv', guitars)
    print("Guitars saved to guitars.csv")

if __name__ == '__main__':
    main()
