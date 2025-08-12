import sys
N, B = sys.stdin.readline().strip().split()
B = int(B)

result = 0
length = len(N)
area = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(length):
    NN = N[length - 1 - i]
    convert = area.index(NN)
    result += convert * (B ** i)

print(result)