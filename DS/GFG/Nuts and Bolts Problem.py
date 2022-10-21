#!/usr/bin/python3

class Solution:

    def matchPairs(self,nuts, bolts, n):
        l = {"!":0, "#":1, "$":2, "%":3, "&":4, "*":5, "@":6, "^":7, "~":8}
        res = [False]*9
        for i in nuts:
            res[l[i]] = i
        start = 0
        for i in res:
            if i:
                nuts[start] = i
                bolts[start] = i
                start += 1

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(nuts, bolts, n)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1
