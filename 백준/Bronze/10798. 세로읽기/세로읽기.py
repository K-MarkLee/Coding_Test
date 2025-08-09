import sys
arr = []
for row in sys.stdin:
    arr.append(list(row.strip()))
    
max_num = max(len(row) for row in arr)
for i in range(max_num):
    for j in range(len(arr)):
        if i < len(arr[j]):
            print(arr[j][i], end='')