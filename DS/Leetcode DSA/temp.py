from sys import stdin
from collections import defaultdict
def compute(n,memset):
    if n<12:
        return n
    if n in memset:
        return memset[n]
    memset[n]=max(n,compute(n//2,memset)+compute(n//3,memset)+compute(n//4,memset))
    return memset[n]

for n in stdin:
  print(compute(int(n),defaultdict(lambda:-1)))
