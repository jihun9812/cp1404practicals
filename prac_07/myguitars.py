import csv
from guitar import Guitar


def main():
    guitars = load_guitars("guitars.csv")
    display_guitars(guitars)

    print("\n--- Sorted Guitars by Year ---")
    guitars.sort()
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Read guitar data from a CSV file and return a list of Guitar objects"""
    guitars = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row[0], int(row[1]), float(row[2])
                guitars.append(Guitar(name, year, cost))
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """Display the list of guitars."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Prompt the user to enter new guitars and add them to the list."""
    print("\nEnter new guitars: ")
    name = input("Guitar Name: ")

    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost:$ "))
            new_guitar = Guitar(name, year, cost)
            guitars.append(new_guitar)
            print(f"Added: {new_guitar}")
        except ValueError:
            print("Invalid input. Please enter numbers for year and cost.")


        name = input("Guitar Name: ")


def save_guitars(filename, guitars):
    """Save the list of guitars to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"Guitars saved to '{filename}'.")


if __name__ == "__main__":
    main()