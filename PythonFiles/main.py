# Airport management system
file_name = 'airports.txt'
airports = []
# load airports from a file 
def load_airports():
    try:
        with open(file_name, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                parts = line.split()
                if len(parts) == 3:
                    # create airport dictionary
                    airport = {
                        "name": parts[0],
                        "city": parts[1],
                        "country": parts[2]
                    }
                # append airport to the list of airports
                airports.append(airport)
    except FileNotFoundError:
# file does not exist yet
        pass
        return airports

# save aiport to a file
def save_aiports(airports):
    with open(file_name, 'w') as file:
        for airport in airports:
            file.write(f"{airport['name']}| {airport['city']} | {airport['country']}")

# 3. Display menu
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

# validate text input
def validate_required_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print('Input cannot be empty. Please try again')

# 5. Check for duplicate airport
def airport_exists(airports, name):
    for airport in airports:
        if airport['name'] == name.lower():
            return True
        return False

# 6. Add airport
def add_aiport(airports):
    print("=== Add Airport ===")
    name = validate_required_input("Airport name: ")
    # prevent duplicate aiports
    if airport_exists(airports, name):
        print("An airport with the same name exists")
        return
    city = validate_required_input("City: ")
    country = validate_required_input("Country: ")
    # create airport dict
    new_airport = {
        "name": name,
        "city": city,
        "country": country
    }
    airports.append(new_airport)

    # save immediately
    save_aiports(airports)
    print("Airport added successfully")

    # View Airports
    def view_airports(airports):
        print("== All Airports ==")
        if not airports:
            print("No airport found")
            return
        for number, airport in enumerate(airports, start=1):
            print(f"{number}. {airport['name']}")
            print(f"    City: {airport['city']}")
            print(f"    Country: {airport['country']}")
            print("-" * 30)

# search airport
def search_airport(airports):
    print("== Search Airport ==")
    if not airports:
        print("No airport found")
        return
    for airport in airports:
        search = validate_required_input("Enter Airport name: ")
        found = False
        for airport in airports:
            if search.lower() in airports['name'].lower():
                print("Airport found")
                print(f"Name: {airport['name']}")
                print(f"City: {airport['city']}")
                print(f"Country: {airport['country']}")
            found = True
    if not found:
        print("No airport was found")

# generate report
def generate_report(airports):
    print("== Generate Report ==")
    if not airports:
        print("No airport available to generate report")
        return
    report_file = "airport_report.txt"
    with open(report_file, 'w') as file:
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