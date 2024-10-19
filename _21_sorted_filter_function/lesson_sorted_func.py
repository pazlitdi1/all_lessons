# fruits = ['banana', 'apple', 'orange', 'pear', 'limon', 'pineapple']
# sorted_fruits = sorted(fruits)
# print(sorted_fruits)
# print(fruits)


# fruits = ['banana', 'apple', 'orange', 'pear', 'limon', 'pineapple']
# sorted_fruits = sorted(fruits, reverse=True)
# print(sorted_fruits)


# fruits = ['banana', 'apple', 'orange', 'pear', 'limon', 'pineapple']
# def sort_by_fruit(element: str) -> int:
#     return len(element)
# print(sort_by_fruit)
# print(type(sort_by_fruit))


# fruits = ['banana', 'apple', 'orange', 'pear', 'limon', 'pineapple']
# def sort_by_fruit(element: str) -> int:
#     return len(element)
# sorted_fruits = sorted(fruits, key=sort_by_fruit)
# print(sorted_fruits)


# people = [
#     {"name": "Mansur", "age": 16},
#     {"name": "Raxmatilla", "age": 16},
#     {"name": "Alina", "age": 16},
#     {"name": "Farzona", "age": 16},
# ]
# def sort_by_age(person: dict) -> int:
#     return person["age"]
# def sort_by_age_name(element: dict) -> tuple[str, int]:
#     return element["age"], element["name"]
# sorted_people = sorted(people, key=sort_by_age_name)
# print(sorted_people)
# sorted_people = sorted(people, key=sort_by_age)
# print(sorted_people)


# def is_even(n: int) -> bool:
#     return n % 2 == 0
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# filtered_numbers = list(filter(is_even, numbers))
# print(type(filtered_numbers))
# print(filtered_numbers)


peoples = [
    {"name": "Mansur", "age": 16},
    {"name": "Raxmatilla", "age": 16},
    {"name": "Alina", "age": 16},
    {"name": "Farzona", "age": 16},
]
def is_adult(person: dict) -> bool:
    return person["age"] >= 13
filtered_peoples = list(filter(is_adult, peoples))
print(filtered_peoples)