import sys

while True:
    num=list(map(int,sys.stdin.readline().strip().split()))
    
    if sum(num) == 0:
        break
    
    if max(num) >= sum(num) - max(num):
        print("Invalid")
    elif len(set(num)) == 1:
        print("Equilateral")
    elif len(set(num)) == 2:
        print("Isosceles")
    else:
        print("Scalene")