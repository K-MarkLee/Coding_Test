def solution(t, p):
    count = 0
    n1 = len(t)
    n2 = len(p)    
    for i in range(n1 - n2 + 1):
        if int(t[i : i + n2]) <= int(p):
            count += 1
    return count
