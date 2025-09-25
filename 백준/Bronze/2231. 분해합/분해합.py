N = int(input())
result = 0

for i in range(max(1, N - len(str(N)) * 9), N):
    s = i + sum(map(int, str(i)))
    if N == s:
        result = i
        break

print(result)