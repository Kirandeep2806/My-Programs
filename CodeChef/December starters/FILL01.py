'''
3
4 1
1010
4 2
0100
11 3
00100000001
'''

n = int(input())
for i in range(n):
    l = list(map(int, input().split()))
    s = input()
    counter = 0
    res = 0
    iter = 0
    while counter < l[0]:
        if s[counter] == '0':
            iter += 1
        else:
            res += (iter//l[1])
            iter = 0
        counter += 1
    if iter:
        res += (iter//l[1])
    print(res)
