import sys
a=set()
for b in range(10):
    n = int(sys.stdin.readline())
    a.add(n % 42)
print(len(a))
    