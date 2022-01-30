#!/usr/bin/python3

# Given a list of numbers in which every number repeats for n-times but expect one number. Find that number

a = [2,2,6,1,1,4,5,2,5,1,5,4,4]
l = [0]*32

for i in a:
    incPos = 0
    while i!=0:
        if i&1:
            l[incPos] += 1
        i >>= 1
        incPos += 1

res = 0
n = 3 # How many times they are repeating
for index, i in enumerate(l):
    if i%n:
        res += 2**index

print(res)
