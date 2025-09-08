import sys

x = []
y = []

for i in range(3):
    a,b = map(int,sys.stdin.readline().strip().split())
    if a in x:
        x.remove(a)
    else:
        x.append(a)
    if b in y:
        y.remove(b)
    else:
        y.append(b)
        
print(f"{x[0]} {y[0]}")
