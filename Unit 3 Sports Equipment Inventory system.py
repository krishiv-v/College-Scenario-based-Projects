import csv
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    reader = csv.DictReader(file)
    records = list(reader)

print("Sports Equipment Inventory:")

for record in records:
    print(record)

equipment_id = "S103"

print("\nSearching for Equipment ID:", equipment_id)

for record in records:
    if record["Equipment ID"] == equipment_id:
        print("Equipment Found:")
        print(record)
        break
else:
    print("Equipment not found.")
