#!/usr/bin/python3

arr = list(map(int, input().split()))
n = len(arr)
targetSum = int(input())

prefixSum = []
s = set()
found = False

prefixSum.append(arr[0])
s.add(arr[0])

if targetSum == prefixSum:
    found = True
else:
    for i in range(1, n):
        curPrefixSum = prefixSum[i-1] + arr[i]
        prefixSum.append(curPrefixSum)
        if (curPrefixSum-targetSum) in s or (curPrefixSum-targetSum)==0:
            found = True
            break
        s.add(curPrefixSum)
if found:
    print("Yes")
else:
    print("No")
print(prefixSum)
