import csv

file = open("files/persons.csv", "r")
csv_dict_reader = csv.DictReader(file)

for row in csv_dict_reader:
    print(row["name"], row["age"], row["occupation"])
file.close()

with open("persons.csv", "r") as file:
    csv_dict_reader = csv.DictReader(file)

    for row in csv_dict_reader:
        print(row["name"], row["age"], row["occupation"])
file.close()