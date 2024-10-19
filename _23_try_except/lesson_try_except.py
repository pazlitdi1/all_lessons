def find_average(*, numbers: list) -> float:
    return sum(numbers) / len(numbers)


try:
    (find_average(numbers=[1, 2, 3]))
except ZeroDivisionError:
    print('The list is empty')
print("Were are here")