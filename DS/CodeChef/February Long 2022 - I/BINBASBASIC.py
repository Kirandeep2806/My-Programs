#!/usr/bin/python3

for i in range(int(input())):
    n, k = list(map(int, input().split()))
    binaryString = input()
    count = 0
    for i in range(n//2):
        if binaryString[i] != binaryString[n-i-1]:
            count += 1
    if k == count:
        print("YES")
    elif count <= k and (k-count)%2 == 0:
        print("YES")
    elif n%2 == 1 and count <= k:
        print("YES")
    else:
        print("NO")
