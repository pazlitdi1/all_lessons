"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Индексы Слайсы >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""

fruits = ['apple', 'orange', 'pear', 'pineapple', 'banana']
print(fruits[4])

fruits = ['apple', 'orange', 'pear', 'pineapple', 'banana']
fruits[0] = "cherry"
print(fruits)

fruits = ['apple', 'orange', 'pear', 'pineapple']
fruits[0], fruits[3] = fruits[3], fruits[0]
print(fruits)


numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:5])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:5]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[0:len(numbers)]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[::2]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[0:20])

string = "Hello lazy developer"
print(string[::2])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = numbers[::-1]
print(new_numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
new_numbers = list(reversed(numbers))
print(type(new_numbers))
print(new_numbers)
