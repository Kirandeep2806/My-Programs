#!/usr/bin/env python3

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
