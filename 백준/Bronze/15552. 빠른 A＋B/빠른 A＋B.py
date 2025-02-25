import sys

a = int(sys.stdin.readline())
result = []

for i in range(a):
    b, c = map(int, sys.stdin.readline().strip().split())
    result.append(str(b + c))

# 한 번에 출력
sys.stdout.write("\n".join(result))
