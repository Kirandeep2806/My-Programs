#!/usr/bin/python3

for i in range(int(input())):
    mean, median = list(map(int, input().split()))
    l = [0, 0, 0]
    l[1] = median
    pendingRes = mean*3-median
    if pendingRes < median:
        if median < 0:
            l[0] = median
            pendingRes -= median
            l[2] = pendingRes
        else:
            l[2] = median
            pendingRes -= median
            l[0] = pendingRes
    else:
        if median < 0:
            l[0] = median
            pendingRes -= median
            l[2] = pendingRes
        else:
            l[2] = median
            pendingRes -= median
            l[0] = pendingRes
    print(*l)
