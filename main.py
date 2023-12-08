import os
os.system("cls")
import csv

# Create a new CSV file with some data
with open('file.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age', 'city']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'John Smith', 'age': 30, 'city': 'New York'})
    writer.writerow({'name': 'Lisa Johnson', 'age': 25, 'city': 'San Francisco'})
    
# Read data from the CSV file
with open('file.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'], row['city'])

# Append data to the CSV file
with open('file.csv', 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'name': 'Sajjad', 'age': 22, 'city': 'Chicago'})

# Change data in the CSV file
with open('file.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    rows = list(reader)

with open('file.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in rows:
        if row['name'] == 'John Smith':
            row['age'] = 31
        elif row['name'] == "Sajjad":
            row['age'] = 21
        writer.writerow(row)
        