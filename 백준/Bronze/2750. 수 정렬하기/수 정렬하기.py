import sys
N, *M = map(int,sys.stdin.read().strip().split())

M.sort()

print('\n'.join(map(str,M)))