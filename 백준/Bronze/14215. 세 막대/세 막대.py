import sys
num = list(map(int,sys.stdin.read().strip().split()))

if max(num)-(sum(num)-max(num)) < 0:
    print(sum(num))
else:
    print(sum(num)-(max(num)-(sum(num)-max(num)))-1)