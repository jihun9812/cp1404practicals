from guitar import Guitar


def main():
    """Collect user input for guitars, store them in a list and display the details of each guitar."""
    guitars = []
    print("My guitars!")


    name = input("Name: ")


    while name:
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
        except ValueError:
            print("Please enter a valid year and cost.")
            name = input("Name: ")
            continue


        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")


        name = input("Name: ")


    if guitars:
        print("\nThese are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
    else:
        print("No guitars in the collection.")


main()
