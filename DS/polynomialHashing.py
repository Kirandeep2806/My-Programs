#!/usr/bin/python3

s = input("Enter String : ")
target = input("Enter Target : ")
if len(target) > len(s):
    print("No Match Found")
else:
    h = []
    p = []
    a = 31
    b = 10**9+7
    targetHash = 1
    found = False
    for i in range(len(target)):
        if i == 0:
            targetHash = ord(target[i])
        else:
            targetHash = (targetHash*a+ord(target[i]))%b

    for i in range(len(s)):
        if i == 0:
            h.append(ord(s[0]))
            p.append(1)
        else:
            h.append((h[i-1]*a + ord(s[i]))%b)
            p.append((p[i-1]*a)%b)

    else:
        for i in range(0, len(s) - len(target) + 1):
            start = i
            end = i + len(target) - 1
            if start == 0:
                if h[end] == targetHash:
                    print(f"Match Found {start}-{end}")
                    found = True
            else:
                currHash = (h[end] - h[start-1]*p[end-start+1])%b
                if currHash == targetHash:
                    print(f"Match Found {start}-{end}")
                    found = True

    if not found:
        print("No Match Found")
