from math import ceil

for i in range(int(input())):
    row, seats = list(map(int, input().split()))
    print(ceil(row/2) * ceil(seats/2))