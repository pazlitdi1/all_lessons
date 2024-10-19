"""<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Списки (list) >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"""
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

my_list1 = [1, 2, 3]
my_list2 = [1, 3, 2]
my_list3 = [1, 2, 3]
print(my_list1 == my_list2)
print(my_list1 == my_list3)

fruits = ['apple', 'orange', 'pear', 'banana']
print("banana" in fruits)
print("watermelon" in fruits)

element1 = "apple"
element2 = "banana"
element3 = "cherry"
fruits = [element1, element2, element3]
print(fruits)

word = "Mansur"
my_list = list(word)
print(my_list)

my_list1 = [1, 2, 3]
my_list2 = [4, 5, 6]
my_list3 = my_list1 + my_list2
print(my_list3)

my_list1 = "Mansur"
my_list2 = "Pazlitdinov"
my_list3 = my_list1 + my_list2
my_list4 = list(my_list3)
print(my_list4)

fruits = ["apple", "orange", "pear", "banana"]
fruits.append("limon")
print(fruits)

my_sting = "Hello lazy developer"
new_sting = my_sting.replace("lazy", "intelligent")
print(my_sting)
print(new_sting)

fruits = ["apple", "orange", "pear", "banana"]
fruit = fruits.pop()
print(fruit)
print(fruits)

fruits = ["apple", "orange", "pear", "banana"]
fruits2 = ["fig", "limon"]
fruits.extend(fruits2)
print(fruits)

fruits = ['apple', 'orange', 'pear', 'banana']
fruits.reverse()
print(fruits)

my_list = [5, 4, 2, 3, 9, 10, 1, 11, 32, 6, 7, 8]
my_list.sort(reverse=True)
print(my_list)

my_list = [5, 4, 2, 3, 9, 10, 1, 11, 32, 6, 7, 8]
my_list.sort()
print(my_list)

my_string = "My name is Mansur"
my_list = my_string.split(" ")
print(my_list)
joined_string = " ".join(my_list)
print(joined_string)

my_list = [5, 4, 2, 3, 9, 10, 1, 11, 13, 6, 7, 8, 14]
print(max(my_list))
print(min(my_list))
print(sum(my_list))
