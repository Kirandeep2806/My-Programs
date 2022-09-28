#!/usr/bin/python3

from math import log2

for _ in range(int(input())):
    l = list(map(int, input().split()))
    maxElement = max(l)
    minElement = min(l)
    maxElementLog = log2(maxElement)
    temp = int(maxElementLog//log2(minElement))
    if pow(minElement, temp)==maxElement:
        print("YES")
    else:
        if maxElement%minElement==0:
            q = maxElement//minElement
            expectedPower = int(maxElementLog//log2(q))
            if pow(q, expectedPower)==maxElement:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
