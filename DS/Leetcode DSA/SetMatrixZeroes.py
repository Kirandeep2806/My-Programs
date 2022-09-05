#!/usr/bin/python3

# matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
m = matrix.__len__()
n = matrix[0].__len__()

x = {}
y = {}

for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            x[i] = True
            y[j] = True

print(x, y)

for i in range(m):
    for j in range(n):
        if i in x or j in y:
            matrix[i][j] = 0

print(matrix)
