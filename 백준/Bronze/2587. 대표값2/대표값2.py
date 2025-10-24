import sys
L = list(map(int,sys.stdin.read().strip().split()))

print(f"{sum(L)//5}\n{sorted(L)[2]}")

