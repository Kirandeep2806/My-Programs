#!/usr/bin/python3
class Solution:
    def countDistinct(self, A, N, K):
        res = []
        A_counter = {}
        count = 0
        for i in range(K):
            if A_counter.get(A[i], 0) == 0:
                A_counter[A[i]] = 1
                count += 1
            else:
                A_counter[A[i]] += 1
        res.append(count)
        for i in range(N-K):
            A_counter[A[i]] -= 1
            if A_counter[A[i]] == 0:
                count -= 1
            if A_counter.get(A[i+K], 0) == 0:
                A_counter[A[i+K]] = 1
                count += 1
            else:
                A_counter[A[i+K]] += 1
            res.append(count)
        return res

#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends