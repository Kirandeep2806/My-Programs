from collections import Counter
for _ in range(int(input())):
    res=0
    an,bn=map(int, input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=Counter(a)
    consecutives=1
    for i in range(1,bn):
        if b[i]==b[i-1]:
            consecutives+=1
        else:
            res+=(consecutives*c.get(b[i-1],0))
            consecutives=1
    if c.get(b[i],0):
        res+=(consecutives*c.get(b[i],0))

    print(res)
