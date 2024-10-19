file_name = ["document.txt", "image.jpg", "document.pdf", "image.png"]
for file_name in file_name:
    print(file_name)

greeting = "Hello lazy developer"
for mans in greeting:
    print(mans)

greeting = "Hello lazy developer"
count_o = 0
for mans in greeting:
    if mans == "o":
        count_o += 1
        print(mans)
print(count_o)

students = ["Mansur", "Fayoz", "Raxmatilla", "Dimka", "Farzona", "Nodira", "Alina", "Alina2"]
for student in students:
    print(student)
    for mans in student:
        print(mans)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number % 2 == 0:
        continue
    print(number)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for number in numbers:
    if number == 10:
        break
    print(number)

range_object = range(10)
print(range_object)
numbers = list(range_object)
print(numbers)

my_range = range(1, 11)
print(list(my_range))

my_range = range(10, 1, -1)
print(list(my_range))

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for number in numbers:
    number += 1
print(numbers)

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(numbers)):
    print(numbers[i])

numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for i in range(len(numbers)):
    numbers[i] += 1
print(numbers)

greeting = "Hello, world !"
indexes = []
count = 0
for i in range(len(greeting)):
    if greeting[i] == "0":
        count += 1
        indexes.append(i)
print(count)
print(indexes)

greeting = "Hello my name is Mansur. I am 16 years old!"
indexes = []
count = 0
for i in range(len(greeting)):
    if greeting[i] == "a":
        count += 1
        indexes.append(i)
print(count)
print(indexes)

