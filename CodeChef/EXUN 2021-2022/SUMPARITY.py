for i in range(int(input())):
    n, a = list(map(int, input().split()))
    if a&1 and n&1:
        print("Odd")
    elif a&1 and (not n&1):
        print("Even")
    else:
        if n == 1 and (not a&1):
            print("Even")
        else:
            print("Impossible")
