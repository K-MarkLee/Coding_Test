import sys
n = int(sys.stdin.readline().strip())
print(4*(n*(n+1)//2) - 4*(n*(n-1)//2))