import sys
a, b, c = sorted(map(int,sys.stdin.read().strip().split()))

print(min(a+b+c, 2*(a+b)-1))