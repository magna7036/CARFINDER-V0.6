# Script name: Project 0-6 
# Author Name: Jose-Abner Gonzalez
# Date of Latest Revision: 11/24/2024
# Purpose: CarFinder
# Note: "Test Passed"


import os

# file name for vehicles
allowed_vehicles_file = 'allowed_vehicles.txt'

# function list of vehicles 
def read_allowed_vehicles():
    if not os.path.exists(allowed_vehicles_file):
        return []
    with open(allowed_vehicles_file, 'r') as file:
        vehicles = [line.strip() for line in file]
    return vehicles

# function to write the list 
def write_allowed_vehicles(vehicles):
    with open(allowed_vehicles_file, 'w') as file:
        for vehicle in vehicles:
            file.write(vehicle + '\n')

# Function to print vehicles
def print_all_vehicles():
    print("\nThe AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles:
        print(vehicle)
    print()

# function for vehicle
def search_vehicle():
    search_vehicle = input("Please enter the full vehicle name: ").strip()
    if search_vehicle in allowed_vehicles:
        print(f"\n{search_vehicle} is an authorized vehicle.")
    else:
        print(f"\n{search_vehicle} is not an authorized vehicle. If you received this in error, please check the spelling and try again.")
    print()

# function to add vehicle
def add_vehicle():
    new_vehicle = input("Please enter the full vehicle name you would like to add: ").strip()
    if new_vehicle not in allowed_vehicles:
        allowed_vehicles.append(new_vehicle)
        write_allowed_vehicles(allowed_vehicles)
        print(f'\nYou have added "{new_vehicle}" as an authorized vehicle.')
    else:
        print(f'\n"{new_vehicle}" is already an authorized vehicle.')
    print()

# function to delete vehicle
def delete_vehicle():
    remove_vehicle = input("Please enter the full vehicle name you would like to REMOVE: ").strip()
    if remove_vehicle in allowed_vehicles:
        confirm = input(f'Are you sure you want to remove "{remove_vehicle}" from the Authorized Vehicles List? (yes/no): ').strip().lower()
        if confirm == 'yes':
            allowed_vehicles.remove(remove_vehicle)
            write_allowed_vehicles(allowed_vehicles)
            print(f'\nYou have REMOVED "{remove_vehicle}" as an authorized vehicle.')
        else:
            print(f'\n"{remove_vehicle}" was not removed.')
    else:
        print(f'\n"{remove_vehicle}" is not an authorized vehicle.')
    print()

# load the list vehicles from file
allowed_vehicles = read_allowed_vehicles()

# if file is empty, initialize default list
if not allowed_vehicles:
    allowed_vehicles = [
        'Ford F-150', 
        'Chevrolet Silverado', 
        'Tesla CyberTruck', 
        'Toyota Tundra', 
        'Rivian R1T', 
        'Ram 1500'
    ]
    write_allowed_vehicles(allowed_vehicles)

# main loop to display the menu
while True:
    print("""
********************************
AutoCountry Vehicle Finder v0.5
********************************
Please enter the following number below from the following menu:

1. PRINT all Authorized Vehicles
2. SEARCH for Authorized Vehicle
3. ADD Authorized Vehicle
4. DELETE Authorized Vehicle
5. Exit
""")
    
    choice = input("Enter your choice: ").strip()
    
    if choice == '1':
        print_all_vehicles()
    elif choice == '2':
        search_vehicle()
    elif choice == '3':
        add_vehicle()
    elif choice == '4':
        delete_vehicle()
    elif choice == '5':
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.\n")
