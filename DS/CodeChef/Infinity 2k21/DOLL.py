from typing import Counter


n = int(input())
for i in range(n):
    peopleAndHeight = [int(i) for i in input().split()]
    count = 0
    for j in [int(i) for i in input().split()]:
        if j > peopleAndHeight[1]:
            count += 1
    print(count)
