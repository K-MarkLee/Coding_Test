import math
def solution(n):
    answer = math.sqrt(n)
    if answer == int(answer):
        return int((answer + 1) ** 2)
    else:
        return -1