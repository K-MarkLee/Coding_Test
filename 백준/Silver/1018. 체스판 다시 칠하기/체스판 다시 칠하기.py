import sys

N, M = map(int,sys.stdin.readline().strip().split())
num = [sys.stdin.readline().strip() for _ in range(N)]

wb = ["WBWBWBWB","BWBWBWBW"]*4
bw = ["BWBWBWBW","WBWBWBWB"]*4
result = 64

for i in range(N-7):
    for j in range(M-7):
        wb_count = 0
        bw_count = 0
        for x in range(8):
            for y in range(8):
                if num[i+x][j+y] != wb[x][y]:
                    wb_count += 1
                if num[i+x][j+y] != bw[x][y]:
                    bw_count += 1
                    
        result = min(wb_count, bw_count, result)

print(result)
            