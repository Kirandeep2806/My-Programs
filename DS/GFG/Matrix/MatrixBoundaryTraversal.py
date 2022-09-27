#!/usr/bin/python3

n = int(input("Enter the matrix that you want : "))
arr = [[i for i in range(j, j+n)] for j in range(1, n**2+1, n)]

print(arr)
