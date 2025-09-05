import sys
num = list(map(int,sys.stdin.readline().strip().split()))

for i in range(1,3):
    num[i+1] = abs(num[i-1]-num[i+1])

num.sort()
print(num[0])
   

