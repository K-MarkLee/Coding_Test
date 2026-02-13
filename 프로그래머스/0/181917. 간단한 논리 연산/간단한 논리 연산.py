def solution(x1, x2, x3, x4):
    first = 1 if int(x1) + int(x2) >= 1 else 0
    second = 1 if int(x3) + int(x4) >= 1 else 0
    
    return bool(first and second)
