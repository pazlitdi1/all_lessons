def add(x: int, y: int):
    return x + y
print(add(3, 2))


def add_all(*args):
    print(args)
    print(type(args))

add_all(1, 5, 8)


def add_all(*args):
    summary = 0
    for i in args:
        summary += i
    return summary

print(add_all(1, 2, 3, 4, 5, 6))


def add_all_numbers(*args):
    summary = 0
    for i in args:
        summary += i
    return summary

values = [1, 2, 3, 4, 5]
other_values = [6, 7, 8, 9, 10]

print(add_all_numbers(*values, *other_values))


def introduce(**kwargs):
    print(kwargs)
    print(type(kwargs))

introduce(name="Mansur", age=16, city="Tashkent")


def introduce1(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
person = {
    "city": "Tashkent",
    "age": 16,
    "first_name": "Farzona",
}

introduce1(name="Farzona", age=16, city="Tashkent")


def introduce2(**kwargs):
    for key, value in kwargs.items():
        print(key)
        print(value)
person = {
    "city": "Tashkent",
    "age": 16,
    "first_name": "Farzona",
}

introduce2(**person)


def func_with_all_argument(x: int, y: int, *args, value: int = 6, **kwargs):
    print(x, y)
    print(args)
    print(value)
    print(kwargs)

person = {
    "city": "Tashkent",
    "age": 16,
    "first_name": "Farzona",
}

func_with_all_argument(1, 2, 3, 4, 5, **person)


def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True
    return old_dict, is_modified


product = {"id": 1, "name": "Lexus", "color": "black", "year": 2023, "price": 1223.99}
structure = modify_dict(old_dict=product, in_stock=True)
print(structure)
print(type(structure))


def modify_dict(old_dict: dict, **kwargs) -> tuple[dict, bool]:
    is_modified = False

    for key, value in kwargs.items():
        if old_dict.get(key) != value:
            old_dict[key] = value
            is_modified = True
    return old_dict, is_modified


product = {"id": 1, "name": "Lexus", "color": "black", "year": 2023, "price": 1223.99}
product, was_modified = modify_dict(old_dict=product, name="Lexus")
print(product)
print(was_modified)
