import sys

N,M,*num_list=map(int,sys.stdin.read().strip().split())
result = 0
num_list.sort()

for i in range(N-2):
    pointer1 = i+1
    pointer2 = N-1
    
    while pointer1 < pointer2:
        sum_num = num_list[i]+num_list[pointer1]+num_list[pointer2]
        
        if sum_num <= M:
            if sum_num > result:
                result = sum_num
            pointer1 += 1
        else:
            pointer2 -= 1
            
        if result == M:
            print(result)
            sys.exit(0)
print(result)