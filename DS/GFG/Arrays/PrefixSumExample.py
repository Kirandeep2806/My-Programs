#!/usr/bin/python3

arr = list(map(int, input().split()))
n = len(arr)
prefixSumArr = [0]*n
prefixSumArr[0] = arr[0]

for i in range(1, n):
    prefixSumArr[i] = prefixSumArr[i-1] + arr[i]

# print(prefixSumArr)

l = int(input("Enter the l value : "))
r = int(input("Enter the r value : "))

if l!=0:
    res = prefixSumArr[r] - prefixSumArr[l-1]
else:
    res = prefixSumArr[l]
print(res)
