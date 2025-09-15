import sys
a, b, c = sorted(map(int,sys.stdin.read().strip().split()))

print(2*(a+b)-1 if a+b<=c else a+b+c)