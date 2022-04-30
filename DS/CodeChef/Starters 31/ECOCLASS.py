for i in range(int(input())):
    n = int(input())
    s = list(map(int,input().split()))
    d = list(map(int,input().split()))
    count = 0
    for i,j in zip(s,d):
        if i == j:
            count += 1
    print(count)

