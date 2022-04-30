#!/usr/bin/python3

from collections import Counter

for i in range(int(input())):
    n = int(input())
    binaryString = input()
    frequency = Counter(binaryString)
    if len(frequency) == 1:
        print(1)
    else:
        if frequency["0"] == frequency["1"]:
            print(n)
        else:
            print(2*min(frequency["0"], frequency["1"])+1)
