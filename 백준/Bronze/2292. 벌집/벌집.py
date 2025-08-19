import sys
n=int(sys.stdin.readline().strip())
area = 1
result = 1
while area < n:
    area += 6 * result
    result += 1
print(result)