import sys
arr = [list(map(int,sys.stdin.readline().strip().split())) for _ in range(9)]

result = arr[0][0]
max_row, max_col = 0, 0
for i in range(9):
    for j in range(9):
        if arr[i][j] > result:
            result = arr[i][j]
            max_row, max_col = i, j
print(result)
print(max_row +1, max_col +1)