for i in range(int(input())):
    max = 0
    for j in range(3):
        pop, coke = list(map(int, input().split()))
        if pop + coke > max:
            max = pop + coke
    print(max)
