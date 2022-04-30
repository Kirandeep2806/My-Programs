for i in range(int(input())):
    a, b = list(map(int, input().split()))
    if (a > b and (not (a-b)%2)) or (a < b and (a-b)%2):
        print("1")
    elif (a > b and (a-b)%2) or (a < b and (not (a-b)%2)):
        print("2")
    else:
        print("0")