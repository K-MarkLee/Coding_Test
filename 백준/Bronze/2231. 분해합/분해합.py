N = int(input())
result = 0

for i in range(1,N):
    sum_num = i + sum(map(int,str(i)))
    if sum_num == N:
        result = i
        break
        
print(result)