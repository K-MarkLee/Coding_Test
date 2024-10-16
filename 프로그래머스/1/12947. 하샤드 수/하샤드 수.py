def solution(x):
    cal = sum(int(i) for i in str(x))
    if x % cal == 0:
        return True
    else:
        return False
    