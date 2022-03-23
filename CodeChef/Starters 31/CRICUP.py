for i in range(int(input())):
    x,y,d = list(map(int,input().split()))
    if abs(x-y) <= d:
        print("YES")
    else:
        print("NO")

