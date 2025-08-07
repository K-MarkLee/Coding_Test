import sys
N, M = map(int,sys.stdin.readline().strip().split())

array_1 = []
array_2 = []

for _ in range(N):
    array_1.append(list(map(int,sys.stdin.readline().strip().split())))
    
for _ in range(N):
    array_2.append(list(map(int,sys.stdin.readline().strip().split())))
    
for i in range(N):
    array_sum = []
    for j in range(M):
        array_sum.append(array_1[i][j] + array_2[i][j])
    print(*array_sum)