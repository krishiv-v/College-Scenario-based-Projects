import csv
import sys

if len(sys.argv) != 2:
    print("Usage: python sports.py <filename>")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\nSports Equipment Inventory:")
        records = list(reader)

        for item in records:
            print(item)

        equipment_id = input("\nEnter Equipment ID to search: ")

        found = False

        for item in records:
            if item["Equipment ID"] == equipment_id:
                print("\nEquipment Found:")
                print(item)
                found = True
                break

        if not found:
            print("Equipment not found.")

except FileNotFoundError:
    print("File not found.")
