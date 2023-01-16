#!/usr/bin/python3

from collections import defaultdict

n=int(input())
l=[]
for i in range(n):
	l.append(int(input()))
k=int(input())

res=-1
d=defaultdict(int)
t=set()
summ=0
for i in range(k):
	summ+=l[i]
	d[l[i]]+=1
	if d[l[i]]>1:
		t.add(l[i])

if len(t)==0:
	res=summ

for i in range(k, n):
	d[l[i-k]]-=1
	if d[l[i-k]]<2 and (l[i-k] in t):
		t.discard(l[i-k])
	summ-=l[i-k]

	d[l[i]]+=1
	if d[l[i]]>1:
		t.add(l[i])
	summ+=l[i]

	if len(t)==0:
		res=max(res, summ)

print(res)
