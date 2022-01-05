for i in range(int(input())):
    l = list(map(int, input().split()))
    if sum(l[1:]) > l[0]:
        print("NO")
    else:
        print("YES")