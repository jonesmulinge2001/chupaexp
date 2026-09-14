#       AIRPORT MANAGEMENT SYSTEM

FILE_NAME = "airports.txt"
# 1. Load airports from file

def load_airports():
    airports = []
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")

                if len(parts) == 3:
                    airport = {
                        "name": parts[0],
                        "city": parts[1],
                        "country": parts[2]
                    }

                    airports.append(airport)

    except FileNotFoundError:
        # File does not exist yet
        pass

    return airports


# ------------------------------------------
# 2. Save airports to file
# ------------------------------------------

def save_airports(airports):

    with open(FILE_NAME, "w") as file:

        for airport in airports:

            file.write(
                f"{airport['name']}|"
                f"{airport['city']}|"
                f"{airport['country']}\n"
            )


# ------------------------------------------
# 3. Display menu
# ------------------------------------------

def display_menu():

    print("\n")
    print("=" * 40)
    print("       AIRPORT MANAGEMENT SYSTEM")
    print("=" * 40)

    print("1. Add Airport")
    print("2. View Airports")
    print("3. Search Airport")
    print("4. Generate Report")
    print("5. Update Airport")
    print("6. Delete Airport")
    print("7. Exit")

    print("=" * 40)


# ------------------------------------------
# 4. Validate text input
# ------------------------------------------

def get_required_input(message):

    while True:

        value = input(message).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


# ------------------------------------------
# 5. Check for duplicate airport
# ------------------------------------------

def airport_exists(airports, name):

    for airport in airports:

        if airport["name"].lower() == name.lower():
            return True

    return False


# ------------------------------------------
# 6. Add airport
# ------------------------------------------

def add_airport(airports):

    print("\n--- ADD AIRPORT ---")

    name = get_required_input("Airport name: ")

    # Prevent duplicate airports
    if airport_exists(airports, name):

        print("An airport with that name already exists.")
        return

    city = get_required_input("City: ")
    country = get_required_input("Country: ")

    airport = {
        "name": name,
        "city": city,
        "country": country
    }

    airports.append(airport)

    # Save immediately
    save_airports(airports)

    print("\nAirport added successfully!")


# ------------------------------------------
# 7. View airports
# ------------------------------------------

def view_airports(airports):

    print("\n--- ALL AIRPORTS ---")

    if not airports:

        print("No airports found.")
        return

    print(f"\nTotal airports: {len(airports)}\n")

    for number, airport in enumerate(airports, start=1):

        print(f"{number}. {airport['name']}")
        print(f"   City: {airport['city']}")
        print(f"   Country: {airport['country']}")
        print("-" * 30)


# ------------------------------------------
# 8. Search airport
# ------------------------------------------

def search_airport(airports):

    print("\n--- SEARCH AIRPORT ---")

    if not airports:

        print("No airports available.")
        return

    search = get_required_input(
        "Enter airport name: "
    )

    found = False

    for airport in airports:

        if search.lower() in airport["name"].lower():

            print("\nAirport found!")
            print(f"Name: {airport['name']}")
            print(f"City: {airport['city']}")
            print(f"Country: {airport['country']}")

            found = True

    if not found:

        print("\nNo airport matched your search.")


# ------------------------------------------
# 9. Generate report
# ------------------------------------------

def generate_report(airports):

    print("\n--- GENERATE REPORT ---")

    if not airports:

        print("No airports available to generate a report.")
        return

    report_file = "airport_report.txt"

    with open(report_file, "w") as file:

        file.write("=" * 40 + "\n")
        file.write("       AIRPORT MANAGEMENT REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Total Airports: {len(airports)}\n\n")

        for number, airport in enumerate(airports, start=1):

            file.write(f"{number}. {airport['name']}\n")
            file.write(f"   City: {airport['city']}\n")
            file.write(f"   Country: {airport['country']}\n")
            file.write("-" * 30 + "\n")

    print(f"\nReport generated successfully!")
    print(f"File: {report_file}")


# ------------------------------------------
# 10. Find airport by exact name
# ------------------------------------------

def find_airport(airports, name):

    for airport in airports:

        if airport["name"].lower() == name.lower():

            return airport

    return None


# ------------------------------------------
# 11. Update airport
# ------------------------------------------

def update_airport(airports):

    print("\n--- UPDATE AIRPORT ---")

    if not airports:

        print("No airports available.")
        return

    name = get_required_input(
        "Enter airport name to update: "
    )

    airport = find_airport(airports, name)

    if airport is None:

        print("Airport not found.")
        return

    print("\nCurrent information:")
    print(f"Name: {airport['name']}")
    print(f"City: {airport['city']}")
    print(f"Country: {airport['country']}")

    print("\nEnter the new information.")

    new_name = get_required_input(
        "New airport name: "
    )

    # Check if the new name belongs to another airport
    if new_name.lower() != airport["name"].lower():

        if airport_exists(airports, new_name):

            print("Another airport already uses that name.")
            return

    new_city = get_required_input(
        "New city: "
    )

    new_country = get_required_input(
        "New country: "
    )

    airport["name"] = new_name
    airport["city"] = new_city
    airport["country"] = new_country

    save_airports(airports)

    print("\nAirport updated successfully!")


# ------------------------------------------
# 12. Delete airport
# ------------------------------------------

def delete_airport(airports):

    print("\n--- DELETE AIRPORT ---")

    if not airports:

        print("No airports available.")
        return

    name = get_required_input(
        "Enter airport name to delete: "
    )

    airport = find_airport(airports, name)

    if airport is None:

        print("Airport not found.")
        return

    print("\nAirport found:")
    print(f"Name: {airport['name']}")
    print(f"City: {airport['city']}")
    print(f"Country: {airport['country']}")

    confirmation = input(
        "\nAre you sure you want to delete this airport? (y/n): "
    ).strip().lower()

    if confirmation == "y":

        airports.remove(airport)

        save_airports(airports)

        print("\nAirport deleted successfully!")

    else:

        print("\nDelete operation cancelled.")


# ------------------------------------------
# 13. Main application
# ------------------------------------------

def main():

    # Load saved data
    airports = load_airports()

    print("\nWelcome to Airport Management System!")

    while True:

        display_menu()

        choice = input(
            "Choose an option (1-7): "
        ).strip()

        if choice == "1":

            add_airport(airports)

        elif choice == "2":

            view_airports(airports)

        elif choice == "3":

            search_airport(airports)

        elif choice == "4":

            generate_report(airports)

        elif choice == "5":

            update_airport(airports)

        elif choice == "6":

            delete_airport(airports)

        elif choice == "7":

            print("\nThank you for using Airport Management System.")
            print("Goodbye!")

            break

        else:

            print(
                "\nInvalid choice. "
                "Please enter a number between 1 and 7."
            )


# ------------------------------------------
# Program entry point
# ------------------------------------------

if __name__ == "__main__":
    main()