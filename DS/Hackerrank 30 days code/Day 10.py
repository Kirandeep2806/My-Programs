#!/bin/python3

if __name__ == '__main__':
    n = int(input().strip())
    maxOnes = 0
    count = 0
    while n!=0:
        if n&1 and n&2:
            count += 1
        else:
            if n&1:
                count += 1
                if count > maxOnes:
                    maxOnes = count
                count = 0
        n >>= 1
    print(maxOnes)
