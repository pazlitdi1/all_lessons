labelled_numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        labelled_numbers.append("even")
    else:
        labelled_numbers.append("odd")
print(labelled_numbers)


numbers_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
labelled_numbers = ["even" if number % 2 == 0 else "odd" for number in numbers_1]
print(labelled_numbers)


square_dict = {x: x ** 2 for x in range(10)}
print(square_dict)


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose_matrix = []
for i in range(len(matrix)):
    transpose_row = []
    for row in matrix:
        transpose_row.append(row[i])
    transpose_matrix.append(transpose_row)
# print(transpose_matrix)
transpose_matrix = [[row[i] for row in matrix] for i in range(len(matrix))]
print(transpose_matrix)
