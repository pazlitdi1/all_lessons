squares = []

for i in range(10):
    squares.append(i**2)
print(squares)


squares_1 = [x ** 2 for x in range(20)]
print(squares_1)


even_squares = []
for x in range(10):
    if x % 2 == 0:
        even_squares.append(x ** 2)
print(even_squares)


even_squares_1 = [x ** 2 for x in range(14) if x % 2 == 0]
print(even_squares_1)
