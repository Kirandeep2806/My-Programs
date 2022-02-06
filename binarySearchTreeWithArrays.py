#!/usr/bin/python3

a = [1,2,3]
h = len(a)-1
res = [None]*(2**(h+1)-1)

def findIndexOfInsertion(root, insertingElement):
    if res[root] is None:
        return root
    elif insertingElement > res[root]:
        return findIndexOfInsertion(2*root+2, insertingElement)
    return findIndexOfInsertion(2*root+1, insertingElement)

for i in a:
    res[findIndexOfInsertion(0, i)] = i

print(res)