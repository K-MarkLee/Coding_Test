import sys
n=int(sys.stdin.readline().strip())
x,y=[],[]
for _ in range(n):
    a,b = map(int,sys.stdin.readline().strip().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
if len(x) == 1:
    print(0)
else:
    print((x[-1]-x[0])*(y[-1]-y[0]))