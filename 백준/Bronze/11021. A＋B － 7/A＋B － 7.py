import sys
a=int(sys.stdin.readline())
for i in range(a):
    b,c=map(int,sys.stdin.readline().strip().split())
    print(f"Case #{i+1}: {b+c}")