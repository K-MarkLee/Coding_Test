import sys
n,m=map(int,sys.stdin.readline().split())
list=list(range(1,n+1))
for _ in range(m):
    i,j=map(int,sys.stdin.readline().split())
    list[i-1:j] = list[i-1:j][::-1]
print(*list)