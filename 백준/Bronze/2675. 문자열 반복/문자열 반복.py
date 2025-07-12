import sys
t=int(sys.stdin.readline().strip())
for _ in range(t):
    r,s = sys.stdin.readline().strip().split()
    r=int(r)
    result=''
    for a in s:
        result+=a*r
    print(result)
    