def sort_by_len(element: str) -> int:
    return len(element)
sort_by_len_labmda = lambda element: len(element)
print(sort_by_len("Banana"))
print(sort_by_len_labmda("Banana"))


fruits = ['apple', 'banana', 'cherry', 'limon', 'date', 'pineapple']
sorted_fruits = sorted(fruits, key=lambda element: len(element))
print(sorted_fruits)


fruits1 = ['apple', 'banana', 'cherry', 'limon', 'date', 'pineapple']
longest_word = max(fruits1, key=lambda element: len(element))
print(longest_word)