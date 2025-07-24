import sys
c=[1,1,2,2,2,8]
n=list(map(int, sys.stdin.readline().strip().split()))
result = [ci-ni for ci, ni in zip(c,n)]
print(*result)