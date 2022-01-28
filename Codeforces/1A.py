from math import ceil
n,m,a = list(map(int ,input().split()))
res = 0
getMax = max(m,n)
if a > getMax:
    print(1)
else:
    if a != 1:
        res += getMax//a+1 if(getMax%a and  getMax > a) else getMax//a
    else:
        res += getMax
    if m == n:
        if n > a:
            res *= ceil(n/a)
    elif m == getMax:
        if n > a:
            res *= ceil(n/a)
    else:
        if m > a:
            res *= ceil(m/a)
    print(res)
