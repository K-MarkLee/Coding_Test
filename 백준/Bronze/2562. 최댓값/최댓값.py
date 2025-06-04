import sys
a = list(map(int,sys.stdin.read().split()))
b=max(a)
print(b)
print(a.index(b)+1)
    