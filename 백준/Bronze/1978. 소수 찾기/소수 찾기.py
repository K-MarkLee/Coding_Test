import sys
N = int(sys.stdin.readline().strip())
result = 0

for i in range(N):
    num_list = list(map(int, sys.stdin.readline().strip().split()))
    
    for n in num_list:
        factors = []
        for j in range(1, n+1):
            if n % j == 0:
                factors.append(j)
        if len(factors) == 2:
            result += 1
print(result)
    