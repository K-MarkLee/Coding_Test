import sys
n,m=map(int,sys.stdin.readline().split())
a=[0]*n
for b in range(m):
    i,j,k=map(int,sys.stdin.readline().split())
    for c in range(i-1,j):
        a[c]=k
print(' '.join(map(str, a)))
        