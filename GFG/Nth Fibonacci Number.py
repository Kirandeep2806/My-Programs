#!/usr/bin/python3

#User function Template for python3

class Solution:
    def nthFibonacci(self, n, mem={}):
        if mem.get(n, 0) != 0:
            return mem[n]
        if n <= 1:
            mem[n] = n
            return n
        mem[n] = (self.nthFibonacci(n-1, mem) + self.nthFibonacci(n-2, mem))%1000000007
        return mem[n]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.nthFibonacci(n))
# } Driver Code Ends
