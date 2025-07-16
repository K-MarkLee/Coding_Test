import sys
l=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
w=sys.stdin.readline()
result=0
for c in w:
    for i in range(len(l)):
        if l[i].find(c) != -1:
            result+=i+3
            break
print(result)
