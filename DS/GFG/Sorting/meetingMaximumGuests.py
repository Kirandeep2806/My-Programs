#!/usr/bin/python3

arr = list(map(int, input().split()))
dept = list(map(int, input().split()))

arr.sort()
dept.sort()

n = arr.__len__()

maxMeetCount = 1
i = 1
j = 0

logBookCount = 1

while i < n and j < n:
    if arr[i] <= dept[j]:
        logBookCount += 1
        i += 1
    else:
        logBookCount -= 1
        j += 1
    maxMeetCount = max(logBookCount, maxMeetCount)

print(maxMeetCount)
