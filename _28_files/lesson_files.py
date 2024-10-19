import json
import csv

data = {"name": "Mansur", "age": 30, "city": "Uzbekistan"}
file = open("files/data.json", "w")
json.dump(data, file, indent=4)
file.close()


file = open("files/data.json", "r")
loaded_data = json.load(file)
file.close()
print(loaded_data)


rows = [['name', 'age', 'occupation'],
        ['Mansur', 16, 'Engineer'],
        ['Raxmatilla', 16, 'Fronted developer'],
        ['Dima', 16, 'Fronted developer'],
        ['Alina', 16, 'Doctor'],

]
file = open("files/persons.csv", "w")
csv_writer = csv.writer(file)
csv_writer.writerow(rows)
file.close()


file = open("files/persons.csv", "r")
csv_dict_reader = csv.DictReader(file)
for row in csv_dict_reader:
        print(row["name"], row["age"], row["occupation"])
file.close()


persons = [
        {"name": "Mansur", "age": 16, "occupation": "Uzbekistan"},
        {"name": "Farzona", "age": 16, "occupation": "Uzbekistan"},
]
file = open("files/persons.csv", "a")
fields = ['name', 'age', 'occupation']
csv_dict_writer = csv.DictWriter(file, fieldnames=fields)
csv_dict_writer.writerows(persons)

file.close()