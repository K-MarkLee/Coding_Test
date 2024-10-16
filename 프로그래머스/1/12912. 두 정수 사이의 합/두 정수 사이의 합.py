def solution(a, b):
    big = max(a,b)
    small = min(a,b)
    return sum(i for i in range(small,big+1))