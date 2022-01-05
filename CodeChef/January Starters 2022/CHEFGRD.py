for i in range(int(input())):
    n, row, col = list(map(int, input().split()))
    print((row+col)%2)