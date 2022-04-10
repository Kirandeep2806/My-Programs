#!/usr/bin/python3


#User function Template for python3

import sys

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        globalMax = -sys.maxsize-1
        localSum = 0
        for i in range(N):
            localSum += arr[i]
            if localSum > globalMax:
                globalMax = localSum
            if localSum < 0:
                localSum = 0
        return globalMax


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends