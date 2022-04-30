#!/usr/bin/python3

# Given a list of numbers in which every number repeats for n-times but expect one number. Find that number

from math import log
from sys import maxsize
import sys

a = [2,2,6,1,1,4,5,2,5,1,5,4,4]
l = [0]*32

getMax = -maxsize-1

for i in a:
    incPos = 0
    if i > getMax:
        getMax = i
    while i!=0:
        if i&1:
            l[incPos] += 1
        i >>= 1
        incPos += 1
# Following is another O(n) time complexity and O(1) extra space method suggested by aj. We can sum the bits in the same positions for all the numbers and take modulo with 3. The bits for which sum is not multiple of 3, are the bits of number with single occurrence. 
# Let us consider the example array {5, 5, 5, 8}. The 101, 101, 101, 1000 
# Sum of first bits%3 = (1 + 1 + 1 + 0)%3 = 0; 
# Sum of second bits%3 = (0 + 0 + 0 + 0)%3 = 0; 
# Sum of third bits%3 = (1 + 1 + 1 + 0)%3 = 0; 
# Sum of fourth bits%3 = (1)%3 = 1; 

res = 0
n = 3 # How many times they are repeating

for i in range(int(log(getMax, 2))+1):
    if l[i]%n:
        res += 2**i

print(res)
