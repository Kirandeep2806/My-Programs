#!/usr/bin/python3

# Pre-requisite : Brian Kerningam Algorithm

from math import log2

s = input("Enter a string : ")
n = len(s)

for i in range(2**n):
    res = ''
    while i>0: # Ex : i=011, i=010
        lastSetBit = i&(~(i-1)) # find the last set bit. => 001, 010
        res += s[int(log2(lastSetBit))] # fetch the character@lastSetBit. => res = 'a', res='ab'
        i = i&(i-1) # remove that particular last set bit and proceed until no bits are set. => i=010, i=000
    if res == '':
        print('Φ')
    else:
        print(res)
