import sys
num = list(map(int,sys.stdin.read().strip().split()))
triangle = ["Equilateral","Isosceles","Scalene"]

if sum(num) == 180:
    for i in range(3):
        if len(set(num)) == i+1:
            print(triangle[i])
else:
    print("Error")