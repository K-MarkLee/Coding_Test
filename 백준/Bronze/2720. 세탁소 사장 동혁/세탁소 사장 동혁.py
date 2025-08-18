import sys
n = int(sys.stdin.readline().strip())
change=[25,10,5,1]

for _ in range(n):
    money = int(sys.stdin.readline().strip())
    result = []
    for ch in change:
        a, money = divmod(money, ch)
        result.append(a)
    print(' '.join(map(str, result)))
    