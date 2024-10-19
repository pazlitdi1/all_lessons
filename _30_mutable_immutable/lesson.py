from copy import deepcopy

x = 42
y = x
print(id(x), id(y), x, y)
y += 1
print(id(x), id(y), x, y)


my_list = [1, 2, 3]
another_list = my_list
print(id(my_list), id(another_list), my_list, another_list)
another_list.append(4)
print(id(my_list), id(another_list), my_list, another_list)


list1 = [1, 2, 3]
list2 = list1
print(list1 is list2)


list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 is list2)
print(list1 == list2)


some_variable = True
print(some_variable is True)


some_variable = None
print(some_variable is None)


my_dict = {"x": 1, "y": 2}
another_dict = my_dict
another_dict["x"] = 100
print(my_dict)


my_dict = {"x": 1, "y": 2}
another_dict = my_dict.copy()
another_dict["x"] = 100
print(my_dict)
print(another_dict)


patient_data = {"heart_rate": [60, 61, 63, 60, 61]}
patient_data_copy = deepcopy(patient_data)
patient_data_copy["heart_rate"].append(63)
print(patient_data)
print(patient_data_copy)


def function_with_computations(*, lst: list[int]) -> list[int]:
    lst.clear()
    return lst


my_list = [1, 2]
my_list = function_with_computations(list=deepcopy(my_list))
print(my_list)


lst = [2, 3, 4]
for num in lst:
    print(num)
    lst.append(num ** 2)


lst = [2, 3, 4]
another_list = [i ** 2 for i in lst]
lst.extend(another_list)
print(lst)


numbers = [1, 3, 5, 4, 8, 6]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)
print(numbers)


numbers = [1, 3, 5, 4, 8, 6]
odd_numbers = []
for num in numbers:
    if num % 2 != 0:
        odd_numbers.append(num)
print(odd_numbers)