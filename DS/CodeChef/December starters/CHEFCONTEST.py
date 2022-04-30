n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    chef = l[0] + l[2]*10
    chefina = l[1] + l[3]*10
    if chef < chefina:
        print("Chef")
    elif chef > chefina:
        print("Chefina")
    else:
        print("Draw")