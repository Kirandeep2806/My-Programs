#!/usr/bin/python3

from collections import defaultdict

def returnTrue():
    return True
for tc in range(int(input())):
    count = 0
    trackMap_x = defaultdict(returnTrue)
    trackMap_y = defaultdict(returnTrue)
    for N in range(int(input())):
        x,y = list(map(int, input().split()))
        if trackMap_x[x]:
            trackMap_x[x] = False
            count += 1
        if trackMap_y[y]:
            trackMap_y[y] = False
            count += 1
    print(count)
