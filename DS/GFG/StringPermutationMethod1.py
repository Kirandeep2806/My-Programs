#!/usr/bin/python3

def permutations(string, l, r):
    if l == r:
        print(string)
    for i in range(l, r):
        string[l], string[i] = string[i], string[l]
        permutations(string, l+1, r)

srcString = "ABC"
string = list(srcString)
permutations(string, 0, len(string))
