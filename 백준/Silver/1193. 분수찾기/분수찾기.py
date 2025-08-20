import sys
X = int(sys.stdin.readline())
area = 0
count = 0

while area < X:
    count += 1
    area += count
    
n = count - (area - X)
m = 1 + (area - X)

if count%2 == 0:
    print(f"{n}/{m}")
else :
    print(f"{m}/{n}")