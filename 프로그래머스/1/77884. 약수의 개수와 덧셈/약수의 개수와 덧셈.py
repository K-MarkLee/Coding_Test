def solution(left, right):
    result = 0
    for i in range(left, right + 1):
        divide = 0
        for a in range(1, i + 1):
            if i % a == 0:
                divide += 1
        if divide % 2 == 0:
            result += i
        else: 
            result -= i
    return result