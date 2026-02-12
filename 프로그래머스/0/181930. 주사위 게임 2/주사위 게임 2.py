def solution(a, b, c):
    result = 1
    for i in range(1, 5 - len(set([a,b,c]))):
        result *= a**i + b**i + c**i
    return result