import sys
N = int(sys.stdin.readline().strip())
max_star = 2 * N - 1
middle = N - 1

for i in range(max_star):
    star = [' '] * max_star
    if i < N:
        left = middle - i
        right = middle + i
    else:
        left = i - (N - 1)
        right = max_star - 1 - left

    for j in range(left, right + 1):
        star[j] = '*'
        
    print(''.join(star).rstrip())
