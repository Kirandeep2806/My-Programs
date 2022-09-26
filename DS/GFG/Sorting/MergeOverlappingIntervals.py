#!/usr/bin/python3

# arr = [[1,3],[2,4],[5,7],[6,8]]
arr = [[7,9],[6,10],[4,5],[1,3],[2,4]]
a = [i[0] for i in arr]
b = [i[1] for i in arr]
n = len(arr)

a.sort()
b.sort()

logs = 0
count = 0

i = 0
j = 0
res = []
consideredI = False
temp = []
temp.append(a[i])
# print(a[i])

while i<n and j<n:
    count += 1
    if a[i] <= b[j]:
        logs += 1
        i += 1
    else:
        logs -= 1
        j += 1
    if logs == 0:
        temp.append(b[j-1])
        # print(b[j-1])
        res.append(temp)
        # print(a[i])
        temp = []
        temp.append(a[i])
else:
    # print(b[n-1])
    temp.append(b[n-1])
    res.append(temp)

print(res)
