#!/usr/bin/python3

# Observe the pattern between the outputs of Transposing a matrix and this problem.

l = [[1,2,3], [4,5,6], [7,8,9]]
n = 3

# 1 2 3
# 4 5 6
# 7 8 9

# Transpose

# 1 4 7
# 2 5 8
# 3 6 9

# 90 Degree Rotation (default)

# 3 6 9
# 2 5 8
# 1 4 7

# 90 Degree Rotation (right)

# 7 4 1
# 8 5 2
# 9 6 3

# Approach

for i in range(n):
    for j in range(i+1, n):
        l[i][j], l[j][i] = l[j][i], l[i][j]
print(l[::-1])
