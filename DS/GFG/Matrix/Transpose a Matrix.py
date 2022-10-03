#!/usr/bin/python3

l = [[1,2,3], [4,5,6], [7,8,9]]
n = 3

for i in range(n):
    for j in range(i+1, n):
        l[i][j], l[j][i] = l[j][i], l[i][j]
print(l)

# 1 2 3
# 4 5 6
# 7 8 9

# 1 4 7
# 2 5 8
# 3 6 9
