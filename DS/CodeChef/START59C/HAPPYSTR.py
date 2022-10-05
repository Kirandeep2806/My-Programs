#!/usr/bin/python3

    
vowels = {'a', 'e', 'i', 'o', 'u'}
for i in range(int(input())):
    arr = input()
    count = 0
    flag = False
    for j in range(len(arr)):
        if j!=len(arr)-1:
            if (arr[j] in vowels) and (arr[j+1] in vowels):
                count += 1
                if count > 2:
                    flag = True
                    break
            elif (arr[j] in vowels):
                count += 1
                if count > 2:
                    flag = True
                    break
                count = 0
        else:
            if arr[j] in vowels:
                count += 1
                if count > 2:
                    flag = True
                    break

    if flag:
        print("Happy")
    else:
        print("Sad")
