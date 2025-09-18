import sys
a1,a0,c,n0 = map(int,sys.stdin.read().strip().split())

if a1<=c and (a1*n0)+a0 <= n0*c :
    print(1)
else:
    print(0)