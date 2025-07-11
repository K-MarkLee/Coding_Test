import sys
s=sys.stdin.readline().strip()
for i in range(26):
    a=chr(ord('a')+i)
    print(s.find(a), end=' ')
    