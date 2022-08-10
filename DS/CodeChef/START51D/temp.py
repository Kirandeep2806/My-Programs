#!/usr/bin/python3

def perm(arr, l, r):
    if l == r-1:
        # print(arr)
        auxArr = []
        for i in range(len(arr)):
            if i%2 == 0: # Odd
                auxArr.append(arr[i//2])
            else: # Even
                auxArr.append((arr[i//2] + arr[i//2-1])//2)
        # print(*auxArr)
        for i in range(1, len(auxArr)):
            if auxArr[i] == auxArr[i-1]:
                break
        else:
            print(f"{auxArr} formed from {arr}")
    else:
        for i in range(l, r):
            arr[i], arr[l] = arr[l], arr[i]
            perm(arr, l+1, r)
            arr[i], arr[l] = arr[l], arr[i]


# inp = input()
listInp = list(map(int, input().split()))
perm(listInp, 0, len(listInp))
