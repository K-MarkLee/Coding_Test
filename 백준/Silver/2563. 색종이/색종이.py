import sys
num = int(sys.stdin.readline().strip())

result = 0
array = [[0]*100 for _ in range(100)]

for _ in range(num):
    n, m = map(int, sys.stdin.readline().strip().split())
    for i in range(n, n+10):
        for j in range(m, m+10):
            if array[i][j] == 0:
                array[i][j] = 1
                result += 1

print(result)