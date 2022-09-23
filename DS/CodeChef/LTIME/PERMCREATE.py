#!/usr/bin/python3

for i in range(int(input())):
    n = int(input())
    if n<=3:
        print("-1")
    else:
        evenCount = n//2
        oddCount = n - evenCount
        for i in range(2, evenCount*2+1, 2):
            print(i, end=" ")
        for j in range(1, oddCount*2, 2):
            print(j, end=" ")
        print()
