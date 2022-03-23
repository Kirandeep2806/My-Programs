#!/usr/bin/python3

for i in range(int(input())):
    I_counter = 0
    P_counter = 0
    count = 0
    I = input()
    P = input()
    while P_counter < len(P):
        if I_counter < len(I) and P[P_counter] == I[I_counter]:
            I_counter += 1
        else:
            count += 1
        P_counter += 1
    if I_counter == len(I):
        print(f"Case #{i+1}: {count}")
    else:
        print(f"Case #{i+1}: IMPOSSIBLE")
