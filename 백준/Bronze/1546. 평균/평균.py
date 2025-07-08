import sys
a = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))
m = max(num)
new = [(n/m)*100 for n in num]
result = sum(new)/a
print(result)