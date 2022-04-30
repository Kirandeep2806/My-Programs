import sys

n = int(input())
for i in range(n):
    t = int(input())
    min = sys.maxsize
    sum = 0
    for j in [int(k) for k in input().split()]:
        if min > j:
            min = j
        sum += j
    print(sum - min)
