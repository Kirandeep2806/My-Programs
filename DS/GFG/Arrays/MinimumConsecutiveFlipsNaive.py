#!/usr/bin/python3

arr = list(map(int, input().split()))
d = {0: 0, 1: 0}

d[arr[0]] += 1

for i in range(1, len(arr)):
    if arr[i] != arr[i-1]:
        d[arr[i]] += 1

minFlips = min(d[0], d[1])
flipNumber = 0
if minFlips == d[1]:
    flipNumber = 1
# print(flipNumber)
start = False
if arr[0] == flipNumber:
    print("From 0-", end="")
    start = True
for i in range(1, len(arr)):
    if arr[i-1] != arr[i]:
        if arr[i] == flipNumber:
            if start == False:
                print(f"From {i}-", end="")
                start = not start
        if arr[i-1] == flipNumber:
            if start == True:
                print(f"{i-1}")
                start = not start
if arr[len(arr)-1] == flipNumber and start == True:
    print(len(arr)-1)
    start = not start
