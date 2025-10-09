import sys
N = int(sys.stdin.read().strip())
result = []
i = 1

while len(result) < N:
    if '666' in str(i):
        result.append(i)
    i += 1

print(result[-1])