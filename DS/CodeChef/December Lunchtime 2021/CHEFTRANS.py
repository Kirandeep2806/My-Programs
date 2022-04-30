for i in range(int(input())):
    l = [int(i) for i in input().split()]
    if l[0] + l[1] < l[2]:
        print("PLANEBUS")
    elif l[0] + l[1] > l[2]:
        print("TRAIN")
    else:
        print("EQUAL")
