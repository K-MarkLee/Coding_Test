import sys
n,m = map(int,sys.stdin.readline().strip().split())
num = list(map(int,sys.stdin.readline().strip().split()))

result = 0
found = False

for i in range(n):
    if found:
        break
    for j in range(i+1,n):
        if found:
            break
        for k in range(j+1,n):
            sum = num[i]+num[j]+num[k]
            if sum == m:
                print(m)
                found = True
                break
            elif sum > result and sum <= m:
                result = sum
if not found:
    print(result)