import sys

T = int(sys.stdin.readline())
for i in range(T):
    n = int(sys.stdin.readline())
    if n&1:
        sys.stdout.write("-1\n")
    else:
        sys.stdout.write("10"*(n//2)+"\n")