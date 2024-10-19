person = {
    "name": "Mansur",
    "age": "16",
    "city": "Parkent",
}
person["job"] = "Software Engineer"
print(person)


person = {}

person["name"] = "Mansur"
person["age"] = 16
person["city"] = "New York"

print(person.get("country", "UZB"))
print(person.get("name", "Fayoz"))


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}

for i in person:
    print(person[i])


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}

for item in person.items():
    key, value = item
    print(item)
    print(key)
    print(value)
    print(type(item))


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}

for key, value in person.items():
    print(key)
    print(value)

person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}

for key in person.keys():
    print(key)


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}

for value in person.values():
    print(value)


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}
new_person = {
    "city": "Tashkent",
    "age": 16,
    "name": "Mansur",
}
print(person == new_person)


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}
additional_person_info = {
    "job": "Software Engineer",
    "married": False,
    "city": "London"
}

person.update(additional_person_info)
print(person)


person = {
    "name": "Mansur",
    "age": 16,
    "city": "Tashkent",
}
additional_person_info = {
    "job": "Software Engineer",
    "married": False,
    "city": "London"
}

person = person | additional_person_info
print(person)
