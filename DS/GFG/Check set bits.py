#!/usr/bin/python3

#User function Template for python3
class Solution:
    def isBitSet (self, N):
        if N == 0:
            return 0
        elif ((N+1)&N) == 0:
            return 1
        else:
            return 0

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.isBitSet(N))
