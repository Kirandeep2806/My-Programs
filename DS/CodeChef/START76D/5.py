for _ in range(int(input())):
    one=True
    for i in range(int(input())):
        if one:print(1,end=" ")
        else:print(2,end=" ")
        one=not one
    print()