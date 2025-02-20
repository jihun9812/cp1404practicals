MENU = "(H)ello\n(G)oodbye\n(Q)uit\n>>> "
name = input("Enter name: ")
choice = input(MENU).upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")

    choice = input(MENU).upper()

print("Finished.")
