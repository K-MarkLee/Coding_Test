import sys

a = int(sys.stdin.readline())
result = []

for _ in range(a):
    b, c = map(int, sys.stdin.readline().strip().split())
    result.append(str(b + c))

sys.stdout.write("\n".join(result) + "\n")
