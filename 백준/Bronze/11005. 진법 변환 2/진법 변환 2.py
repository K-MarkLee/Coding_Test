import sys
N, B = map(int,sys.stdin.readline().strip().split())
area = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = []
while True:
    x, y = divmod(N,B)
    result.append(y)
    N = x
    if N == 0:
        break
result = result[::-1]

for num in result:
    print(area[num], end='')