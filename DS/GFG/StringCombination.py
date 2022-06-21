#!/usr/bin/python3

def combinations(string, l, r, n):
    if l == r-n:
        print(string[l:r])
        return
    else:
        for i in range(l, r):
            string[i], string[l] = string[l], string[i]
            combinations(string, l+1, r, n)

string = "ABCDEFGH"
string = list(string)
combinations(string, 0, len(string), 2)
