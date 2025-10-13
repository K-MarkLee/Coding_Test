import sys
N = int(sys.stdin.read().strip())
result = -1
for i in range(N//3+1):
    a, b = divmod(N-3*i,5)
    if b == 0 :
        result = a+i
        break
print(result)
        