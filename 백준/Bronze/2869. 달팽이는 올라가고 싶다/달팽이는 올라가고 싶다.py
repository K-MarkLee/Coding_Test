import sys
A, B, V = map(int, sys.stdin.readline().strip().split())

day = A - B
total = V - A
if total <= 0:
    print(1)
else:
    days = total // day
    if total % day != 0:
        days += 1
    print(days + 1)