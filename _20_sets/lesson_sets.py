my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))


my_set_1 = set()
for i in range(10):
    my_set_1.add(i)
print(my_set_1)


my_set_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set_2.remove(5)
print(my_set_2)


your_set = {1, 2, 3, 5}
your_set.add(2)
print(your_set)


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}
print(set1.union(set2))


set1 = {1, 2, 3, 4, 5}
set2 = {1, 2, 3, 4, 5}
union_set = set1.union(set2)
print(list(union_set))


set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
print(set3.intersection(set4))


set3 = {1, 2, 3, 4}
set4 = {3, 4, 5, 6}
print(set3.difference(set4))


squares = {x ** 2 for x in range(10)}
print(squares)


numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]
unique = list(set(numbers))
print(type(unique))
print(unique)
unique = list(numbers)
print(unique)


numbers = [1, 2, 2, 3, 3, 4, 4, 5, 6, 6, 7, 7, 8, 8, 9]
unique_numbers = list(set(numbers))
print(unique_numbers)
print(type(unique_numbers))